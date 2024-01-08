import numpy as np
import os
import sys
import shutil
import time

os.system("rm -r schede_html")
os.system("mkdir schede_html")
os.system("cd schede_png && python3 convert.py")

files = [] # Lista dei file
files_noex = [] # Lista dei file senza estensione
domande_tutte = []
domande_vere = [] # Array delle domande con risposta V
domande_false = [] # Array delle domande con risposta F
domande_multipla = [] # Array delle domande a risposta multipla

for root,dirs,flies in os.walk("schede_png/png/"): ## Questo ciclo for riempie la lista "files" con tutti i nomi dei file nella directory 
    for file in flies:
        files.append(file)
        files_noex.append(file.replace(".png", "")) ## senza estensione

for file in files_noex:
    if file.replace("_M", "").replace("_V", "").replace("_F", "").replace("_r", "") not in domande_tutte: 
        domande_tutte.append(file.replace("_M", "").replace("_V", "").replace("_F", "").replace("_r", ""))    ### Crea una lista di domande uniche
    if file.replace("_r", "") == file:  ## Smista le domande tra v e f e multiple
        if file.replace("_V", "").replace("_F", "") == file: 
            domande_multipla.append(file.replace("_V", "").replace("_F", "").replace("_M", ""))
        if file.replace("_V", "").replace("_M", "") == file: 
            domande_false.append(file.replace("_V", "").replace("_M", "").replace("_F", ""))
        if file.replace("_M", "").replace("_F", "") == file: 
            domande_vere.append(file.replace("_M", "").replace("_F", "").replace("_V", ""))

# print(domande_vere)
# print(domande_false)
# print(domande_multipla)

## Di seguito le variabili da sostituire nel documento
next_question = ""
question = ""
answer = ""

## Ci teniamo larghi e consideriamo come numero di lezioni quello massimo, ovvero il numero di domande
## Idem anche per il numero di domande per lezione
for lezione in range(1, len(domande_tutte), 1):
    if str(lezione) + "_1" in domande_tutte:
        print("Lezione " + str(lezione))
        for i in range(1, len(domande_tutte), 1): 
            if str(lezione) + "_" + str(i) in domande_tutte:
                ### Smista la domanda
                if str(lezione) + "_" + str(i) in domande_vere: 
                    shutil.copy("domanda_vera.html", "schede_html/" + str(lezione) + "_" + str(i) + ".html") # Crea il file corrispondente secondo modello
                    question = "../schede_png/png/" + str(lezione) + "_" + str(i) + "_V.png"
                    answer = "../schede_png/png/" + str(lezione) + "_" + str(i) + "_r.png"
                elif str(lezione) + "_" + str(i) in domande_multipla:
                    shutil.copy("domanda_multipla.html", "schede_html/" + str(lezione) + "_" + str(i) + ".html") # Crea il file corrispondente secondo modello
                    question = "../schede_png/png/" + str(lezione) + "_" + str(i) + "_M.png"
                    answer = "../schede_png/png/" + str(lezione) + "_" + str(i) + "_r.png"
                elif str(lezione) + "_" + str(i) in domande_false: 
                    shutil.copy("domanda_falsa.html", "schede_html/" + str(lezione) + "_" + str(i) + ".html") # Crea il file corrispondente secondo modello
                    question = "../schede_png/png/" + str(lezione) + "_" + str(i) + "_F.png"
                    answer = "../schede_png/png/" + str(lezione) + "_" + str(i) + "_r.png"
                ### Capisce se è l'ultima della serie
                if str(lezione) + "_" + str(i+1) in domande_tutte:
                    next_question = str(lezione) + "_" + str(i+1) + ".html"
                else: next_question = "../end.html"
                ### Effettua le sostituzioni
                with open( "schede_html/" + str(lezione) + "_" + str(i) + ".html", 'r') as file: ## Legge il file ed effettua le sostituizioni
                    data = file.read()
                    data = data.replace("%%NEXT_QUESTION", next_question)
                    data = data.replace("%%QUESTION", question)
                    data = data.replace("%%ANSWER", answer)
                with open( "schede_html/" + str(lezione) + "_" + str(i) + ".html", 'w') as file: ## Scrive le sostituizioni sul file
                    file.write(data)

os.system("git add .")
os.system('git commit -m "' + str(time.ctime()) + '"')
os.system('git push')
