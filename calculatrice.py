from tkinter import *
import math
from tkinter.font import Font as f

def evaluer(event):
    chaine.configure(text="Resultat : "+str(eval(entree.get())))

fen = Tk()

fen.title("Caculatrice")
entree = Entry(fen, width=20)
entree.bind("<Return>", evaluer)
entree.config(font= f(size=30))
chaine = Label(fen, fg='black')
chaine.config(font= f(size=30))
entree.pack()
chaine.pack()
fen.mainloop()