class A:
    pass


class B:
    pass


class C(A, B):
    pass


class D(C):
    pass


class E(C):
    pass


print(C.__mro__)
print(C.__subclasses__())
