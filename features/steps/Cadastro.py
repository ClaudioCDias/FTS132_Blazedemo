from behave import when, then
from selenium.webdriver.common.by import By


@when(u'clico em Register')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'Register').click()

@then(u'vejo o formulario de cadastro')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.panel-heading').text == 'Register'

@when(u'preencho "<nome>" "<empresa>" "<email>" "<senha>"')
def step_impl(context):
    context.driver.find_element(By.ID, 'name').send_keys('Juca Pirama')
    context.driver.find_element(By.ID, 'company').send_keys('Iterasys')
    context.driver.find_element(By.ID, 'email').send_keys('juca@iterasys.com.br')
    context.driver.find_element(By.ID, 'password').send_keys('123456')
    context.driver.find_element(By.ID, 'password-confirm').send_keys('123456')

@when(u'clico no botao Register')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR,'button.btn.btn-primary').click()

@then(u'exibe a confirmacao do cadastro')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.code').text == '419'
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.message').text == 'Page Expired'
