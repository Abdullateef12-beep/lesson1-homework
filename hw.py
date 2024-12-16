# Homework : Try out the basic functions of dictionaries such as create a dictionary with basic details from user input and print the dictionary and change the particular value afterwards.

students_mark = {
"abdullateef" :95,
"anas" :90, 
"amir" :85,
"anna":75,

}

print(students_mark)
print("marks of anas are :" , students_mark["anas"])

del students_mark["amir"]
print(students_mark)


students_mark["kamil"] = 95
print(students_mark)


students_mark["lucian"] = 90
print(students_mark)


students_mark["sir"] = 99
print(students_mark)