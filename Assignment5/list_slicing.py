# Task 2: Demonstrate List Slicing

initial_num = 1
final_num = 10

num_list = list(range(initial_num,final_num+1,1))
ext_list = num_list[0:5]

print("Original list:",num_list)
print("Extracted first five elements:",ext_list)
ext_list.reverse()
print("Reversed extracted elements:",ext_list)

