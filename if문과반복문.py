 # #if문
# name='Alice'
# if name =='Alice' : 
#   print('반가워요 '+name)
#   print('여기도 출력?')
# print('종료') #여기는 참,거짓 모두 실행되는 부분

# #if else 문
# if name == '':
#   print('참')
# else :
#   print('거짓')
#   print('거짓')
#   print('거짓')
# print('종료')

# name=input('이름을 입력하세요.')
# if name=="":
#    print('이름을 입력하지 않았습니다.')
# else :
#  print('당신의 이름은 '+name+'입니다.')
# if bool(name):
#   print('당신의 이름은 '+name+'입니다.')
# else :
#   print('이름을 입력하지 않았습니다.')
# if name:
#   print('당신의 이름은 '+name+'입니다.')
# else :
#   print('이름을 입력하지 않았습니다.')

# while 반복문
# count = 0
# while count<3:
#   print('횟수:',count)
#   count += 1
# treehit=0
# while treehit<10:
#   treehit+=1
#   print(f'나무를 {treehit}번 찍습니다.')
#   if treehit == 10:
#     print('나무가 넘어 갑니다.')

# continue, break
# count =0
# while count <10:
#   count +=1
#   if count <4:
#     continue
#   if count ==8:
#     break
# print(count)
# coffee = 10
# while True:
#   money = int(input('돈을 넣어 주세요.'))
#   if money == 300:
#     print('커피를 줍니다.')
#     coffee -=1
#     break
#   elif money<=(coffee*300):
#       quantity = int(money/300)
#       money = money%300
#       print('거스름돈 %d 원을 주고 커피를 %a 잔 줍니다.'%(money,quantity))
#       coffee -= quantity
#       print('현재 커피는 %s 잔 남아 있습니다.'%coffee)
#   else:
#     print('돈을 반환하고 커피는 주지 않습니다.')
#     print('현재 커피는 %s 개입니다.' %(coffee))
#     break
#   if coffee == 0:
#     print('커피가 다 떨어졌습니다. 판매중지!')
#     break      

# for 반목문
# for num in [1,2,3]:
#   print(num)

# for ch in '홍길동':
#   print(ch)

# animals =["dog","cat","lion","tiger"]
# for animal in animals:
#   print(animal)

# # range() 괄호안의 숫자 전까지 범위 설정. 0부터숫자까지. -1도
# for n in range(3):
#   print(n)

# # (start,stop)
# for nn in range(4,6):
#   print(nn)

# 구구단 2단 출력
# for i in range(2,10):
#   for j in range(1,10):
#     print('{}x{}={}'.format(i,j,j*i),end=" ")
#   print()

#연습문제

# 예제1
# a ="Life is too short, you need python"
# if "wife"in a: print("wife")
# elif "python" in a and "you" not in a: print("python")
# elif "shirt" not in a: print("shirt")
# elif "need" in a: print("need")
# else: print("none")

# 예제2
# i=1
# sum=0
# while i<=1000:
#   if(i%3==0):
#     sum+=i
#   i+=1
# print(sum)

# 예제3
# for i in range(1,6):
#   while i>0:
#     print("*",end="")
#     i-=1
#   print()  
# for i in range(6):
#   print('*'*i)

# 예제4
# A =[70,60,55,75,95,90,80,80,85,100]
# len(A)
# total=0
# for score in A:
#   total+=score
# avg =total/len(A)
# print(avg)

# 리뷰문제
# print("Hello World")
# x = 1000
# y = "일이삼사오"
# z = 1.2345
# print(x,y,z) 
# print("신씨가 소리질렀다.\"도둑이야\".")
# print("안녕하세요.\n만나서\t반갑습니다.")
# x,y=10,3
# print("%.3f"%(x/y))
# x=int(input("정수입력:"))
# y=int(input("정수입력:"))
# print('합은 : {} 입니다.'.format(x+y))
# for x in range(10):
#   x='x'
#   print(x,end='')
# x=int(input("정수입력:"))
# y=int(input("정수입력:"))
# print('first number:{}'.format(x))
# print('second number:{}'.format(y))
# print('add:{}'.format(x+y))
# print('sub:{}'.format(x-y))
# print('mul:{}'.format(x*y))
# print('div:{}'.format(x/y))
# div=48584
# term=36
# print('총금액은 {}원'.format(div*term))
# name=input("이름?:")
# color=input("컬러?:")
# print('안녕하세요. 제이름은 {}이고 좋아하는 색상은 {}입니다.'.format(name,color))
