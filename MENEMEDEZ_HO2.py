import tkinter as tkin


window = tkin.Tk()
window.title("Profile Page")
window.geometry("600x600")
window.resizable(False,True)
window.configure(bg = "#6dd5ed")


profile_page = tkin.Label(window, text="Profile Page", font=("Matrix",40,"bold"), bg="#6dd5ed",fg="#0b3c5d")
profile_page.pack(pady=20)

profile_name = tkin.Label(window,text="Name: Andrei Leand A. Menemedez",font=("Arial",15),bg="#6dd5ed",fg="#0b3c5d")
profile_name.pack(pady=10,padx=0,anchor="w")

profile_age = tkin.Label(window,text="Age: 20",font=("Arial",15),bg="#6dd5ed",fg="#0b3c5d")
profile_age.pack(pady=10,padx=0,anchor="w")

profile_course = tkin.Label(window,text="Course: Bachelor of Science in Information Technology",font=("Arial",15),bg="#6dd5ed",fg="#0b3c5d")
profile_course.pack(pady=10,padx=0,anchor="w")

profile_bday = tkin.Label(window,text="Birthday: September 22 2005",font=("Arial",15),bg="#6dd5ed",fg="#0b3c5d")
profile_bday.pack(pady=10,padx=0,anchor="w")

profile_motto = tkin.Label(window,text="Motto:",font=("Arial",15),bg="#6dd5ed",fg="#0b3c5d")
profile_motto.pack(pady=10,padx=0,anchor="w")

profile_motto1 = tkin.Label(window,text="“No matter how high you rise or how much knowledge you gain, always remain humble, because whatever God has given you, He can also take away if He needs to humble you.”",font=("Arial",15),bg="#6dd5ed",fg="#0b3c5d",wraplength=500,justify="center")
profile_motto1.pack(pady=10,fill="x")

def rainbow(label):
    colors = ["#FF0000","#262727","#0000FF","#031f25","#800080","#01181D"]
    i = 0

    def change_color():
        nonlocal i
        label.config(fg=colors[i])
        i = (i + 1) % len(colors)
        label.after(500, change_color)

    change_color()

rainbow(profile_motto1)



window.mainloop()