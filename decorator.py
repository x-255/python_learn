def outer(fn):
    def inner():
        print('before')
        fn()
        print('after')

    return inner


@outer
def do_something():
    print('do something')


do_something()
