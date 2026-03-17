import tkinter as tk


window = tk.Tk()
window.title("Profile Builder")
window.geometry("600x300")
window.resizable(False,False)
window.configure(bg="skyblue")


"""FUNCTION"""


def compute_age(year):    
    return 2006 - int(year)


def get_gender():
    if gender.get() == 1:
        return "Male"
    elif gender.get() == 2:
        return "Female"
    else:
        return "Not Set"

def get_color():
    if gender.get() == 1:
        return "purple"
    elif gender.get() == 2:
        return "blue"
    else:
        return "gray"

def change_color():
    if gender.get() == 1:
        window.config(bg="skyblue")
        window.config(bg="blue")
    elif gender.get() == 2:
        window.config(bg="purple")
        window.config(bg="purple")


def submit():
    f = f_entry.get()
    m = m_entry.get()
    l = l_entry.get()
    b = b_entry.get()

    if not b.isdigit():
        return

    age = 2026 - int(b)
    g_text = get_gender()

    if gender.get() == 1:
        top_color = "blue"
    elif gender.get() == 2:
        top_color = "purple"
    else:
        top_color = "gray"

    top = tk.Toplevel(window)
    top.configure(bg=top_color)
    top.geometry("250x150")

    head = tk.Label(top, text="Student ID", bg=top_color)
    head.pack()

    name = f"{f} {m} {l}"
    name_l = tk.Label(top, text=f"Name: {name}", bg=top_color)
    name_l.pack()

    age_l = tk.Label(top, text=f"Age: {age}", bg=top_color)
    age_l.pack()

    gender_l = tk.Label(top, text=f"Gender: {g_text}", bg=top_color)
    gender_l.pack()

"""LABEL"""

title_label = tk.Label(window,text="Profile Builder",bg="skyblue",font=("Arial",15,"bold"))
title_label.place(x=240,y=10)

f_name = tk.Label(window,text="First Name",bg="skyblue")
f_name.place(x=60,y=80)

m_name = tk.Label(window,text="Middle Name",bg="skyblue")
m_name.place(x=250,y=80)

l_name = tk.Label(window,text="Last Name",bg="skyblue")
l_name.place(x=450,y=80)

b_date = tk.Label(window,text="Birth Year",bg="skyblue")
b_date.place(x=60,y=130)

gender_l = tk.Label(window,text="Gender",bg="skyblue")
gender_l.place(x=60,y=155)


"""BUTTON"""

def on_enter(event):
    sub["bg"] = "skyblue"

def leave_enter(event):
    sub["bg"] = "white"

sub = tk.Button(window,text="Submit",relief="sunken",bg="white",command=submit)
sub.place(x=250,y=190)
sub.bind("<Enter>",on_enter)
sub.bind("<Leave>",leave_enter)


"""VAR"""
gender = tk.IntVar()

lalaki = tk.Radiobutton(window,text="Male",variable=gender,value=1,command=change_color,bg="skyblue")
lalaki.place(x=230,y=150)

Babae = tk.Radiobutton(window,text="Female",variable=gender,value=2,command=change_color,bg="skyblue")
Babae.place(x=300,y=150)


"""ENTRY"""

f_entry = tk.Entry(window)
f_entry.place(x=40,y=60)

m_entry = tk.Entry(window)
m_entry.place(x=230,y=60)

l_entry = tk.Entry(window)
l_entry.place(x=430,y=60)

b_entry = tk.Entry(window)
b_entry.place(x=40,y=110)


window.mainloop()