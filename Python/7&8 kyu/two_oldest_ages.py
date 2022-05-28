
'''The two oldest ages function/method needs to be completed. It should take an array of numbers as its argument and return the two highest numbers within the array. The returned value should be an array in the format [second oldest age, oldest age].

The order of the numbers passed in could be any order. The array will always include at least 2 items. If there are two or more oldest age, then return both of them in array format.

For example:

two_oldest_ages([1, 3, 10, 0]) # should return [3, 10]'''
def two_oldest_ages(ages):
    oldest=0
    second_oldest=0
    two_ages=[]
    for age in ages:
        if age>oldest:
            second_oldest=oldest
            oldest = age
        elif age> second_oldest:
            second_oldest=age
    two_ages.append(second_oldest)
    two_ages.append(oldest)
    return two_ages
def two_oldest_ages(ages):
    return sorted(ages)[-2:]
def two_oldest_ages(ages):
    max_number = max(ages)
    ages.remove(max_number)
    return [max(ages), max_number]
