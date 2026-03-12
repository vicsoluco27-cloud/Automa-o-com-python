# teste de automaçao com pyautogui

import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.press("WIN")
pyautogui.write("opera")
pyautogui.press("Enter")
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("Enter")
pyautogui.click(x=876, y=363)
pyautogui.write("victor@gmail.com")
pyautogui.press("Tab")
pyautogui.write("123456")
pyautogui.press("Tab")
pyautogui.press("Enter")
pyautogui.click(x=866, y=247)




import pandas

tabela = pandas.read_csv("produtos.csv")


for linha in tabela.index:
    pyautogui.click(x=866, y=247)
    
    #codigo
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("Tab")

    #marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("Tab")

    #tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("Tab")

    #categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("Tab")

    #preco_unitario
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("Tab")

    #custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("Tab")

    #obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("Tab")

    pyautogui.press("Enter")
    pyautogui.scroll(100)
 #triste
 