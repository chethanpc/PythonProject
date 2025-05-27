# Write and Append Data to a Same File

first_str = input("Enter text to write to the file:")

file = open('output.txt','w')
write_file = file.write(first_str)
print('Data successfully written to output.txt.\n')
file.close()

append_str = input("Enter additional text to append:")

file = open('output.txt','a')
next_line = file.write("\n")
append_file = file.write(append_str)
print("Data successfully appended.")
file.close()

file = open('output.txt','r')
read_file = file.read().strip()
print("\nFinal content of output.txt:\n",read_file,sep='')
file.close()
