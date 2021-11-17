# Check the given number sequence is a palindrome or not
def one_digit(num:int):
    return ((num >= 0) and (num < 10))

def ispal_util(num: int, dupNum: list):

    if one_digit(num):
        return (num == (dupNum[0]) % 10)

    if not ispal_util(num // 10, dupNum):
        return False

