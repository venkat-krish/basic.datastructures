# The search element is compared with middle element, if it matches then return x
# Else the mid < x then left half of the array is compared
# if the mid > x then right half of the array is compared
#
#

def binary_search(arr: list, low: int, high: int, x: int) -> int:
    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # if element is present at the middle itself
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binary_search(arr, mid + 1, high, x)
        else:
            return binary_search(arr, low, mid - 1, x)
    else:
        return -1


if __name__ == '__main__':
    arr = [2, 4, 5, 6, 7, 8, 9]
    print("Enter the search number: ")
    x = int(input())

    result = binary_search(arr, 0, len(arr) - 1, x)

    if result != -1:
        print("Element is present at index :", str(result))
    else:
        print("Element is not present in an array")