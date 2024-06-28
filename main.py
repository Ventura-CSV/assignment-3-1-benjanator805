import random


def main():
    number1 = random.randint(0, 100)
    print("First number: ", number1)
    number2 = random.randint(0, 100)
    print("Second number: ", number2)
    number3 = random.randint(0, 100)
    print("Third number: ", number3)

    ########################################
    if number1 <= number2 and number1 <= number3:
        min_value = number1
    elif number2 <= number1 and number2 <= number3:
        min_value = number2
    else: number3

    print("The minimum value is: ", min_value)
    ########################################
    
    ########################################
    # Do not delete the return statement
    ########################################
    return number1, number2, number3, min_value


if __name__ == '__main__':
    main()
