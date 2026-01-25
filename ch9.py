#9장 클래스
#9.1 게임 소개
#보병 : 공격 유닛, 군인, 총을 쏠 수 있음
name='보병'  #이름
hp=40
damage=5

print('{} 유닛을 생성했습니다.'.format(name))
print('체력 {0}, 공격력 {1}\n'.format(hp, damage))  

#탱크 : 공격 유닛, 포를 쏠 수 있음, 두 가지 모드(일반/시지모드)
tank_name = '탱크'
tank_hp = 150
tank_damage = 35

print('{} 유닛을 생성했습니다.'.format(tank_name))
print('체력 {0}, 공격력 {1}\n'.format(tank_hp, tank_damage))

#새로운 탱크2 추가
tank2_name = '탱크'
tank2_hp = 150
tank2_damage = 35
print('{} 유닛을 생성했습니다.'.format(tank2_name))
print('체력 {0}, 공격력 {1}\n'.format(tank2_hp, tank2_damage))

#공격 함수
def attack(name, location, damage):
    print('{0} : {1} 방향 적군을 공격합니다.[공격력 {2}]'.format(name, location, damage))

attack(name, '1시', damage)  #보병 공격 명령
attack(tank_name, '1시', tank_damage)  #탱크 공격 명령
attack(tank2_name, '1시', tank2_damage)  #탱크2 공격 명령
print()



#9.2 클래스와 객체 생성하기
class Unit:  #클래스
    def __init__(self, name, hp, damage):  #메서드
        self.name=name  #인스턴스 변수 name에 전달값 name 저장
        self.hp=hp  #인스턴스 변수 hp에 전달값 hp 저장
        self.damage=damage  #인스턴스 변수 damage에 전달값 damage 저장
        print('{0} 유닛을 생성했습니다.'.format(self.name))
        print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))

#객체 생성(Unit 클래스의 인스턴스)
soldier1 = Unit('보병', 40, 5)  #보병1 생성, 전달값으로 이름/체력/공격력 전달
soldier2 = Unit('보병', 40, 5)  #보병2 생성, 전달값으로 이름/체력/공격력 전달
tank = Unit('탱크', 150, 35)  #탱크 생성, 전달값으로 이름/체력/공격력 전달


#9.2.1 생성자:init()
#에러 발생
#soldier3 = Unit('보병')  #전달값 3개 중 1개만 넘김


#9.2.2 인스턴스 변수
#전투기 : 공중 유닛, 은폐 불가
stealth1 = Unit('전투기', 80, 5)  #객체 생성, 체력 80, 공격력 5
#인스턴스 변수 접근
print('유닛 이름 : {0}, 공격력 : {1}'.format(stealth1.name, stealth1.damage))
#은폐 가능
stealth2 = Unit('업그레이드한 전투기', 80, 5)
#업그레이드한 전투기만을 위한 특별한 인스턴스 변수 정의, 은폐 상태
stealth2.cloaking=True  #은폐
if stealth2.cloaking == True:  #은폐 상태라면
    print('{0}는 현재 은폐 상태입니다.'.format(stealth2.name))
""" 에러 발생 : cloaking은 stealth2에만 해당하는 변수
if stealth1.cloaking == True :  #다른 전투기의 은폐 여부
    print('{0}는 현재 은폐 상태입니다'.format(stealth1.name))
"""


#9.2.3 메서드
class AttackrUnit:  #공격 유닛
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):  #전달받은 방향으로 공격
        print('{0} : {1} 방향 적군을 공격합니다. [공격력 {2}]'\
              .format(self.name, location, self.damage))

    def damaged(self, damage):  #damage만큼 유닛 피해
        #피해 정보 출력
        print('{0} : {1}만큼 피해를 입었습니다.'.format(self.name, damage))
        self.hp -= damage  #유닛의 체력에서 전달 받은 damage만큼 감소
        #남은 체력 출력
        print('{0} : 현재 체력은 {1}입니다.'.format(self.name, self.hp))
        if self.hp<=0:  #남은 체력이 0 이하이면
            print('{0} : 파괴됐습니다.'.format(self.name))  #유닛 파괴 처리

#객체 생성(AttackUnit 클래스의 인스턴스)
#화염방사병 : 공격 유닛, 화염방사기를 사용함
flamethrower1 = AttackrUnit('화염방사병', 50, 16)
#객체 생성, 체력 50, 공격력 16
flamethrower1.attack('5시')  #5시 방향으로 공격 명령
#25만큼의 공격을 2번 받음
flamethrower1.damaged(25)  #남은 체력 25
flamethrower1.damaged(25)  #남은 체력 0



#9.3 클래스 상속하기
#9.3.1 상속이란
#일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name=name
        self.hp=hp

#공격 유닛
class AttackUnit:
    def _init(self, name, hp, damage):
        self.name=name  #공통 부분
        self.hp=hp  #공통 부분
        self.damage=damage

class AttackUnit(Unit):  #Unit 클래스 상속
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)  #부모 클래스의 생성자 호출
        self.damage=damage
    

#9.3.2 다중 상속
#비행 가능
class Flyable:
    def __init__(self, flying_speed):  #비행 속도
        self.flying_speed=flying_speed

    def fly(self,name, location):  #유닛 이름, 비행 방향
        print('{0} : {1} 방향으로 날아갑니다 [속도 {2}]'\
              .format(name, location, self.flying_speed))
        
#다중 상속; FlyableAttackUnit(AttackUnit, Flyable):
#공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    #유닛 이름, 체력 공격력, 비행 속도
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)  #유닛 이름, 체력, 공격력
        Flyable.__init__(self, flying_speed)  #비행 속도

#요격기 : 공중 공격 유닛, 미사일 여러 발을 한 번에 발사
#유닛 이름, 체력, 공격력, 비행 속도
interceptor = FlyableAttackUnit('요격기',200,6,5)
interceptor.fly(interceptor.name, '3시')  #3시 방향으로 이동


#9.3.3 매서드 오버라이딩
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):  #speed 추가
        self.name=name
        self.hp=hp
        self.speed=speed  #지상 이동 속도

    def move(self, location):  #이동 동작 정의
        print('[지상 유닛 이동]')
        print('{0} : {1} 방향으로 이동합니다. [속도 {2}]'\
              .format(self.name, location, self.speed))
        
# 공격 유닛
class AttackUnit(Unit):  #Unit 클래스 상속
    def __init__(self, name, hp, damage, speed):  #speed 추가
        Unit.__init__(self, name, hp, speed)  #speed 추가
        self.damage = damage
    #(생략)

#공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0)  #지상 이동 속도 0
        Flyable.__init__(self, flying_speed)  #비행 속도

    def move(self, location):  #Unit 클래스의 move() 메서드를 오버라이딩
        print('[공중 유닛 이동]')
        self.fly(self.name, location)

#호버 바이크 : 지상 유닛, 기동성 좋음
hoverbike = AttackUnit('호버 바이크', 80, 20, 10)  #지상 이동 속도
#우주 순양함 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
spacecruiser = FlyableAttackUnit('우주 순양함',500,25,3) #비행 속도 3

hoverbike.move('11시')
#spacecruiser.fly(spacecruiser.name,'9시')
spacecruiser.move('9시')  #오버라이딩한 move() 메서드 호출



#9.4 동작 없이 일단 넘어가기 : pass
#건물 유닛
class BuildingUnit(Unit):
    def __init__ (self, name, hp, location):
        pass

#보급고 : 건물 유닛, 1개 건물 유닛 = 8유닛
supply_depot = BuildingUnit('보급고',500,'7시')  #체력 500, 생성 위치 7시

def game_start():
    print('[알림] 새로운 게임을 시작합니다.')

def game_over():
    pass

game_start()
game_over()



#9.5 부모 클래스 호출하기 : super()
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0)  #지상 이동 속도 0, 건물은 지상 이동 불가
        super().__init__(name, hp, 0)  #부모 클래스 접근, self 없이 사용
        self.location = location



#9.6 게임 완성
from random import *

#일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print('{0} 유닛을 생성했습니다.'.format(name))

    def move(self, location):
        print('{0} {1} 방향으로 이동합니다. [속도 {2}]'\
              .format(self.name, location, self.speed))
        
    def damaged(self, damage):
        print('{0} : {1}만큼 피해를 입었습니다.'.format(self.name, damage))
        self.hp -= damage
        print('{0} : 현재체력은 {1}입니다.'.format(self.name, self.hp))
        if self.hp<=0:
            print('{0} : 파괴했습니다.'.format(self.name))

#공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print('{0} : {1} 뱡향 적군을 공격합니다. [공격력{2}]'\
              .format(self.name,location,self.damage))

#보병 유닛
class Soldier(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, '보병', 40, 5, 1)  #이름, 체력, 공격력, 이동 속도

    #강화제 : 일정 시간 동안 이동 속도와 공격 속도 증가, 체력 10 감소
    def booster(self):
        if self.hp>10:
            self.hp-=10  #체력 10 소모
            print('{0} : 강화제를 사용합니다. (hp 10 감소)'.format(self.name))
        else:
            print('{0} : 체력이 부족해 기술을 사용할 수 없습니다.'.format(self.name))

#탱크 유닛
class Tank(AttackUnit):
    #시지 모드 : 탱크를 지상에 고정, 이동 불가, 공격력 증가
    siege_developed = False  #시지 모드 개발 여부

    def __init__(self):
        AttackUnit.__init__(self, '탱크', 150, 35, 1)  #이름, 체력, 공격력, 이동 속도
        self.siege_mode = False  #시지 모드 (해제 상태)
    
    #시지 모드 설정
    def set_siege_mode(self):
        if Tank.siege_developed == False:  #시지 모드가 개발되지 않았으면 바로 반환
            return
        #현재 일반 모드일 때
        if self.siege_mode == False:
            print('{0} : 시지 모드로 전환합니다.'.format(self.name))
            self.damage *= 2  #공격력 2배 증가
            self.siege_mode = True  #시지 모드 설정
        #현재 시지 모드일 때
        else :
            print('{0} : 시지 모드를 해제합니다.'.format(self.name))
            self.damage //= 2  #공격력 절반으로 감소
            self.siege_mode = False  #시지 모드 해제

#비행 가능
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print('{0} : {1} 방향으로 날아갑니다. [속도 {2}]'\
              .format(name, location, self.flying_speed))

#공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)

#전투기 유닛
class Stealth(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, '전투기', 80, 20, 5)
        self.cloaked = False  #은폐 모드 (해제 상태)
    
    #은폐 모드
    def cloaking(self):
        #현재 은폐 모드일 때
        if self.cloaked == True:
            print('{0} : 은폐 모드를 해제합니다.'.format(self.name))
            self.cloaked = False
        #현재 은폐 모드가 아닐때
        else:
            print('{0} : 은폐 모드를 설정합니다.'.format(self.name))
            self.cloaked = True

#게임 시작
def game_start():
    print('[알림] 새로운 게임을 시작합니다.')

#게임 종료
def game_over():
    print('Player : Good Game')
    print('[Player]님이 게임에서 퇴장했습니다.')

#실제 게임 진행
game_start()  #게임 시작

#보병 3기 생성
so1=Soldier()
so2=Soldier()
so3=Soldier()

#탱크 2기 생성
ta1=Tank()
ta2=Tank()

#전투기 1기 생성
st1=Stealth()

#유닛 일괄 관리(생성된 모든 유닛 추가)
attack_units=[]
attack_units.append(so1)
attack_units.append(so2)
attack_units.append(so3)
attack_units.append(ta1)
attack_units.append(ta2)
attack_units.append(st1)

#전군 이동
for unit in attack_units:
    unit.move('1시')

#탱크 시지 모드 개발
Tank.siege_developed = True
print('[알림] 탱크의 시지 모드 개발이 완료됐습니다.')

#공격 모드 준비(보병: 강화제, 탱크: 시지 모드, 전투기: 은폐 모드)
for unit in attack_units:
    if isinstance(unit, Soldier):  #Soldier 클래스의 인스턴스이면 강화제
        unit.booster()
    elif isinstance(unit, Tank):  #Tank 클래스의 인스턴스이면 시지 모드
        unit.set_siege_mode()
    elif isinstance(unit, Stealth):  #Stealth 클래스의 인스턴스이면 은폐 모드
        unit.cloaking()

#전군 공격
for unit in attack_units:
    unit.attack('1시')

#전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 20))  #피해는 무작위로 받음(5~20)

#게임 종료
game_over()



#9.8 실습 문제:부동산 프로그램 만들기
"""
문제 : 주어진 코드를 활용해 부동산 프로그램을 작성하세요.

조건
1. 생성자로 인스턴스 변수를 정의한다. 매물 정보를 표시하는
    show_detail() 메서드를 인스턴스 변수를 순서대로 출력한다.
2. 실행결과에 나온 3가지 매물을 객체로 만들고 총 매물수를 출력한 뒤
    show_detail() 메서드를 호출해 각 매물 정보를 표시한다.
class House:
    매물 초기화: 위치, 건물 종류, 매물 종류, 가격, 준공연도
    def __init__(self, location, house_type, deal_type, price, completion_year):
        pass
    
    #매물 정보 표시
    def show_detail(self):
        pass
    
결과
총 3가지 매물이 있습니다.
강남 아파트 매매 10억 원 2010년
마포 오피스텔 전세 5억 원 2007년
송파 빌라 월세 500/50만 원 2000년
"""
class House:
    #매물 초기화: 위치, 건물 종류, 매물 종류, 가격, 준공연도
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location=location
        self.house_type=house_type
        self.deal_type=deal_type
        self.price=price
        self.completion_year=completion_year
    
    #매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

houses=[]
hosue1=House('강남','아파트','매매','10억 원','2010년')
house2=House('마포','오피스텔','전세','5억 원', '2007년')
house3=House('송파', '빌라', '월세', '500/40만원', '2008년')

houses.append(hosue1)
houses.append(house2)
houses.append(house3)

print("총 {0}가지 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()



#셀프체크
"""
문제 : 주어진 코드를 활용해 주차 차량 등록 관리 프로그램을 작성하세요.

조건
1. 총 주차 가능 대수인 capacity는 객체를 생성할 때 전달받아 인스턴스
    변수로 정의한다.
2. 현재 등록된 차량 수를 관리하는 count는 객체를 생성할 때 0으로
    정의한다.
3. 객체를 생성할 때 등록 가능한 대수를 출력한다.
4. 차를 신규 등록하는 register() 메서드를 정의한다.
5. 신규 등록 시 등록 현황을 추력한다.
6. 총 주차 가능 대수를 초과하는 경우 '더 이상 등록할 수 없습니다.'라는
    메세지를 출력한다.
class ParkingManager:
    #주차 정보 초기화: 총 주차 가능 대수
    def __init__(self, capacity):
        pass
    
    #신규 차량 등록
    def register(self):
        pass
    
#테스트 코드
manage=ParkingManager(5)
for i in range(6):
    manager.register()
"""
class ParkingManager:
    #주차 정보 초기화: 총 주차 가능 대수
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        print(f'총 {capacity}대를 등록할 수 있습니다.')
    
    #신규 차량 등록
    def register(self):
        if self.count >= self.capacity:
            print('더 이상 등록할 수 없습니다.')
            return
        self.count += 1
        print(f'차량 신규 등록 ({self.count}/{self.capacity})')

manager=ParkingManager(10)
for i in range(10):
    manager.register()