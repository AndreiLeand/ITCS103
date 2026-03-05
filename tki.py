import tkinter as tk

window = tk.Tk()
window.title("One piece")
window.resizable(True,True)
window.geometry("600x600")
window.configure(bg = "skyblue")

frame = tk.Frame(window, bg ="skyblue")
frame.pack()


label = tk.Label(window,text="Who are you?",font=("Arial",12),bg="skyblue",fg="black",anchor="w")
label.pack()

img = tk.PhotoImage(file="luffy.png")
img = img.subsample(5,5)

img_label = tk.Label(window,image = img, bg = "skyblue")
img_label.pack()

user_label = tk.Label(window, text="Username:",bg="skyblue",font=("Poppins",12,"bold"))
user_label.pack()

user_ent = tk.Entry(window,show="")
user_ent.pack()

pass_label = tk.Label(window, text="Password:",bg="skyblue",font=("Poppins",12,"bold"))
pass_label.pack()

pass_label = tk.Entry(window,show="*")
pass_label.pack()


menu = tk.Menu(window)
window['menu'] = menu

popup = tk.Toplevel(window)
popup.grab_set()

file = tk.Menu(menu,tearoff=0)
file.add_command(label="Home")
file.add_command(label="Dashboard")
file.add_command(label="Settings")
file.add_command(label="Create New")
menu.add_cascade(label="File",menu=file)

view_drop = tk.Menu(menu,tearoff=1)
view_drop.add_command(label="Zoom")
view_drop.add_command(label="Minimize")
menu.add_cascade(label="View",menu=view_drop)

def la():
    label1 = tk.Label(window,text="Hello")
    label1.pack()


def git():
    username = user_ent.get()
    succ = tk.Label(window,text="Succes")
    succ.pack()
    label ['text'] = f"My name is,{username},Ore wa kaizoku no ou ni naru tsumori da"
    
btn = tk.Button(window,text="Submit",command=git,activebackground="blue", activeforeground="black",relief="sunken")
btn.pack(pady=10)





window.mainloop()