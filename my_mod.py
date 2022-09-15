def count_lines(name=input('enter name file \n')):
    file = open(name, 'r')
    count = file.readlines()
    print(len(count))


def count_chars(name=input('enter name file \n')):
    file = open(name, 'r')
    count = file.read()
    print(len(count))


def test():
    return count_chars(), count_lines()


if __name__ == "__main__":
    test()

