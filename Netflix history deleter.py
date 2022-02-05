from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


def makeConfig():
    global ID, email, password
    with open('config.lk', 'w') as f:
        ID = str(input('Please enter your netflix id (from viewing page): '))
        email = str(input('Please enter the email used to make your netflix account: '))
        password = str(input('Please enter your netflix password (this is saved as plain text so make sure you trust eveyone with access): '))
        f.write(f'''id: {ID}
email: {email}
password: {password}''')

try:
    with open('config.lk', 'r') as f:
            lines = f.readlines()
            try:
                ID = lines[0].split(':')[1].strip('\n').strip(' ')
                email = lines[1].split(':')[1].strip('\n').strip(' ')
                password = lines[2].split(':')[1].strip('\n').strip(' ')
                print(ID, email, password)
            except IndexError:
                makeConfig()

except FileNotFoundError:
    makeConfig()

driver = webdriver.Firefox()
driver.get(f'https://www.netflix.com/settings/viewed/{ID}')

def login():
    driver.find_element(By.ID, 'id_userLoginId').send_keys(email)
    driver.find_element(By.ID, 'id_password').send_keys(password)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div[1]/form/button').click()

def clearhistory():
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[3]/div[2]/a[1]').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[3]/div[3]/div/footer/div/button[1]').click()

try:
    login()
    clearhistory()
except NoSuchElementException:
    print('The History is already clear, or the netflix page has changed.\nThe program will terminate in 10 seconds')
finally:
    sleep(10)
    driver.close()
