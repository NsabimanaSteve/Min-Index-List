"""Write a function called min_index that, given a list of numbers, returns the index of the
smallest value in the list. For example, given the list [40, 50, 10, 90, 100, 70], the function
will return 2."""

def min_index(numbers):
    if not numbers:
        return None
    return numbers.index(min(numbers))
list_num=[40, 50, 10, 90, 100, 70]
result=min_index(list_num)
print(result)