columns = ["a","b","c","d","e","f","g","h","i","j"]
rows = range(1, 11)
keys=[]

#Printing the header
print(" " + "  ".join(columns))

#Print all columns
for letter in columns:
    #Print all rows
    for row in rows:
        key = f"{letter}{row}"
        keys.append(key)

print()