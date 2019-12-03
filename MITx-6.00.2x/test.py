a = [0, 1, 2, 3, 4, 5, 6]
b = [3, 3, 3, 3, 3, 3, 3]
c = [0, 0, 0, 3, 6, 6, 6]
d = [3, 3, 5, 7, 7]
e = [1, 5, 5, 5, 9]

for i in [a,b,c,d,e]:
    si = sum(i)
    li = len(i)
    mi = si/li
    v = 0
    for el in i:
        v += (el-mi)**2
    var = v/li
    std = (var)**0.5
    print('var = {} ---- std = {}'.format(var, std))


d = [3, 3, 5, 7, 7]
e = [1, 5, 5, 5, 9]

def stdDevOfLengths(L):
    ls = []
    for i in L:
        ls.append(len(i))
    si = sum(ls)
    li = len(ls)
    v = 0
    try:
        mi = si/li

        for el in ls:
            v += (el-mi)**2
        var = v/li
    except:
        return None
    std = (var)**0.5
    return std

L = ['apples', 'oranges', 'kiwis', 'pineapples']
stdDevOfLengths(L)

L = ['a', 'z', 'p']
stdDevOfLengths(L)


def coef_var(L):
    si = sum(L)
    li = len(L)
    v = 0
    try:
        mi = si/li

        for el in L:
            v += (el-mi)**2
        var = v/li
        std = (var)**0.5
        return std/mi
    except:
        return None

L = [1, 2, 3]
print(coef_var(L))

L = [11, 12, 13]
print(coef_var(L))

L = [10, 4, 12, 15, 20, 5]
print(coef_var(L))
