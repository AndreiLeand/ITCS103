
word = input("Input name: ")
length = len(word)
total = 0
liss = []
        
for i in range(1,length+1,1):
    num = int(input("Enter a number: "))
    liss.append(num)
    total += num
print(liss)
print(f"The length of the word is {length}")
print(f"The average is {total / length}")

if length > total:
    print(f"The Lenght of the word '{word}' is greater than the average. ")
elif length < total:
    print(f"The Lenght of the word '{word}' is less than the average. ")
else:
    print(f"The Length of the word '{word}' is equal the average")
