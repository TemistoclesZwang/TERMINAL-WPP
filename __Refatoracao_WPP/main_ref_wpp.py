# -- coding: utf-8 --

class Whats:
    def __init__(self):
        from selenium import webdriver  # pip install ou setting/project interpreter
        from selenium.webdriver.common.keys import Keys  # apertar teclas com funções
        from time import sleep
        import os
        from selenium.webdriver.support.ui import WebDriverWait

        
        chrome_options = webdriver.ChromeOptions()
        # this is the directory for the cookies
        chrome_options.add_argument("user-data-dir=Cookies Webdriver Selenium")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_experimental_option(
            "detach", True)  # Para manter o Chrome aberto
        
        self.navegador = webdriver.Chrome(chrome_options=chrome_options)
        self.url = self.navegador.get('https://web.whatsapp.com/')

    def Color(self, texto):
        OKGREEN = '\033[92m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        FUNDO_PRETO = '\033[40m'

        print(f'{OKGREEN}{FUNDO_PRETO}{BOLD}--------- {texto} {ENDC}')
        
    def search(self, contato):
        # contato = (input(#O RANGE É BASEADO NOS CONTATOS QUE ESTÃO APARECENDO NA TELA,SE DESCER A PÁGINA O RANGE MUDA
        # 'Digite o contato para buscar \n [Exatamente igual aparece na sua lista de contatos:')).strip()
        try:
            for c in range(1, 22):  # vai rodar números dentro do range
                element = self.navegador.find_element_by_xpath(
                    f'//*[@id="pane-side"]/div[1]/div/div/div[{c}]/div/div/div[2]/div[1]/div[1]')
                if contato in element.text:  # Se tiver esta string nos resultados vai clicar no xpath dela
                    element.click()
                    print('Encontrei e cliquei: ')
                    self.Color(element.text)
    
        except:
            # print('não achei o contato informado')
            pass
    # teste

    def notifications(self):  # Mostra as notificações
        for c in range(1, 25):  # vai rodar números dentro do range
            try:
                element = self.navegador.find_element_by_xpath(  # Xpath dos ícones de notificação. Com o tempo pode parar de funcionar
                    f'//*[@id="pane-side"]/div[1]/div/div/div[{c}]/div/div/div[2]/div[2]/div[2]/span[1]')
                if element.text != '':  # Se a notificação for diferente de nada ou seja se tem algum número
                    print('_' * 30)
                    # Para exibir todos os contatos que tem notificação
                    print(element.text, 'Notificações')
                    element = self.navegador.find_element_by_xpath(  # Vai procurar o contato que foi clicado
                        f'//*[@id="pane-side"]/div[1]/div/div/div[{c}]/div/div/div[2]/div[1]/div[1]')
                    # Vai mostrar o nome do contato que ele clicou
                    print('Nome do contato:')
                    self.Color(element.text)
                    print('teste 2')
            except:
                pass

    def reply(self):  # Encontra uma notificação e clica
        for c in range(1, 25):  # vai rodar números dentro do range
            try:
                element = self.navegador.find_element_by_xpath(
                    # Xpath dos ícones de notificação. Com o tempo pode parar de funcionar
                    f'//*[@id="pane-side"]/div[1]/div/div/div[{c}]/div/div/div[2]/div[2]/div[2]/span[1]')
                if element.text != '':  # Se a notificação for diferente de nada ou seja se tem algum número
                    element.click()
                    # print(element.text,'Notificações') #Para exibir todos os contatos que tem notificação
                    print('Encontrei uma notificação e cliquei')
                    element = self.navegador.find_element_by_xpath(  # Vai procurar o contato que foi clicado
                        f'//*[@id="pane-side"]/div[1]/div/div/div[{c}]/div/div/div[2]/div[1]/div[1]')
                    # Vai mostrar o nome do contato que ele clicou
                    print('Nome do contato:')
                    self.Color(element.text)
                    print('_' * 30)
                    break  # Apagar se quiser exibir todos os contatos que tem notificações
            except:
                pass

    def msg(self, x):  # Escreve uma mensagem
        element = self.navegador.find_element_by_xpath(
            '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')  # Procurar barra de enviar mensagem
        element.click()  # clicar na barra de escrever mensagem
        element.send_keys(x)

    # Envia mensagem

    def send(self):
        from selenium.webdriver.common.keys import Keys
        element = self.navegador.find_element_by_xpath(
            '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')  # Procurar barra de enviar mensagem
        element.send_keys(Keys.RETURN)  # Eviar mensagem

    def read(self, contato):  # lê as últimas mensagens enviadas e recebidas precisa usar o search primeiro
        self.search(contato)
        for c in range(13, 27):  # vai rodar números dentro do range
            try:
                element = self.navegador.find_element_by_xpath(  # Xpath dos ícones de notificação. Com o tempo pode parar de funcionar
                    f'//*[@id="main"]/div[3]/div/div/div[3]/div[{c}]')
                print('_' * 30)
                print(element.text)
            except:
                pass

   # Vai esperar por X segundos até eu clicar no contato ou o elemento aparecer na tela e aí verifica se tá ou não online

    def se_online(self):

        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        element_on = self.navegador.find_element_by_xpath(
            '//*[@id="main"]/header/div[2]/div[2]/span')

        if element_on.text == 'online':
            print('Está online2222')

        elif element_on.text != 'online':
            # element_off = WebDriverWait(self.navegador, 10).until(EC.presence_of_element_located(#(By.XPATH, '//*[@id="main"]/header/div[2]/div[2]/span')))
            self.navegador.implicitly_wait(10)
            # print(element_off.text)
            print(element_on.text)
        else:
         self.Color('Nenhum elemento encontrado')
         pass

wpp = Whats()


wpp.notifications()
wpp.search('Mozao')




'''
   def se_online(self):
      from selenium.webdriver.support.ui import WebDriverWait
      from selenium import webdriver# pip install ou setting/project interpreter
      from selenium.webdriver.common.keys import Keys #apertar teclas com funções
      from time import sleep
      import pyautogui
      import os
      from selenium.webdriver.support.ui import WebDriverWait 

      element = self.navegador.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[2]/span')
      print('Aguardar contato ficar online')
      return bool(element) #Se tiver algo no elements retornara True
      
      WebDriverWait(self.navegador, 10)
      wdw.until(se_online, 'teste')
'''


class Color:
    PINK = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'  # Fim
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    FUNDO_PRETO = '\033[40m'
    # Exemplo: print(f'{Color.OKGREEN}{Color.FUNDO_PRETO}{Color.BOLD} T E S T E 1 2 3 {Color.ENDC}')


class Audio():
    import os
    duration = 0.5
    freq = 180  # Hz
    os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
