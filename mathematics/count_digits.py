# Count the number of digits given by the user
def count_digit(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count

if __name__ == '__main__':
    print("Enter the number to count the digits: ")
    x = int(input())
    print(f"The count of digits: {count_digit(x)}")
