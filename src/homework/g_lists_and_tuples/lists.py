def test_config():
    return True

#1-a function gamed get_lowest_list_value that returns the lowest value 
# (do not use built-in functionality)   Use loops.
def get_lowest_list_value(numbers):
    if not numbers:
        return None
    lowest = numbers[0]
    for i in numbers:
        if i < lowest:
            lowest = i
    return lowest

#2-a function gamed get_highest_list_value that returns the highest value, Use loops.
def get_highest_list_value(numbers):
    if not numbers:
        return None
    highest = numbers[0]
    for i in numbers:
        if i > highest:
            highest = i
    return highest
