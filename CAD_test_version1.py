import random

dict_order_shorcut = {
    "LINE" : "L",
    "CIRCLE" : "C",
    "ARC" : "A",
    "ERASE" : "E",
    "OFFSET" : "O",
    "TRIM" : "TR",
    "EXTEND" : "EX",
    "RECTANGLE" : "REC",
    "POLYGON" : "POL",
    "ELLIPES" :  "EL",
    "SPLINE" : "SPL",
    "HATCH" : "H",
    "POINT" : "PO",
    "CHAMFER" : "CHA",
    "FILLET" : "F",
    "MOVE" :  "M",
    "ROTATE" : "RO",
    "COPY" : "CO",
    "MIRROR" : "MI",
    "ARRAY" : "AR",
    "SCALE" : "SC",
    "STRETCH" : "NULL", # 단축키 없음
    "JOIN" : "J",
    "BREAK" : "BR",
    "MTEXT" : "T",
    "LENGTHEN" : "LEN",
    "EXPLODE" : "X",
    "ZOOM" : "Z",
    "LAYER" : "LA",
    "MATCHPROP" : "MA",
    "GRID" : "F7",
    "SNAP" : "F9",
    "ORTHO" : "F8",
    "OSNAP" : "F3",
    "REDRAW" : "R",
    "REDRAWALL" : "RA",
    "REGEN" : "RE",
    "REGENALL" : "REA",
    "UNDO" : "^Z", # 단축키 : Ctrl Z
    "CALCULATOR" : "CAL",
    "DIM" : "DIM",
    "DIMSTYLE" : "D",
    "DIMLINEAR" : "DIMLIN",
    "DIMALIGNED" : "DIMALI",
    "DIMANGULAR" : "DIMANG",
    "DIMDIAMETER" : "DIMDIA",
    "DIMRADIUS" : "DIMRAD",
    "DIMSCALE" : "NULL", # 단축키 없음
    "QLEADER" : "LE"
    }

order = list(dict_order_shorcut.keys()) # 키 값만 리스트에 넣음
random_order = random.shuffle(order) # 셔플 함수로 리스트의 요소를 무작위로 섞음
count_correct = 0
count_incorrect = 0
incorrect_answer = {}

# for test_shortcut in order: # 섞인 order(리스트)의 요소 test_shortcut 을 차례로 꺼냄
#     user = input(f"{test_shortcut} : ") # 명령어를 보여주고 단축키를 입력 받기
#     if user == dict_order_shorcut[test_shortcut]: # 사용자의 입력이 딕셔너리의 값과 일치하면 (정답이면)
#         continue # order의 다음 요소로 입력 받기 반복
#     else: # 틀린 경우
#         break # 종료
i = 0
while i < len(dict_order_shorcut): # 49번 반복
    for test_shortcut in order: # 섞인 order(리스트)의 요소 test_shortcut 을 차례로 꺼냄
        i+=1 # for문 한번 돌 때 마다 1씩 증가
        user = input(f"{test_shortcut} : ") # 명령어를 보여주고 단축키를 입력 받기
        if user == dict_order_shorcut[test_shortcut]: # 사용자의 입력이 딕셔너리의 값과 일치하면 (정답이면)
            count_correct += 1 # 맞은 개수 1씩 증가
            continue # order의 다음 요소로 입력 받기 반복
        else: # 틀린 경우
            count_incorrect += 1 # 틀린 개수 1씩 증가
            incorrect_answer[test_shortcut] = dict_order_shorcut[test_shortcut] # 틀린 문제를 명령어:단축키(정답) 형태로 저장
            print(incorrect_answer) # 틀린 문제 딕셔너리 출력
            print(f"맞은 개수 : {count_correct}, 틀린 개수 : {count_incorrect}") # 맞은 개수, 틀린 개수 출력
            continue 
     

