#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
'''
Ler notícias do portal NSC, sem ter cadastro ou assinatura
Apenas para estudo :)
'''

import requests
from tkinter import *

def bt_click():   
    if len(edURL.get()) == 0:
        from tkinter import messagebox
        messagebox.showinfo("W A R N", "Insira a URL")
    else:
        import webbrowser
        url = (edURL.get())
        response = requests.get(url).text
        arquivo = open("temp.html", "w")
        arquivo.write(response)
        arquivo.close
        link = "temp.html"
        webbrowser.open(link, new=2)
        edURL.delete(0, END)

janela = Tk()
janela.geometry("735x110+358+195")
janela.minsize(1, 1)
janela.maxsize(3271, 1050)
janela.resizable(1, 1)
janela.title("..:: NSC Notícias FULL ::..")

lb1 = Label(janela, text="Insira a URL :")
lb1.place(x=30, y=20)
lb2 = Label(janela, text="#ZELOTES")
lb2.place(x=652, y=80)
lb3 = Label(janela, text="#OPERACAOZELOTES")
lb3.place(x=580, y=60)

edURL = Entry(janela, width=73)
edURL.place(x=130, y=20)

btGerar = Button(janela, width=14, text="Gerar...", command=bt_click)
btGerar.place(x=280, y=70)

janela.mainloop()
