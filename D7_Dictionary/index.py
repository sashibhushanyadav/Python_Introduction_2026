student = {
    "fname": "Sashi",
    "lname": "Yadav",
    "age": 21,
    "height": 5.11,
    "address": {"pinCode": 23400, "district": "Rautahat"},
}

print(student.get("address"))  # it gives mention keys
print(student.keys())  # it returns all the keys
print(
    student.values()
)  # it returns all the values (even the values is in other data type)
print(student.items())  # it gives all the details in key-value pairs
student.update({"height": 5.10, "gender": "Male"})
print(student)  # it adds and updates the excisting values
student.pop("age") # removes the mentions key-value pairs
print(student)
# print(student.pop('age'))
student.popitem() # removes the latest inserted key-value pairs
print(student)

student_Copy = student.copy() # copy the original content
print(student_Copy)

student_Copy.clear() # empty the dictionay
print(student_Copy)

student.setdefault('Grade', 'B') # behaves like ('Grade': 'B')
print(student)

subjects = ["Math", "CS", "AI"]
marks = dict.fromkeys(subjects, 0)
print(marks)
