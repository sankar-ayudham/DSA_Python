my_list=[10,20,30,40,50,60,70,80,90]

#  in method
if 20 in my_list:
    print(my_list.index(20))
else:
    print("the element that you are looking for doesnot exist")

# linear search
def linear_search(list,value):
    for i in my_list:
        if i == value:
            return my_list.index(value)
    return "the element that you are looking for doesnt exist"

print(linear_search(my_list,200))