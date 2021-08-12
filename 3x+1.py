n = input("Enter number: ")
mododd = n % 2
if mododd != 0:
    while mododd >= 0:
        print(mododd)
        mododd = (3 * mododd) + 169
