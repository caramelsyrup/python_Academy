# 내장 함수
# # dir 객체가 가진 메소드를 보여준다.
# print(dir('1'))
# #len() 아이템 개수 세는 메소드
# print(len([1,2,3,4]))
# # max() min()
# print(max([1,2,3,4]))
# print(max("python"))
# print(max("한글이다"))
# # sum()
# A=[50,40,10]
# print(sum(A))
# print(sum(A)/len(A))

#함수 만들기
# def hello():
#   print('하이!')
#   print('안녕!')

# hello()  
# hello()  
# hello()  

# def hello(name):
#   print(name+'하이')
# hello('펭수')

# def hello(name):
#   print(name)
#   return 3
# print(hello('길동'))

# x=int(input("숫자를 입력하세요."))
# def is_odd(x):
#   if(x%2==0):
#     print("짝수입니다.")
#   else:
#     print("홀수입니다.")
#   return "끝"
# print(is_odd(x))

# def foo(*arg):
#   return sum(arg)/len(arg)
# print(foo(1,2,3))

# x=10  # 전역변수
# def foo():
#   print(x)
# foo()
# print(x)

# def fool():
#   y=10    # 지역변수
#   print(y)
# fool()

# def spam():
#   eggs = 99
#   bacon()
#   print(eggs)
# def bacon():
#   ham = 101
#   eggs = 0  
#   print(ham+eggs)
# spam()
# def div10(num):
#   try:
#     return 10/num
#   except ZeroDivisionError:
#     return 'ZeroDivisionError'
# print(div10(2))
# print(div10(0)) # 에러 발생
# print(div10(5))

# 숫자 맞추기 게임
# 랜덤숫자 생성
# i=1
# import random
# number = random.randint(10,20)
# print('안녕하세요. 10~20사이 숫자 맞춰보세요.')
# while True:
#   if(i<=5):
#     x=int(input('숫자를 써보세요.>>>'))
#     if(number==x):
#       print('정답입니다. {}번 만에 맞추었습니다.'.format(i))
#       break
#     elif(number>x):
#       i+=1
#       print('더 큰 수 입니다. 다시~')
#       continue
#     elif(number<x):
#       i+=1
#       print('더 작은 수 입니다. 다시~')
#       continue
#   else:
#     print('실패하셨습니다. 정답은 {} 입니다.'.format(number))
#     break
