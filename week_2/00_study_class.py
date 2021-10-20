class Person:
    def __init__(self,param_name):     # 생성자(constructor) 호출 함수
        print('i am created!', self)    # self -> 인자에 넘겨주는 자기 자신
        self.name = param_name

    def talk(self):
        print('안녕하세요, 제 이름은 ', self.name, '입니다.')

person_1 = Person('유재석')
print(person_1.name)
print(person_1)
person_1.talk()


person_2 = Person('박명수')
print(person_2.name)
print(person_2)
person_2.talk()