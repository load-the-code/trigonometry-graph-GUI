import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

def plot_sin():
    # ! Sin Wave
    x = np.arange(0,4*np.pi-1,0.1)  
    y = np.sin(x)
    plt.plot(x,y)
    plt.xlabel('x values from 0 to 4pi') 
    plt.ylabel('sin(x)')
    plt.title('Plot of sin from 0 to 4pi')
    plt.legend(['sin(x)'])
    plt.show()

def plot_cos():
    # ! Cos Waves
    x = np.arange(0,4*np.pi-1,0.1)   
    y = np.cos(x)
    plt.plot(x,y,"#FF8C00")
    plt.xlabel('x values from 0 to 4pi') 
    plt.ylabel('cos(x)')
    plt.title('Plot of cos from 0 to 4pi')
    plt.legend(['cos(x)'])
    plt.show()

def plot_sin_cos():
    # ! Sin and cos 
    x = np.arange(0,4*np.pi-1,0.1)   
    y = np.sin(x)
    z = np.cos(x)
    plt.plot(x,y,x,z)
    plt.xlabel('x values from 0 to 4pi') 
    plt.ylabel('sin(x) and cos(x)')
    plt.title('Plot of sin and cos from 0 to 4pi')
    plt.legend(['sin(x)', 'cos(x)'])      
    plt.show()


root = tk.Tk()
root.geometry('500x400+450+200')
root.title('Basic Trigonometric Graphs Simulator By Load_thecode ')
root.resizable(False,False)

bg = tk.PhotoImage(file='math_bg.png')
bg_label = tk.Label(root,image=bg)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)


sin_button = tk.Button(root,text='Sin Wave',font=('Helvetica',20,'bold'),bg='#507166',fg='#000000',relief=tk.SUNKEN,command=plot_sin)
sin_button.place(x=305,y=85)

cos_button = tk.Button(root,text='Cos Wave',font=('Helvetica',20,'bold'),bg='#507166',fg='#000000',relief=tk.SUNKEN,command=plot_cos)
cos_button.place(x=305,y=185)

sin_cos_button = tk.Button(root,text='Sin and Cos Wave',font=('Helvetica',15,'bold'),bg='#507166',fg='#000000',relief=tk.SUNKEN,command=plot_sin_cos)
sin_cos_button.place(x=295,y=285)



root.mainloop()