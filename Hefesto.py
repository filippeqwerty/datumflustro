import threading
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def record_capture(nib, nome, cpf, dtn, tel1, tel2):
    try:
        file = open('record.csv', 'r')
        file.close()
    except:
        file = open('record.csv', 'w')
        file.close()

    file_name = 'record.csv'
    file = open(file_name, 'a')
    line = f"{nib};{nome};{cpf};{dtn};{tel1};{tel2}\n"
    file.write(str(line))
    file.close()


def element_lock(drive, xpath):
    lock = True
    while lock == True:
        try:
            element = drive.find_element(By.XPATH, str(xpath))
            print('capturando elemento')
            lock == False
            return element
        except:
            print('sleep')
            time.sleep(1)

class bot():
    def __init__(self):
        self.drive = webdriver.Chrome(executable_path = 'chromedriver.exe')

    def preencher(self):

        options = webdriver.ChromeOptions()
        options.headless = True
        drive = self.drive
        print('Iniciando navegação')
        drive.get('https://sistemavanguard.com.br/vanguard/index.php/')
        user = element_lock(drive, '//*[@id="exten"]')
        print('elemento usuario capturado')
        user.send_keys('filipe@5505')
        print('usuario inserido')
        # user.send_keys(input('Login:')) # filipe@5505
        senha = element_lock(drive,'//*[@id="login-form"]/div[3]/div/input')
        senha.send_keys('123456')
        print('senha inserida')
        # senha.send_keys(input('Senha:')) # 123456
        btn_entrar = element_lock(drive,'//*[@id="login-form"]/div[4]/button')
        print('elemento botao entrar capturado')
        btn_entrar.click()
        print('elemento botao entrar acionado')
        print('Iniciando login')
        login_verify = element_lock(drive, '//*[@id="menu-10"]')
        print('usuario logado com sucesso!')
        print('navegando para listagem')
        drive.get('https://sistemavanguard.com.br/vanguard/index.php/listacampanha/listar')
        btn_inss = element_lock(drive, '/html/body/div/div[3]/div[2]/div/div[4]/div[1]/a/div')
        print('elemento botao inss capturado')
        btn_inss.click()
        print('elemento botao inss acionado')

        while True:
            print('aguardando elemento olho')
            btn_eye = element_lock(drive,'//*[@id="btnOcultar"]')
            print('olho encontrado')
            btn_eye.click()
            print('olho acionado')

            nib = element_lock(drive, '//*[@id="numBeneficio2"]').text
            print('nib capturado', nib)
            nome = element_lock(drive, '//*[@id="cliNome2"]').text
            print('nome capturado', nome)
            cpf = element_lock(drive, '//*[@id="cliCpf2"]').text
            print('cpf capturado', cpf)
            try:
                dtn = drive.find_element(By.XPATH, '//*[@id="cliNascimento"]').text
                print('data de nascimento capturada', dtn)
            except:
                dtn = '-'
            try:
                tel1 = drive.find_element(By.XPATH, '//*[@id="telefoneHot1"]').text
                print('telefone 1 capturado', tel1)
            except:
                tel1 = '-'
            try:
                tel2 = drive.find_element(By.XPATH, '//*[@id="telefoneHot2"]').text
                print('telefone 2 capturado', tel2)
            except:
                tel2 = '-'
            print('iniciado registro')
            threading.Thread(target=record_capture, args = [nib, nome, cpf, dtn, tel1, tel2]).start()
            print('registro finalizado')
            next_client =element_lock(drive, '/html/body/div[1]/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/form/div[2]/a')
            print('elemento proximo capturado')
            next_client.click()
            print('elemento proximo acionado')

        print('fechando driver')
        drive.quit()



bot = bot()
bot.preencher()

