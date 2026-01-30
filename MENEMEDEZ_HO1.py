def word_average():
    word = input("\nInput name: ")
    length = len(word)
    total = 0
    liss = []

    for i in range(1, length + 1):
        num = int(input("Enter a number: "))
        liss.append(num)
        total += num

    average = total / length

    print(liss)
    print(f"The length of the word is {length}")
    print(f"The average is {average}")

    if length > average:
        print(f"The length of the word '{word}' is greater than the average.")
    elif length < average:
        print(f"The length of the word '{word}' is less than the average.")
    else:
        print(f"The length of the word '{word}' is equal to the average.")

    word_average()
word_average()
