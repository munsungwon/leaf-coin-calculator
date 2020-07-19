import tkinter as tk
from functools import partial
import math

def call_result1(label_result1,n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    hour = 10**(1.998-1.536*math.log10(float(num1)/float(num2)))  ## int -> float 
    label_result1.config(text="Result is %0.2f (hr)" % hour)

def call_result2(label_result2,n1):
    num1 = (n1.get())
    need = float(num1)/(10**((1.998-math.log10(24))/1.536))  ## int -> float 
    label_result2.config(text="Result is %0.2f (EA)" % need)

root = tk.Tk()
root.geometry('300x150+100+200')
root.title('Calculator')

number1 = tk.StringVar()
number2 = tk.StringVar()

labelTitle = tk.Label(root, text="Input").grid(row=0, column=1)
labelNum1 = tk.Label(root, text="PPM").grid(row=1, column=0)
labelNum2 = tk.Label(root, text="수박개수").grid(row=2, column=0)

labelResult1 = tk.Label(root)
labelResult1.grid(row=4, column=1)
labelResult2 = tk.Label(root)
labelResult2.grid(row=5, column=1)

entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=1)
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=1)

call_result1 = partial(call_result1, labelResult1, number1, number2)
call_result2 = partial(call_result2, labelResult2, number1)

buttonCal1 = tk.Button(root, text="피해발현시간", command=call_result1).grid(row=4, column=0)
buttonCal2 = tk.Button(root, text="필요한 수박개수", command=call_result2).grid(row=5, column=0)

root.mainloop()