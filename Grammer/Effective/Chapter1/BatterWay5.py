"""Batter Way 5 : 시퀀스를 슬라이스 하는 법

@NOTE
- 슬라이스 대상 내장 타입은 : list, set , bytes
- __getitem__ 과 __setitem__ 메서드를 구현하는 파이썬의 클래스에도 적용가능
"""
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# 1 리스트의 처음부터 슬라이스 할떄는 보기 편하게 인덱스 0을 생략
assert a[:5] == a[0:5]

# 2 리스트이 끝까지 슬라이스 할 때, 마지막 인덱스는 넣지 않아도 되므로 생략
# assert a[:5] == a[5:len(a)]

# 3 리스트의 끝을 기준으로 오프셋을 계산할 떄는 음수로 슬라이스 하는 게 편한다
a[:]
a[:5]
a[:-1]
a[4:]
a[-3:]
a[2:5]
a[2:-1]
a[-3:-1]

"""
- 슬라이싱의 결과는 완전히 새로운 리스트
- 원본 리스트에 들어있는 객체에 대한 참조는 유지
- 슬라이스한 결과를 수정해도 원본 리스트에 아무런 영향을 미치지 않음
"""
b = a[4:]
print("Before:  ", b)
b[1] = 99
print("After:   ", b)
print("No Change :", a)