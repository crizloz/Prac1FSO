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
import tkFileDialog, Tkinter, tkFileDialog, tkMessageBox, ScrolledText, os, os.path #importar mòduls extra


#----------------------------------------------FUNCIONS-----------------------------------------------

def escull_dir():
	global dirFont, dirDesti #directoris com a variables globals
	#diàlegs per a escollir els directoris font i destí:
	dirFont = tkFileDialog.askdirectory(title='Escull directori font') 
	dirDesti = tkFileDialog.askdirectory(title='Escull directori destí')

def llistaOriginals(): #llista amb els fitxers originals
	global dirFont
	for (dirpath, dirnames, filenames) in os.walk(dirFont):
		for element in filenames:
			lori.insert(END, element) #afegim tots els fitxers que es trobin a la llista del fitxer original, al final (END)

def llistaIguals(): #llista amb els fitxers iguals (nom i contingut)
	global dirDesti
	for (dirpath, dirnames, filenames) in os.walk(dirDesti):
		i = 0 #comptador
		#for element in filenames: #hauriem de recorrer tota la llista lori per a cada element en el fitxer de desti??????????? --> poc optim, pensar una altra solucio
			
def llistaSemblants(): #llista amb els fitxers semblants (nom)
	global dirFont, dirDesti
		#lsem = ""

def cerca():
	print "executa script per a fer les cerques"

#en les següents funcions passem per paràmetre la llista pertinent --> estalviar codi
def borra_seleccio(list): #esborrar els elements seleccionats en la llista pertinent
    index = list.curselection()
    if index:
	list.delete(index)
    else: 
	print "selecciona alguna cosa"

def selec_tot(list): #selecciona tots els fitxers de la llista pertinent
	list.select_set(0, END) #seleccionar de 0 al final

def selec_cap(list): #desselecciona tots els fitxers de la llista pertinent
	list.selection_clear(0, END) #desselecciona de 0 fins al final

def esborra(list): #Esborra els elements seleccionats
	global finestra
	elems = list.curselection() #obtenim els elements seleccionats
	for i in elems:
		rm_file=list.get(i) #fitxers a eliminar
		rm_dir = os.path.join(dirFont+'/',rm_file[1:]) #eliminem el fitxer del path
		os.system("rm "+' \"'+rm_dir+'\" ')
		list.delete(i) #Eliminem els arxius seleccionats
	finestra.destroy() #Eliminem la finestra top level


def esborra_confirmacio(list): #Finestra toplevel de confirmació per esborrar fitxers
	global finestra
	finestra=Toplevel(finestra) #Creem una finestra topLevel
	finestra.minsize(20,20)
	finestra.title('Esborrar fitxers') #etiqueta de la finestra
	ftxt = Label(finestra, text="Segur que vols esborrar els fitxers seleccionats?") #missatge de la finestra
	ftxt.pack(fill=BOTH)
	espai = Label(finestra, text=" ")
	espai.pack(fill=BOTH)
	bSi=Button(finestra,text='Sí',command=esborra(list)) #procedim a esborrar els arxius
	bSi.pack(side=RIGHT,anchor=W)
	bNo=Button(finestra,text='No',command=finestra.destroy) #tanquem la finestra topLevel
	bNo.pack(side=RIGHT,anchor=W)

def renombra(list): #re-nombra el fitxer del directori destí fent que el nom del fitxer del directori destí comenci per un substring demanat a l’usuari
	global fRenombrar, substring
	subs=substring.get() #substring demant a l'usuari
	elems = list.curselection()
	for i in elems:  #CANVIAR BUCLE --> FER MÉS ÒPTIM
		dirFitxer = list.get(i)
		dirSrc = os.path.join(dirFont+'/',dirFitxer[1:])
		dirFitxer=dirFitxer.replace(dirSrc,subs) #canviem el nom original pel mateix nom amb l'element afegit
		dirDst = os.path.join(dirFont+'/',dirFitxer[1:])
		list.delete(i) #Els esborrem de la llista per tornarlos a afegir amb el nou nom
		list.insert(i,dirFitxer)
		os.system("mv "+' \"'+dirSrc+'\" \"'+dirDst+'\"')
	fRenombrar.destroy() #Tanquem finestra topLevel


def renombra_finestra(): #Finestra per a demanar a l'usuari quin substring afegir
	global fRenombrar, substring
	fRenombrar=Toplevel(finestra) #Interfície de la finestra topLevel
	fRenombrar.minsize(0,0)
	fRenombrar.title('Renombrar fitxer')
	frtxt= Label(fRenombrar, text="Afegeix substring inicial: ")
	frtxt.pack(side=LEFT,anchor=W)
	substring=Entry(fRenombrar,width=5)
	substring.pack(anchor=W,side=LEFT)
	bR=Button(fRenombrar,text='Renombrar',command=renombra)
	bR.pack(side=RIGHT,anchor=W)


#--------------------------------------INTERFÍCIE GRÀFICA------------------------------------------

#MAIN WINDOW
finestra=Tk()
finestra.title("Cerca fitxers redundants")
finestra.minsize(600,00)

#subfinestres de les llistes
#-->fitxers originals (1)
f1=Frame(finestra)				#creem la finestra
l1=Label(f1,text="Fitxers originals")		#li posem una etiqueta
scrollist = Scrollbar(f1,orient=VERTICAL)	#creem una scrollbar per la nostra finestra
lori = Listbox(f1,yscrollcommand=scrollist.set) #linkem la llista pertinent a la finestra
scrollist.config(command=lori.yview)		#per a visualitzar la llista
scrollist.pack(side=RIGHT,fill=BOTH)		#pack de la scrolllist (visualitzar per pantalla)
lori.pack(side=LEFT,anchor=W,expand=FALSE,fill=BOTH)	#situació de la llista
l1.pack(anchor=W, side=LEFT)			#packs de la finestra i l'etiqueta
f1.pack(expand=TRUE,fill=Y)
print lori.get(1)

#-->fitxers iguals (2)
f2=Frame(finestra)
l2=Label(f2,text="Fitxers iguals")
scrollist = Scrollbar(f2,orient=VERTICAL)
ligu = Listbox(f2,yscrollcommand=scrollist.set)
scrollist.config(command=ligu.yview)
scrollist.pack(side=LEFT,fill=BOTH)
ligu.pack(side=LEFT,anchor=N,expand=FALSE,fill=BOTH)
l2.pack(anchor=N, side=RIGHT)
f2.pack(expand=FALSE,fill=BOTH)
print ligu.get(1)

#-->fitxers semblants (3)
f3=Frame(finestra)
l3=Label(f3,text="Fitxers semblants")
scrollist = Scrollbar(f3,orient=VERTICAL)
lsem = Listbox(f3,yscrollcommand=scrollist.set)
scrollist.config(command=lsem.yview)
scrollist.pack(side=LEFT,fill=BOTH)
lsem.pack(side=LEFT,anchor=S,expand=FALSE,fill=BOTH)
l3.pack(anchor=S, side=RIGHT)
f3.pack(expand=FALSE,fill=BOTH)
print lsem.get(1)

#botons per a escollir el directori
bt=Button(finestra,text='Escolliu directori font',command=tkFileDialog.askdirectory)
bt.pack(anchor=N)

bt=Button(finestra,text='Escolliu directori destí',command=tkFileDialog.askdirectory)
bt.pack(anchor=N)

bt=Button(finestra,text='Cerca',command=cerca)
bt.pack(anchor=N)

bb=Button(finestra,text='Borra',command=borra_seleccio)
bb.pack(anchor=E)

#botó de sortida
b=Button(finestra,text='Sortir',command=finestra.quit)
b.pack(side=BOTTOM,anchor=W)
#------------------------------------------------------------------------------------------------------

''' COPIA LAB4 --> S'HA DE CANVIAR
def copia_seleccio():
    index = list.curselection()
    element = list.get(index)
    list.insert(END,element)

bl=Button(finestra,text='Copia',command=copia_seleccio)
bl.pack(anchor=E)

def tecla(event):
    print "premut", repr(event.char)

def ratoli(event):
    print "click en ", event.x, event.y

finestra.bind("<Key>", tecla)
finestra.bind("<Button-1>", ratoli)
'''
finestra.mainloop()
