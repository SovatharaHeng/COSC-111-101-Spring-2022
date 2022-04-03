print ("ex 2")
def index_power(array,index):
    try:
        array[index]    
    except IndexError:
        x=-1
        return x
    x=array[index]**index
    return x
print(index_power([1, 2, 3, 4], 3))

print(-----------------------------------)
