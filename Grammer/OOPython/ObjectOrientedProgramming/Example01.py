# 클래스의 기본적인 사용방법

class Flight:
    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError("첫 두글자가 알파벳이 아닙니다")
        if not number[:2].isupper():
            raise ValueError("첫 두글자가 대문자가 아닙니다")
        if not number[2:].isdigit():
            raise ValueError("세번째 글자 이상이 양의 숫자가 아닙니다.")
        self._number:str =  number

    def number(self):
        return self._number

f = Flight("AB001")
print(f.number())
print(f._number)