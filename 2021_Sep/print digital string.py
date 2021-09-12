if __name__ == '__main__':
    n = int(input())
    string_n = ""
    while n > 0:
        string_n = str(n) + string_n
        n = n - 1
    #string_n = str(sorted(string_n))
    print(string_n)