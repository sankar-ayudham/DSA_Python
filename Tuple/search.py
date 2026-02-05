my_tuple=("a","b","c","d")
print("b" in my_tuple)
# method 2 linear serch

def search(tuple,value):
    for i in tuple:
        if i == value:
            return  my_tuple.index(value)
    return " the item you are trying to search doesnt availble"

print(search(my_tuple,"b"))