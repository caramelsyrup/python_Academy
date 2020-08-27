import json
import difflib  # 비슷한 단어를 찾는 라이브러리

data = json.load(open('data.json'))

# data안에 있는 단어(key)가 있으면 value를 출력.
def translate(word):
    if(word.lower() in data):
        return data[word.lower()]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.title() in data:
        return data[word.title()]
    else:
        # match에 리스트형태로 값이 저장
        match=difflib.get_close_matches(word,data.keys())
        if len(match)>0:
            print(f'입력한 단어가 {match[0]}인가요?')
            answer = input('맞으면 y, 아니면 n을 입력')
            if answer=='y':
                return data[match[0]]
        return 'check your spell'    
while True:    
    word = input("영어 단어 입력 :")
    output = translate(word)
    if type(output)==list:
        for item in output:
            print(item)
    else:
        print(output)        
   
   
        