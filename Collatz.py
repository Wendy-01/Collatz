def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return number * 3 + 1


if __name__ == "__main__":
    while True:
        try:
            input_num = int(input("Your Number Please:"))
        except ValueError:
            continue

        while True:
            input_num = collatz(input_num)
            print (input_num)
            if input_num == 1:
                break
        print("Game over!")
        break