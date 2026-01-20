# 7장 함수
#7.1 함수 정의하기
#7.1.1실습 : 은행 계좌 개설하기
def open_account():
    print('새로운 계좌를 개설합니다.')

open_account()



#7.2 전달값과 반환값
#7.2.1 실습 : 입금하기
def deposit(balance, money):  #입금 처리 함수
    print('{0}원을 입금했습니다. 잔액은 {1}원입니다.'.format(money, balance+money))
    return balance + money  #입금 후 잔액 정보 반환

balance = 0  #초기 잔액
balance = deposit(balance, 1000)  #1,000원 입금


#7.2.2 실습 : 출금하기
def withdraw(balance, money):  #출금 처리 함수
    if balance >= money :  #잔액이 출금액보다 많으면
        print('{0}원을 출금했습니다. 잔액은 {1}원입니다.'.format(money, balance-money))
        return balance-money  #출금 후 잔액 반환
    else :
        print('잔액이 부족합니다. 잔액은 {0}원입니다.'.format(balance))
        return balance  #기존 잔액 반환
    
balance = 0  #초기 잔액
balance = deposit(balance, 1000)  #1,000원 입금

#출금
balance = withdraw(balance, 2000)  #2,000원 출금 시도
balance = withdraw(balance, 500)  #500원 출금 시도


#7.2.3 실습 : 수수료 부과하기
def withdraw_night(balance, money):  #업무 시간 외 출금
    commission = 100  #출금 수수료 100원
    print('업무 시간 외에 {}원을 출금했습니다.'.format(money))
    return commission, balance-money-commission

balance=0  #초기 잔액
balance=deposit(balance,1000)  #1,000원 입금

#업무 시간 외 출금 시도
commission, balance = withdraw_night(balance, 500)
print('수수료 {0}원이며, 잔액은 {1}원입니다.'.format(commission, balance))



#7.3 함수 호출하기
#7.3.1 기본값 사용하기
def profile(name, age, main_lang):
    print('이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}'.format(name, age, main_lang))

profile('찰리', 20, '파이썬')
profile('루시', 25, '자바')

def profile(name, age=20, main_lang='파이썬'):  #age,main_lang 기본값 설정
    print('이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}'.format(name, age, main_lang))

profile('찰리')  #age, main_lang 기본값 사용
profile('찰리', 22,)  #main_lang은 기본값 사용
profile('찰리', 24, '자바')  #기본값 사용 X


#7.3.2 키워드 인자 사용하기
def profile(name, age, main_lang):  #키워드 인자 : name, age, main_lang
    print(name, age, main_lang)

profile(name='찰리', main_lang='파이썬', age=20) #키워드 인자o, 순서 상관 x
profile(main_lang='자바', age=25, name='루시')

profile('찰리', age=20, main_lang='파이썬')
#profile(name='루시', 25, '파이썬') -> 키워드 인자 먼저 작성 = error


#7.2.3  가변 인자 사용하기
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print('이름 : {0}\t나이 : {1}\t'.format(name, age))
    print(lang1, lang2, lang3, lang4, lang5)

profile('찰리', 20, '파이썬', '자바', 'C', 'C++', 'C#')
profile('루시', 25, '코틀린', '스위프트', '', '', '')

def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    #줄 바꿈 대신 띄어쓰기
    print('이름 : {0}\t나이 : {1}\t'.format(name, age),end=' ')
    print(lang1, lang2, lang3, lang4, lang5)

profile('찰리', 20, '파이썬','자바','C','C++','C#')
profile('루시', 25, '코틀린', '스위프트', '','','')

#가변인자
def profile(name, age, *language):
    print('이름 : {0}\t나이 : {1}\t'.format(name, age),end=' ')
    print(language, type(language))

profile('찰리',20,'파이썬','자바','C','C++','C#','자바스크립트')
profile('루시',25,'코틀린','스위프트')

#튜플 활용하기; for문
def profile(name, age, *language):
    print('이름 : {0}\t나이 : {1}\t'.format(name, age),end=' ')
    #print(language, type(language))
    for lang in language:
        print(lang, end=' ')  #언어를 모두 한 줄에 표시
    print()  #줄 바꿈 목적

profile('찰리', 20, '파이썬', '자바', 'C', 'C++', 'C#', '자바스크립트')
profile('루시', 25, '코틀린', '스위프트')



#7.4 변수의 범위 : 지역변수와 전역변수
"""  전역변수를 함수 내에서 쓰면 error
glasses = 10

def rent(people):
    glasses = glasses-people
    print('[함수 내부] 남은 3D 안경 개수 : {0}'.format(glasses))

print('전체 3D 안경 개수 : {0}'.format(glasses))
rent(2)
print('남은 3D 안경 개수 : {0}'.format(glasses))
"""

glasses = 10

def rent(people):
    glasses = 20  #변수 정의 추가
    glasses = glasses-people
    print('[함수 내부] 남은 3D 안경 개수 : {0}'.format(glasses))

print('전체 3D 안경 개수 : {0}'.format(glasses))
rent(2)
print('남은 3D 안경 개수 : {0}'.format(glasses))  #지역변수 glasses 값이 전역변수 glasses에 저장 되지 않음

glasses=10

def rent(people):
    global glasses  # 전역변수 glasses를 함수 안에서 사용하겠다
    glasses=glasses-people
    print('[함수 내부] 남은 3D 안경 개수: {0}'.format(glasses))

print('전체 3D 안경 개수 : {0}'.format(glasses))
rent(2)
print('남은 3D 안경 개수 : {0}'.format(glasses))

glasses=10

def rent_return(glasses, people):  #전체3D 안경 수, 대여 관객 수
    glasses=glasses-people  #전달값을 담은 glasses 사용
    print('[함수 내부] 남은 3D 안경 개수 : {0}'.format(glasses))
    return glasses

print('전체 3D 안경 개수 : {0}'.format(glasses))
glasses=rent_return(glasses,2)
print('남은 3D 안경 개수 : {0}'.format(glasses))



#7.5 실습 문제 : 표준 체중 구하기
"""
문제 : 표준 체중을 구하는 프로그램을 작성하세요.
    표준 체중 : 키에 따른 평균 체중
    성별에 따른 표준 체중 공식
    남자 : 키(m) X 키(m) X 22
    여자 : 키(m) X 키(m) X 21
    
조건
1. 표준 체중은 별도 함수로 계산한다, 단, 키는 미터(m) 단위로 받는다.
    함수명 : std_weight
    전달값 : 키(height), 성별(gender)
2. 실행결과에서 표준 체중은 소수점 이하 둘째 자리까지 표시한다

실행결과
키 175cm 남자의 표준 체중은 67.38"""

height = 1.75
gender = '남자'

def std_weight(height, gender):
    if gender == '남자' :
        weight = height*height*22
        return weight
    else :
        weight = height*height*21
        return weight
weight = round(std_weight(height,gender), 2)
print(f'키 {100*height}cm인 {gender}의 표준체중은 {weight}')



# 셀프체크
"""
문제 : 미세먼지 수치를 입력받아 대기질 상태를 출력하는 함수를 만들어 보세요.

조건
1. get_air_quality라는 이름으로 함수를 만든다.
2. 이 함수는 전달값으로 미세먼지 수치를 입력받는다.
3. 이 함수는 대기질 상태를 반환한다.
4. 미세먼지 수치에 따른 대기질 상태는 다음과 같다.
    좋음 : 0~30
    보통 : 31~80
    나쁨 : 81~150
    매우 나쁨 : 151이상
5. 함수에 전달되는 전달값은 항상 0 이상의 값이라고 가정한다.

실행결과
#print(get_air_quality(15))
좋음
#print(get_air_quality(85))
나쁨
"""

def get_air_quality(air):
    if air >= 151 :
        quality='매우 나쁨'
        return quality
    elif air >= 81:
        quality='나쁨'
        return quality
    elif air >= 31:
        quality='보통'
        return quality
    else :
        quality = '좋음'
        return quality

print(get_air_quality(15))
print(get_air_quality(85))