import tkinter as tkin


window = tkin.Tk() # it creates main window
window.title("Profile Page") #obvious naman this is title of your window or lets say your app
window.geometry("600x600") # Ito naman it use para sa size nung window
window.resizable(False,True) #this use naman for resize your window, first is W and second is H,False means Fixed na siya pag True pwede pa magalaw
window.configure(bg = "#6dd5ed") #It changes naman ng background color ng window


profile_page = tkin.Label(window, text="Profile Page", font=("Matrix",40,"bold"), bg="#6dd5ed",fg="#0b3c5d")
profile_page.pack(pady=20) #I think its use to place widget inside the window

profile_name = tkin.Label(window,text="Name: Andrei Leand A. Menemedez",font=("Arial",15),bg="#6dd5ed",fg="#0b3c5d")
profile_name.pack(pady=10,padx=0,anchor="w") #anchor w means west so it align to the west
                                            #pady 10 means add pixels space above and below the label
                                            

profile_age = tkin.Label(window,text="Age: 20",font=("Arial",15),bg="#6dd5ed",fg="#0b3c5d")
profile_age.pack(pady=10,padx=0,anchor="w")

profile_course = tkin.Label(window,text="Course: Bachelor of Science in Information Technology",font=("Arial",15),bg="#6dd5ed",fg="#0b3c5d")
profile_course.pack(pady=10,padx=0,anchor="w")

profile_bday = tkin.Label(window,text="Birthday: September 22 2005",font=("Arial",15),bg="#6dd5ed",fg="#0b3c5d")
profile_bday.pack(pady=10,padx=0,anchor="w")

profile_motto = tkin.Label(window,text="Motto:",font=("Arial",15),bg="#6dd5ed",fg="#0b3c5d")
profile_motto.pack(pady=10,padx=0,anchor="w")

profile_motto1 = tkin.Label(window,text="“No matter how high you rise or how much knowledge you gain,always remain humble, because whatever God has given you, He can also take away if He needs to humble you.”"
                            ,font=("Arial",15) #inside the font is font style and also the size of the text
                            ,bg="#6dd5ed" #this is background for text
                            ,fg="#0b3c5d" #this is foreground for text it means color of the text
                            ,wraplength=500 # Ito naman it means if yung text naging longer than 500pixels automatic the next line goes down
                            ,justify="center") #It controls naman for alignment of text inside the label

profile_motto1.pack(pady=10,fill="x") #fill x use to fill entire width of the window horizontally


#This function is for the color para bang nakislap kislap
def sarisari(label): #the parameter is label, kasi need natin lagyan ng kislap kislap si label which is yung motto
    colors = ["#FF0000","#262727","#0000FF","#031f25","#800080","#01181D"] #this is the list of color na mag papaikot ikot sa text
    i = 0 #this variable para sa color index it means mag sisimula siya sa zero index which is yung red

    def change_color(): #This is nested function it means its inside the function of SARI SARI
        nonlocal i
        label.config(fg=colors[i])  #The label is motto1, .config is to modify widget properties, 
                                    #tapos fg=colors[i] ito yung gamit para mag papalit palit yung color ng text
                                    #nakalagay sa loob yung variable ni colors tapos ng i which is yung index 0
        
        i = (i + 1) % len(colors) #Ito naman yung ginagamit to create infinite loop, bale mag papaikot ikot hanggang makapunta ulit sa index 0
                                    
        label.after(500, change_color) #It means after 500milliseconds or 0.5 seconds mag papalit siya ng color, nakalagay diyan yung function ni change_color

    change_color() #this function trabaho niya palitan ang kulay kada 0.5 seconds

sarisari(profile_motto1) #as you can see tinawag natin si function at nasa loob niya si label which is yung profile_motto1
                        #Parang sinasabi nito na i apply mo yung color changing effect sa profile_motto1



window.mainloop()
