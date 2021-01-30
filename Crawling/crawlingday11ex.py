from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path='.\\chromedriver.exe', options=options)

papago_url = 'https://papago.naver.com/'
driver.get(papago_url)
time.sleep(3)

my_dict = {}

for i in range(3):
    question = input('번역할 영단어 입력 : ')
    driver.find_element_by_css_selector('textarea#txtSource').send_keys(question)
    driver.find_element_by_css_selector('button#btnTranslate').click()
    time.sleep(1)
    
    output = driver.find_element_by_css_selector('div#txtTarget').text
    my_dict[question] = output

    driver.find_element_by_css_selector('textarea#txtSource').clear()

print(my_dict)
