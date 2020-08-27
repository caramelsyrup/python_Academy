# 파일을 읽을때는 f
f = open("fruits.txt",encoding="utf-8")
# print(f.read())
# print(f.read()) 
# # 두번 코드를 작성해도, 한번만 출력. 
# # 첫번째 코드실행되고나서 커서가 이미 파일의 끝에 위치해있음.
# # 그래서 두번째 코드에서는 읽을 내용이 없음.
# content = f.read() # 변수에 내용을 저장하고, 연속하여 쓴다.
# f.close()       # 파일을 열어서 사용을 했으면, 반드시 닫아준다.
# print(content)
# print(content)
# print(content)

# 자동으로 파일 닫는 with open
# with open("fruits.txt",encoding="utf-8") as f:
#     content = f.read()
# print(content)

# 파일을 쓸떄는 w 없으면 생성시킴
# with open("view.txt","w",encoding="utf-8") as f:
#     f.write('무\n')
#     f.write('배추\n')
#     f.write('마늘\n')
#     f.write('양파\n')
#     f.write('대파\n')

# 파일의 마지막에 추가내용 a
# with open("view.txt","a",encoding="utf-8") as f:
# #    f.write('다마내기\n')
#     f.write('고추가루\n')

# 파일 쓰기, 읽기, 덧붙이기 모두 가능
# with open("view.txt","a+",encoding="utf-8") as f:
#     f.write('마지막 붙여쓰기\n') # 커서가 맨 마지막에 있음.
#     f.seek(0)           # 커서를 0번째로 이동(제일 처음).
#     content = f.read()  # 그래서 읽어도 공백만 읽는 경우를 방지.
# print(content)

# 예제
# with open("fruits.txt",encoding="utf-8") as f:
#     content1 = f.read()
# with open("view.txt",encoding="utf-8") as g:
#     content2 = g.read()    
# with open("fruitnVegi.txt","a+",encoding="utf-8") as w:
#     w.write(content1)
#     w.write(content2)
#     w.seek(0)
#     content3 = w.read()
# print(content3)