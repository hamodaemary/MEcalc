from tkinter import *
from tkinter import ttk
from math import *
import math as m
x = Tk()
x.title('ME:CALC')
x.config(bg='black')
nb = ttk.Notebook(x,width=300)
nb.grid(columnspan=4)
fr1 = Frame(nb,width=100,height=100,bg='black')
nb.add(fr1,text="calc")
fr2 = Frame(nb,width=100,height=100,bg='black')
nb.add(fr2,text='tri')
fr3 = Frame(nb,width=100,height=100,bg='black')
nb.add(fr3,text='phys')
en = Entry(fr1,bg='grey',bd=2)
en.grid(row=0,column=0)
lvl = Label(fg='green',bg='black')
lvl.place(x=550,y=100)
''' THE FUNCTIONS'''
def click(number):
	#en.delete(0,END)
	cur = en.get()
	en.delete(0,END)
	en.insert(0,str(cur) + str(number))
def clear():
	en.delete(0,END)
def addn():
	first = en.get()
	global f_num
	global math
	math = 'addition'
	f_num = float(first)
	en.delete(0,END)

def equal():
	second_num = en.get()
	en.delete(0,END)
	if math == 'addition':
		en.insert(0,f_num + float(second_num))
	if math == 'multiply':
		en.insert(0,f_num * float(second_num))
	if math == 'division':
		en.insert(0,f_num / float(second_num))
	if math == 'subtract':
		en.insert(0,f_num - float(second_num))
	if math == 'skrt':
		en.insert(0,sqrt(f_num))
	if math == 'sinn':
		en.insert(0,m.sin(f_num*m.pi/180))
	if math == 'coss':
		en.insert(0,m.cos(f_num*m.pi/180))
	if math == 'tann':
		en.insert(0,m.tan(f_num*m.pi/180))
	if math == 'csc':
		en.insert(0,(m.asin(f_num))*180/m.pi)
	if math == 'sec':
		en.insert(0,(m.acos(f_num))*180/m.pi)
	if math == 'cot':
		en.insert(0,(m.atan(f_num))*180/m.pi)
	lvl.config(text=en.get(),font=('System',500))	





def multi():
	first = en.get()
	global f_num
	global math
	math = 'multiply'
	f_num = float(first)
	en.delete(0,END)
def divide():
	first = en.get()
	global f_num
	global math
	math = 'division'
	f_num = float (first)
	en.delete(0,END)
def subt():
	first = en.get()
	global f_num
	global math
	math = 'subtract'
	f_num = float(first)
	en.delete(0,END)
def sqrt0():
	first = en.get()
	global f_num
	global math
	math = 'skrt'
	f_num = float(first)
	en.delete(0,END)
def sin0():
	first = en.get()
	global f_num
	global math
	math = 'sinn'
	f_num = float(first)
	en.delete(0,END)
def cos0():	
	first = en.get()
	global f_num
	global math
	math = 'coss'
	f_num = float(first)
	en.delete(0,END)
def tan0():
	first = en.get()
	global f_num
	global math
	math = 'tann'
	f_num = float(first)
	en.delete(0,END)

def csc0():
	first = en.get()
	global f_num
	global math
	math = 'csc'
	f_num = float(first)
	en.delete(0,END)
def sec0():
	first = en.get()
	global f_num
	global math
	math = 'sec'
	f_num = float(first)
	en.delete(0,END)
def cot0():
	first = en.get()
	global f_num
	global math
	math = 'cot'
	f_num = float(first)
	en.delete(0,END)
'''PHYSICS'''
def forc():
	en.insert(0,float(ento.get())*float(ento1.get()))

''' THE KOL 7AGA '''
x.geometry('500x640')
poin = Button(fr1,text='.',padx=30,pady=30,bg='black',fg='yellow',command=lambda: click('.'))
poin.grid(row=1,column=1)
zeco = Button(fr1,text='0',padx=30,pady=30,bg='black',fg='yellow',command=lambda: click(0))
zeco.grid(row=1)
pi = Button(fr1,text='π',padx=30,pady=30,bg='black',fg='yellow',command=lambda: click(m.pi))
pi.grid(row=1,column=2)
button = Button(x,text='1',padx=50,pady=50,bg='black',fg='yellow',command=lambda: click(1))
button.grid(row=1,column=0)
bu = Button(x,text='2',padx=50,pady=50,bg='black',fg='yellow',command=lambda: click(2))
bu.grid(row=1,column=1)
bux = Button(x,text='3',padx=50,pady=50,bg='black',fg='yellow',command=lambda: click(3))
bux.grid(row=1,column=2)
bu4 = Button(x,text='4',padx=50,pady=50,bg='black',fg='yellow',command=lambda: click(4))
bu4.grid(row=2,column=0)
bu5 = Button(x,text='5',padx=50,pady=50,bg='black',fg='yellow',command=lambda: click(5))
bu5.grid(row=2,column=1)
bu6 = Button(x,text='6',padx=50,pady=50,bg='black',fg='yellow',command=lambda: click(6))
bu6.grid(row=2,column=2)
bu7 = Button(x,text='7',padx=50,pady=50,bg='black',fg='yellow',command=lambda: click(7))
bu7.grid(row=3,column=0)
bu8 = Button(x,text='8',padx=50,pady=50,bg='black',fg='yellow',command=lambda: click(8))
bu8.grid(row=3,column=1)
bu9 = Button(x,text='9',padx=50,pady=50,bg='black',fg='yellow',command=lambda: click(9))
bu9.grid(row=3,column=2)
add = Button(x,text='+',padx=50,pady=50,bg='black',fg='yellow',command=addn)
add.grid(row=4,column=0)
sub = Button(text='-',padx=50,pady=50,bg='black',fg='yellow',command=subt)
sub.grid(row=4,column=1)
equ = Button(text='=',padx=50,pady=50,bg='black',fg='yellow',command=equal)
equ.grid(row=4,column=2)
mult = Button(text='X',padx=50,pady=50,bg='black',fg='yellow',command=multi)
mult.grid(row=1,column=3)
div = Button(text='/',padx=50,pady=50,bg='black',fg='yellow',command=divide)
div.grid(row=2,column=3)
clr = Button(text='clr',padx=50,pady=50,bg='black',fg='yellow',command=clear)
clr.grid(row=3,column=3)
sqr = Button(text='sqrt',padx=50,pady=50,fg='yellow',bg='black',command=sqrt0)
sqr.grid(row=4,column=3)
sin = Button(fr2,text='sin',padx=2,pady=2,fg='yellow',bg='black',command=sin0)
sin.grid(row=1,column=0)
cos = Button(fr2,text='cos',padx=2,pady=2,fg='yellow',bg='black',command=cos0)
cos.grid(row=1,column=1)
tan = Button(fr2,text='tan',padx=2,pady=2,fg='yellow',bg='black',command=tan0)
tan.grid(row=1,column=2)
csc = Button(fr2,text='csc',padx=2,pady=2,fg='yellow',bg='black',command=csc0)
csc.grid(row=1,column=3)
sec = Button(fr2,text='sec',padx=2,pady=2,fg='yellow',bg='black',command=sec0)
sec.grid(row=1,column=4)
cot = Button(fr2,text='cot',padx=2,pady=2,fg='yellow',bg='black',command=cot0)
cot.grid(row=1,column=5) 
lblo = Label(fr3,text='f=ma,w=mg,G=m1m2/r^2',fg='yellow',bg='black')
lblo.grid()
lbm = Label(fr3,text='mass',bg='black',fg='yellow')
lbm.grid(column=1)
ento = Entry(fr3,width=5)
ento.grid(row=2,column=1)
lba = Label(fr3,text='accelaration',bg='black',fg='yellow')
lba.grid(row=1,column=2)
ento1 = Entry(fr3,width=5)
ento1.grid(row=2,column=2)
butr = Button(fr3,text='calculate',bg='white',command=forc)
butr.grid(row=4,column=1)
x.mainloop()