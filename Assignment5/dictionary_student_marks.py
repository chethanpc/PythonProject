# Create a Dictionary of Student Marks

try:
    dictionary = {'Mike':75,'Nina':80,'Alice':85,'Khiem':65,'Harry':'78','Tom':60,'Kate':92}
    str = input("Enter the student's name:")
    print("{}'s marks: {}".format(str,dictionary[str]))
except:
    print("Student not found.")

