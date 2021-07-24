# http://hleecaster.com/python-function-arguments/

# return을 명시하지않으면 기본값은 None
def no_return():
    print("no return")

test = no_return()

print(test)


# 함수는 매개변수는 선택적으로 받을수 있고, 기본값 설정이 가능하다.
"""
주의할 점은 def구문에서 필수매개변수를 먼저, 선택적인 매개변수는 나중에 써줘야한다는거다. 함수 처리할때 괄호안에 적힌 순서대로 인수를 받아 처리하기 떄문이다.
"""
def test(a, b, c=False):
    return

