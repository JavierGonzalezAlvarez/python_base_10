import math

def count_integer_digits(number: int | float):
    '''
    Write a Python function that accepts "a number"
      and outputs the number of (base-10) digits needed 
      to write the integer part of that number on a 
      piece of paper. Here, "a number" is any Python 
      type in the standard library that behaves as a 
      number (including but not limited to `int` and `float`).
    '''
    if number == 0:
        return 1
    if isinstance(number, (int, float)):
        return int(math.log10(abs(number))) + 1
    return "Input must be a number"

def main() -> None:
    '''returned data'''
    print(count_integer_digits(100))
    print(count_integer_digits(999))
    print(count_integer_digits(10))
    print(count_integer_digits(3.1415))
    print(count_integer_digits(0))
    print(count_integer_digits('hello world'))

if __name__ == "__main__":
    main()