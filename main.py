# Passo a passo:
# Passo 1 - entrar no sistema;
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")


time.sleep(1)
sistema = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(sistema)
pyautogui.press("enter")

time.sleep(2)

# Passo 2 - fazer login;


#pyautogui.click(x=559, y=462)
pyautogui.press("tab")
pyautogui.write("admin@gmail.com")

pyautogui.press("tab")
pyautogui.write("supersecreto")

pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(1)

# Passo 3 - importar o db;
import pandas

tabela = pandas.read_csv("produtos.csv")


# Passo 4 - cadastrar;

for i in tabela.index:
    pyautogui.click(x=756, y=317)
    pyautogui.write(tabela.loc[i , "codigo"]) # code

    pyautogui.press("tab")
    pyautogui.write(tabela.loc[i , "marca"]) # brand

    pyautogui.press("tab")
    pyautogui.write(tabela.loc[i , "tipo"]) # type

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[i , "categoria"])) # category

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[i , "preco_unitario"])) # price

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[i , "custo"])) #cost
    
    if not pandas.isna(tabela.loc[i , "obs"]):
        pyautogui.press("tab")
        pyautogui.write(tabela.loc[i , "obs"]) # description

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("enter")

    pyautogui.scroll(5000)
    time.sleep(0.5)



    
