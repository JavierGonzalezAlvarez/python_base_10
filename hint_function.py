import math


def count_integer_digits(number: int | float | str):
    """Do int | float and return the number of (base-10) digits needed
to write the integer part of that number"""
    if number == 0:
        return 1
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a number or float")
    return int(math.log10(abs(number))) + 1


def main() -> None:
    '''function(int | float)'''
    print(count_integer_digits(100))
    print(count_integer_digits(999))
    print(count_integer_digits(10))
    print(count_integer_digits(3.1415))
    print(count_integer_digits(0))
    print(count_integer_digits('hello world'))


if __name__ == "__main__":

    main()
