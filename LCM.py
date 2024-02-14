from math import *


def lcm(numbers):  # function for finding the LCM
    lcm = numbers[0]
    for num in numbers[1:]:
        lcm = lcm * num // gcd(lcm, num)
    return lcm


def gcd(number_1, number_2):  # function for finding GCD(greatest common divisor)
    while number_2:
        number_1, number_2 = number_2, number_1 % number_2
    return number_1


def main():
    numbers = []
    while True:  #inputing the integers values which we want to find HCF and LCM.
        try:
            number = int(input("Enter the number: "))
            if number == 0:
                break
            else:
                numbers.append(number)
        except:
            # print(f"Invalid Input")
            pass
    print(f"LCM of the {numbers}: ", lcm(numbers))


if __name__ == "__main__":
    main()
