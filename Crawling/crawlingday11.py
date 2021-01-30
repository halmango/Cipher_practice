from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path='.\\chromedriver.exe', options=options)

papago_url = 'https://papago.naver.com/'
driver.get(papago_url)
time.sleep(3)

my_dict = {}

def get_papago_result(question):
    driver.find_element_by_css_selector('textarea#txtSource').send_key(question)
    driver.find_element_by_css_selector('button#btnTranslate').click()
    time.sleep(1)

    output = driver.find_element_by_css_selector('div#txtTarget').text
    driver.find_element_by_css_selector('textarea#txtSource').clear()
    return output

for i in range(5):
    question = input("번역할 단어")
    my_dict[question] = get_papago_result(question)

print(my_dict)