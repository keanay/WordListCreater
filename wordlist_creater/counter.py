
def bruter(lis, maximum, num_max):
    err = 0
    shouldpass = 0
    while len(lis) <= maximum:
        try:
            bruterhand(lis)
        except NameError:
            print("[!]you should define a func called bruterhand() to use the output of this func[!]")
            err = 1
        if err == 1:
            break
        for i in range(len(lis)):
            if i == 0:
                lis[i] += 1
            if lis[i - 1] > num_max:
                lis[i] += 1
                lis[i - 1] = 0
            if lis[i] > num_max:
                lis[i + 1] += 1
                lis[i] = 0
        if lis[len(lis) - 2] & lis[len(lis) - 1] == num_max:
            shouldpass = 0
            for s in range(len(lis)):
                if lis[s] == num_max:
                    shouldpass += 1
                else:
                    shouldpass = 0
            if shouldpass == len(lis):
                bruterhand(lis)
                lis.append(0)
                for D in range(len(lis)):
                    lis[D] = 0
