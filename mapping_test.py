
def square(n):
    return n*n
my_list = [2,3,4,5,6,7,8,9]
updated_list = map(square, my_list)
print(updated_list)
print(list(updated_list))

list_updated_list = list(updated_list)
for item in list_updated_list:
    print(item)