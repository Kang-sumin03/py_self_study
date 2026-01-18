#4장 문자열
#4.1 문자열이란
sentence1 = '나는 소년입니다.'
print(sentence1)

sentence2 = "파이썬은 쉬워요."
print(sentence2)

print(sentence1, type(sentence1))
print(sentence2, type(sentence2))

sentence3="""
나는 소년이고,
파이썬은 쉬워요.
"""
print(sentence3)



#4.2 슬라이싱
#인덱싱
jumin='990229-1234567'
print('성별 식별번호 : '+jumin[7]) 

#슬라이싱1
print("연 : "+jumin[0:2])  #0부터 2직전까지(0,1)
print("월 : "+jumin[2:4])  #2부터 4직전까지(2,3)
print("일 : "+jumin[4:6])  #4부터 6직전까지 (4,5)

#슬라이싱2
print("생년월일 : "+jumin[:6])  #처음부터 6직전까지->jumin[0:6]
print("주민등록번호 뒷자리 : "+jumin[7:])  #7부터 끝까지->jumin[7:14]

#슬라이싱3; 역순으로
print("주민등록번호 뒷자리 : "+jumin[-7:]) #뒤에서 7번째 위치부터 끝까지



#4.3 함수로 문자열 처리하기
python='Python is Amazing'

print(python.lower()) #전체 소문자로 변환
print(python.upper()) #전체 대문자로 변환
print(python[0].isupper()) #인덱스 0에 있는 값이 대문자인지 확인
print(python[1:3].islower()) #인덱스 1부터 2에 있는 값이 소문자인지 확인
print(python.replace("Python", "Java")) #Python을 Java로 바꾸기

#find() vs index(); 없을 때 -1 vs error
find=python.find('n')
print(find)
find=python.find('n', find+1)
print(find)
find=python.find("Java")
print(find)

index = python.index('n')
print(index)
index = python.index('n', index+1)
print(index)
index = python.index('n', 2,6)
print(index)
#index = python.index('Java')
#print(index)

#count(); 문자 세기
print(python.count('n'))
print(python.count('v'))

#len(); 문자열 길이
print(len(python))



#4.4 문자열 포매팅
#4.4.1 서식 지정자; %
print('나는 %d살입니다.' %20)
print('나는 %s을 좋아합니다.' %"파이썬")
print('Apple은 %c로 시작해요.' %"A")
print('나는 %s살입니다.' %20)  #%s로도 정숫값 표현 가능

print('나는 %s색과 %s색을 좋아해요.' %('파란', '빨간')) #값 여럿


#4.4.2 format() 함수
#only 값
print('나는 {}살입니다'.format(20))
print('나는 {}색과 {}색을 좋아해요.'.format('파란', '빨간'))
print('나는 {0}색과 {1}색을 좋아해요.'.format('파란', '빨간'))
print('나는 {1}색과 {0}색을 좋아해요.'.format('파란', '빨간'))

#이름-값
print('나는 {age}살이며, {color}색을 좋아해요.'.format(age=20, color='빨간'))
print('나는 {age}살이며, {color}색을 좋아해요.'.format(color='빨간', age=20))


#4.4.3 f-문자열
age=29
color='빨간'
print(f'나는 {age}살이며, {color}색을 좋아해요.')



#4.5 탈출 문자
#4.5.1 줄바꿈; \n
#한 문장
print('백문이 불어일견 백견이 불여일타')
""" error
print("백문이 불어일견
백견이 불여일타")
"""
#탈출문자; 두 문장
print('백문이 불여일견\n백견이 불여일타')


#4.5.2 문자열 내 따옴표 넣기; \"와 \'
""" error
print('저는 '나도코딩'입니다.')
"""
#두 종류 따옴표 쓰기
print('저는 "나도코딩"입니다.')
print("저는 '나도코딩'입니다.")
#탈출문자; 따옴표 넣기
print('저는 \'나도코딩\'입니다.')
print("저는 \'나도코딩\'입니다.")


#4.5.3 파일 경로 출력; \\
#error
#print("C:\Users\mpmsm\OneDrive\바탕 화면\PythonWorkspace)
#탈출문자; \\
#print('C:\\Users\\mpmsm\\OneDrive\\바탕 화면\\PythonWorkspace')
#r 붙이기
#print(r'C:\Users\mpmsm\OneDrive\바탕 화면\PythonWorkspace')


#4.5.4 \r
#커서 맨 앞으로 보내기(\r뒤 어절을 맨 앞 어절에 덮어쓰기)
print("Red Apple\rPine")


#4.5.5 \b
#백스페이스
print('Redd\bApple')


#4.5.6 \t
#Tab
print("Red\tApple")



#4.6 실습문제 : 비밀번호 만들기
"""
문제 : 사이트별로 비밀번호를 생성하는 프로그램을 작성하세요.
    http://naver.com
    http://daum.net
    http://google.com
    http://youtube.com

조건
1. http:// 부분은 제외한다.
2. 처음 만나는 점(.)이후 부분도 제외한다.
3. 남은 글자 중 처음 세 자리 + 글자 개수 + 글자 내 'e'개수 +'!'로 구성한다.
4. 프로그램을 실행했을 때 실행결과는 다음 형태로 나와야 한다.

결과
http://naver.com의 비밀번호는 nav51!입니다.

예시
1. http://부분 제외 -> naver.com
2. 처음 만나는 점 이후 부분 제외 -> naver
3. 남은 글자 중 처음 세자리(nav) + 글자 개수(5) + 글자 내 'e'의 개수(1) + (!)
"""

n="http://naver.com"
d="http://daum.net"
g="http://google.com"
y="http://youtube.com"

remove_http=n.replace('http://', "")
remove_com=remove_http[:remove_http.index(".")]
password=remove_com[:3]+str(len(remove_com))+str(remove_com.count("e"))+"!"
print(f'{n}의 비밀번호는 {password}입니다.')



#셀프체크
"""
문제 : 영어 문장의 첫글자는 대문자로, 나머지는 모두 소문자로
변환하는 프로그램을 작성하세요.

결과
#주어진 문장 : the early bird cathches the worm.
The early bird catches the worm.

#주어진 문장 : Actions Speak Louder Than Words.
Acotions speak Louder Than Words.

#주어진 문장 : PRACTICE MAKES PERFECT.
Practice makes perfect.
"""

#sentence="the early bird catches the worm."
sentence="Actions Speak Louder Than Words."
#sentence="PRACTICE MAkes PERFECT."

#change_sentence=sentence.upper(sentence[0])+sentence.lower(sentence[1:])
change_sentence=sentence[0].upper()+sentence[1:].lower()
print(change_sentence)