import os

FILENAME = "dreams.txt"

#This function makes sure the file exists with your default messages
def setup_file():
    if not os.path.exists(FILENAME):
        f = open(FILENAME, "w")
        f.write("Dream Big: I want to become a skilled programmer who builds systems that help people.\n")
        f.write("Stay Curious: I will keep learning even when things get difficult.\n")
        f.write("Embrace Failure: Every error is a step closer to success.\n")
        f.write("Create Impact: I want my code to solve real-world problems.\n")
        f.write("Be Consistent: Small progress every day leads to big results.\n")
        f.write("Believe in Yourself: I am capable of learning and growing. Someday we will be free\n")
        f.close()
        print("File 'dreams.txt' created successfully!")

# Ito ay para sa pag "Read the file"
def read_messages():
    print("\n--- YOUR INSPIRING MESSAGES ---")
    f = open(FILENAME, "r")
    content = f.read()
    f.close()
    
    if content == "":
        print("The file is empty.")
    else:
        print(content)
    print("-------------------------------")

# Ito naman is for Adding new message
def add_message():
    print("\n--- ADD NEW MESSAGE ---")
    msg = input("Enter your message: ")
    
    if msg != "":
        f = open(FILENAME, "a")  
        f.write("\n" + msg)       # This is for adding new line before message
        f.close()
        print("Message added!")
    else:
        print("You entered nothing.")

# This is for rewrite everything inside the file
def rewrite_file():
    print("\n--- REWRITE FILE ---")
    confirm = input("This deletes everything. Type 'yes' to continue: ")
    
    if confirm == "yes":
        print("Type your new text below. Type 'DONE' when finished:")
        
        all_lines = []
        while True:
            line = input().lower()
            if line == "done":
                break
            all_lines.append(line)
            
        # It Joins all lines together with new lines
        final_text = "\n".join(all_lines)
        
        f = open(FILENAME, "w") 
        f.write(final_text + "\n")
        f.close()
        print("File rewritten!")
    else:
        print("Cancelled.")

# MAIN MENU LOOP
setup_file() 
while True:
    print("\n==========================")
    print("   DREAMS MANAGER MENU")
    print("==========================")
    print("1. Read inspiring messages")
    print("2. Add a new inspiring message")
    print("3. Rewrite the entire file")
    print("4. Exit")
    print("==========================")
    
    choice = input("Choose 1-4: ")
    
    print("\n" * 2) 

    if choice == "1":
        os.system('cls')
        read_messages()
    elif choice == "2":
        os.system('cls')
        add_message()
    elif choice == "3":
        os.system('cls')
        rewrite_file()
    elif choice == "4":
        os.system('cls')
        print("Goodbye nakama! Keep dreaming big.")
        break
    else:
        print("Invalid choice. Try again.")