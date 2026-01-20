#6장 반복문
#6.1 조건문 : 조건에 따라 분기하기
#6.1.1 if 문 : 조건이 하나일 때
weather = '비'

if weather == '비':  #대입 연산자(=)가 아닌 비교 연산자(==) 사용
    print('우산을 챙기세요.')


#6.1.2 elif 문 : 조건이 여러 개일 때
weather = '맑음'

if weather == '비':
    print('우산을 챙기세요.')

weather = '미세먼지'

if weather == '비':
    print('우산을 챙기세요.')  #1번
elif weather == '미세먼지' :
    print('마스크를 챙기세요.')  #2번


#6.1.3 else 문 : 모든 조건에 맞지 않을 때
weather = '맑음'

if weather == '비':
    print('우산을 챙기세요.')
elif weather == '미세먼지':
    print('마스크를 챙기세요.')
else :
    print('준비물이 필요 없어요.')


#6.1.4 input()으로 값 입력받아 비교하기
weather = input('오늘 날씨는 어때요?')

if weather == '비':
    print('우산을 챙기세요.')
elif weather == '미세먼지':
    print('마스크를 챙기세요.')
else:
    print('준비물이 필요 없어요.')

#조건 변경
if weather == '비' or weather == '눈':
    print('우산을 챙기세요.')
elif weather == '미세먼지' :
    print('마스크를 챙기세요.')
else :
    print('준비물이 필요 없어요.')

#정수 입력받기
temp = int(input('오늘 기온은 어때요? '))  #입력값을 정수형으로 형변환

if 30<=temp :  #30도 이상이면
    print('너무 더워요. 외출을 자제하세요.')
elif 10<=temp and temp<30 :  #10도 이상 30도 미만이면
    print('활동하기 좋은 날씨예요.')
elif 0<=temp and temp<10 :  #0도 이상 10도 미만이면
    print('외투를 챙기세요.')
else:  #그 외의 모든 경우(0도 미만이면)
    print('너무 추워요. 나가지 마세요.')

#간략히 작성하기
temp = int(input('오늘 기온은 어때요? '))

if 30 <= temp:
    print('너무 더워요. 외출을 자제하세요.')
elif 10 <= temp < 30:
    print('활동하기 좋은 날씨예요.')
elif 0 <= temp < 10:
    print('외투를 챙기세요.')
else :
    print('너무 추워요. 나가지 마세요.')

#<생략하기
temp = int(input('오늘 기온은 어때요?'))

if temp >= 30:
    print('너무 더워요. 외출을 자제하세요.')
elif temp >= 10:
    print('활동하기 좋은 날씨예요.')
elif temp >= 0:
    print('외투를 챙기세요.')
else:
    print('너무 추워요. 나가지 마세요.')



#6.2 반복문 : 같은 일 반복하기
#6.2.1 for 문 : 범위 안에서 반복하기
for waiting_no in [1,2,3,4,5]:
    print('대기번호 : {0}'.format(waiting_no))

for waiting_no in range(5):
    print('대기번호 : {0}'.format(waiting_no))

for waiting_no in range(1,6):
    print('대기번호 : {0}'.format(waiting_no))

for waiting_no in range(1, 6, 2):
    print('대기번호 : {0}'.format(waiting_no))

orders = ['아이언맨', '토르', '스파이더맨']  #손님 닉네임 리스트
for customer in orders:
    print('{0}님, 커피가 준비됐습니다. 픽업대로 와 주세요.'.format(customer))


#6.2.2 while 문 : 조건을 만족할 동안 반복하기
customer='토르'  #손님 닉네임
index = 5  #초깃값, 부르는 횟수 최대 5번

while index >= 1:  #부르는 횟숙 1 이상일 때만 실행
    print('{}님, 커피가 준비됐습니다.'.format(customer))
    index -= 1  #횟수 1회 차감
    print('{}번 남았어요.'.format(index))
    if index==0:  #5번 모두 불렀다면
        print('커피를 폐기 처분합니다.')

"""무한루프 -> Ctrl + C로 강제종료
customer='아이언맨'
index=1

while True:
    print('{0}님, 커피가 준비됐습니다. 호출 {1}회".format(customer, index))
    index += 1
"""

customer='토르'
person = None

while person != customer:
    print('{0}님, 커피가 준비됐습니다.'.format(customer))
    person = input('이름이 어떻게 되세요?')


#6.2.3 continue와 break : 흐름 제어하기
absent = [2,5] 
no_book = [7]

for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print('오늘 수업은 여기까지. {0}번 학생은 교무실로 따라와요.'.format(student))
        break
    print('{0}번 학생, 책을 읽어보세요.'.format(student))


#6.2.4 for 문 한 줄로 작성하기
students = [1,2,3,4,5]
print(students)

#한 줄 for 문으로 각 항목에 100 더하기
students = [i + 100 for i in students]
print(students)
"""의미 해석
studnets = [i + 100 for i in students]

students=[students[0]+100, studnets[1]+100, studnets[3]+100,
            studnets[4]+100, studnets[5]+100]

studnets=[1+100, 2+100, 3+100, 4+100, 5+100]
"""
#길이 정보로 리스트 변형
students = ['Iron man', 'Thor', 'Spider Man']
print(students)

students=[len(i) for i in students]
print(students)
"""의미해석
students=[len(studnets[0]), len(studnets[1]), len(students[2])]

students=[len('Iron man'), len('Thor'), len('Spider Man')]
"""
students = ['Iron man', 'Thor', 'Spider Man']
print(students)

#한 줄 for 문으로 각 이름을 모두 대문자로 변경
students = [i.upper() for i in students]
print(students)



#6.3 실습 문제 : 택시 승객 수 구하기
"""
문제 : 당신은 Cocoa 서비스를 이용하는 택시기사입니다.
손님이 총 50명일 때, 조건을 만족하는 총 탑승객 수를 구하는 프로그램 작성.

조건
1. 손님별 운행 소요시간은 5~50분으로 난수로 정한다.
2. 운행 소요시간 5~15분인 손님만 매칭한다.
3. 실행결과는 다음 형태로 출력하되, 매칭되면 [0], 매칭되지 않으면 []로 표시한다.

실행결과
[0] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[0] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 16분)
총 탑승객 : 2명
"""
from random import *

person = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5<=time<=15 :
        person += 1
        print(f'[0] {i}번째 손님 (소요시간 : {time})')
    else :
        print(f'[ ] {i}번째 손님 (소요시간 : {time})')
print(f'총 탑승객 : {person}명')



#셀프체크
"""
문제 : 편의점에서 동일한 상품 2개를 구매하면 상품 1개를 무료로 제공하는
2+1 이벤트를 진행하고 있습니다. 구매 상품 수에 따라 가격 계산하는 프로그램 작성

조건
1. 상품 1개의 가격은 1,000원이다.
2. 고객은 3, 6, 9, ...처럼 항상 3의 배수에 해당하는 상품을 구매한다고 가정한다.
3. 상품은 각각 스캔하며, 한 상품을 스캔할 때마다 '2+1 상품입니다.'를 출력한다.

실행결과
#구매 상품 수가 3개일 때
2+1 상품입니다.
2+1 상품입니다.
2+1 상품입니다.
총 가격은 2000원입니다.

#구매 상품 수가 6개일 때
2+1 상품입니다.
2+1 상품입니다.
2+1 상품입니다.
2+1 상품입니다.
2+1 상품입니다.
2+1 상품입니다.
총 가격은 4000원입니다.
"""
price = 1000
item = 3
total_price = 0

for i in range(1, item+1):
    print('2+1 상품입니다.')
    if i % 3 == 0:
        continue
    total_price += price
print('총 가격은 '+str(total_price)+'원입니다.')