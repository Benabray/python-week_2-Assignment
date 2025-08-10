#create empty list
my_list=[]

#append data to list
my_list.append(10)
my_list.append(20)
my_list.append(30)

#item_at_position_2=15
my_list[1]=15

#extend values to a list
extended_list=[50,60,70]
my_list.extend(extended_list)

#remove the last element from the list
my_list.pop(-1)

#sorting in ascending order

my_list.sort()

index_of_30=my_list.index(30)


print(index_of_30)
print(my_list)
