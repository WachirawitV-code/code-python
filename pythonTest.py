#print("Tee")
#x = 1
#print(x)
#x = 10
#print(x)

#x = 10(int),1.5(float),"Tee"(string),True/False(boolean)
#x = int("5")
#x = str("Tee")
#x = float("5.5")
#y = 10
#z = x+y
#print(z)

#x = 100_000_000 = 100000000
# + - * / % **(ยกกำลัง) //(หารปัดเศษทิ้ง) (x+1)*y
#x = x+3 = x+=3
#a1 = x > y,x >= y, x == y, x != y (boolean)

#p = True
#q = False
#a1 = p and q #false
#a2 = p or q #true
#a3 = not p #false
#print (a1,a2,a3)

#score = 70
#if score >= 80:
#    print("A")
#elif score >= 50:
#    print("C")
#else :
#    print("F")

#for i in range(3):
#    print(i) 0,1,2
#for i in range(1,4):
#    print(i) 1,2,3
#for i in range(1,4):
#    double = i*2
#    print(double)
#for i in range (1,7):
#    if i % 3 == 0:
#        continue
#    print(i) 1,2,4,5
#for i in range(1,11):
#    if i == 5:
#        break;
#    print(i) 1,2,3,4

#def calArea(width,length,height):
#   if width < 0 or length < 0 or width < 0:
#        return 0
#   area = width*length*height
   #print(area)
#   return area
   
#box1=calArea(4,-4,2)
#box2=calArea(width=4,length=4,height=2)
#print(box1)

import shape as s
circle = shape.caklCircle(10)
circle = s.calCircle(10)
print(circle)

#import tkinter as tk

#def setMessage():
#    text = text_input.get()
#    title_label.configure(text=text)

#window = tk.Tk()
#window.title("JustPython")
#window.minsize(width=400,height=400)

#title_label = tk.Label(master = window,text="Tee")
#title_label.pack()

#text_input = tk.Entry(master=window)
#text_input.pack()

#ok_button = tk.Button(master=window,text="Okay",command=setMessage)
#ok_button.pack()

#window.mainloop()

import tkinter as tk
import time

def showOutput ():
    number = int(num_input.get())

    if number == 0:
        output_label.configure(text = "NOOOOOOOO")
        return

    output = ''
    for i in range(1,13):
        output += str(number)+"x"+str(i)
        output += "="+str(number*i)+'\n'

    output_label.configure(text=output)
    start = time.time()

window = tk.Tk()
window.title("Loop")
window.minsize(width=400,height=400)

title_label = tk.Label(master = window,text="สูตรคูณ")
title_label.pack(pady=20)

num_input = tk.Entry(master=window,width = 15)
num_input.pack()

go_button = tk.Button(
    master=window,text="GO",
    command = showOutput,
    width = 15,height = 2,
    )
go_button.pack()

output_label = tk.Label(master = window)
output_label.pack(pady=20)

window.mainloop()

#import time
#start = time.time()
print("time",(time.time()-start)*1000)























































