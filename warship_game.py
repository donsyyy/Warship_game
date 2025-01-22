from asyncio import wait
from turtle import numinput, textinput
import turtle
from time import sleep
#import keyboard
#from tabulate import tabulate


t, t2, t3, t4, t5 = turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()
t.hideturtle(); t2.hideturtle(); t4.hideturtle(); t5.hideturtle()
t2.penup(); t3.penup()
t.speed(0); t4.speed(0); t5.speed(0)

r = 50
CURSOR_SIZE = 20
FONT_SIZE = 12
FONT = ('Arial', FONT_SIZE, 'bold')
t3.shape('circle')
t3.fillcolor('red')
t3.sety(100 - FONT_SIZE - CURSOR_SIZE)
t3.write("Click to advance!", align='center', font=FONT)
t3.sety(100)

def pause():
    while True:
        #if keyboard.read_key() == 'space':
            break

def title(txt):
    t.penup()
    t.goto(0,250)
    style = ('Courier', 60, 'italic')
    t.color('darkblue')
    t.write(txt, font=style, align='center')

sleep(2)
title('Welcome')

player1 = textinput("Name", "Player 1, what is your name?")
player2 = textinput("Name", "Player 2, what is your name?")

sleep(1)
t.clear()
sleep(1)

title('WARSHIP Game!')
t.color('black')
def draw(r,t):
    for i in range(4):
        t.forward(r)
        t.left(90)

def X():
    t.left(45)
    t.pendown()
    for i in range(4):
        t.forward(20)
        t.back(20)
        t.left(90)
    t.right(45)
    t.penup()
    t.goto(0,0)

def block(x,y,r,p,t):
    for i in range(4):
        for j in range(4):
            t.penup()
            t.goto(x+r*j, y-r*i)
            t.pendown()
            t.color()
            draw(r,t)
    for i in range(1,5):
        t.penup()
        t.goto(x+25+r*(i-1), y+55)
        t.write(i)
    for i in range(1,5):
        t.goto(x-20, y+15-r*(i-1))
        t.write(i)
    t.goto(x+100, y+80)
    style = ('Courier', 30, 'italic')
    t.write(f'Camp {p}', font=style, align='center')

sleep(2)
block(-500,80,r,1,t4)
block(250,80,r,2,t5)
t.goto(0,0)
sleep(2)
u = int(numinput("Number of rounds","Enter desired number of rounds :    ",None, minval=1, maxval=10))

def table():
    style = ('Courier', 18, 'italic')
    t.goto(-650,-260)
    t.write(f'Player1', font=style, align='center')
    t.goto(-650,-340)
    t.write(f'Player2', font=style, align='center')
    for i in range(2):
        t.goto(-700,-290+80*i)
        t.pendown()
        t.forward(300*u)
        t.penup()

def attack(n,c):
    t.goto(-580,-140)
    t.right(90)
    t.pendown()
    t.forward(230)
    t.penup()
    t.goto()
    t.goto(0,0)

b = int(numinput(f"Number of squares","Enter desired number of squares per player to be targeted :   ",None, minval=1, maxval=16))

def camp(p):
    L = []
    sleep(1)
    for i in range(1,b+1):
        n = int(numinput(f"{p}'s turn. Square number {i}","Line number :                                               ",None, minval=1, maxval=4))
        m = int(numinput(f"{p}'s turn. Square number {i}, Line number : {n}","Column number :                                                                      ",None, minval=1, maxval=4))
        L.append((n,m))
    return L

def strike(p):
    print(f'\n{p}, Enter coordinates for your next strike:')
    sleep(1)
    n = int(numinput(f"{p}'s turn. Strike number {i+1}","Line number :                                               ",None, minval=1, maxval=4))
    m = int(numinput(f"{p}'s turn. Strike number {i+1}, Line number : {n}","Column number :                                                                      ",None, minval=1, maxval=4))
    t.color('black')
    if p == player1 :
        t.goto(275+50*(m-1), 105-50*(n-1))
        if (n,m) in boat2 :
            t.color('red')
            S1.append((n,m))
    else :
        t.goto(-475+50*(m-1), 105-50*(n-1))
        if (n,m) in boat1 :
            t.color('red')
            S2.append((n,m))
    X()
    return (n,m)

sleep(2)
boat1 = camp(player1)
sleep(2)
boat2 = camp(player2)
S1, S2 = [], []
t.speed(4)
data = [["",player1, player2]]
t.showturtle()

hit1 = hit2 = []

for i in range(u):
    w = strike(player1)
    sleep(2)
    v = strike(player2)
    sleep(2)
    L = [f'Attack num {i+1}',w,v]
    data.append(L)
    t2.clear()
    #print(f'''\n{tabulate(data, tablefmt='fancy_grid')}''')
    style = ('Courier', 15, 'italic')
    sleep(2)
    t2.goto(-25,-230)
    #t2.write(tabulate(data, tablefmt='fancy_grid'), font=style, align='center')
    sleep(2)

t.hideturtle()

def nothit(p,L,S):
    t.color('green')
    for i in L:
        if i not in S:
            if p == 2 :
                t.goto(275+50*(i[1]-1), 105-50*(i[0]-1))
                X()
            else :
                t.goto(-475+50*(i[1]-1), 105-50*(i[0]-1))
                X()


nothit(1,boat1,S2)
nothit(2,boat2,S1)


def final(p,L):
    if L == []:
        t = f'''\n{p}, you've not hit any occupied square. Better Luck Next Time!'''
    else :
        t = f'''\n{p}, you've hit {len(L)} occupied squares whose coordinates are:\n{L}\nGood Job!'''
    return t

def winner(L1,L2):
    l1 = len(L1)
    l2 = len(L2)
    if l1 == l2:
        t = f'''\nCongratulations to both players! You both hit an equal number of squares.'''
    else :
        if l1 > l2:
            p = player1
            r  = l1 - l2
        elif l1 < l2:
            p = player2
            r = l2 - l1
        t = f'''\nCongratulations to {p} winner of this game! You have hit {r} more squares than your opponent.'''
    return t

sleep(2)

nothit(1,boat1)
nothit(2,boat2)

sleep(3)

g = final(player1,S1)
h = final(player2,S2)
print(g)
print(h)

sleep(3)

tf = winner(S1,S2)
print(tf)

turtle.mainloop()
