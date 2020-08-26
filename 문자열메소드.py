# 문자열 메소드
# 대 소문자
# string1 ='HellO world'
# print(string1.upper())
# print(string1.lower())
# print(string1)
# print("title title".title()) # 단어의 첫글자를 대문자로

# 문자개수세기
# print(string1.count('wor'))
# print(string1.count('l'))

# 잰말놀이
# String2 = "신춘 샹송쇼를 샹글리라 호텔에서 연 샹송가수 송샹성씨가 저기 저 미트 소시지 소스 스파게티는 깐쇼새우 크림 소스 소시지 소스 스테이크보다 비싸다며 단식에 들어가 호텔의 빈축을 사고 있습니다."
# print(String2.count('샹'))
# print(String2.count('소'))

# 알파벳, 숫자, 공백 인지 확인
# print('hell0'.isalpha())
# print('hello'.isalpha())  # 문자만 있을시
# print('hell0'.isalnum())  # 문자와 숫자가 결합시
# print('0'.isdecimal()) # 자연수만 0 포함
# print(' '.isspace())  # 공백 여부

# 시작과 끝을 체크
# print('hello'.startswith('h'))
# print('hello'.startswith('d'))
# print('hello'.endswith('o'))

# 문자열 삽입 join
# print(','.join('abcd'))
# print('=:='.join(['1','b','c','4']))
# print('-'.join(['2020','05','20']))

# 문자열 나누기 split()
# print("2020-05-20".split('-')) # -를 기준으로 문자열이 나눠져서 리스트가 형성
# print("2020 05 20".split()) # 기본이 공백을 기준.

# 공백제거(입력을 받을 떄)
# print(' 하이 '.strip()) # 문자 중간의 공백은 아님.

# 문자열 바꾸기
# a = "인생은 짧다."
# print(a.replace("인생은","하루가"))