# 이것은 주석!
print('안녕하세요.')
print('이름이 무엇인가요?')
myName = input()
print('만나서 반갑습니다. {} 님'.format(myName))
print('당신의 이름 길이는 {}자 입니다.'.format(len(myName)))
print('당신의 나이는 ?')
myAge = input()
print('당신은 내년에 '+str(int(myAge)+1)+'살 입니다.')