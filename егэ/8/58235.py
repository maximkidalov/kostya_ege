def count_numbers(n):
    if n == 0:
        return 1
    return n * count_numbers(n - 1)

def is_valid(number):
    first_digit = number[0]
    last_digit = number[2]
    middle_digit = number[1]
    return first_digit + last_digit > middle_digit

def main():
    print(count_numbers(3) - count_numbers(2))

if __name__ == "__main__":
    main()