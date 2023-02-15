from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.instagram.com/accounts/login/?next=%2Fispammyrightstick%2F&source=desktop_nav')

login_main_button_classname = "_aacl._aaco._aacw._aad6._aade"
allow_cookies_classname = "_a9--._a9_0"
username_field_name = "username"
password_field_name = "password"
login_button_classname = "_acan._acap._acas._aj1-"
not_now_button_classname = "_acan._acao._acas._aj1-"

#driver.find_element(By.CLASS_NAME,allow_cookies_classname)

def allowCookies() :
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME,allow_cookies_classname)))
    button.click()

def clickOnLoginButton() :
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, login_main_button_classname)))
    button.click()

def loginPage() :
    input_field_username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, username_field_name)))
    input_field_password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, password_field_name)))
    input_field_username.send_keys('yaniswalou')
    input_field_password.send_keys('Ina3zuma5')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, login_button_classname))).click()

def notNow() :
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, not_now_button_classname)))
    button.click()


allowCookies()
#clickOnLoginButton()
loginPage()
time.sleep(5)
notNow()
time.sleep(8)
# parentElement = driver.find_element(By.CLASS_NAME,"_ab8w._ab94._ab99._ab9f._ab9m._ab9o._abcm")
# elementList = parentElement.find_elements(By.TAG_NAME,"div")
all_posts = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[2]/article/div[1]/div')
all_children_by_xpath = all_posts.find_elements(By.XPATH,"./*")

for child in all_children_by_xpath :
    print(str(child) + " ---- " + str(child.get_attribute('class')))
print('len(all_children_by_xpath): ' + str(len(all_children_by_xpath)))

time.sleep(5)