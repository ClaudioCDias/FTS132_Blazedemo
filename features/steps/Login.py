import time

from behave import when, then
from selenium.webdriver.common.by import By


@when(u'clico em home')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'home').click()

@when(u'preencho "<email>" "<senha>" e clico no botão Login')
def step_impl(context):
    context.driver.find_element(By.ID, 'email').send_keys('claudio@iterasys.com.br')
    context.driver.find_element(By.ID, 'password').send_keys('123456')
    time.sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').click()

@then(u'visualizo a mensagem de confirmação')
def step_impl(context):
    time.sleep(3)
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.code').text == '419'
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.message').text == 'Page Expired'