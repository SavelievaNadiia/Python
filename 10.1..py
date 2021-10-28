def dict1():
    r = {}
    while True:
        print('Enter key (empty enter - exit)')
        k = input()
        if k == '':
            break
        print('Enter value')
        v = input()
        r[k] = v
    return r


d = dict1()
print(d)
