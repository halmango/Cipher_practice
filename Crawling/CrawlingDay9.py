import requests
from bs4 import BeautifulSoup

keyword = input("뉴스 검색 키워드: ")
count = 0

for page in range(1, 3):
    news_url = 'https://search.hankyung.com/apps.frm/search.news?query=' + keyword + '&page=' + str(page)
    raw = requests.get(news_url)

    soup = BeautifulSoup(raw.text, 'html.parser')

    box = soup.find('ul', {'class' : 'article'})
    titles = box.find_all('em', {'class': 'tit'})

    dates = soup.find_all('span', {'class': 'date_time'})

    for title,date in zip(titles,dates):
        count += 1
        t = title.text
        d = date.text
        print(count,'-','[',d,']',t.strip())
        
