
# Convert list to string
weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat']
weekday_str = ', '.join(weekdays)
print(weekday_str)

# Convert list to tuple
weekday_tuple = tuple(weekdays)
print(weekday_tuple)

# Convert list to set
weekday_set = set(weekdays)
print(weekday_set)

# Count the occurances of the item in list
print(weekdays.count('Mon'))

print([[x, weekdays.count(x)] for x in weekday_set])