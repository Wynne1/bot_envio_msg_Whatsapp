# Quais passos manuais preciso fazer para enviar uma mensagem para várias pessoas?

#1.Ter uma lista
#3.Escrever a mensagem
#4.Enviar a mensagem
#5.Fazer uma pausa entre as mensagens, para não tomar ban
import pyautogui
import webbrowser
from time import sleep

telefones=[5579981183130,557999998888,557988888888]


for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}') #ESSE É O PONTO CHAVE DO PROBLEMA
    sleep(10)
    pyautogui.click(936,420,duration=1)
    sleep(10)
    pyautogui.typewrite('Testando mais uma automação agora')
    sleep(5)
    pyautogui.press('enter')
    sleep(300)