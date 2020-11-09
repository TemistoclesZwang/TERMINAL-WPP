# -- coding: utf-8 --000

from selenium import webdriver  # pip install ou setting/project interpreter
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
from selenium.webdriver.support.ui import WebDriverWait

    
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=Cookies Webdriver Selenium")
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)  # Para manter o Chrome aberto
navegador = webdriver.Chrome(chrome_options=chrome_options)
url =navegador.get('https://web.whatsapp.com/')


def Color(texto):
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    FUNDO_PRETO = '\033[40m'

    print(f'{OKGREEN}{FUNDO_PRETO}{BOLD}--------- {texto} {ENDC}')


def search(contato):
    try:
        for c in range(1, 22):  # vai rodar números dentro do range
            element = navegador.find_element_by_xpath(
                f'//*[@id="pane-side"]/div[1]/div/div/div[{c}]/div/div/div[2]/div[1]/div[1]')
            if contato in element.text:
                element.click()
                print('Encontrei e cliquei: ')
                Color(element.text)

    except:
        # print('não achei o contato informado')
        pass


def notifications():  # Mostra as notificações
    for c in range(1, 25): 
        try:
            element = navegador.find_element_by_xpath( 
                f'//*[@id="pane-side"]/div[1]/div/div/div[{c}]/div/div/div[2]/div[2]/div[2]/span[1]')
            if element.text != '':  # Se a notificação for diferente de nada ou seja se tem algum número
                print('_' * 30)
                print(element.text, 'Notificações')
                element = navegador.find_element_by_xpath(  
                    f'//*[@id="pane-side"]/div[1]/div/div/div[{c}]/div/div/div[2]/div[1]/div[1]')
                print('Nome do contato:')
                Color(element.text)
                print('teste 2')
        except:
            pass


def reply():  # Encontra uma notificação e clica
    for c in range(1, 25):  
        try:
            element = navegador.find_element_by_xpath(
                f'//*[@id="pane-side"]/div[1]/div/div/div[{c}]/div/div/div[2]/div[2]/div[2]/span[1]')
            if element.text != '':  
                element.click()
                print('Encontrei uma notificação e cliquei')
                element = navegador.find_element_by_xpath(  
                    f'//*[@id="pane-side"]/div[1]/div/div/div[{c}]/div/div/div[2]/div[1]/div[1]')
                print('Nome do contato:')
                Color(element.text)
                print('_' * 30)
                break 
        except:
            pass


def msg(mensagem):  # Escreve uma mensagem
    element = navegador.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')  
    element.click() 
    element.send_keys(mensagem)


# Envia mensagem

def send():
    from selenium.webdriver.common.keys import Keys
    element = navegador.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]') 
    element.send_keys(Keys.RETURN)  


def read(contato):  # lê as últimas mensagens enviadas e recebidas precisa usar o search primeiro
    search(contato)
    for c in range(13, 27): 
        try:
            element = navegador.find_element_by_xpath(  
                f'//*[@id="main"]/div[3]/div/div/div[3]/div[{c}]')
            print('_' * 30)
            print(element.text)
        except:
            pass



def se_online():

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    element_on = navegador.find_element_by_xpath(
        '//*[@id="main"]/header/div[2]/div[2]/span')

    if element_on.text == 'online':
        print('Está online2222')

    elif element_on.text != 'online':
        navegador.implicitly_wait(10)
        print(element_on.text)
    else:
        Color('Nenhum elemento encontrado')
        pass



notifications()
search('Mozao')


#Efeito sonoro de notificação
duration = 0.5
freq = 180  # Hz
os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
