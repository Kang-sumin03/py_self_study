#10장 예외처리
#10.1 예외 처리하기
#10.1.2 예외 처리하기 : try-except 문

print('나누기 전용 계산기입니다.')
num1 = int(input('첫 번째 숫자를 입력하세요 : '))
num2 = int(input('두 번째 숫자를 입력하세요 : '))
print('{0} / {1} = {2}'.format(num1, num2, int(num1/num2)))

try:
    print('나누기 전용 계산기입니다.')
    num1 = int(input('첫 번째 숫자를 입력하세요 : '))
    num2 = int(input('두 번째 숫자를 입력하세요 : '))
    print('{0} / {1} = {2}'.format(num1, num2, int(num1/num2)))
except ValueError:
    print('오류 발생! 잘못된 값을 입력했습니다.')


#10.1.3 오류 메세지를 예외 처리로 출력하기 : as
try:
    print('나누기 전용 계산기입니다.')
    num1 = int(input('첫 번째 숫자를 입력하세요 : '))
    num2 = int(input('두 번째 숫자를 입력하세요 : '))
    print('{0} / {1} = {2}'.format(num1, num2, int(num1/num2)))
except ValueError:
    print('오류 발생! 잘못된 값을 입력했습니다.')
except ZeroDivisionError as err:
    print(err)

#리스트 만들어서 하기
try :
    print('나누기 전용 계산기입니다.')
    nums=[]
    nums.append(int(input('첫 번째 숫자를 입력하세요 : ')))
    nums.append(int(input('두 번째 숫자를 입력하세요 : ')))
    #nums.append(int(nums[0]/nums[1]))
    print('{0}/{1}={2}'.format(nums[0], num[1], nums[2]))
except ValueError:
    print('오류 발생! 잘못된 값을 입력했습니다.')
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print('알 수 없는 오류가 발생했습니다.')
    print(err)



#10.2 오류 발생시키기
try:
    print('나누기 전용 계산기입니다.')
    num1 = int(input('첫 번째 숫자를 입력하세요 : '))
    num2 = int(input('두 번째 숫자를 입력하세요 : '))
    if num1 >= 10 or num2 >= 10 :  #입력받은 수가 한 자리인지 확인
        raise ValueError
    print('{0} / {1} = {2}'.format(num1, num2, int(num1/num2)))
except ValueError:
    print('값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.')



#10.3 사용자 정의 예외 처리하기
class BigNumberError(Exception) : #사용자 정의 예외 처리, Exception 클래스 상속
    pass

try:
    print('한 자리 숫자 나누기 전용 계산기입니다.')
    num1 = int(input('첫 번째 숫자를 입력하세요 : '))
    num2 = int(input('두 번째 숫자를 입력하세요 : '))
    if num1 >= 10 or num2 >= 10 :  #입력받은 수가 한 자리인지 확인
        #raise ValueError
        raise BigNumberError
    print('{0}/{1}={2}'.format(num1, num2, int(num1/num2)))
except ValueError:
    print('값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.')
except BigNumberError:  #사용자 정의 예외 처리
    print('오류가 발생했습니다. 한자리 숫자만 입력하세요.')

class BigNumberError(Exception):  #사용자 정의 예외 처리, Exception 클래스 상속
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg
    
try:
    print('한 자리 숫자 나누기 전용 계산기입니다.')
    num1 = int(input('첫 번째 숫자를 입력하세요 : '))
    num2 = int(input('두 번째 숫자를 입력하세요 : '))
    if num1 >= 10 or num2 >= 10:  #입력받은 수가 한 자리인지 확인
        #자세한 오류 메세지
        raise BigNumberError('입력값 : {0}, {1}'.format(num1, num2))
    print('{0}/{1}={2}'.format(num1,num2,int(num1/num2)))
except ValueError:
    print('값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요')
except BigNumberError as err:  #사용자 정의 예외 처리
    print('오류가 발생했습니다. 한 자리 숫자만 입력하세요.')
    print(err)  #오류 메시지 출력

class BigNumberError(Exception):  #사용자 정의 오류
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return '[오류 코드 001]' + self.msg  #오류 메세지 가공
        
try:
    print('한 자리 숫자 나누기 전용 계산기입니다.')
    num1 = int(input('첫 번째 숫자를 입력하세요 : '))
    num2 = int(input('두 번째 숫자를 입력하세요 : '))
    if num1 >= 10 or num2 >= 10:  #입력받은 수가 한 자리인지 확인
        #자세한 오류 메세지
        raise BigNumberError('입력값 : {0}, {1}'.format(num1, num2))
    print('{0}/{1}={2}'.format(num1,num2,int(num1/num2)))
except ValueError:
    print('값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요')
except BigNumberError as err:  #사용자 정의 예외 처리
    print('오류가 발생했습니다. 한 자리 숫자만 입력하세요.')
    print(err)  #오류 메시지 출력



#10.4 오류와 상관없이 무조건 실행하기 : finally
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return '[오류 코드 001]' + self.msg
        
try:
    print('한 자리 숫자 나누기 전용 계산기입니다.')
    num1 = int(input('첫 번째 숫자를 입력하세요 : '))
    num2 = int(input('두 번째 숫자를 입력하세요 : '))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError('입력값 : {0}, {1}'.format(num1, num2))
    print('{0}/{1}={2}'.format(num1,num2,int(num1/num2)))
except ValueError:
    print('값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요')
except BigNumberError as err:
    print('오류가 발생했습니다. 한 자리 숫자만 입력하세요.')
    print(err)

finally:  #오류 발생 여부와 상관없이 항상 실행
    print('계산기를 이용해 주셔서 감사합니다.')



#10.5 실습 문제: 치킨 주문하기
"""
문제:항상 대기 손님이 많은 맛있는 치킨 가게가 있습니다. 손님들의 대기
    시간을 줄이고자 자동 주문 프로그램을 만들었습니다. 다음 코드를
    확인하고 적절한 예외 처리 구문을 추가하세요.

chicken = 10  #남은 치킨 수
waiting = 1  #대기번호, 1부터 시작

while True:
    print('[남은 치킨 :{0}]'.format(chicken))
    order = int(input('치킨을 몇 마리 주문하시겠습니까?'))
    
    if order > chicken:  #남은 치킨보다 주문량이 많을 때
        print('재료가 부족합니다.')
    else:
        print('[대기번호 {0}] {1}마리를 주문했습니다.'.format(waiting, order))
        waiting += 1  #대기번호 1 증가
        chicken -= order  #주문 수만큼 남은 치킨 감소

조건
1. 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리한다.
    [결과] 값을 잘못 입력했습니다.
2. 대기 손님이 주문할 수 있는 최대 주문량은 10마리로 제한한다.
3. 치킨 소진 시 오류(SoldOutError)를 발생시키고 프로그램을 종료한다.

결과
재료가 소진돼 더 이상 주문을 받지 않습니다.
"""
class SoldOutError(Exception):
    pass
chicken = 10  #냠은 치킨 수
waiting = 1  #대기번호, 1부터 시작

while True:
    try:
        print('[남은 치킨 : {0}]'.format(chicken))
        order = int(input('치킨을 몇 마리 주문하시겠습니까? '))
        if order > chicken:  #남은 치킨보다 주문량이 많을 때
            print('재료가 부족합니다.')
        elif order <= 0 :
            raise ValueError
        else:
            print('[대기번호 {0}] {1}마리를 주문했습니다.'.format(waiting, order))
            waiting += 1  #대기번호 증가
            chicken -= order  #주문 수만큼 남은 치킨 감소

        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print('잘못된 값을 입력했습니다.')
    except SoldOutError:
        print('재료가 소진돼 더 이상 주문을 받지 않습니다.')
        break



#셀프체크
"""
문제 : 배터리 잔량에 따라 스마트폰 배터리를 관리하는 프로그램을 만들어보세요.

조건
1. save_battery라는 이름으로 함수를 만든다.
2. 함수에는 배터리 잔량 정보인 level을 전달값으로 받으며, 별도의 반환값은 없다.
3. 함수를 호출하면 배터리 잔량을 출력한 뒤 잔량에 따라 동작을 수행한다.
    이때 함수 안에 적절한 예외 처리를 해서 프로그램이 비정상적으로 종료되지 않게 한다.
4. 배터리 잔량에 따른 동작은 다음과 같다.
    - 잔량 30% 초과 : 일반 모드
    - 잔량 5% 초과, 30% 이하 : 절전 모드
    - 잔량 5% 이하 : 종료(오류 발생)
5. 배터리 잔량이 5% 이하이면 종료 메세지를 담은 Exception 객체를
    생성해 오류를 발생시키고, 오류를 처리하는 곳에서 메세지가 출력되도록 한다.

#테스트 코드
save_battery(75)
save_battery(25)
save_battery(3)"""
def save_bettery(level):
    try:
        print(f'배터리 잔량 : {level}%')
        if level > 30 :
            print('일반 모드로 사용합니다.')
        elif level > 5:
            print('절전 모드로 사용합니다.')
        else:
            raise Exception("배터리가 부족해 스마트폰을 종료합니다")
    except Exception as e:
        print(e)
    print()

save_bettery(75)
save_bettery(25)
save_bettery(3)