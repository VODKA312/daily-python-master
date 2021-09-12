if __name__ == '__main__':
    n = int(input()) - 1
    list_n = []
    while n >= 0:
        list_n.append(n)
        n = n - 1
    list_n = sorted(list_n)
    for i in list_n:
        print(i ** 2)

