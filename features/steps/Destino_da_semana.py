from behave import when, then
from selenium.webdriver.common.by import By


@when(u'clico em  destination of the week! The Beach!')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'destination of the week! The Beach!').click()

@then(u'vejo a promocao da semana')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, '//body/div[2]').text == 'Destination of the week: Hawaii !'
    print('O retorno é ' + context.driver.find_element(By.XPATH, '//body/div[2]/img[1]').get_attribute('src'))
    assert context.driver.find_element(By.XPATH, '//body/div[2]/img[1]').get_attribute(
        'src') == 'https://www.blazedemo.com/assets/vacation.jpg'
