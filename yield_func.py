
# Yield function example

def daygen(index):
    weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat']

    yield weekdays[index]
    yield weekdays[index + 1]

if __name__ == '__main__':
    day = daygen(1)

    print(next(day), next(day))


