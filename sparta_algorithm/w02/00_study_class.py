class Person:
    # pass # 빈 클래스로 두겠다는 의미
    def __init__(self, param_name):  # self는 자기자신
        print("메렁", self)
        self.name = param_name  # name이라는 변수에 param_name 저장하겠다는 의미


    def talk(self):
        print("안녕하세요. 저는", self.name, "입니다.")

person_1 = Person("유재석")  # Person()은 Person클래스를 통해 새로운 객체를 만들겠다는 것
print(person_1.name)
person_1.talk()
print(person_1)
# <__main__.Person object at 0x000001EDF9ACEAD0> 주소값: AD0
## at 뒤는 객체 공간 주소값
person_2 = Person("박명수")
print(person_2.name)
person_2.talk()
print(person_2)
# <__main__.Person object at 0x000001EDF9ACEB30> 주소값: B30
## at 뒤는 객체 공간 주소값
