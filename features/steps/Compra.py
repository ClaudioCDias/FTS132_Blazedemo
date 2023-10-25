import time

from behave import given, when, then
from selenium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Precisa sempre importar a classe environment (onde estão o Antes e o Depois do Teste)
from features import environment

# método executado antes da feature e serve para chamar os passos seguintes
def before_feature(context, feature):
    if 'compra_passagem' in feature.tag:
        context.execute_steps(
            # pode ser incluidas outras ações
        )

@given(u'que acesso o site Blazedemo')
@given(u'que acesso o portal Blazedemo')
def step_impl(context):
    context.driver.get('https://www.blazedemo.com')
    print('Passo 1 - Acessou o site Blazedemo')
    # time.sleep(3) # Espera bruta - sempre remover - alfinete

@when(u'seleciono a origem como "{origem}"')
def step_impl(context, origem):

    # Mapeia o combo com as cidades de origem
    combo_origem = context.driver.find_element(By.NAME, 'fromPort')

    # Cria um objeto para permitir selecionar as opções do combo
    objeto_origem = Select(combo_origem)

    # Seleciona o elemento no combo
    objeto_origem.select_by_visible_text(origem)
    # objeto_origem.select_by_value(origem)

    print('Passo 2 - Selecionou a cidade de origem')

@when(u'seleciono a cidade de destino "{destino}"')
def step_impl(context, destino):
    # Mapeia o combo com as cidades de origem
    combo_origem = context.driver.find_element(By.NAME, 'toPort')

    # Cria um objeto para permitir selecionar as opções do combo
    objeto_origem = Select(combo_origem)

    # Seleciona o elemento no combo
    objeto_origem.select_by_visible_text(destino)

    print('Passo 3 - Selecionou a cidade de destino')
    # time.sleep(3)  # Espera bruta - sempre remover - alfinete

@when(u'clico no botão Find Flights')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()
    print('Passo 4 - Clicou no botão Find Flights')

@then(u'sou direcionado para a página de seleção de vôos de "{origem}" para "{destino}"')
def step_impl(context, origem, destino):
    print()
    # 3 Principais motivos para o teste de automação não funcionar
    # - Seletores ou Indentificadores
    # - Sincronismo
    # - "Programação Exótica"

    # assert context.driver.find_element(By.TAG_NAME, 'h3').text() == 'Flights from São Paolo to Rome: '

    time.sleep(5)
    re = f'Flights from {origem} to {destino}:'
    print('texto é ' + context.driver.find_element(By.XPATH, '/html[1]/body[1]/div[2]/h2[1]').text)
    assert context.driver.find_element(By.XPATH, '/html[1]/body[1]/div[2]/h2[1]').text == re

    print('Passo 5 - Direcionou para a pagina de seleção de vôos')


@when(u'seleciono o primeiro vôo')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-small').click()
    print('Passo 6 - Selecionou o primeiro vôo')

@then(u'sou direcionado para a página de pagamento')
def step_impl(context):
    re = 'Please submit the form below to purchase the flight.'
    assert context.driver.find_element(By.XPATH,
      "//p[contais(text(), 'Please submit the form below to purchase the flight.')]").text == re
    print('Passo 7 - Direcionou para a página de pagamento')

@when(u'preencho os dados para o pagamento')
def step_impl(context):
    context.driver.find_element(By.ID, 'inputName').send_keys('James Bond')
    print('Passo 8 - Preencheu os dados para pagamento')

@when(u'clico no botão Purchase Flight')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()
    print('Passo 9 - Clicou no botão Purchase Flight')

@then(u'sou direcionado para a página de confirmação')
def step_impl(context):
    print()

    assert context.driver.find_element(By.TAG_NAME, 'h1').text == 'Thank you for your purchase today!'
    print('Passo 10 - Direcionou para a página de confirmação ')

@when(u'seleciono de "{origem}" para "{destino}"')
def step_impl(context, origem, destino):
    # Mapeia o combo com as cidades de origem
    combo_origem = context.driver.find_element(By.NAME, 'fromPort')

    # Cria um objeto para permitir selecionar as opções do combo
    objeto_origem = Select(combo_origem)

    # Seleciona o elemento no combo
    objeto_origem.select_by_visible_text(origem)
    # objeto_origem.select_by_value(origem)

    # Mapeia o combo com as cidades de origem
    combo_origem = context.driver.find_element(By.NAME, 'toPort')

    # Cria um objeto para permitir selecionar as opções do combo
    objeto_origem = Select(combo_origem)

    # Seleciona o elemento no combo
    objeto_origem.select_by_visible_text(destino)

    context.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()

    print('Passo 2c - Selecionou a cidade de origem e destino ')