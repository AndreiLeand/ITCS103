import tkinter as tk

window = tk.Tk()
window.title("GUI app")
window.resizable(True,True)
window.configure(bg="lightblue",cursor="cross")
window.geometry("500x500")

menu = tk.Menu(window)
window ['menu'] = menu

popup = tk.Toplevel(window)
top = tk.Label(popup,text="This is a toplevel",bg="lightblue",font=("Poppins",19,"bold"))
top.pack(pady=10)

popup.transient(window)
popup.grab_set()

file_drop = tk.Menu(menu,tearoff=0)
file_drop.add_command(label="New")
file_drop.add_command(label="Open")
file_drop.add_command(label="Exit")

menu.add_cascade(label="File",menu=file_drop)

view_drop = tk.Menu(menu,tearoff=1)
view_drop.add_command(label="Zoom")
view_drop.add_command(label="Minimize")

menu.add_cascade(label="View",menu=view_drop)

label = tk.Label(window,text="Hello World",bg="lightblue",font=("Poppins",19,"bold"))
label.pack(pady=10)

frame = tk.Frame(window,bg="lightpink")
frame.pack()

img = tk.PhotoImage(file="cats.png")
img = img.subsample(4,4)
img_label = tk.Label(frame,image = img,text="This is a cat!",compound ="top" )
#img_label.pack(pady=10,padx=10)

label3 = tk.Label(frame,text="Username:",bg="lightblue",font=("Poppins",19,"bold"))
label3.pack(pady=10,padx=10)

username_ent = tk.Entry(frame,show="*")
username_ent.pack(padx=10)

def show():
    username = username_ent.get()
    label2=tk.Label(window,text="Button is clicked!")
    label2.pack()
    label ['text'] = f"Hello, {username}"

    remember = check_val.get()
    if remember == 1:
        label4 = tk.Label(window,text="You are remembered")
        label4.pack()
    else:
        label4 = tk.Label(window,text="You are NOT remembered")
        label4.pack()
    
    gender=radio_val.get()
    if gender==1:
        label3 = tk.Label(window,text="You are a MALE")
        label3.pack()
    else:
        label3 = tk.Label(window,text="You are a FEMALE")
        label3.pack()

    house= listbox.curselection()
    label5=tk.Label(window,text=f"Your house is {house}")
    label5.pack()

radio_val = tk.IntVar()

female = tk.Radiobutton(frame,text="Female",variable=radio_val,value=0)
female.pack()

male = tk.Radiobutton(frame,text="Male",variable=radio_val,value=1)
male.pack()

listbox_lbl=tk.Label(frame,text="Choose your house:")

xscrollbar=tk.Scrollbar(frame,orient="horizontal")
xscrollbar.pack(side="bottom",fill="x")

yscrollbar=tk.Scrollbar(frame)
yscrollbar.pack(side="right",fill="y")

listbox= tk.Listbox(frame,selectmode="multiple",xscrollcommand = xscrollbar.set,yscrollcommand = yscrollbar.set)
listbox.insert(0,"Pythondfgdfsghfdhgfhdf")
listbox.insert(1,"Java")
listbox.insert(2,"C#")
listbox.insert(3,"Perl")
listbox.insert(0,"Python")
listbox.insert(1,"Java")
listbox.insert(2,"C#")
listbox.insert(3,"Perl")
listbox.insert(0,"Python")
listbox.insert(1,"Java")
listbox.insert(2,"C#")
listbox.insert(3,"Perl")
listbox.insert(0,"Python")
listbox.insert(1,"Java")
listbox.insert(2,"C#")
listbox.insert(3,"Perl")
listbox.insert(0,"Python")
listbox.insert(1,"Java")
listbox.insert(2,"C#")
listbox.insert(3,"Perl")
listbox.pack()

xscrollbar['command'] = listbox.xview
yscrollbar['command'] = listbox.yview


check_val = tk.IntVar()

check_btn = tk.Checkbutton(frame,text="Remember Me",variable=check_val)
check_btn.pack()

button = tk.Button(window,text="Submit",command=show,relief="sunken",activebackground="green",activeforeground="white")
button.pack(pady=10)

window.mainloop()