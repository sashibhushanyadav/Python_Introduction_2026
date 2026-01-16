# Conditional Statement
# Syntax (if_elif_else)
#   if logic:
#       statement
#   elif logic:
#       statement
#   else:
#      statement


age = (int(input(f"Enter a number: ")))

if age>=18:
    print("adult")
elif age<18 and age>=0:
    print("Not an adult")
else:
    print("Not a number")