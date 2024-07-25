class A(object):
    def method(self):
        print("Class A")
        super().method()
class B(object):
    def method(self):
        print("Class B")
        super().method()
class C(object):
    def method(self):
        print("Class C")
        #super().method()
class X(A,B):
    def method(self):
        print("Class X")
        super().method()
class Y(B,C):
    def method(self):
        print("Class Y")
        super().method()
class P(X,Y,C):
    def method(self):
        print("Class P")
        super().method()
p=P()
p.method()
print(P.__mro__)