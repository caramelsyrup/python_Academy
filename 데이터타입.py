#기본 데이터 타입
int     #정수
float   #실수
bool    #불린(참,거짓)
str     #문자
list    #배열
tuple
set
dict    #none dictionary
None    # null

# 숫자
# type() 자료형 리턴
# print(2+4)
# print(2-4)
# print(2*4)
# print(2/4)
# print(type(2+4))
# print(type(2-4))
# print(type(2*4))
# print(type(2/4))

# # 제곱 나누기
# # 거듭제곱
# print(2**4)
# # 나누기 몫
# print(10//4)
# # 나누기 나머지
# print(10%3)

# # math 수학 함수
# # 반올림
# num = round(3.14235567,5)
# print(num)

# # 절대값
# num1 = abs(-50)
# print(num1)

# # 계산 순서
# print(num1-70+2**5)
# print(num1+(-70+2)**5)
# # () , **, *, +, -

# # 이진수 변환 bin
# # print(bin(0))
# # print(bin(1))
# # print(bin(2))
# # print(bin(5))

# # 변수
# iq = 190 # 메모리에 숫자 190은 2진수로 바꿔서 저장됨.
# print(iq)

# # 여러개의 변수 초기화
# a,b,c=1,2,3
# print(a)
# print(b)
# print(c)
# #예제1
# 놀이기구 = "자이로드롭"
# print(놀이기구)
# #21살 = 1,2,3,4  
# 살21 = 1,2,3,4
# print(살21)
# #이름★ = "박써니"
# 이름="박써니"
# print(이름)
# _myname = "홍길동"
# print(_myname)

# #예제2
# x = 10
# print(x)
# #예제3
# x,y,z = 1,2,3
# print(x+y+z)
# #예제4
# x,y,z = 1,0.23,'name'
# print(type(x))
# print(type(y))
# print(type(z))

#문자열 데이터 str
# print(type("문자열"))
# var1 = '한따옴표'
# var2 = "쌍따옴표"
# print("문자열은 "+var1+var2)
# print("문자열은",var1,var2)
# # 따옴표가 3개씩 ''' """
# var3 = '''
# 따옴표 3개는 문장 모두를 문자열로 처리
# ************************
# '''
# print(var3)
# # 문자열 + 연산
# 성 = '홍'
# 이름 = "길동"
# name = 성+" "+이름
# print(name)

# 타입 변환 str(),int(),float()
# num = input("숫자하나 변환:")
# print(int(num)+10)

#이스케이프 시퀀스
# weather = "it\'s \"kind of\" sunny"
# print(weather)
#예제1
# weather = "\t it\'s \"kind of\" sunny \n Have a nice day!"
# print(weather)
# #예제2
# string1 ="다스베이더가 말했다.\n\"내가 니 애비다!\"\n그 말을 들은 루크는 \'깜짝\'놀랐다."
# print(string1)

# # 문자열 f-string
# name = '홍길동'
# age = 20

# #일반적인 +사용
# print('안녕하세요 '+name+"님 나이가 "+str(age)+"이군요")

# # f-string사용
# print(f'안녕하세요 {name}님 나이가 {age}이군요')

# # 자바의 printf 방식
# print("안녕하세요 %s님 나이가 %d이군요"%(name,age))

#문자열.format() 함수 방법
# number = 20
# welcome = '환영합니다.'
# base = '{}번 손님 {}'
# print(base.format(number,welcome))
# print('{}번 손님 {}'.format(number,welcome))
#예제1
# name = 'seo'
# color = 'navy'
# base = '안녕하세요. 제이름은 {}이고 좋아하는 색상은 {}입니다.'
# print('안녕하세요. 제이름은 {}이고 좋아하는 색상은 {}입니다.'.format(name,color))
# print(base.format(name,color))
# print(f'안녕하세요. 제이름은 {name}이고 좋아하는 색상은 {color}입니다.')

# 문자열 인덱스, 순서는 0번부터
# String1 = '0123456789'
# print(String1[0])

# 문자열 슬라이싱
# print(String1[0:3])
# print(String1[:3])
# print(String1[3:])

# 시작:끝:증감
# print(String1[::2])
# print(String1[::-1])
# print(String1[::-2])
# String2 = 'god'
# print(String2[::-1])
# #예제
# rainbow = ["빨","주","노","초","파","남","보"]
# red_colors = rainbow[:3]
# print("red_colors 의 값 : {}".format(red_colors))
# blue_colors = rainbow[4:]
# print("red_colors 의 값 : {}".format(blue_colors))

# 문자열의 변경불가(부분적 변경은 불허)
# string1 = '123'
# string1[0] = '9'

#len(문자열) 문자열 길이. 내장함수
# print(len(String1))

# bool형 참,거짓
# bool1 = True
# bool2 = False
# bool3 = 1<3
# bool4 = 1==2
# print(bool1,bool2,bool3,bool4)
# x,y=1,2
# print(x>y)
# print(x!=y)
# print(bool(1))
# print(bool(0))
# print(bool('True'))
# print(bool('안녕'))
# print(type('name'))
# print(type(0))
# print(type(0.0))
# print(type([1,2,3,4]))
# print(type(1==0)) # 알아서 바로 참거짓 판단

# 논리 연산자
# and
print(True and True)
print(True and False)
print(False and True)
print(False and False)

#or
print(True or True)
print(True or False)
print(False or True)
print(False or False)

#not
print(not True)
print(not False)