# While loop
i = 3
while i <= 6:
    print(i)
    i += 1

# for loop
num = [1, 5, 6, 3, 2, 1]
for item in num:
    print(item)

# for loop with else
string = "Sashi"
for itr in string:
    print(itr)
else:
    print("Completion")

# for loop with Range
for even in range(0, 10, 2):
    print(even)
    
# Break, Continue, and Pass    
    
# Break
for i in range(5):
    if i == 4:
        break
    print(f"Break: {i}")
    
# Continue
for i in range(1, 6):
    if i == 4:
        continue
    print(f"Continue: {i}")
    
# Pass
for i in range(1, 5):
    if i == 4:
        pass
    print(f"Pass: {i}")
    