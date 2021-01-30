from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path='.\\chromedriver.exe', options=options)

papago_url = 'https://papago.naver.com/'
driver.get(papago_url)
time.sleep(3)

f = open('./my_papago.csv', 'r')
rdr = csv.reader(f)
next(rdr)

translate_into_kr = {}

for row in rdr:
    word = row[0]
    meaning = row[1]
    translate_into_kr[meaning] = word

for meaning in translate_into_kr:
    driver.find_element_by_css_selector('textearea#txtSource').send_key(meaning)
    driver.find_element_by_css_selector('button#btnTranslate').click()
    time.sleep(1)

    word = driver.find_element_by_css_selector('div#txtTarget').text
    translate_into_kr[meaning] =word

    driver.find_element_by_css_selector('textarea#txtSource').clear

for key in translate_into_kr:
    print(key, ":", translate_into_kr)

driver.close()

f.close()
