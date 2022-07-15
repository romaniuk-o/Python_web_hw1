class Meta(type):
    class_number = 0

    def __new__(mcs, name, bases, namespace, **kwargs):
        print(f'__new__ Meta {mcs.class_number}')
        instance = super().__new__(mcs, name, bases, namespace, **kwargs)
        instance.class_number = mcs.class_number
        mcs.class_number += 1
        mcs.children_number = mcs.class_number
        return instance


Meta.children_number = 0


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data


if __name__ == '__main__':
    assert (Cls1.class_number, Cls2.class_number) == (0, 1)
    a, b = Cls1(''), Cls2('')
    assert (a.class_number, b.class_number) == (0, 1)
    print(Meta.children_number)