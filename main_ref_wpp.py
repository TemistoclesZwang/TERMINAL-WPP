# -- coding: utf-8 --

from selenium import webdriver  #O chromedriver precisar estar na pasta bin do venv
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
from selenium.webdriver.support.ui import WebDriverWait

    
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=Cookies Webdriver Selenium")
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)  # Para manter o Chrome aberto,pois, esta fechando
navegador = webdriver.Chrome(chrome_options=chrome_options)
url =navegador.get('https://web.whatsapp.com/')

#Efeito sonoro de notificação
def som():
    duration = 0.5
    freq = 180  # Hz
    os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))


def Color(texto):
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    FUNDO_PRETO = '\033[40m'

    print(f'{OKGREEN}{FUNDO_PRETO}{BOLD}--------- {texto} {ENDC}')


def search(contato): #procura contatos recentes
    try:
        for c in range(1, 22):  # vai rodar números dentro do range
            element = navegador.find_element_by_xpath(
                f'//*[@id="pane-side"]/div[1]/div/div/div[{c}]/div/div/div[2]/div[1]/div[1]') 
            if contato in element.text:
                element.click()
                print('Encontrei e cliquei: ')
                Color(element.text)

    except:
        print('não achei o contato informado')
        pass

def search2(contato): #procura contatos recentes
    try:
        element = navegador.find_element_by_tag_name(
            f'_3CneP')
        if contato in element.text:
            element.click()
            print('Encontrei e cliquei: ')
            Color(element.text)

    except:
        print('não achei o contato informado')
        pass
search2('Mozao')



def notifications():  # Mostra todas notificações não lidas
    lista_notificacoes = []
    for c in range(1, 25): 
        try:
            element = navegador.find_element_by_xpath( 
                f'//*[@id="pane-side"]/div[1]/div/div/div[{c}]/div/div/div[2]/div[2]/div[2]/span[1]')
            if element.text != '':  # Se a notificação for diferente de nada ou seja se tem algum número
                lista_notificacoes.append(c)
                print('_' * 30)
                element = navegador.find_element_by_xpath(  
                    f'//*[@id="pane-side"]/div[1]/div/div/div[{c}]/div/div/div[2]/div[1]/div[1]')
                print('Nome do contato: ', end='')
                Color(element.text)
                print(f'Notificação número: {c}')
        except:
            pass


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


def msg(text):  # Escreve uma mensagem
    element = navegador.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')  
    element.click() 
    element.send_keys(text)


def send():# Envia mensagem
    from selenium.webdriver.common.keys import Keys
    element = navegador.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]') 
    element.send_keys(Keys.RETURN)  


def online(): # verifica se um contato está ou não online, precisa escolher o contato primeiro com search()

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    element_on = navegador.find_element_by_xpath(
        '//*[@id="main"]/header/div[2]/div[2]/span')

    if element_on.text == 'online':
        print('Está online')

    elif element_on.text != 'online':
        navegador.implicitly_wait(5) #espera 5 segundos para ver se o contato ficará online
        print(element_on.text)
    else:
        Color('Nenhum elemento encontrado')
        pass


#TODO:


#FIXME: 
# chrome driver,
# selenium
# apt install sox(audio no ubuntu)
#som de notificação não funciona se outros sons estiverem sendo reproduzidos