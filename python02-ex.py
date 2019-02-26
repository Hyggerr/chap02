print('문자열 Q1')
pin = "881120-1068234"
yyyymmdd = pin.split('-')
num = pin.split('-')
print(yyyymmdd[0])
print(num[1])

print()
print('문자열 Q1-')
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

print()
print('문자열 Q2')
print(pin[7])

print()
print('리스트 Q1')
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

print()
print('리스트 Q2')
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)
result = '{0} {1} {2} {3}'.format(a[0], a[1], a[2], a[3])
print(result)
result = a[0] +' '+ a[1] +' '+ a[2] +' '+ a[3]
print(result)

print()
print('튜플 Q1')
a = (1, 2, 3)
a = a + (4,)
print(a)

print()
print('딕셔너리 Q1')
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B') # 해당하는 값을 추출하여 반환 후 삭제
# result = a['b']
# del(a['b'])
print(a)
# a.pop('B')
print(result)

print()
print('변수 Q1')
a = b = [1, 2, 3]
a[1] = 4
print(b)
# b가 a의 주소를 참조하기 때문