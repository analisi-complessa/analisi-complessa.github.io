import numpy as np
import os
import sys

os.system("rm -r pdf")
os.system("rm -r png")
os.system("mkdir pdf")
os.system("mkdir png")

rows = [] # file scomposto per righe
lezione = 0 # numero di lezione della scheda in questione
scheda = 0
writing = 0 # non sto scrivendo, sto scrivendo nella scheda, sto scrivendo nella risposta
my_path = os.getcwd()


my_files = []

file_to_open = "domande.tex"

with open(file_to_open, 'r') as file:
    for line in file:
        rows.append(line)

for row in rows:
    if row == "%%% Lezione\n":
        lezione += 1
        print(lezione)
    else:
        if row[0] == "%":
            if row[1] == "%":
                if row[2] == " ":
                    if row[3] == "S":
                        if row[4] == "C":
                            if row[5] == "H":
                                if row[6] == "E":
                                    if row[7] == "D":
                                        if row[8] == "A":
                                            scheda += 1
                                            writing = 1
                                            titolo_scheda = str(lezione) + "_" + str(scheda) + "_" + row[10]
                                            my_files.append(titolo_scheda)
                                            FILE_TEX = open("pdf/" + titolo_scheda + ".tex", "a")
                                            FILE_TEX.write("\documentclass[border=10pt]{standalone}\n")
                                            FILE_TEX.write("\input{standalone_unito}\n")
                                            FILE_TEX.write("\\begin{document}\n")
                                            FILE_TEX.write("\\begin{tcolorbox}[parbox=false, colback=white,colframe=white,sharpish corners, width=390pt]\n")
                    else: 
                        if row[3] == "R":
                            if row[4] == "I":
                                if row[5] == "S":
                                    if row[6] == "P":
                                        writing = 1
                                        titolo_scheda = str(lezione) + "_" + str(scheda) + "_r"
                                        my_files.append(titolo_scheda)
                                        FILE_TEX = open("pdf/" + titolo_scheda + ".tex", "a")
                                        FILE_TEX.write("\documentclass[border=10pt]{standalone}\n")
                                        FILE_TEX.write("\input{standalone_unito}\n")
                                        FILE_TEX.write("\\begin{document}\n")
                                        FILE_TEX.write("\\begin{tcolorbox}[parbox=false, colback=white,colframe=white,sharpish corners, width=390pt]\n")
                        else: 
                            if row[3] == "E":
                                if row[4] == "N":
                                    if row[5] == "D":
                                        writing = 0
                                        FILE_TEX.write("\end{tcolorbox}\n")
                                        FILE_TEX.write("\end{document}")
                                        FILE_TEX.close()
        else: 
            if writing == 1:
                FILE_TEX.write(row)

for x in my_files:
    os.system("pdflatex -output-directory=pdf " + x + ".tex")
    os.system("pdflatex -output-directory=pdf " + x + ".tex")
for x in my_files:
    os.system("convert -density 300 pdf/" + x + ".pdf png/" + x + ".png")

os.system("rm -r pdf")