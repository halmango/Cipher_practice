from selenium import webdriver
import time


search_word = input('뉴스 검색 키워드 : ') # 검색어 입력

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path='.\\chromedriver.exe', options=options)

count = 0 # 개수 셀 꺼임
for page in range(1,4): # 1~3페이지 
    news_url = f'https://search.hankyung.com/apps.frm/search.news?query={search_word}&mediaid_clust=HKPAPER,HKCOM&page={page}'
    driver.get(news_url)
    time.sleep(1)

    articles_one_page = driver.find_elements_by_css_selector('em.tit') # 한 페이지의 모든 기사 제목들

    for article in articles_one_page:
        title = article.text # 기사 한 개 제목
        article.click() # 기사 클릭
        time.sleep(1)

        driver.switch_to.window(driver.window_handles[-1]) # 가장 최근 탭

        try:
            content = driver.find_element_by_id('articletxt').text # 이 코드 실행하다 예외 발생시
        except:
            content = driver.find_element_by_id('newsVles').text # 이 코드 실행
        
        seperate = content.split('\n') # 줄바꿈을 기준으로 나눔

        count += 1
        print(f"<{count} 번째 기사>\n[{title}]\n")
        for sep in seperate: # content 줄바꿈 없이 출력하는 코드
            if sep != '':
                print(sep, end = '')
        print()
        print()

        driver.close() # 기사 탭 닫기

        driver.switch_to.window(driver.window_handles[0]) # 첫번째 탭으로 이동
        time.sleep(1)

driver.close()