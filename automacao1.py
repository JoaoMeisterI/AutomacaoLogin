#BOT NO COMPUTADOR - PYAUTOGUI
#BOT NA WEB - SELENIUM
import pyautogui
import time

#Colocando um time de pause para tudo
pyautogui.PAUSE = 2

#APERTAR TECLA WINDOWS
pyautogui.press("win")
#ESCREVER O NOME DA PLANILHA
pyautogui.write("login.xlsx")
time.sleep(2)
pyautogui.press("enter")
time.sleep(3)


#Pegando a posição do mouse




#print(pyautogui.position())
#PREENCHER LOGIN
pyautogui.click(x=630, y=363)
pyautogui.write("Joao Pedro Meister Ivacow")
pyautogui.click(x=553, y=423)
pyautogui.write("1010DSQAKO**8748")
pyautogui.click(x=475, y=537)
time.sleep(3)
pyautogui.click(x=663, y=699)
#Apertando no x para sair da tela
pyautogui.click(x=1905, y=33)
#Apertando para não salvar
pyautogui.click(x=994, y=543)

#PREENCHER SENHA
