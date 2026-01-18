#5장 자료구조
#5.1 리스트
#5.1.1 리스트 생성하기

#지하철 칸별 10명, 20명, 30명 승차
subway1 = 10
subway2 = 20
subway3 = 30
#하나의 리스트로 표현하기
subway = [10,20,30]
print(subway)


#5.1.2 값 추가/삽입/삭제하기
subway = ['푸', '피글렛', '티거']
print(subway)

#index(); 피글렛이 몇 번째 칸에 탔는가?
print(subway.index('피글렛'))
#append(); 이요르 탑승
subway.append('이요르')
print(subway)
#insert(); 루를 푸와 피글렛 사이(인덱스 위치 1)에 삽입
subway.insert(1, '루')
print(subway)
#pop(); 지하철 역마다 한 명씩 내림
print(subway.pop())  #이요르 내림
print(subway)

print(subway.pop())  #티거 내림
print(subway)

print(subway.pop())  #피글렛 내림
print(subway)
#clear(); 지하철에서 모두 내림
subway.clear()
print(subway)


#5.1.3 중복 값 확인하기
#count(); 같은 이름이 몇 명 있는지 확인
subway = ['푸', '피글렛', '티거']
subway.append('푸')
print(subway)
print(subway.count('푸'))


#5.1.4 리스트 정렬하기
num_list = [5,2,4,3,1]
#sort(); 오름차순
num_list.sort()
print(num_list)
#sort(reverse=True); 내림차순
num_list.sort(reverse=True)
print(num_list)
#reverse(); 순서 뒤집기
num_list.reverse()
print(num_list)

##sorted(); 정렬된 리스트 새로 생성
my_list=[1,3,2]
print(my_list)

your_list=[1,3,2]
new_list = sorted(your_list)  #정렬할 리스트를 소괄호 안에 넣기
print(your_list)  #원본 데이터는 변경 X
print(new_list)


#5.1.5 리스트 확장하기
mix_list=['푸', 20, True, [5,2,4,3,1]]
print(mix_list)

#extend(); 리스트 합치기
mix_list=['푸', 20, True]
num_list=[5,2,4,3,1]
num_list.extend(mix_list)  #리스트 합치기
print(mix_list)
print(num_list)



#5.2 딕셔너리
#5.2.1 딕셔너리 생성하기
cabinet = {3: '푸', 100:'피글렛'}

#[]; key로 value 접근하기
print(cabinet[3])
print(cabinet[100])
#get()
print(cabinet.get(3))

#[] vs get()
print(cabinet.get(5))  #None
print("hi")
#print(cabinet[5])  #KeyError
print("hi")

#get(key, default=None)
print(cabinet.get(5,"사용가능"))
#in; key 유무로 True/False
print(3 in cabinet)
print(5 in cabinet)

#key에 문자열 넣기
cabinet={'A-3':'푸', 'B-100':'피글렛'}
print(cabinet['A-3'])
print(cabinet['B-100'])


#5.2.2 값 변경/추가/삭제
#[key]='변경/추가하려는 value'
cabinet['A-3'] = '티거'
cabinet['C-20'] = '이요르'
print(cabinet)
#del; key에 해당하는 value 삭제
del cabinet['A-3']
print(cabinet)


#5.2.3 값 확인하기
#keys(); key 확인하기
print(cabinet.keys())
#values(); value 확인하기
print(cabinet.values())
#items(); both 확인하기
print(cabinet.items())
#clear(); 초기화
cabinet.clear()
print(cabinet)



#5.3 튜플
menu = ('돈가스', '치즈 돈가스')
print(menu[0])
print(menu[1])

name='피글렛'
age=20
hobby='코딩'
print(name, age, hobby)

(name, age, hobby) = ('피글렛', 20, '코딩')
print(name, age, hobby)

#언패킹 활용
(departure, arrival) = ('김포', '제주')
print(departure, '>', arrival)
(departure, arrival) = (arrival, departure)
print(departure, '>', arrival)



#5.4 세트
my_set = {1,2,3,3,3}
print(my_set)

#{} vs set()
java={'푸','피글렛', '티거'}
python=set(['푸','이요르'])
#교집합; 자바와 파이썬을 모두 다룰 수 있는 개발자
print(java&python)
print(java.intersection())
#합집합; 자바 또는 파이썬을 다룰 수 있는 개발자
print(java|python)
print(java.union(python))
#차집합; 자바는 할 수 있지만 파이썬은 할 줄 모르는 개발자
print(java-python)
print(java.difference(python))

#add(); 파이썬 개발자 추가
python.add('피글렛')
print(python)
#remove(); 자바 개발자 삭제
java.remove('피글렛')
print(java)



#5.5 자료구조 변환하기
menu={'커피', '우유', '주스'}
print(menu)
print(type(menu))
menu=list(menu)  #리스트로 변환
print(menu, type(menu))
menu=tuple(menu)  #튜플로 변환
print(menu, type(menu))
menu=set(menu)  #세트로 변환
print(menu, type(menu))



#5.6 실습문제 : 당첨자 뽑기
"""
문제 : 파이썬 코딩 대회가 열립니다. 참석률을 높이기 위해
댓글 이벤트를 진행했습니다. 댓글 작성자 중에서 추첨을 통해 1명은
치킨 쿠폰, 3명은 커피 쿠폰을 주려고 합니다. 당첨자를 뽑는 추첨
프로그램을 작성하세요.

조건
1. 편의상 댓글은 20명이 작성했고, 아이디는 1~20이라고 가정한다.
2. 무작위로 추첨하되 중복은 허용하지 않는다.
3. random 모듈의 shuffle()과 smaple() 함수를 활용한다.
4. 실행결과는 다음과 같이 표시하고 치킨 당첨자 1명, 커피 당첨자 3명을 뽑는다.

실행결과
-- 당첨자 발표 --
치킨 당첨자 : 6
커피 당첨자 : [9, 3, 10]
-- 축하합니다! --
"""
from random import *

id=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(id)
choose=sample(id, 4)

print("-- 당첨자 발표 --")
print(f"치킨 당첨자 : {choose[0]}")
print(f"커피 당첨자 : {choose[1:]}")
print("-- 축하합니다 --")



#셀프체크
"""
문제 : 나도대학교에서 수강신청 기간에 시스템 오류로 일부 과목이 중복
신청되는 문제가 발생했습니다. 중복 과목을 없애는 프로그램을 작성하세요.

조건
1. 신청 과목은 리스트로 관리된다.
2. 리스트 같은 과목이 2번 이상 포함된 경우 1개만 남기고 나머지는 삭제한다.
3. 출력 시 신청 과목의 순서는 변경해도 괜찮다.

힌트
1. 자료구조는 서로 변환할 수 있습니다.
2. 세트는 중복을 허용하지 않습니다.
3. 세트는 데이터의 순서를 보장하지 않으므로 실행할 때마다 실행결과의 순서는 달라질 수 있습니다.

결과
#리스트에 '자료구조, 알고리즘, 자료구조, 운영체제'를 넣었을 때
신청한 과목은 다음과 같습니다.
['자료구조', '알고리즘', '운영체제']
"""

subject=['자료구조','알고리즘', '자료구조', '운영체제']
subject=set(subject)
subject=list(subject)
print('신청한 과목은 다음과 같습니다.')
print(subject)