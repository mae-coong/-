# 변수 선언과 할당
pi = 3.141592
r = 10
# 변수 참조
print("원주율 =", pi)
print("반지름 =", r)
print("원의 둘레 =", 2*pi*r)
print("원의 넓이 =", pi*r*r)

# 복합 대입 연산자
# □= 는 □후 대입
number = 100
number += 10
number += 30
print("number:", number)

string = "자이루"
string += "!"
print("string:", string)

# input
input("인삿말을 입력하세요> ")
string = input("인삿말을 입력하세요> ")
print(string)      # input 과 같이 함수의 결과로 나오는 값 = 리턴값 (반환값의 타입은 문자열)

# 자료형 알아보기 type()
print(type(string))
number = input("숫자를 입력하세요>")
print(number)
print(type(number))  # 문자, 숫자, (T or F)불 값 모두 문자열

# 문자열을 숫자로 바꾸기
# int() : 정수로 변환
# float() : 실수 또는 부동 소수점으로 변환
string_a = input("입력A> ")
int_a = int(string_a)

string_b = input("입력B> ")
int_b = int(string_b)

print("문자열 자료:", string_a + string_b)
print("숫자 자료:", int_a + int_b)

# int 와 float 활용하기
output_a = int("52")
output_b = float("52.273")

print(type(output_a), output_a)
print(type(output_b), output_b)

# int 와 float 조합하기
input_a = float(input("첫번째 숫자> "))
input_b = float(input("두번째 숫자> "))

print("덧셈 결과:", input_a + input_b)
print("뺼셈 결과:", input_a - input_b)
print("곱셈 결과:", input_a * input_b)
print("나눗셈 결과:", input_a / input_b)

# 숫자를 문자열로 바꾸기 str()함수
output_a = str(52)
output_b = str(52.273)
print(type(output_a), output_a)
print(type(output_b), output_b)