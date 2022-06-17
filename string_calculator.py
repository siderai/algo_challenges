from operator import mul


def calc(string):
    sum_elems = []
    l = string.split("+")
    i = 0
    while i < len(l):
        if "*" in l[i]:
            elems = l[i].split("*")
            sum_elems.append(mul(*[int(x) for x in elems]))
            l[i] = 0
        i += 1
    ints = [int(x) for x in l]
    sum_elems.extend(ints)
    return sum(sum_elems)


print(calc("2+2*10"))  # 22
