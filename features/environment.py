from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService, Service

# Início
def before_all(context):  # Antes de Tudo

    # Declarar o Selenium, instanciar como o navegador e apontar o driver
    # context.driver = webdriver.Chrome('C:/Users/Claudio/PycharmProjects/FTS132_Blazedemo/drivers/chromedriver109/chromedriver.exe')
    service = Service(
        executable_path='C:/Users/Claudio/PycharmProjects/FTS132_Blazedemo/drivers/chromedriver109/chromedriver.exe')
    context.driver = webdriver.Chrome(service=service)
    # Maximizar a janela do navegador
    context.driver.maximize_window()

    # Define uma espera máxima para todos os elementos do script
    context.driver.implicitly_wait(30)

    print('Passo A - Antes de Tudo')

# Fim
def after_all(context):  # Depois de Tudo

    # Desligar / Destruir o objeto do Selenium
    context.driver.quit()

    print('Passo Z - Depois de Tudo')

    # Bloco executado ao final de cada step
    def after_step(context, step):
        print()