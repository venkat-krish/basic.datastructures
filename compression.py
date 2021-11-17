# Get the bit size
import sys

num: int = 4
bytes: int = sys.getsizeof(num)

print(f'Variable size is : {bytes} bytes, which is {bytes * 8} bits')
