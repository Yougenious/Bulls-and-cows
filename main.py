from random import randint
from tkinter import *
from FontColour import FontColour
from BackgroundColour import BackgroundColour
from FontSize import FontSize

def create_number(n):
    """Create a random number
    :param n: number of digits
    :return: random number"""
    print(n,type (n))
    result = randint(10**(n-1), 10**n - 1)
    while len(set(str(result))) != n:
        result = randint(10 ** (n - 1), 10 ** n - 1)
    return str(result)

def cows(n1, n2):
    """Calculate number of cows in game
    :param n1: created number
    :param n2: entered number
    :return: number of cows"""
    n1 = str(n1)
    #n2 = str(n2)
    digits1 = set(n1)
    digits2 = set(n2)
    cows = 0
    for digit in digits1:
        if digit in digits2:
            cows += 1
    for i in range(len(n1)):
        if n1[i] == n2[i]:
             cows -= 1
    return cows


def bulls(n1, n2):
    """Calculate number of bulls in game
    :param n1: created number
    :param n2: entered number
    :return: number of bulls"""
    n1 = str(n1)
    #n2 = str(n2)
    bulls = 0
    for i in range(len(n1)):
        if n1[i] == n2[i]:
            bulls += 1
    return bulls

def write_file(filename, username, attempts):
    results = list()
    with open(filename, "r") as file:
        for line in file:
            results.append(line.split())
    if len(results):
        for i in range(len(results)):
            if attempts < int(results[i][1]):
                results.insert(i, [username, str(attempts)])
                break
    else:
        results.append([username, str(attempts)])
    for i in range(len(results)):
        results[i] = results[i][0] + ' ' + results[i][1]+'\n'
    with open(filename, "w") as file:
            file.writelines(results)

def checknumber(event): # n1 = str(created_number) #n2 = str(entered_number)
    global b
    global c
    global attempts
    global ly
    n2 = txt.get()
    b = bulls(created_number, n2)
    c = cows(created_number, n2)
    attempts += 1
    ly += 70
    Label(text=f"Attempt #{attempts}; tried number {n2}\n{b} bulls, {c} cows", font="Arial 16").place(x=250, y=ly )
    if b == choice.get():
        ly += 70
        Label(text=f"Game over\nAmount of attempts #{attempts}\nGuessed number {created_number}", font="Arial 16", fg="red").place(x=250, y=ly)
        write_file(getfilename(b), username, attempts)

def create(event):
    global created_number
    created_number = create_number(choice.get())
    print(created_number)

def changename(event):
    global username
    username = user.get()
    userlb.config(text=f"Username: {username}")

def getfilename(digits):
     return str(digits) + '.txt'

def clearhistory():
    for i in range(2,9):
        with open(f'{i}.txt', "w") as file:
            file.writelines([])

def records():
    results = list()
    with open("2.txt", "r") as file:
        for line in file:
            results.append(line.split())
    for i, player in enumerate(results, 1):
        print(i, player)

def getfontcolour():
    with open("fontcolour.txt", 'r') as file:
        return file.readline()

def changefontcolour():
    wnd=FontColour()
    print(wnd.color)
    wnd.mainloop()


def getbackgroundcolour():
    with open("backgroundcolour.txt", 'r') as file:
        return file.readline()

def changebackgroundcolour():
    wnd=BackgroundColour()
    wnd.mainloop()

def getfontsize():
    with open("fontsize.txt", 'r') as file:
        return file.readline()

def changefontsize():
    wnd = FontSize()
    wnd.mainloop()

root = Tk()
root.title("Bullsandcows")
root.geometry("1000x500+300+50")

choice = IntVar()

created_number = 0
b = 0
c = 0
attempts = 0
ly = 150
username = "Anonymous"

radiobutton2 = Radiobutton(text="2 digits", value=2, variable=choice, padx=15,pady=10)
radiobutton2.grid(row=0,column=0,sticky=W, pady=2)

radiobutton3 = Radiobutton(text="3 digits", value=3, variable=choice, padx=15,pady=10)
radiobutton3.grid(row=1,column=0,sticky=W, pady=2)

radiobutton4 = Radiobutton(text="4 digits", value=4, variable=choice, padx=15, pady=10)
radiobutton4.grid(row=2,column=0,sticky=W, pady=2)

radiobutton5 = Radiobutton(text="5 digits", value=5, variable=choice, padx=15,pady=10)
radiobutton5.grid(row=3,column=0,sticky=W,pady=4)

radiobutton6 = Radiobutton(text="6 digits", value=6, variable=choice, padx=15,pady=10)
radiobutton6.grid(row=4,column=0,sticky=W, pady=4)

radiobutton7 = Radiobutton(text="7 digits", value=7, variable=choice, padx=15,pady=10)
radiobutton7.grid(row=5,column=0,sticky=W, pady=4)

radiobutton8 = Radiobutton(text="8 digits", value=8, variable=choice, padx=15,pady=10)
radiobutton8.grid(row=6,column=0,sticky=W, pady=4)

# selection = Label(textvariable=choice, padx=15, pady=10)
# selection.grid(row=8, column=0, sticky=W)

btn1 = Button(text="Check", height=1, width=15, font="Arial 22")
btn1.bind("<Button-1>", checknumber) # обязательно привязать функцию к кнопке
btn1.grid(row=2, column=1)

lb1 = Label(text="Input:", font="Arial 22")
lb1.grid(row=0, column=1)

txt = StringVar()
txtarea = Entry(textvariable=txt, width=15, font="Arial 22")
txtarea.grid(row=1, column=1)

userlb = Label(text="User name:", font="Arial 22")
userlb.grid(row=0, column=2, padx=1)

userbtn = Button(text="Change name", height=1, width=15, font="Arial 22")
userbtn.bind("<Button-1>", changename)
userbtn.grid(row=2, column=2, padx=70)

user = StringVar()
usertxtarea = Entry(textvariable=user, width=15, font="Arial 22")
usertxtarea.grid(row=1, column=2)

btn2 = Button(text="Create", height=1, width=10, font="Arial 22")
btn2.grid(row=8, column=0, sticky=W)
btn2. bind("<Button-1>", create)

mainmenu = Menu(root)
root.config(menu=mainmenu)
gamemenu = Menu(mainmenu, tearoff=0)
gamemenu.add_command(label="New")
gamemenu.add_separator()
gamemenu.add_command(label="Quit")

viewmenu = Menu(mainmenu, tearoff=0)
viewmenu.add_command(label='Time')
viewmenu.add_command(label='Moves')

recordsmenu = Menu(mainmenu, tearoff=0)
recordsmenu.add_command(label='2 digits', command=records)
recordsmenu.add_command(label='3 digits')
recordsmenu.add_command(label='4 digits')
recordsmenu.add_command(label='5 digits')
recordsmenu.add_command(label='6 digits')
recordsmenu.add_command(label='7 digits')
recordsmenu.add_command(label='8 digits')
recordsmenu.add_separator()
recordsmenu.add_command(label='Clear records', command=clearhistory)

settingsmenu = Menu(mainmenu, tearoff=0)
settingsmenu.add_command(label='Font colour', command=changefontcolour)
settingsmenu.add_command(label='Font size', command=changebackgroundcolour)
settingsmenu.add_command(label='Background colour', command=changefontsize)

mainmenu.add_cascade(label='Game', menu=gamemenu)
mainmenu.add_cascade(label='View', menu=viewmenu)
mainmenu.add_cascade(label='Records', menu=recordsmenu)
mainmenu.add_cascade(label='Settings', menu=settingsmenu)

root.mainloop()
