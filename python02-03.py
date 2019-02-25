# 자바에서 배열 선언
# int[] array = new int[5];
# string[] strArray = {"배열1", "배열2", "배열3"}

# 파이썬에서 리스트 선언
# 파이썬에서 리스트는 자바에서 배열과 같은 기능을 함
# 자바에서는 배열에 자료형을 입력하기 때문에 같은 자료형의 데이터만 입력할 수 있으나 
# 파이썬에서는 자료형을 입력하지 않기 때문에 어떠한 자료형도 하나의 리스트에 입력이 가능함

print("리스트 사용하기")
a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

print("빈 리스트 : {0}".format(a))
print("숫자형 리스트 : {0}".format(b))
print("문자열형 리스트 : {0}".format(c))
print("숫자와 문자열 혼합형 리스트 : {0}".format(d))
print("숫자와 리스트 혼합형 리스트 : {0}".format(e))

# 리스트의 인덱싱과 슬라이싱
# 자바의 배열과 같이 인덱싱이 가능함
# index 번호는 0번부터 시작 (list[index])
# 리스트의 사용방법은 자바의 배열 사용방법과 기본적으로 같음
# 값 출력 : a[index]
# 값 입력 : a[index] = 입력할 값
# 리스트의 마지막 요소 출력 : a[-1]
# 리스트의 크기 구하기 : len(리스트명)

a = [1, 2, 3]
print("리스트 a의 index 1번 출력 : {0}".format(a[1]))

print("리스트를 사용하여 연산하기 : {0}".format(a[0] + a[2]))
print("리스트의 마지막 요소 출력 : {0}".format(a[-1]))
print("리스트의 마지막 요소 출력하기 : {0}".format(a[len(a)-1]))
print("리스트의 길이 출력하기 : {0}".format(len(a)))
print("=" * 50)

# 리스트에 안의 리스트 사용하기
# 리스트 안에 리스트를 입력하면 하나의 리스트 요소로 리스트를 가질 수 있음
# 리스트 안의 리스트의 요소에 접근하려면 자바의 2차원 배열을 사용하는 것처럼 접근가능
# 출력 : a[첫번째리스트 index][2번째리스트 index]
# 입력 : a[첫번째리스트 index][2번째리스트 index] = 값
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print("리스트 a의 3번째 요소 출력 : {0}".format(a[2]))
print("리스트 a의 4번째 요소 출력 : {0}".format(a[3]))
print("리스트 a의 4번째 요소의 2번째 요소 출력 출력 : {0}".format(a[3][1]))
print(a[-1])
print(a[3])

print(a[-1][0])
print(a[-1][1])
print(a[-1][2])
print("=" * 50)

# 리스트의 슬라이싱
# 문자열 슬라이싱 방법과 동일함
a = [1, 2, 3, 4, 5]
print("리스트의 index 0 ~ 1 출력 : {0}".format(a[0:2]))
a = "12345"
print("문자열의 index 0 ~ 1 출력 : {0}".format(a[0:2]))
a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]
print("처음부터 a[1] 까지 출력 : {0}".format(b))
print("a[2] 부터 마지막까지 출력 : {0}".format(c))

# 중첩된 리스트 슬라이싱
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print("a[2] 부터 a[4]까지 출력: {0}".format(a[2:5]))
print("a[3][0] 부터 a[3][1]까지 출력: {0}".format(a[3][:2]))

print("=" * 50)
# 리스트 연산자
# 기존 리스트에 다른 리스트를 연산하여 하나의 리스트로 만듬
# + 연산자 : 기존의 리스트에 추가함
# * 연산자 : 기존의 리스트를 곱하여 추가함
a = [1, 2, 3]
b = [4, 5, 6]
print("+ 연산자를 사용하여 2개의 리스트를 합함 : {0}".format(a+b))
print("* 연산자를 사용하여 a 리스트를 {0}번 반복한 리스트 생성 : {1}".format(3, a * 3))

# 리스트의 수정, 변경과 삭제
a = [1, 2, 3]
b = [1, 2, 3]
print("원본 리스트a 출력 : {0}".format(a))
print("원본 리스트b 출력 : {0}".format(b))
a[2] = 4
print("수정한 리스트 출력 : {0}".format(a))

# 연속된 범위 수정
# 리스트의 값을 입력할 경우 같은 하나의 인덱스를 선택하더라도 a[1:2]와 a[1]은 다름
# a[1:2]의 경우는 범위 설정을 통하여 하나의 인덱스 값만 출력한 형태이나, a[1]은 하나의 인덱스만을 선택한 형태임
print()
print("리스트 a의 1:2 값 출력 : {0}".format(a[1:2]))
a[1:2] = ["a", "b", "c"]
print("리스트 a의 범위 수정 : {0}".format(a))
b[1] = ["a", "b", "c"]
print("리스트 b의 index 1에 리스트 넣기 : {0}".format(b))

# []사용해 리스트 요소 삭제하기
# 리스트의 요소에 빈 리스트를 입력하면 해당 리스트의 인덱스가 삭제됨
print()
print("삭제 전 리스트 출력 : {0}".format(a))
a[1:3] = []
print("삭제 전 리스트 출력 : {0}".format(a))
a[1:2] = []
print("요소 하나만 삭제 : {0}".format(a))

# del 함수를 사용하여 리스트 요소 삭제
# del(삭제할 리스트 요소)
print("삭제 전 리스트 출력 : {0}".format(a))
del a[-1]
print("삭제 후 리스트 출력 : {0}".format(a))

# 리스트 관련 함수
# 입력 함수 insert, append
# insert()는 입력하려는 위치의 index번호에 지정한 값을 입력함
a = [1, 2, 3]
print("원본 리스트 : {0}".format(a))
a.insert(1, 100)
print("insert를 이용하여 값 추가 : {0}".format(a))
print()

# append()는 리스트의 가장 마지막 요소 뒤에 지정한 값을 추가함
a = [1, 2, 3]
print("원본 리스트 : {0}".format(a))
a.append(100)
print("append를 이용하여 값 추가 : {0}".format(a))

# 제거 함수 remove, pop
print()
# remove() 함수는 리스트에서 첫번째로 검색되는 지정된 값을 삭제
a = [1, 2, 3, 1, 2, 3]
print("원본리스트 : {0}".format(a))
a.remove(3)
print("remove 를 이용하여 해당하는 값 삭제 : {0}".format(a))

# pop() 함수는 해당하는 인덱스의 값을 반환하고 리스트에서 삭제
a = [1, 2, 3, 1, 2, 3]
print("원본리스트 : {0}".format(a))
print("pop 를 이용하여 해당하는 index의 값 삭제 : {0}".format(a.pop(1)))
print("pop 를 이용하여 해당하는 index의 값을 삭제 후 리스트 출력 : {0}".format(a))

# 리스트 정렬 sort, reverse
# sort() 함수는 리스트 내부의 값을 오름차순으로 정렬하여 리스트에 출력함
print()
a = [1, 4, 3, 2]
print("원본 리스트 : {0}".format(a))
a.sort()
print("sort를 사용하여 정렬 된 리스트 : {0}".format(a))

# reverse() 함수는 정렬은 하지 않고 리스트 내부의 값의 순서만 뒤바꿈
a = [1, 4, 3, 2]
print("원본 리스트 ; {0}".format(a))
a.reverse()
print("순서가 뒤집어진 리스트 : {0}".format(a))

# 내림차순으로 정렬하려면 sort()함수를 먼저 사용하고 그후에 reverse() 함수를 사용하여 순서를 뒤바꿈
a = [1, 4, 3, 2]
print("원본 리스트 ; {0}".format(a))
a.sort()
print("sort를 사용하여 정렬 된 리스트 : {0}".format(a))
a.reverse()
print("순서가 뒤집어진 리스트 : {0}".format(a))

# 위치 찾기 index
print()
a = [1, 2, 3]
print("index 함수를 이용하여 리스트의 값 찾기: {0}".format(a.index(3)))
print("index 함수를 이용하여 리스트의 값 찾기: {0}".format(a.index(1)))
print("index 함수를 이용하여 리스트의 값 찾기: {0}".format(a.index(2)))

# 리스트에 포함된 값의 수 확인
print()
a = [1, 4, 3, 2, 5, 3]
print("리스트 a에 포함된 3의 총 개수 확인 : {0}".format(a.count(3)))

# 리스트 확장 extend
# append를 사용해도 되고 리스트 연산자 중 + 를 사용해도 같은 효과
# extend() 에는 리스트만 입력할 수 있음
print()
a = [1, 2, 3]
print("원본 리스트 : {0}".format(a))
a.extend([4, 5, 6])
print("extend 로 확장된 리스트 : {0}".format(a))
a = a + [7, 8, 0]
print("+연산자로 리스트를 추가한 리스트: {0}".format(a))