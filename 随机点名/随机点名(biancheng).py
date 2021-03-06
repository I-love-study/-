from tkinter import *
import tkinter.font as tkFont
import time
import random
import gc

def center_window(root, width, height):  
    screenwidth = root.winfo_screenwidth()  
    screenheight = root.winfo_screenheight()  
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)  
    print(size)  
    root.geometry(size)

def name():
    huang_gif = PhotoImage(file = 'tupian/huang.gif')
    pict["image"] = huang_gif
    button["text"] = '先别点我'
    fp=open(r"7.txt")
    name=[]
    for lines in fp.readlines():
        lines=lines.replace("\n","")
        name.append(lines)
    fp.close()
    do = len(name)-1
    ft1 =  tkFont.Font(family = 'Fixdsys',size = 80,weight = tkFont.BOLD)
    hua = time.time()
    for i in range(3):
        num["text"] = 3-i
        for a in range(23):
            index = random.randint(0,do)
            echo["text"] = name[index]
            root.update_idletasks()
            time.sleep(1/23-0.003)
    num["text"] = 0
    root.update_idletasks()
    index = random.randint(0,do)
    echo["text"] = name[index]
    root.update_idletasks()
    print ((time.time()-hua))
    for a in range(5):
        root.update
        time.sleep(0.06)
    index = random.randint(0,do)
    echo["text"] = name[index]
    button["text"] = '开始点名'
    for x in locals().keys():
        del locals()[x]
    gc.collect()
    pict.configure(image = huaji_gif)

color = '#40E0D0'

root = Tk()

root['bg'] = color

root.title ("随机点名器(by FJJ)")

center_window(root, 500, 150)

ft =  tkFont.Font(family = 'Fixdsys',size = 40,weight = tkFont.BOLD)
echo = Label(root,text = '我爱学习',font = ft,width = 8,bg = color)
echo.grid(row=1,column=1)
Label(root,text = 'Make by I_love_study',bg = color).grid(row=3,column=1)
ft1 =  tkFont.Font(family = 'Fixdsys',size = 80,weight = tkFont.BOLD)
Label(root,text = '★',font = ft1,bg = color).grid(row=1,column=2,rowspan=3)
num = Label(root,text = '0',font = ft1,bg = color)
num.grid(row=1,column=2,rowspan=3)
huaji_gif = PhotoImage(file = 'tupian/huaji.gif')
pict = Label(root,image=huaji_gif)
pict.grid(row=1,column=0,rowspan=3)
button = Button(root, text='开始点名', command=name)
button.grid(row=2,column=1)

root.mainloop()
