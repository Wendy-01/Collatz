def collatz(number):
    if number % 2 == 0:
        return (number//2)
    else:
        return (number * 3 + 1)


if __name__ == "__main__":
    try:
        input_num = int(input("Your Number Please:"))
    except ValueError:
        input_num = int(input("请输入整数:"))
        #non_int = "输入整数"

    #while True:
        #input_num = int(input("Your Number Please:"))
        #if non_int != "输入整数":
          #  break

    while True:
        input_num = collatz(input_num)
        print (input_num)
        if input_num == 1:
            break
    print("Game over!")