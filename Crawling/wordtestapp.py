import csv # 모듈 임포트
import time

my_wordbook = {} # 딕셔너리 정의
list_wronganswer = []
f= open('./my_wordbook.csv', 'r') # 파일열기
rdr = csv.reader(f) # 읽기

for row in rdr:
    word = row[0]
    meaning = row[1]
    my_wordbook[word] = meaning # 딕셔너리에 영단어(키)와 뜻(값) 넣기

for key in my_wordbook:
    your_answer = input(my_wordbook[key]+'\n') # 딕셔너리의 뜻 출력
    answer = key 
    if your_answer == answer: # 정답과 같은 영단어 입력시 
        print("Correct!")
    else: # 틀렸을 시
        print(f"Wrong! The answer is <{answer}>.\n")
        list_wronganswer.append(answer)

for wronganswer in list_wronganswer:
    print(wronganswer)

time.sleep(10)