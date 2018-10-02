#coding:utf8

class Person:
    instance = 0
    def __new__(cls, *args, **kwargs):
        if cls.instance == 0:
            cls.instance = super().__new__(cls)
        return cls.instance

c1 = Person()
c2 = Person()
print(id(c1),id(c2))
c1.instance = 3
print(c2.instance)