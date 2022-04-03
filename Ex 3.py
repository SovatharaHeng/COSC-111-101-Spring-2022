def remove_all_after(numbers, border):
    for i in range(len(numbers)):
        if numbers[i] == border:
            return numbers[:i + 1]
    return numbers

print(remove_all_after([1, 2, 3, 4, 5], 3))
            
                   
