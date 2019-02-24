
import sys



def cake(input):
    if int(input) == 10:
        print("Happiness is here")
        return 10
    elif int(input) == 9:
        try:
            cake(3,5,4,6)
        except:
            print("I found an error, but I don't care")
    else:
        print("There is only sadness")


def main():
    x = 5
    if x == 5:
        print("hi")

    assert(cake(9) == 10)

main()