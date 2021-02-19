class A:
    x = 10
    def add(self):
        self.x += 1

x = A()
y = A()
x.add()
Y=A()


print("Y's x: ", y.x)
print("Y's x: ", x.x)
print("Y's x: ", Y.x)

"""10"""


class B:
    x = []
    def add(self):
        self.x.append(1)

x = B()
y = B()
x.add()

print("Y's x: ", y.x)

#OUTPUT

"""[1]"""