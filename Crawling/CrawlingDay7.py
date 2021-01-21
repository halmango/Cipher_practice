from bs4 import BeautifulSoup #라이브러리에서 BeautifulSoup 메소드만 불러옴
import requests

lotto_url = 'https://dhlottery.co.kr/gameResult.do?method=byWin'
raw = requests.get(lotto_url)

#soup = BeautifulSoup(raw.text, 'html.parser') 
#print(soup)
#html 코드를 텍스트 형태로 가져온 다음 실제 코드로 변환

#soup = BeautifulSoup(raw.text, 'html.parser')

#box = soup.find('div', {'class' : 'nums'}) #html코드에서 <div class = 'num'> 찾기
#print(box)

soup = BeautifulSoup(raw.text, 'html.parser')

box = soup.find('div', {'class' : 'nums'})
numbers = box.find_all('span') #모든 span 태그로 감싸진 내용 찾기
#print(numbers)

#for number in numbers:
#    print(number)
#for문으로 정리해 줌

print('< 최근 로또 당첨 번호 >')
for number in numbers:
    print(number.text) #숫자만 출력