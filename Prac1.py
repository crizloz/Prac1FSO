#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Pràctica 1 FSO
-------------------------
Annabel Pizarro López
Cristina Izquierdo Lozano
-------------------------
'''

from Tkinter import * #Llibreria Tkinter
import tkFileDialog, Tkinter, tkFileDialog, tkMessageBox, ScrolledText, os, os.path #importar moduls extra

#--------------------------------------INTERFICIE GRAFICA------------------------------------------

#MAIN
finestra=Tk()
finestra.title("Cerca fitxers redundants")
finestra.minsize(600,00)
#--> IMPORTANT --> S'HAN DE CANVIAR ELS NOMS DE LES LLISTES
#Frames i labels
#-->fitxers originals (1)
f1=Frame(finestra)				#creem la finestra
l1=Label(f1,text="Fitxers originals")		#li posem una etiqueta
scrollist = Scrollbar(f1,orient=VERTICAL)	#creem una scrollbar per la nostra finestra
list = Listbox(f1,yscrollcommand=scrollist.set) #linkem la llista pertinent a la finestra
scrollist.config(command=list.yview)		#per a visualitzar la llista
scrollist.pack(side=RIGHT,fill=BOTH)		#pack de la scrolllist (visualitzar per pantalla)
list.pack(side=LEFT,anchor=W,expand=FALSE,fill=BOTH)	#situació de la llista
l1.pack(anchor=W, side=LEFT)			#packs de la finestra i l'etiqueta
f1.pack(expand=TRUE,fill=Y)

#-->fitxers iguals (2)
f2=Frame(finestra)
l2=Label(f2,text="Fitxers iguals")
scrollist = Scrollbar(f2,orient=VERTICAL)
list = Listbox(f2,yscrollcommand=scrollist.set)
scrollist.config(command=list.yview)
scrollist.pack(side=LEFT,fill=BOTH)
list.pack(side=LEFT,anchor=N,expand=FALSE,fill=BOTH)
l2.pack(anchor=N, side=RIGHT)
f2.pack(expand=FALSE,fill=BOTH)

#-->fitxers semblants (3)
f3=Frame(finestra)
l3=Label(f3,text="Fitxers semblants")
scrollist = Scrollbar(f3,orient=VERTICAL)
list = Listbox(f3,yscrollcommand=scrollist.set)
scrollist.config(command=list.yview)
scrollist.pack(side=LEFT,fill=BOTH)
list.pack(side=LEFT,anchor=S,expand=FALSE,fill=BOTH)
l3.pack(anchor=S, side=RIGHT)
f3.pack(expand=FALSE,fill=BOTH)

#----------------------------------------------FUNCIONS--------------------------------------

class Fitxers:
	font = ""
	desti = ""

	def __init__(self):
		self.font = tkFileDialog.askdirectory(title='Escull directori font')
		self.desti = tkFileDialog.askdirectory(title='Escull directori desti')

#botons per a escollir el directori
bt=Button(finestra,text='Escolliu directori font',command=tkFileDialog.askdirectory)
bt.pack(anchor=N)

bt=Button(finestra,text='Escolliu directori destí',command=tkFileDialog.askdirectory)
bt.pack(anchor=N)

''' S'HA D'ACABAR
	def llistaOriginals(self, font, desti):
		lori = ""
	def llistaIguals(self, font, desti):
		ligu = ""
	def llistaSemblants(self, font, desti):
		lsem = ""
'''
def cerca():
	print "executa script per a fer les cerques"

bt=Button(finestra,text='Cerca',command=cerca)
bt.pack(anchor=N)



#--------------------------------------------------------------------------------

''' COPIA LAB4 --> S'HA DE CANVIAR
def copia_seleccio():
    index = list.curselection()
    element = list.get(index)
    list.insert(END,element)

bl=Button(finestra,text='Copia',command=copia_seleccio)
bl.pack(anchor=E)

def borra_seleccio():
    index = list.curselection()
    if index:
	list.delete(index)
    else: 
	print "selecciona alguna cosa"

bb=Button(finestra,text='Borra',command=borra_seleccio)
bb.pack(anchor=E)





def tecla(event):
    print "premut", repr(event.char)

def ratoli(event):
    print "click en ", event.x, event.y

finestra.bind("<Key>", tecla)
finestra.bind("<Button-1>", ratoli)
'''

#botó de sortida
b=Button(finestra,text='Sortir',command=finestra.quit)
b.pack(side=BOTTOM,anchor=W)

finestra.mainloop()
