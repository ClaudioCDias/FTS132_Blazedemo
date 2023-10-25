from behave import when, then
from selenium.webdriver.common.by import By


@when(u'clico no link Forgot Your Password?')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'Forgot Your Password?').click()

@then(u'vejo a pagina de reiniciar a senha')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.panel-heading').text == 'Reset Password'

@when(u'preencho meu "{email}" e clico no botao Send Password Reset Link')
def step_impl(context, email):
    context.driver.find_element(By.ID, 'email').send_keys(email)
    context.driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').click()