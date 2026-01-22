#8장 : 입출력
#8.1 input():표준 입력받기
answer=input('아무 값이나 입력하세요 : ')
print('입력한 값은 '+answer+'입니다.')
print(type(answer))  #<class 'str'>
print(type(int(answer)))  #<class 'int'>
answer=10
print(type(answer))  #<class 'int'>
#변수에 숫자 넣기 vs input()함수로 숫자 넣기



#8.2 표준 출력 시 유용한 기능
#8.2.1 sep:구분자 넣기
#sep 기본값=' '
print('파이썬','자바')
print('파이썬'+'자바')
print('파이썬','자바',sep=',')

print('파이썬','자바','자바스크립트')
print('파이썬','자바','자바스크립트',sep=' VS ')  #값을 VS로 구분


#8.2.2 end:문장 끝 지정하기
#end 기본값=\n
print('파이썬', '자바', sep=',', end='? ')
print('무엇이 더 재미있을까요?')


#8.2.3 file:출력 위치 지정하기
import sys

print('파이썬', '자바', file=sys.stdout)  #표준 출력
print('파이썬', '자바', file=sys.stderr)  #표준 오류


#8.2.4 ljust()와 rjust():공간 확보해 정렬하기
#딕셔너리와, for문으로 과목 및 점수 출력하기
scores={'수학':0, '영어':50, '코딩':100}

for subject, score in scores.items():  #(key, value)
    print(subject, score)

#과목 왼쪽 정렬, 점수 오른쪽 정렬
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=':')


#8.2.5 zfill():빈간 0으로 채우기
#자릿값 고려 X
for num in range(1,21):
    print('대기번호 : '+str(num))

#자릿값 고려 O
for num in range(1,21):
    print('대기번호 : '+str(num).zfill(3))



#8.3 format():다양한 형식으로 출력하기
print('{0}'.format(500))
#빈칸으로 두기, 오른쪽 정렬, 공간 10칸 확보
print('{0: >10}'.format(500))

#빈칸으로 두기, 오른쪽 정렬, + 기호 붙이기, 공간 10칸 확보
print('{0:>+10}'.format(500))
print('{0:>+10}'.format(-500))  #음수일 때
#빈칸을 _로 채우기, 왼쪽 정렬, 공간 10칸 확보
print('{0:_<10}'.format(500))

#쉼표 넣기
print('{0:,}'.format(100000000000)) # 3자리마다 쉼표 찍기
print('{0:+,}'.format(100000000000))  #+기호 붙이기, 3자리마다 쉼표 찍기
print('{0:+,}'.format(-100000000000))  #음수일 때, 3자리마다 쉼표 찍기

#빈칸 ^로, 왼쪽 정렬, +기호 붙이기, 공간 30칸, 3자리마다 쉼표 찍기
print('{0:^<+30,}'.format(100000000000))

#실수 출력
print('{0}'.format(5/3))
print('{0:f}'.format(5/3))  #6자리까지 출력
print('{0:.2f}'.format(5/3))  #2자리까지 출력



#8.4 파일 입출력
#8.4.1 open(), close():파일 열고 닫기
#score.txt 파일을 쓰기 모드로 열기
score_file = open('score.txt', 'w', encoding='utf8')
print('수학 : 0', file=score_file)  #score.txt 파일에 내용 쓰기
print('영어 : 50', file=score_file)  #score.txt 파일에 내용 쓰기
score_file.close()  #score.txt 파일 닫기


#8.4.2 write():파일 쓰기
#score.txt 파일에 이어쓰기 모드로 열기
score_file = open('score.txt', 'a', encoding='utf8')
#write() 함수는 줄 바꿈이 없으므로 \n 추가
score_file.write('과학 : 80\n')
score_file.write('코딩 : 100\n')
score_file.close()


#8.4.3 read(), readline(), readlines():파일 읽기
#read()_파일 전체 읽기
score_file=open('score.txt', 'r', encoding='utf8')
print(score_file.read())
score_file.close()

#readline()_한줄씩 읽기
score_file=open('score.txt','r',encoding='utf8')

print(score_file.readline(),end='')  #한 줄씩 읽어 오고 커서는 다음 줄로 이동
print(score_file.readline(), end='')  #end 값을 설정해 줄 바꿈 중복 수행 방지
print(score_file.readline(), end='')
print(score_file.readline(), end='')

score_file.close()

#readline()_while문 활용
score_file=open('score.txt', 'r', encoding='utf8')

while True:
    line=score_file.readline()
    if not line:  #더 이상 읽어 올 내용이 없을 때
        break  #반복문 탈출
    print(line, end='')  #읽어 온 내용 출력

score_file.close()

#readlines()_for문 활용
score_file=open('score.txt', 'r', encoding='utf8')

lines=score_file.readlines()  #파일에서 모든 줄 읽어와 리스트 형태로 저장
for line in lines:  #lines에 내용이 있을 때까지
    print(line, end='')

score_file.close()



#8.5 pickle 모듈:데이터를 파일로 저장하기
#dump()함수
import pickle  #pickle 모듈 가져다 쓰기

profile_file=open('profile.pickle', 'wb')  #바이너리 형태로 저장
profile={'이름':'스누피', '나이':30, '취미':['축구','골프','코딩']}
print(profile)
pickle.dump(profile, profile_file)  #profile 데이터를 파일에 저장
profile_file.close()  #파일 닫기

profile_file = open('profile.pickle', 'rb')  #읽어올 때도 바이너리 형태 명시
profile=pickle.load(profile_file)  #파일에 있는 정보 불러와 profile에 저장

print(profile)
profile_file.close()



#8.6 with 문:파일 한 번에 열고 닫기
#기존 파일 불러오기
import pickle

with open('profile.pickle', 'rb') as profile_file:
    print(pickle.load(profile_file))

#새로운 파일 만들기
import pickle

with open('study.txt','w',encoding='utf8') as study_file:
    study_file.write('파이썬을 열심히 공부하고 있어요.')

with open('study.txt', 'r', encoding='utf8') as study_file:
    print(study_file.read())



#8.7 실습 문제:보고서 파일 만들기
"""
문제 : 회사에서 매주 1회 보고서를 작성하라고 합니다.
      1주차부터 50주차까지 보고서 파일을 만드는 프로그램을 작성.

조건
1. 파일명은 '1주차.txt', '2주차.txt', ...로 만듭니다.
   완성코드를 실행하면 소스코드와 동일한 위치에 다음과 같이
   50개 파일을 생성합니다
   1주차.txt
   2주차.txt
   ...
   49주차.txt
   50주차.txt
2. 각 파일에는 각 주차에 해당하는 내용이 다음 형태로 포함.

결과
#35주차.txt 파일 내용
- 35주차 주간보고 -
부서 :
이름 :
업무 요약 :
"""
for i in range(1,51):
    with open(str(i)+'주차.txt','w',encoding='utf8') as report_file:
        report_file.write('- {0}주차 주간 보고 -\n'.format(i))
        report_file.write('부서 : \n')
        report_file.write('이름 : \n')
        report_file.write('업무 요약:')



#셀프체크
"""
문제 : 나도 유치원에는 각 반의 이름, 연령, 인원 정보가 띄어쓰기로
구분되어 한 줄에 정리된 파일이 있습니다. 파일 내용을 읽어 와서 각
반의 정보를 출력하는 프로그램을 작성하세요.

조건
1. 다음 내용을 넣어 텍스트 파일을 생성한다.
    이때 텍스트 파일명은 class.txt로 한다.
    [파일 내용] 초록반 5세 20명 파랑반 6세 18명 노랑반 7세 22명
2. 생성한 파일을 읽어 와서 내용을 각각 빈칸으로 구분해 출력한다.
    단, 구분을 위해 문자열 함수 중 하나인 split()을 활용한다.
3. 정보가 '명'으로 끝나는 경우 줄 바꿈한다.
    단, 확인을 위해 문자열 함수 중 하나인 endswith()를 활용한다.

결과
초록반 5세 20명
파랑반 6세 18명
노랑반 7세 22명
"""
with open('class.txt','w',encoding='utf8') as class_file:
    class_file.write('초록반 5세 20명 파랑반 6세 18명 노랑반 7세 22명')

with open('class.txt', 'r', encoding='utf8') as class_file:
    class_list=class_file.read()
    words=class_list.split()
    for word in words:
        print(word, end=' ')
        if word.endswith('명'):
            print()