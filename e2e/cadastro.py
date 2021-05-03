import names
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

delay = 10


def get_email():
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    full_name = first_name + " " + last_name
    email = first_name + "_" + last_name + "@gmail.com"
    return full_name, email


driver = webdriver.Chrome('/Users/hsouza/Downloads/chromedriver')

''' Step 1 - Go to login page '''
driver.get('https://dev.app.bossabox.com/login')
WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//input[@id='input-email']")))
driver.find_element_by_xpath("//input[@id='input-email']")
driver.find_element_by_xpath("//input[@id='input-password']")

''' Step 2 - Click sign '''
driver.find_element_by_xpath("//button[contains(text(),'Cadastre-se')]").click()

''' Step 3 - Generate full name and email '''
full_name, email = get_email()
print(full_name)

''' Step 4 - Check alert need fill all fields '''
WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//input[@id='input-fullName']")))
driver.find_element_by_xpath("//input[@id='input-password']").send_keys('12345')
driver.find_element_by_xpath("//input[@id='input-confirmPassword']").send_keys('12345')
driver.find_element_by_xpath("//button[contains(text(),'Cadastrar')]").click()
WebDriverWait(driver, delay).until(EC.presence_of_element_located(
    (By.XPATH, "//p[contains(text(),'Lembre-se de preencher os campos')]")))

''' Step 5 - Check alert passcode need 8 characters '''
driver.find_element_by_xpath("//input[@id='input-fullName']").send_keys(full_name)
driver.find_element_by_xpath("//input[@id='input-email']").send_keys(email)
driver.find_element_by_xpath("//button[contains(text(),'Cadastrar')]").click()
WebDriverWait(driver, delay).until(EC.presence_of_element_located(
    (By.XPATH, "//p[contains(text(),'A senha deve ter pelo menos 8 caracteres')]")))

''' Step 6 - Check alert passcode is equal  '''
driver.find_element_by_xpath("//input[@id='input-password']").clear()
driver.find_element_by_xpath("//input[@id='input-confirmPassword']").clear()
driver.find_element_by_xpath("//input[@id='input-password']").send_keys('12345678')
driver.find_element_by_xpath("//input[@id='input-confirmPassword']").send_keys('87654321')
driver.find_element_by_xpath("//button[contains(text(),'Cadastrar')]").click()
WebDriverWait(driver, delay).until(EC.presence_of_element_located(
    (By.XPATH, "//p[contains(text(),'As senhas não correspondem')]")))

''' Step 7 - Check alert need accept terms  '''
driver.find_element_by_xpath("//input[@id='input-password']").clear()
driver.find_element_by_xpath("//input[@id='input-confirmPassword']").clear()
driver.find_element_by_xpath("//input[@id='input-password']").send_keys('12345678')
driver.find_element_by_xpath("//input[@id='input-confirmPassword']").send_keys('12345678')
driver.find_element_by_xpath("//button[contains(text(),'Cadastrar')]").click()
WebDriverWait(driver, delay).until(EC.presence_of_element_located(
    (By.XPATH, "//p[contains(text(),'É necessário aceitar os termos de uso e política de privacidade para prosseguir')]")))

''' Step 8 - Check alert email or passcode invalid '''
driver.find_element_by_xpath("//input[@id='input-email']").clear()
driver.find_element_by_xpath("//input[@id='input-email']").send_keys("teste.teste")
driver.find_element_by_xpath("//button[contains(text(),'Cadastrar')]").click()
WebDriverWait(driver, delay).until(EC.presence_of_element_located(
    (By.XPATH, "//p[contains(text(),'E-mail e/ou senha inválidos')]")))


''' Step 9 - Check alert ops error '''
driver.find_element_by_xpath("//input[@id='input-email']").clear()
driver.find_element_by_xpath("//input[@id='input-email']").send_keys(email)
driver.find_element_by_xpath("//div[contains(@class, 'checkbox-icon')]").click()
driver.find_element_by_xpath("//button[contains(text(),'Cadastrar')]").click()

try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, "//p[contains(text(),'Ocorreu um erro, tente novamente!')]")))
    print("Test case failed")
except Exception:
    print("Test case passed")


driver.close()
