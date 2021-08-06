
# game program : rock , paper , scissord

import random
import tkinter as tk  #این کتابخانه باعث میشود برنامه ما به صورت گرافیکی اجرا شود 

window = tk.Tk()              # 'tkinter'ساخت یک پنجره با کتابخانه 
window.geometry("400x300")    # مشخص کردن ابعاد کتابخانه
window.title("rock , paper , scissord")

user_distinction = 0
computer_distinction = 0

user_choice = ""
computer_choice = ""

def choice_to_number (choice):
    rps ={"rock":0 , "paper":1 , "scissord":2 }
    return rps [choice]

def number_to_choice (number):
    rps = {0:"rock" , 1:"paper" , 2:"scissord"}
    return rps [number] 

def random_camputer_choice ():
    return random.choice(["rock" , "paper" , "scissord"])

def resulti (human_choice , computer_choice):
    global user_distinction
    global computer_distinction
    user = choice_to_number(human_choice)
    computer = choice_to_number(computer_choice)
    if (user==computer):
        print("the game equalised.")

    elif ((user - computer)%3==1):
        print("good job user.")
        user_distinction +=1

    else :
        print("computer win.")
        computer_distinction +=1

    text_arya = tk.Text(master=window , height=12, width=30 ,bg="#ffff80" )
    text_arya.grid(column=0 , row=4)       # تعداد سطر و ستون محیط گرافیکی که دارای یک ستون و چهر سطر است

    answer = f" user select: {user_choice}\n computer select: {computer_choice}\n your distinction: {user_distinction}\n computer distinction: {computer_distinction}"

    text_arya.insert(tk.END,answer)

def rock():
    global user_choice
    global computer_choice
    user_choice = "rock"
    computer_choice = random_camputer_choice()
    resulti(user_choice , computer_choice)

def paper():
    global user_choice
    global computer_choice
    user_choice = "paper"
    computer_choice = random_camputer_choice()
    resulti(user_choice , computer_choice)

def scissord():
    global user_choice
    global computer_choice
    user_choice = "scissord"
    computer_choice = random_camputer_choice()
    resulti(user_choice , computer_choice)


button_rock = tk.Button(text="rock" , bg="skyblue", command=rock)
button_rock.grid(column=0 , row=1)

button_paper = tk.Button(text="paper" , bg="pink", command=paper)
button_paper.grid(column=0 , row=2)

button_scissord = tk.Button(text="scissord" , bg="red", command=scissord)
button_scissord.grid(column=0 , row=3)

window.mainloop()
