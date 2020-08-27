# def mult_two(a, b):
#     #함수를 완성시킨다.
#     return a*b

# if __name__ == '__main__':
#     print(mult_two(3, 2))
    
#     # 다음과 같이 리턴결과가 나와야 한다.
#     assert mult_two(3, 2) == 6
#     assert mult_two(1, 0) == 0

# def easy_unpack(elements):
#     return (elements[0],elements[2],elements[-2])  # 튜플로 리턴

# if __name__ == '__main__':
#     print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))
#     print(easy_unpack((1, 1, 1, 1)))
#     print(easy_unpack((6, 3, 7)))

#     # 다음과 같이 리턴결과가 나와야 한다.
#     assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
#     assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
#     assert easy_unpack((6, 3, 7)) == (6, 7, 3)

# def first_word(text):
#   return text.split()[0]

# if __name__ == '__main__':
#     print(first_word("Hello world"))
#     print(first_word("a word"))
#     print(first_word("hi"))
    
#     # 다음과 같이 리턴결과가 나와야 한다.
#     assert first_word("Hello world") == "Hello"
#     assert first_word("a word") == "a"
#     assert first_word("hi") == "hi"

# def is_acceptable_password(password):
#     if (len(password)>6):
#         return True
#     else:
#         return False     
    
# if __name__ == '__main__':
#     print(is_acceptable_password('short'))
#     print(is_acceptable_password('muchlonger'))
#     print(is_acceptable_password('ashort'))
#     # 다음과 같이 리턴결과가 나와야 한다.
#     assert is_acceptable_password('short') == False
#     assert is_acceptable_password('muchlonger') == True
#     assert is_acceptable_password('ashort') == False

# def number_length(a):
#     return len(str(a))

# if __name__ == '__main__':
#     print(number_length(10))
#     print(number_length(0))
#     print(number_length(4))
#     print(number_length(44))

#     # 다음과 같이 리턴결과가 나와야 한다.
#     assert number_length(10) == 2
#     assert number_length(0) == 1
#     assert number_length(4) == 1
#     assert number_length(44) == 2

# def backward_string(val):
#     return val[::-1]

# if __name__ == '__main__':
#     print(backward_string('val'))
#     print(backward_string(''))
#     print(backward_string('ohho'))
#     print(backward_string('123456789'))
#     # 다음과 같이 리턴결과가 나와야 한다.
#     assert backward_string('val') == 'lav'
#     assert backward_string('') == ''
#     assert backward_string('ohho') == 'ohho'
#     assert backward_string('123456789') == '987654321'

# def remove_all_before(items, i):
#     try:
#         items.index(i)
#         return items[items.index(i):]
#     except ValueError:
#         return items
     
# if __name__ == '__main__':
#     print(list(remove_all_before([1, 2, 3, 4, 5], 3)))
#     print(list(remove_all_before([1, 1, 2, 2, 3, 3], 2)))
#     print(list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)))
#     print(list(remove_all_before([1, 1, 5, 6, 7], 2)))
#     print(list(remove_all_before([], 0)))
#     print(list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)))

#     # 다음과 같이 리턴결과가 나와야 한다.
#     assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
#     assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
#     assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
#     assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
#     assert list(remove_all_before([], 0)) == []
#     assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]

# def is_all_upper(text):
#     if(text.isspace()):
#         return True
#     elif(text.isupper()):
#         return True
#     elif(text.strip()==''):
#         return True
#     else:
#         return False            
    
# if __name__ == '__main__':
#     print(is_all_upper('ALL UPPER'))
#     print(is_all_upper('mixed UPPER and lower'))
#     print(is_all_upper('all lower'))
#     print(is_all_upper(''))

#     # 다음과 같이 리턴결과가 나와야 한다.
#     assert is_all_upper('ALL UPPER') == True
#     assert is_all_upper('all lower') == False
#     assert is_all_upper('mixed UPPER and lower') == False
#     assert is_all_upper('') == True

# def replace_first(items):
#     try:
#         items.append(items[0])
#         items.remove(items[0])
#         return items
#     except:
#         return items
  
# if __name__ == '__main__':
#     print(list(replace_first([1, 2, 3, 4])))
#     print(list(replace_first([1])))
#     print(list(replace_first([])))

#     # 다음과 같이 리턴결과가 나와야 한다.
#     assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
#     assert list(replace_first([1])) == [1]
#     assert list(replace_first([])) == []

def max_digit(number):
    list = [int(i) for i in str(number)]
    maxnum = max(list)
    return maxnum

if __name__ == '__main__':
    print("Example:")
    print(max_digit(0))
    print(max_digit(52))
    print(max_digit(634))
    print(max_digit(1))
    print(max_digit(10000))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1