def number(bus_stops):
    passengers = 0
    for i in bus_stops:
        #print(i[0],i[1])
        for j in range(0,len(i)):
            if j==0:
                passengers += i[j]
            else:
                passengers -= i[j]
    return passengers
