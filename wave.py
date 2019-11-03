#---------Imports
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import  *
import tkinter as ttk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#---------End of imports
root = Tk()
root.geometry('1080x600')
root.title("Wave Simulation")
fig = plt.Figure()
x = np.arange(0, 2*np.pi, 0.01)
f=1
l = 1

def animate(i):
    global f,l
    ax.set(ylim=(-l-0.5, l+0.5))
    line.set_ydata(l*np.sin((x+i/10)*f))
    return line,
def run():
    global f,l
    if(Hz.get()!='' and Lenght.get()!=''):
        f = float(Hz.get())
        l= float(Lenght.get())

label = ttk.Label(root,text="Wave Simulation",font=('Angsana New',30,'bold')).place(x=450,y=10)

TextHz = Label(root,text='f (Hz)',font=('Angsana New',20,'bold'),)
TextHz.place(x=720,y=200)
Hz = StringVar()
EntryHz = ttk.Entry(root,textvariable= Hz,font=('Angsana New',18,'bold'))
EntryHz.place(x=820,y=200)
Hz.set(f)

TextLenght = Label(root,text='Lenght',font=('Angsana New',20,'bold'),)
TextLenght.place(x=720,y=250)
Lenght = StringVar()
EntryLenght = ttk.Entry(root,textvariable= Lenght,font=('Angsana New',18,'bold'))
EntryLenght.place(x=820,y=250)
Lenght.set(l)

bts = Button(root,text='Process',font=('Angsana New',15,'bold'),command= run)
bts.place(x=850,y=310)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().place(x=20,y=80)

ax = fig.add_subplot(111)
line, = ax.plot(x, f*np.sin(x))
ani = animation.FuncAnimation(fig, animate, interval=100, blit=False)

root.mainloop()
