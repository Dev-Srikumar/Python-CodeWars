def tickets(people):
    print(people)
    bills = {25:0 , 50:0, 100:0}
    for i in people:
        if i <=25:
            bills[i] += 1
        elif i==50:
            bills[i] += 1
            bills[i-25] -= 1
        elif i==100:
            bills[i] += 1
            if bills[i-50]>0:
                bills[i-50] -= 1
                bills[i-75] -= 1
            else:
                bills[i-75] -= 3
        bool_dict=all(values >=0 for values in bills.values())
        print(bills)
        print(bool_dict)
        if bool_dict is False:
            return "NO"
    return "YES"
