a =  "Sashi bhushan"
b = " yadav"
c = "heLlo"

print(a+ " " + b) # concatenation

# Indexing concept
print(len(a)) # length of string
print(a[1:3]) # slicing concept
print(a[1::3]) # slicing and gaping (by 2) concept
print(b[-2:-1]) # negative slicing and indexing

# Case Conversion
print(a.lower())
print(a.capitalize()) # just starting letter in capital form
print(a.title()) # each of words of starting letters are in capital form
print((a+ " " + b).title()) # same here
print(b.swapcase()) # it does opposite, if small letter converts into capital and vice-versa

# Searching and Checking
print(a.find('b')) # it gives index position of that letter
print(a.index('a')) # same as above
print(a.count('a')) # it counts the a letters in that given variable
print(a.startswith('s')) # boolean form (based on statement it gives true or false)
print(b.endswith('v')) # same as above

# Trimming and Cleaning
print(b.strip()) # remove the space from the both sides
print(b.lstrip()) # same but from left side
print(b.rstrip()) # right side
print(a.replace('bh', 'v')) # it replace 'bh' instead of 'v'

# Splitting and Joining
print(b.split()) # it converts string into list form

# Validation (True/False)
print(c.isalpha()) # it checks only letter (whether it is in small or capital) not space, number etc
print(b.isalnum()) # it checks number + letter
print(b.isdigit()) # it checks number only
print(b.isspace()) # it checks spaces only
print(b.islower()) # it checks number + letter

# Formatting and Alignments
print(c.center(10)) # padding concept
print(c.ljust(10)) # padding left concept
print(c.rjust(10)) # padding right concept




