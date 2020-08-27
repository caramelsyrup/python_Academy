#문제1
# def add(a,b):
#   result = 0
#   result = a+b
#   print("{} + {} = {}".format(a,b,result))
# add(10,5)

# 문제2
# def add(a,b):
#   return a+b
# print(add(10,5))

# 문제3
# rainbow=['빨','주','노','초','파','남','보']
# first_color = rainbow[0]
# print('무지개의 첫번째 색깔은 {}이다'.format(first_color))

# 문제4
# rainbow=['빨','주','노','초','파','남','보']
# last_color = rainbow[-1]
# print('무지개의 첫번째 색깔은 {}이다'.format(last_color))

# 문제5
# list1 = [1,2,3]
# list1.append(4)
# print(list1)
# list = [1,2,3]
# list +=[4]
# print(list)

# 문제6
# number = [1,2,3,4,5]
# n = 5
# if n in number:
#   print('{}가 리스트에 있다.'.format(n))
# else:
#   print('{} 숫자를 확인하세요.'.format(n))

# 문제7
# list1 = [1,2,3]
# list1.remove(2)
# del list1[1]
# print(list1)

# 문제8
# days_in_month = {'1월':31,'2월':28,'3월':31}
# print(days_in_month)

# 문제9
# dict = {
#   '이름':'홍길동','번호':1010,'취미':["낮잠","숨쉬기","커피"]
# }
# print(dict)

# 문제10
# days_in_month = {'1월':31,'2월':28,'3월':31}
# days_in_month['2월']=29
# print(days_in_month)

# 문제11
# days_in_month = {'1월':31,'2월':28,'3월':31,'-1월':97845461}
# # days_in_month.pop('-1월')
# # del days_in_month['-1월']
# print(days_in_month)

# 문제12
# days_in_month = {'1월':31,'2월':28,'3월':31,'4월':30,'5월':31}
# for key in days_in_month.keys():
#   print(key)

# 문제13
# days_in_month = {'1월':31,'2월':28,'3월':31,'4월':30,'5월':31}
# for key,value in days_in_month.items():
#   print('{}은 {}일이 있습니다.'.format(key,value))

# 문제14
# import random
# list=['빨','주','노','초','파','남','보']
# random_element = random.choice(list)
# print(random_element)

# 문제15
# import random
# random_number = random.randint(2,5)
# print(random_number)

# 문제16
# import random
# list=['빨','주','노','초','파','남','보']
# random.shuffle(list)
# print(list)

# 문제17
# import datetime
# print(datetime.date.today())

# 문제18
# string1 = "다스베이더가 말했다.\n \"내가 니 애비다!\"\n 그 말을 들은 루크는 \'깜짝\'놀랐다."
# a=list(string1.split())
# print(a[4])

# 문제19
# day = [31,29,31,30,31,30,31,31,30,31,30,31]
# for i in range(0,12):
#   print('{}월의 날짜수는 {}입니다.'.format(i+1,day[i]))

# 문제20
# a,b=23,5
# div=a//b
# print("a를 b로 나눈 몫은 {}입니다.".format(div))

# 문제21
# numbers = [1,2,3]
# length = len(numbers)
# i = 0
# while i<length:
#   print(numbers[i])
#   i+=1

# 문제22
# size=[33,35,34,37,32,35,39,32,35,39]
# for i,size in enumerate(size):
#   if size == 32:
#     print("사이즈 32인 바지는 {}번쨰에 있다.".format(i+1))
#     break

# 문제23
# try: 
#   a=3/0
#   print(a)
# except Exception:
#   print("0으로 나눌수 없습니다.")

# 문제24
# try:
#   a=5
#   b=0
#   c=a/b
# except Exception as ex:
#   print('다음과 같은 에러가 발생 : ',ex)

# 문제25
# shop = {
#   "송일문방구":{"가위":500,"크레파스":3000},
#   "알파문구":{"풀":800,"도화지":300,"A4용지":8000},
#   "다이소":{"풀":500,"목공본드":2000,"화분":3000}
#   }
# for shop,product in shop.items():
#   for product,price in product.items():
#     if product=="풀":
#       print("{} : {} 원".format(shop,price))

# 문제26
# if[]: print("[]는 true입니다.")
# if[1,2,3]: print("[1,2,3]는 true입니다.")
# if{}: print("{}는 true입니다.")
# if{'abc':1}: print("{'abc':1}는 true입니다.")
# if 0: print("0는 true입니다.")
# if 1: print("1는 true입니다.")

# 문제27
# a = 1 or 10
# b = 0 or 10
# print("a:{}, b:{}".format(a,b))

# 문제28
# list1 = [1,2,3,4]
# list1.insert(1,8)
# print("첫 번째 자리에 8을 넣은 결과 : {}".format(list1))
# list1.sort()
# print("list1을 작은 수부터 큰 수로 정렬한 결과 : {}".format(list1))
# list1.reverse()
# print("list1을 큰 수부터 작은 수로 정렬한 결과 : {}".format(list1))

# 문제29
# str="오늘은 날씨가 흐림"
# words = list(str.split())
# position=words.index('흐림')
# print(position)
# words[position] ="맑음"
# new_str = " ".join(words)
# print(new_str)

# 문제30
# list=['빨','주','노','초','파','남','보']
# red_color = list[:3]
# print(red_color)
# blue_color = list[4:]
# print(blue_color)