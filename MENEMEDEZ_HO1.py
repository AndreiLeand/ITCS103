word = len(input("Input name: "))
length = word
total = 0
liss = []
for i in range(1,length+1,1):
    num = int(input("Enter a number: "))
    liss.append(num)
    total += num
print(liss)
print(f"The length of the word is {length}")
print(f"The average is {total / length}")

if word > total:
    print("The Lenght of the word is greater than")
