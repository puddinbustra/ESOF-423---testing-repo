import math

def mean():
    n = int(input("Number of data entries? "))
    sum = 0
    set = []
    for data in range(n):
        i = int(input("Point %d: " % (data+1)))
        sum += i
        set.append(i)
    return sum/n, set

def std(mean, set):
    total = 0

    for entry in set:
        result = entry - mean
        total += result * result
    mean2 = total/len(set)
    return math.sqrt(mean2)


def main():
    dataCount = int(input("Enter number of means? "))
    for count in range(dataCount):
        m,set = mean()
        s = std(m,set)
        print("Mean:",m,"  STD:",s)
    #return 0
main()
