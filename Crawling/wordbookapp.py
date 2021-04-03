from selenium import webdriver
import time
import csv

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path='.\\chromedriver.exe', options=options)

Daumdic_url = 'https://dic.daum.net/index.do?dic=eng&q='
driver.get(Daumdic_url)
time.sleep(3)


f = open('./my_wordbook.csv', 'a', newline = '')
wtr = csv.writer(f)

My_wordbook = {}

while True:
    word = input('영단어 입력 (0 입력하면 종료) : ')
    
    if word == '0':
        print('번역 종료')
        break

    if word in My_wordbook.keys():
        print('이미 번역한 영단어입니다! 뜻은\n', My_wordbook[word], '입니다.')
    else:
        driver.find_element_by_xpath('//*[@id="q"]').send_keys(word) 
        driver.find_element_by_css_selector('button#daumBtnSearch').click()
        try:
            driver.find_element_by_xpath('//*[@id="mSub"]/div/ul')
            time.sleep(1)
            meaning = driver.find_element_by_xpath('//*[@id="mSub"]/div/ul').text 
        except:
            driver.find_element_by_xpath('//*[@id="mArticle"]/div[1]/div[2]/div[2]/div[1]/ul')
            time.sleep(1)
            meaning = driver.find_element_by_xpath('//*[@id="mArticle"]/div[1]/div[2]/div[2]/div[1]/ul').text
            try:
                driver.find_element_by_xpath('//*[@id="mArticle"]/div[1]/div[3]/div[2]/div/ul')
                time.sleep(1)
                meaning = driver.find_element_by_xpath('//*[@id="mArticle"]/div[1]/div[3]/div[2]/div/ul').text
            except:

                    
                print(meaning)

        wtr.writerow([word, meaning])
        My_wordbook[word] = meaning

        driver.find_element_by_xpath('//*[@id="q"]').clear()
        time.sleep(1)

driver.close()
f.close()

