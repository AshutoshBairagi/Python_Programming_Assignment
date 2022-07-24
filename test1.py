def happy_n():
    a = set()

    def h(n):
        ans = 0
        for i in range(1, len(str(n)) + 1):
            ans = ans + (int(str(n)[i - 1])) ** 2
            if ans != 1:
                if ans in a:
                    print(False)
                    return
                a.add(ans)
                return h(ans)
            else:
                print(True)
                return

    for n in range(1, 11):
        a1 = h(n)
        print(n, a1)


happy_n()