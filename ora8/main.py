print("1.feladat")


def percek(het, ora):
    p = het * 7 * ora * 60
    return p


print("ennyi perc van egy héten: " + str(percek(1, 26)))

print("2.feladat")


def oszt(alma, ember):
    o = lambda alma: alma // ember
    return o


print("ennyi alma jut egy embernek: " + str(oszt(124, 34)))

print("3.feladat")


def terker(r):
    K = 2 * r * 3.14
    T = r * r * 3.14
    return print("kerulet: ", K, "terulet: ", T)


terker(24)

print("4.feladat")


def nehezebb(olom, rez):
    if (olom * 11.34 > rez * 8.69):
        print("az ólom nehezebb")
    else:
        print("a réz nehezebb")


nehezebb(18, 23)
