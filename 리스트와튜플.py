# 리스트[,,]]
# spam = ['개','고양이','박쥐','곰']
# print(spam)
# print(spam[0])
#print(spam[5]) 에러메시지
# for a in spam:
#   print(a)

#리스트에 또 리스트
# ham = [['고양이','강아지'],[10,20,30,40]]
# print(ham)
# print(ham[0]) # [],[] 중에 첫번째[]
# print(ham[0][1]) # 첫번쨰[] 중에서 '','' 중에서 두번째''
# print(ham[0][1][2]) # 첫번쨰[] 중에서 '','' 중에서 두번째''에서 단어의 세번째글자
# #print(ham[3]) 에러

#인덱스가 음수
# print(spam[-1]) # 음수는 뒤에서부터 순서를 센다
# print(spam[-3]) # 제일 오른쪽이 -1 이고 왼쪽으로 가면서 -2,-3식으로 나열

#슬라이싱
# print(spam[0:2])
# print(spam[2:]) # 0,1,2순서 이기에, 2에서부터 끝까지

#예제
# mylist=[1,3.14,"나날이"]
# print(mylist)
# print(mylist[2])

# 튜플
# 리스트와 유사, 값은 변경불가, 순서 존재.
# list1 = [1,2,3]
# list1[0] =9
# print(list1)  # list1의 0번쨰가 9로 바뀐것을 확인.
# tuple = (1,2,3)
# tuple[0] = 9 # 에러가 나는 부분. 바뀌지 않음
# print(tuple[2])

# 더하기 나열되는 순서가 길어짐
# list2 = list1 + list1
# print(list2)
# tuple2 = tuple+tuple
# print(tuple2)

# 곱하기
# list3 = list1*3
# print(list3)
# tuple3 = tuple*4
# print(tuple3)

# 길이 구하기
# print(len(list3))
# print(len(tuple3))

# 리스트의 메소드
# list1 = ['개','고양이','박쥐','곰']

# 추가 append()
# list1.append('양')
# list1.append('염소')
# print(list1)

# 빼기 pop()
# list1.pop() # 제일 오른쪽 요소 삭제
# list1.pop(0)  # 지정된 순서 번호의 요소 삭제
# list1.pop(3)
# print(list1)

# 리스트에 요소 추가
# list1.insert(2,'양')
# list1.insert(0,'말')
# print(list1)

# 아이템의 값으로 제거
# list1.remove('말')
# list1.remove('양')

# 값이 몇번째 있는지 확인
# print(list1.index('곰'))

# 리스트의 정렬
# list1 = [5,1,9,8]
# list1.sort()  # 오름차순 정렬
# list1.sort(reverse=True)  # 내림차순 정렬

# 딕셔너리, 키와 값이 쌍으로 이루어져 있음.
# print(type({}))
# dict1 ={}
# dict1[3]='c'
# dict1['b']=2

# mycat 만들기
# mycat = {'size':'small','color':'brown','skill':'sleeping'}
# print('사이즈는 '+mycat['size'])
# 인덱스 번호가 없고, 키값으로 벨류값을 얻음.

# 키값과 value값 구분
# print(list(mycat.keys())) # 리스트화 시킴
# print(mycat.values())

# 반복문을 사용해서 출력
# for k in mycat.keys():
#   print(k)
# for k,v in mycat.items():
#   print(k,v)

# get 메소드, 키 값이 있는 경우 리턴, 없는 경우 None을 리턴
# print(mycat.get('size'))
# print(mycat.get('이름')) # None리턴

# 문자카운트
# count = {}
# message = "메시가 바르셀로나에 이적 요청서를 제출했다. 축구 역사상 최고의 선수로 꼽히는 메시가 바르셀로나를 떠난다는 소식이 전해지자 벌써부터 차기 행선지를 두고 많은 추측이 쏟아지고 있다. 메시를 영입하기 위해선 막강한 자급력이 뒷받침되어야 하는 만큼 많은 클럽들이 거론되지는 않고 있다."
# for char in message:
#   count.setdefault(char,0)  # key가 없을떄는 작동. 0으로 초기화.
#   count[char] += 1 # char의 value값에 1을 누적시킴. char가 key값임.
# print(count)

