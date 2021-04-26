from selenium import webdriver # webdriver 는 해당 파일과 같은 디렉토리에 위치해야 함. 오류가 난다면 구글 버전을 확인한다.
import time
import csv # csv형태로 파일을 저장 할 예정

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
        driver.find_element_by_css_selector('button#daumBtnSearch').click() # 검색창에 단어를 입력하고 검색 버튼 누르기
        try:
            driver.find_element_by_xpath('//*[@id="mSub"]/div/ul') 
            time.sleep(1)
            meaning = driver.find_element_by_xpath('//*[@id="mSub"]/div/ul').text # 검색 결과에서 따온 뜻을 text 형태로 변환
        except:
            driver.find_element_by_xpath('//*[@id="mArticle"]/div[1]/div[2]/div[2]/div[1]/ul') # 몇 개의 단어는 오류가 발생. 이 코드로 단어 검색 결과를 가져온다.
            time.sleep(1)
            meaning = driver.find_element_by_xpath('//*[@id="mArticle"]/div[1]/div[2]/div[2]/div[1]/ul').text 
                    
        print(meaning) # 검색한 단어의 뜻을 출력

        wtr.writerow([word, meaning])
        My_wordbook[word] = meaning # csv파일에 단어 -  뜻

        driver.find_element_by_xpath('//*[@id="q"]').clear() # 검색 창에 남아있는 이전에 검색한 단어 지우기
        time.sleep(1)

driver.close()
f.close()
