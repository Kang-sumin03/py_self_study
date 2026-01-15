"""
3. 연산자
3.1 연산자의 종류
"""
#3.1.1 산술 연산자
print(1+1) #덧셈
print(3-2) #뺄셈
print(5*2) #곱셈
print(6/3) #나눗셈

print(2*3) #거듭제곱
print(10%3) #나머지 출력
print(10//3) #몫 출력


#3.1.2 비교 연산자
#True/False로 출력
print(10 > 3) #10이 3보다 크다
print(4 >= 7) #4가 7보다 크거나 같다
print(10 < 3) #10이 3보다 작다
print(5 <= 5) #5가 5보다 작거나 같다

print(3==3) #3과 3이 같다
print(4==2) #4와 2가 같다
print(3+4==7) #3+4의 결과가 7과 같다
print(1!=3) #1과 3이 다르다


#3.1.3 논리 연산자
print((3>0)and (3>5)) #3은 0보다 크고, 5보다 크다
print((3>0)or(3>5)) #3은 0보다 크거나, 5보다 크다
print(not(1 != 3)) #1은 3과 다르지 않다



#3.2 연산자의 우선순위
print(2+3*4) #14
print((2+3)*4) #20



#3.3 변수로 연산하기
number=2+3*4
print(number)
number=2+3*4+2
print(number)

number=2+3*4
print(number)
number=number+2  #(2+3*4)+2
print(number)

number=2+3*4
print(number)
number +=2  #number=number + 2와 동일
print(number)

number -= 2  #number=number - 2와 동일
print(number)
number *= 2  #number=number * 2와 동일
print(number)
number /= 2  #number=number / 2와 동일
print(number)
number **= 2  #number=number ** 2와 동일
print(number)
number //= 2  #number=number // 2와 동일
print(number)
number %= 2  #number=number % 2와 동일
print(number)



#3.4 함수로 연산하기
#3.4.1 숫자 처리 함수
print(abs(-5)) #-5의 절대값
print(pow(4,2)) #4를 제곱한 값
print(max(5,12)) #5와 12 중 큰 값
print(min(5,12)) #5와 12 중 작은 값
print(round(3.14)) #3.14를 소수점 이하 첫째 자리에서 반올림한 정수
print(round(4.678,2)) #4.678을 소수점 이하 셋째 자리에서 반올림한 값


#3.4.2 math 모듈
#from 모듈명 import 기능
from math import * #math 모듈의 모든 기능을 가져다 쓰겠다

result=floor(4.99)
print(result) #4.99의 내림
result=ceil(3.14)
print(result) #3.14의 올림
result=sqrt(16)
print(result) #16의 제곱근

#import 모듈명
import math #math 모듈의 모든 기능을 가져다 쓰겠다

#math.을 함께 작성
result=math.floor(4.99)
print(result) #4.99의 내림
result = math.ceil(3.14)
print(result) #3.14의 올림
result=math.sqrt(16)
print(result) #16의 제곱근


#3.4.3 random 모듈
from random import * #random 모듈의 모든 기능을 가져다 쓰겠다

print(random())
print(random())
print(random())

print(random()*10)  #0.0 이상 10.0 미만에서 난수 생성
print(int(random()*10))  #0 이상 10 미만 정수에서 난수 생성(random() 결과를 int()로 감싸서 정수로 변환)
print(int(random()*10)+1)  #1 이상 11 미만 정수에서 난수 생성 (random() 결과를 정수로 변환해 1을 더함)

print(int(random()*45+1))  #1 이상 46 미만 정수에서 난수 생성
print(randrange(1,46))  #1 이상 46 미만에서 난수 생성
print(randint(1,45))  #1 이상 45 이하에서 난수 생성



#3.5 실습 문제 : 스터디 날짜 정하기
"""
문제 : 코딩스터디 모임이 월 4번 모인다. 
3번은 온라인으로, 1번은 오프라인으로 모이기로 했다.
오프라인 모임 날짜를 정하는 프로그램을 작성해라.

조건
1. 날짜를 무작위로 뽑는다.
2. 월별 일수가 다르므로 최소 일수인 28일 이내로 정한다.(28까지만 날짜 선정).
3. 매월 1~3일은 스터디를 준비해야 하므로 제외한다.
4. 실행결과는 다음과 같은 형태로 나와야 한다.
(단, 날짜는 무작위이므로 책과 결과가 다를 수 있다.)

결과
오프라인 스터디 모임 날짜는 매월 18일로 선정됐습니다.
"""
#from random import * -> 빼먹은 코드
date=randrange(4,29)
print("오프라인 스터디 모임 날짜는 매월 "+str(date)+"일로 선정됐습니다.")



#셀프체크
"""
문제 : 연산자를 이용해 온도 단위를 변환하는 프로그램을 만들어 보세요.

조건
1. 섭씨 온도를 저장하기 위한 변수를 만든다.
2. 다음 공식을 이용해 섭씨 온도를 화씨 온도로 변환하고 새로운 변수에 저장한다.
    화씨 온도=(섭씨 온도*9/5)+32
3. 섭씨 온도와 화씨 온도를 다음과 같이 출력한다.

결과
#섭씨 온도가 30도일 때
섭씨 온도 : 30
화씨 온도 : 86.0

#섭씨 온도가 10도일 때
섭씨 온도 : 10
화씨 온도 : 50.0
"""
C=30
F=(C*9/5)+32
print("섭씨 온도 :",C)
print("화씨 온도 :", F)