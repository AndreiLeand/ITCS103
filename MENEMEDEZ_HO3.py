import tkinter as tk

window = tk.Tk()
window.title("Culcoletor")
window.geometry("500x500")
window.configure(bg = "skyblue")

top_label = tk.Label(window,text="Simple Calculator",bg="white",font=("Arial",12,"bold"),padx=150)
top_label.place(x=30,y=10)

"""THIS IS FOR LABEL"""
num1_label = tk.Label(window,text="Enter the first number:",font=("Arial",15,"bold"))
num1_label.place(x=5,y=50)
num2_label = tk.Label(window,text="Enter the 2nd number:",font=("Arial",15,"bold"))
num2_label.place(x=5,y=100)

"""THIS IS FOR ENTRY"""
num1_ent = tk.Entry(window)
num1_ent.place(x=280,y=55)
num2_ent = tk.Entry(window)
num2_ent.place(x=280,y=105)

"""THIS IS FOR FUNCTION"""
def add():
    num1 = float(num1_ent.get())
    num2 = float(num2_ent.get())
    result = num1 + num2
    top_label ["text"] = f"The addition of {num1} + {num2} = {result}"

def subtraction():
    num1 = float(num1_ent.get())
    num2 = float(num2_ent.get())
    result = num1 - num2
    top_label ["text"] = f"The subtraction of {num1} - {num2} = {result}"

def multiply():
    num1 = float(num1_ent.get())
    num2 = float(num2_ent.get())
    result = num1 * num2
    top_label ["text"] = f"The multiplications of {num1} x {num2} = {result}"

def division():
    num1 = float(num1_ent.get())
    num2 = float(num2_ent.get())
    result = num1 + num2    
    top_label ["text"] = f"The division of {num1} ÷ {num2} = {result}"


"""THIS IS FOR BUTTON"""
add_btn = tk.Button(window,text="+",bg="orange",fg="darkblue",font=("Arial",20,"bold"),command=add,bd=5)
sub_btn = tk.Button(window,text="-",bg="orange",fg="darkblue",font=("Arial",25,"bold"),command=subtraction,bd=5)
mul_btn = tk.Button(window,text="x",bg="orange",fg="darkblue",font=("Arial",20,"bold"),command=multiply,bd=5)
div_btn = tk.Button(window,text="÷",bg="orange",fg="darkblue",font=("Arial",20,"bold"),command=division,bd=5)
add_btn.place(x=200,y=150)
sub_btn.place(x=249,y=150)
mul_btn.place(x=200,y=210)
div_btn.place(x=248,y=210)




window.mainloop()
