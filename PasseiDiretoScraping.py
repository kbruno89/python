#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
'''
Ver arquivos do portal PasseiDireto, sem ter cadastro ou assinatura premium
Em desenvolvimento...
Apenas para estudo :)
'''

from bs4 import BeautifulSoup
from tkinter import *
import requests, sys, os

def bt_click():   
    if len(edURL.get()) == 0:
        from tkinter import messagebox
        messagebox.showinfo("W A R N", "Insira a URL")
    else:
        import webbrowser
        headers = {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 0.5; en-us) AppleWebKit/522+ (KHTML, like Gecko) Safari/419.3'}
        url = (edURL.get())
        html = requests.get(url, headers=headers).content
        soup = BeautifulSoup(html, 'html.parser')
        var = soup.find("div", class_="box_default previews v2 simple")
        arquivo = open("temp.html", "w")
        arquivo.write(var.prettify())
        arquivo.close
        link = "temp.html"
        webbrowser.open(link, new=2)
        edURL.delete(0, END)

janela = Tk()
janela.geometry("735x110+358+195")
janela.resizable(0, 0)
janela.title("..:: PasseiDireto Scraping ::..")

lb1 = Label(janela, text="Insira a URL :")
lb1.place(x=30, y=20)

edURL = Entry(janela, width=73)
edURL.place(x=130, y=20)

btGerar = Button(janela, width=14, text="Gerar...", command=bt_click)
btGerar.place(x=280, y=70)

janela.mainloop()
