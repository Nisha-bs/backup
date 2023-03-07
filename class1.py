# class student:
def reversenum():
    number = int(input("enter a number"))
    rev_num = 0

    while number > 0:
        remainder = number % 10
        rev_num = (rev_num * 10) + remainder
        number = number // 10
    print(rev_num)


# student.hello()
# reversenum()

def amstrongnumber():
    number = int(input("enter a number "))
    ams = 0
    cub = 0
    while (number > 0):
        remain = number % 10
        ams = (ams + remain**3)
        number = number // 10
    print(ams)


# amstrongnumber()
def triangle():
    for i in range(3):
        for j in range(i + 1):
            print("*", end="")
        print("")


# triangle()

def fibonacci():
    number = int(input("enter a number"))
    num = number - 2
    first = 0
    second = 1
    feb = 0
    ran = 0
    print(first, "\n", second)
    while (ran < num):
        feb = first + second
        first = second
        second = feb

        # if (feb > number):
        #     break
        # else:
        print(feb)
        ran += 1


fibonacci()
