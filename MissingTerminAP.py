def find_missing(sequence):
    diff = (sequence[len(sequence)-1]-sequence[0])/(len(sequence))
    print(diff)
    for i in range(0,len(sequence)-1):
        if sequence[i]+diff != sequence[i+1]:
            return sequence[i]+diff
    return sequence[0]
