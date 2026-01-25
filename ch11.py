#11장 모듈과 패키지
#11.1 모듈 다루기
#11.1.1 모듈 만들기

#11.1.2 모듈 사용하기
import theater_module  #모듈 가져오기

theater_module.price(3)  #3명이 영화를 보러 갔을 때 가격
theater_module.price_morning(4)  #4명이 조조 영화를 보러 갔을 때 가격
theater_module.price_soldier(5)  #군인 5명이 영화를 보러 갔을 때 가격

import theater_module as mv  #theater_module을 별명인 mv로 사용한다는 의미

mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import *  #theater_module에서 모든 기능을 가져와 사용함
price(3)  #theater_module.을 작성할 필요 없음
price_morning(4)
price_soldier(5)

#일부 함수만 import해서 사용하기
from theater_module import price, price_morning
price(3)
price_morning(4)
#price_soldier(5)  import하지 않아서 사용 불가

#price_soldier를 별명인 price로 대체 사용
from theater_module import price_soldier as price
price(5)  #price_solider() 함수 호출



#11.2 패키지 다루기
#11.2.1 패키지 만들기
#11.2.2 패키지 사용하기
import travel.thailand  #travel 패키지의 thailand 모듈 가져오기

trip_to=travel.thailand.ThailandPackage()
trip_to.detail()

#travel.thailand 모듈에서 ThailandPackage 클래스 가져오기
from travel.thailand import ThailandPackage

trip_to=ThailandPackage()  #from-import 문에서는 travel.thailand. 제외
trip_to.detail()

from travel import vietnam  #travel 패키지에서 vietnam 모듈 가져오기

trip_to=vietnam.VietnamdPackage()  #travel. 생략
trip_to.detail()



#11.3 모듈 공개 설정하기 : __all__
from travel import *

trip_to = vietnam.VietnamdPackage()  #베트남
trip_to.detail()

trip_to = thailand.ThailandPackage()  #태국
trip_to.detail()



#11.4 모듈 직접 실행하기
from travel import *

trip_to = thailand.ThailandPackage()
trip_to.detail()



#11.5 패키지와 모듈 위치 확인하기
import inspect
import random

print(inspect.getfile(random))  #random 모듈 위치(경로)

import inspect
from travel import *

print(inspect.getfile(thailand))  #thailand 모듈 위치