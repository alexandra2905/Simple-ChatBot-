#librari
from tkinter import *
from turtle import *
from chatterbot import ChatBot
import os
import time as tm
from sys import exit
import webbrowser
root=Tk()
#root.iconbitmap('chat.bmp')
current_time=tm.strftime('Time:''%H:%M')
name_author="Contact author: Alexandra Babătă"
#un nume pentru fereastra
root.title('Tommy')
#dimensiuni pt fereastra
#root.geometry('400x500')
#root.configure(bg='blue')#adaugare culoare fereastra
#webbrowser.open('https://www.youtube.com/channel/UCI-KMg8ORy0e_5pM7aDxgnQ') #incercare adaugare link pentru nume autor
#create a main menu bar
main_menu=Menu(root)

#create the sub menu
file_menu=Menu(root)
file_menu.add_command(label='New...')
file_menu.add_command(label='Save as...')
file_menu.add_command(label='Exit')
main_menu.add_cascade(label='File')
main_menu.add_command(label="Clear Chat")
main_menu.add_command(label='Quit')

main_menu.add_command(label=current_time)
main_menu.add_command(label=name_author)
root.config(menu=main_menu)

#txt-fereastra unde apar mesajele
#e- ferestra unde scrii
#creaza functie de a trimite si a primi raspuns
def send():
    send="You-->"+e.get()
    txt.insert(END,"\n"+send)

    if(e.get()=="Hello!"):
        txt.insert(END,"\n"+"Tommy-->Hi!")
    elif (e.get() == "How are you?"):
        txt.insert(END, "\n" + "Tommy-->I'm fine, but you?")

    elif (e.get() == "I'm ok"):
        txt.insert(END, "\n" + "Tommy-->Nice to hear")
    elif (e.get() == "What's your name?"):
        txt.insert(END, "\n" + "Tommy--> My name is Tommy.")
    elif (e.get() == "Thanks"):
        txt.insert(END, "\n" + "Tommy--> How can I help?")
    elif (e.get() == "Can you recommend a movie to me?"):
        txt.insert(END, "\n" + " Tommy--> Yes. I recommend to see 'Django' ")
    elif (e.get() == "Thanks"):
        txt.insert(END, "\n" + "Tommy--> Something else?")
    elif (e.get() == "Yes. A good university in Romania? "):
        txt.insert(END, "\n" + "Tommy--> Maybe, 'Stefan Cel Mare Univeristy in Suceava' ")
    elif (e.get() == "Oh, thanks."):
        txt.insert(END, "\n" + "Tommy--> Something else?")
    elif (e.get() == "Music"):
        txt.insert(END, "\n" + "Tommy--> I recommend: https://www.kissfm.ro ,https://www.profm.ro ")
    elif (e.get() == "Food Suceava"):
       txt.insert(END, "\n" + "Tommy--> I recommend: Padrino, Centru Vechi, Zamca ")
    elif (e.get() == "Medical offices"):
        txt.insert(END, "\n" + "Tommy--> I recommend: Biotest, Dorna Medical, Bethesda ")
    elif (e.get() == "Thanks."):
        txt.insert(END, "\n" + "Tommy-->Something else? ")
    elif (e.get() == "No. Thanks."):
        txt.insert(END, "\n" + "Tommy--> Ok. Have a nice day! ")
    elif (e.get() == "Too you. Bye!"):
        txt.insert(END, "\n" + " Bye! "+exit())

    else:
        txt.insert(END,"\n"+"Tommy-->Sorry, I didnt get it...")




    e.delete(0,END)

txt=Text(root,bg='light blue')
txt.grid(row=0,column=0,columnspan=2)
e=Entry(root, width=100)
send=Button(root, text="Send", command=send,bg='blue', width=8,height=3,font=('Arial',12)).grid(row=1, column=1)

e.grid(row=1, column=0)

#chatWindow=Text(root, bd=1,bg='blue', width=50, height=8)
#chatWindow.place(x=6,y=6, height=385, width=370)
#creaza mesaje
#messageWindow=Text(root,bg='blue', width=30,height=4,)
#messageWindow.place(x=128,y=400, height=88,width=260)

#buton pt a trimite mesaje
#send=Button(root, text='Send',command=send, bg='red', width=12,height=5, font=('Arial',15))
#send.place(x=6, y=400,height=88, width=120)
#adaugare
#scrollbar=Scrollbar(root, command=root.yview())
#scrollbar.place(x=375, y=6, height=385)



root.mainloop() #va deschide o fereastra mica


