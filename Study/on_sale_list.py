# d = {'a': 3, 'b': 2, 'c': 1}
# for k in sorted(list(d.keys())):
#     print(k, d[k],sep='', end='')

# phonebook = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456","David King": "0438966581"}
#
# for name in phonebook:
#     print(phonebook[name])


class Thing:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def change(self, b):
        self.a += b


def run_tests():
    it = Thing(5, 6)
    it.change(2)
    print(it.a, it.b)


if __name__ == '__main__':
    run_tests()