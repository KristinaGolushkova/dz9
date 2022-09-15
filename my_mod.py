def count_lines(name=input('enter name file \n')):
    file = open(name, 'r')
    count = file.readlines()
    print(len(count))


count_lines()


def count_chars(name=input('enter name file \n')):
    file = open(name, 'r')
    count = file.read()
    print(len(count))


count_chars('news.txt')


def test(name):
    return count_lines(name), count_chars(name)


print(test('news.txt'))
