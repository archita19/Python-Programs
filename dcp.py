def check(k) :
    sum = 0
    list = [10,15,3,7]
    length = len(list)
    for i in range(length) :
        for j in range(i,length) :
            if (list[i] == list[j]):
                continue
            else :
                sum = list[i] + list[j]
                if (sum != k):
                    sum = 0
                    continue
                else :
                    print ('number found')
check(18)
