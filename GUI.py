from tkinter import *

from connector_01 import connector_01
from connector_03 import connector_03
from connector_12 import connector_12
from connector_13 import connector_13
from connector_5 import connector_5

def fun1():
    a = [label, label0, label1, label2, label3, label4, label5, label6, label7, label8,
         label5_0, label5_1,
         label12_0, label12_1, label12_2, label13_0, label13_1, label13_2, label13_3, label13_4,
         entry, entry_fun13,
         button1, button3, button5, button11, button12,
         button_5_sure,
         button_12_sure, button_12_finalsure_blue, button_12_finalsure_red, button_reset,
         button_13_sure, button_13_finalsure_last, button_13_finalsure_first,
         textWindow]
    for i in a:
        i.place_forget()
    root.title("改变头像")
    label1_0.place(relx=0.3, relwidth=0.4, relheight=0.1)
    label1_1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.05)
    label8.place(relx=0.3, rely=0.475, relwidth=0.4, relheight=0.05)
    button_1_sure.place(relx=0.3, rely=0.35, relwidth=0.4, relheight=0.1)
    entry_fun1.place(relx=0.3, rely=0.2, relwidth=0.4, relheight=0.1)
    textWindow.place(relx=0.1, rely=0.55, relwidth=0.8, relheight=0.2)
    button_reset.place(relx=0.3, rely=0.8, relwidth=0.4, relheight=0.1)

def fun1_sure():
    id = entry_fun1.get()
    connector_01(id)
    textWindow.insert("insert", "已经改变为")
    textWindow.insert("insert", id)
    textWindow.insert("insert", "号头像")

def fun3():
    a = [label, label0, label1, label2, label3, label4, label5, label6, label7, label8,
         label1_0, label1_1,
         label5_0, label5_1,
         label12_0, label12_1, label12_2, label13_0, label13_1, label13_2, label13_3, label13_4,
         entry,
         entry_fun1,
         entry_fun13,
         button1, button3, button5, button11, button12,
         button_1_sure,
         button_5_sure,
         button_12_sure, button_12_finalsure_blue, button_12_finalsure_red, button_reset,
         button_13_sure, button_13_finalsure_last, button_13_finalsure_first,
         textWindow]
    for i in a:
        i.place_forget()
    root.title("改变段位")
    label1_0.place(relx=0.3, relwidth=0.4, relheight=0.1)
    label3_1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.05)
    label8.place(relx=0.3, rely=0.475, relwidth=0.4, relheight=0.05)
    button_3_sure.place(relx=0.3, rely=0.35, relwidth=0.4, relheight=0.1)
    label3_2.place(relx=0.1, rely=0.15, relwidth=0.3, relheight=0.05)
    label3_3.place(relx=0.6, rely=0.15, relwidth=0.3, relheight=0.05)
    entry.place(relx=0.6, rely=0.2, relwidth=0.3, relheight=0.1)
    entry_fun1.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.1)
    textWindow.place(relx=0.1, rely=0.55, relwidth=0.8, relheight=0.2)
    button_reset.place(relx=0.3, rely=0.8, relwidth=0.4, relheight=0.1)

def fun3_sure():
    rank = entry_fun1.get()
    division = entry.get()
    connector_03(rank, division)
    textWindow.insert("insert", "段位已经改变为")
    textWindow.insert("insert", rank)
    textWindow.insert("insert", division)

def fun5():
    a = [label, label0, label1, label2, label3, label4, label5, label6, label7,
         label5_0, label5_1,
         label12_0, label12_1, label12_2, label13_0, label13_1, label13_2, label13_3, label13_4,
         entry, entry_fun13,
         button1, button3, button5, button11, button12,
         button_12_sure, button_12_finalsure_blue, button_12_finalsure_red, button_reset,
         button_13_sure, button_13_finalsure_last, button_13_finalsure_first,
         textWindow]
    for i in a:
        i.place_forget()
    root.title("战绩查询功能")
    label5_0.place(relx=0.3, relwidth=0.4, relheight=0.1)
    label5_1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.05)
    label8.place(relx=0.3, rely=0.325, relwidth=0.4, relheight=0.05)
    button_5_sure.place(relx=0.3, rely=0.2, relwidth=0.4, relheight=0.1)
    button_reset.place(relx=0.3, rely=0.75, relwidth=0.4, relheight=0.1)
    textWindow.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.2)

def fun5_sure():
    idname, consequece = connector_5()
    for i in range(len(consequece)):
        textWindow.insert("insert", idname[i])
        textWindow.insert("insert", "是:")
        textWindow.insert("insert", consequece[i])

def fun12():
    a = [label, label0, label1, label2, label3, label4, entry, button1, button3, button5, button11, button12]
    for i in a:
        i.place_forget()
    root.title("团队BP功能页面")
    print(oursparehero)
    label12_0.place(relx=0.3, relwidth=0.4, relheight=0.1)
    label12_1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.05)
    label12_2.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.05)
    entry.place(relx=0.3, rely=0.25, relwidth=0.4, relheight=0.1)
    label5.place(relx=0.3, rely=0.35, relwidth=0.4, relheight=0.05)
    label6.place(relx=0.3, rely=0.40, relwidth=0.4, relheight=0.05)
    label7.place(relx=0.3, rely=0.55, relwidth=0.4, relheight=0.05)
    button_12_sure.place(relx=0.1, rely=0.45, relwidth=0.2, relheight=0.1)
    button_12_finalsure_blue.place(relx=0.325, rely=0.45, relwidth=0.3, relheight=0.1)
    button_12_finalsure_red.place(relx=0.65, rely=0.45, relwidth=0.3, relheight=0.1)
    textWindow.place(relx=0.2, rely=0.60, relwidth=0.6, relheight=0.1)
    button_reset.place(relx=0.3, rely=0.75, relwidth=0.4, relheight=0.1)

def fun13():
    a = [label, label0, label1, label2, label3, label4, label5, label6, label7, label12_0, label12_1, label12_2,
         entry,
         button1, button3, button5, button11, button12,
         button_12_sure, button_12_finalsure_blue, button_12_finalsure_red, button_reset,
         textWindow]
    for i in a:
        i.place_forget()
    root.title("个人BP功能页面")
    label13_0.place(relx=0.3, relwidth=0.4, relheight=0.1)
    label13_1.place(relx=0.05, rely=0.1, relwidth=0.8, relheight=0.05)
    label13_2.place(relx=0.025, rely=0.15, relwidth=0.9, relheight=0.05)
    label13_3.place(relx=0.2, rely=0.2, relwidth=0.3, relheight=0.05)
    label13_4.place(relx=0.6, rely=0.2, relwidth=0.3, relheight=0.05)
    entry.place(relx=0.2, rely=0.25, relwidth=0.3, relheight=0.1)
    entry_fun13.place(relx=0.6, rely=0.25, relwidth=0.3, relheight=0.1)
    label5.place(relx=0.3, rely=0.35, relwidth=0.4, relheight=0.05)
    label6.place(relx=0.3, rely=0.40, relwidth=0.4, relheight=0.05)
    label7.place(relx=0.3, rely=0.55, relwidth=0.4, relheight=0.05)
    button_13_sure.place(relx=0.1, rely=0.45, relwidth=0.2, relheight=0.1)
    button_13_finalsure_first.place(relx=0.325, rely=0.45, relwidth=0.3, relheight=0.1)
    button_13_finalsure_last.place(relx=0.65, rely=0.45, relwidth=0.3, relheight=0.1)
    textWindow.place(relx=0.2, rely=0.60, relwidth=0.6, relheight=0.1)
    button_reset.place(relx=0.3, rely=0.75, relwidth=0.4, relheight=0.1)


def fun_sure(oursparehero):
    a = entry.get()
    print(a)
    oursparehero.append(a)
    labelvalue.set(len(oursparehero))
    print(labelvalue)
    print(oursparehero)
    print(len(oursparehero))
    print(label6)
    label6.place(relx=0.3, rely=0.40, relwidth=0.4, relheight=0.05)

def fun13_sure(oursparehero):
    a = entry.get()
    b = entry_fun13.get()
    print(a)
    print(b)
    oursparehero.append(a)
    global enemyhero
    enemyhero = b
    labelvalue.set(len(oursparehero))
    print(labelvalue)
    print(oursparehero)
    print(len(oursparehero))
    label6.place(relx=0.3, rely=0.40, relwidth=0.4, relheight=0.05)


def finalsure_blue(oursparehero):
    BannedHero = connector_12(oursparehero)
    print(BannedHero)
    textWindow.insert("insert", "蓝方推荐一ban")
    textWindow.insert("insert", BannedHero[0])
    textWindow.insert("insert", "\n")
    textWindow.insert("insert", "蓝方推荐第一次二ban")
    textWindow.insert("insert", BannedHero[1])
    textWindow.insert("insert", ", ")
    textWindow.insert("insert", BannedHero[2])
    textWindow.insert("insert", "\n")
    textWindow.insert("insert", "蓝方推荐第一次二ban")
    textWindow.insert("insert", BannedHero[3])
    textWindow.insert("insert", ", ")
    textWindow.insert("insert", BannedHero[4])
    textWindow.insert("insert", "\n")

def finalsure_first(oursparehero, enemyhero):
    BannedHero, counter = connector_13(oursparehero, enemyhero)
    print(BannedHero)
    textWindow.insert("insert", "推荐ban")
    textWindow.insert("insert", BannedHero[0])

def finalsure_last(oursparehero, enemyhero):
    BannedHero, counter = connector_13(oursparehero, enemyhero)
    print(BannedHero, counter)
    textWindow.insert("insert", "根据您的预选英雄给出的推荐ban")
    textWindow.insert("insert", "\n")
    textWindow.insert("insert", BannedHero[0])
    textWindow.insert("insert", "\n")
    textWindow.insert("insert", "此处给出能够克制对方已经选取的英雄的pick选项")
    textWindow.insert("insert", "\n")
    textWindow.insert("insert", counter[0])
    textWindow.insert("insert", "\n")
    textWindow.insert("insert", counter[1])
    textWindow.insert("insert", "\n")
    textWindow.insert("insert", counter[2])

def finalsure_red(oursparehero):
    BannedHero = connector_12(oursparehero)
    print(BannedHero)
    textWindow.insert("insert", "红方推荐第一次二ban")
    textWindow.insert("insert", BannedHero[0])
    textWindow.insert("insert", ", ")
    textWindow.insert("insert", BannedHero[1])
    textWindow.insert("insert", "\n")
    textWindow.insert("insert", "蓝方推荐第一次二ban")
    textWindow.insert("insert", BannedHero[2])
    textWindow.insert("insert", ", ")
    textWindow.insert("insert", BannedHero[3])
    textWindow.insert("insert", "\n")
    textWindow.insert("insert", "红方最后一ban")
    textWindow.insert("insert", BannedHero[4])
    textWindow.insert("insert", "\n")

def reset():
    a = [label, label0, label1, label2, label3, label4, label5, label6, label7, label8,
         label1_0, label1_1,
         label2_1,
         label3_2,
         label3_1,
         label3_3,
         label5_0, label5_1,
         label12_0, label12_1, label12_2, label13_0, label13_1, label13_2, label13_3, label13_4,
         entry,
         entry_fun1,
         entry_fun13,
         button1, button3, button5, button11, button12,
         button_1_sure,
         button_3_sure,
         button_5_sure,
         button_12_sure, button_12_finalsure_blue, button_12_finalsure_red, button_reset,
         button_13_sure, button_13_finalsure_last, button_13_finalsure_first,
         textWindow]
    for i in a:
        i.place_forget()
    global oursparehero
    oursparehero = []
    root.title('LOL智能助手')
    labelvalue.set(0)
    label.place(relx=0.3, relwidth=0.4, relheight=0.1)
    label0.place(relx=0.07, rely=0.10, relwidth=0.8, relheight=0.05)
    label1.place(relx=0.07, rely=0.15, relwidth=0.8, relheight=0.05)
    label2.place(relx=0.07, rely=0.20, relwidth=0.8, relheight=0.05)
    label3.place(relx=0.07, rely=0.25, relwidth=0.8, relheight=0.05)
    label4.place(relx=0.07, rely=0.30, relwidth=0.8, relheight=0.05)
    button1.place(relx=0.32, rely=0.40, relwidth=0.3, relheight=0.075)
    button3.place(relx=0.32, rely=0.50, relwidth=0.3, relheight=0.075)
    button5.place(relx=0.32, rely=0.60, relwidth=0.3, relheight=0.075)
    button11.place(relx=0.32, rely=0.70, relwidth=0.3, relheight=0.075)
    button12.place(relx=0.32, rely=0.80, relwidth=0.3, relheight=0.075)
    textWindow.delete('1.0', 'end')

oursparehero = []
root = Tk()
root.title('LOL智能助手')
root.geometry("600x800+450+20")
label = Label(root, text="使用说明：", font=("宋体", 25), fg="red")
label.place(relx=0.3, relwidth=0.4, relheight=0.1)
labelvalue = IntVar()
labelvalue.set(0)
label0 = Label(root, text="[1] Icon Changer, [2] Background Changer, [3] Rank Changer")
label1 = Label(root, text="[4] Status Changer, [5] AutoAccept, [6] Change Locale")
label2 = Label(root, text="[7] Offline Status, [8] Online Status, [9] More Bots In Practice Tool")
label3 = Label(root, text="[10] Custom Request, [12] Team BP, [13] Person BP")
label4 = Label(root, text="[0] Exit")
label5 = Label(root, text="请输入预选英雄，目前已选数量")
label6 = Label(root, textvariable=labelvalue)
label7 = Label(root, text="结果显示区")
label8 = Label(root, text="结果显示区")
label1_0 = Label(root, text="功能说明", font=("宋体", 25), fg="red")
label1_1 = Label(root, text="在这个功能中，输入ID，按下确认，您将改变您的头像")
label2_1 = Label(root, text="在这个功能中，输入ID，按下确认，您将改变您的游戏背景")
label3_1 = Label(root, text="在这个功能中，输入段位和小段位，按下确认，您将改变您的段位显示")
label3_2 = Label(root, text="段位")
label3_3 = Label(root, text="小段位")
label5_0 = Label(root, text="功能说明", font=("宋体", 25), fg="red")
label5_1 = Label(root, text="在这个功能中，在对局开始阶段按下确认，您将获得队友最近的对局信息和系统评价")
label12_0 = Label(root, text="功能说明", font=("宋体", 25), fg="red")
label12_1 = Label(root, text="在这个功能中，你需要为团队的每个人输入他们的三名预选英雄，")
label12_2 = Label(root, text="        总共15名英雄，并选择自己的阵营，蓝色方或者红色方，程序将按照流程进行推荐BP")
label13_0 = Label(root, text="功能说明", font=("宋体", 25), fg="red")
label13_1 = Label(root, text="在这个功能中，你需要为你自己输入三名预选英雄")
label13_2 = Label(root, text="        并决定自己是先手还是后手，也就是对方的同位置英雄是否选出，程序在指定位置给出推荐BP")
label13_3 = Label(root, text="此处输入预选英雄")
label13_4 = Label(root, text="此处输入对位英雄")
label0.place(relx=0.07, rely=0.10, relwidth=0.8, relheight=0.05)
label1.place(relx=0.07, rely=0.15, relwidth=0.8, relheight=0.05)
label2.place(relx=0.07, rely=0.20, relwidth=0.8, relheight=0.05)
label3.place(relx=0.07, rely=0.25, relwidth=0.8, relheight=0.05)
label4.place(relx=0.07, rely=0.30, relwidth=0.8, relheight=0.05)
entry0 = StringVar()
entry0.set("默认信息")
entry = Entry(root, font=("宋体", 25), fg="red", textvariable=entry0)
entry_fun1_0 = StringVar()
entry_fun1_0.set("0")
entry_fun1 = Entry(root, font=("宋体", 25), fg="red", textvariable=entry_fun1_0)
entry_fun13_0 = StringVar()
entry_fun13_0.set("无")
entry_fun13 = Entry(root, font=("宋体", 25), fg="red", textvariable=entry_fun13_0)
button1 = Button(root, text="改变头像", command=fun1)
button3 = Button(root, text="改变段位显示", command=fun3)
button5 = Button(root, text="战绩查询", command=fun5)
button11 = Button(root, text="团队BP", command=fun12)
button12 = Button(root, text="个人BP", command=fun13)
button1.place(relx=0.32, rely=0.40, relwidth=0.3, relheight=0.075)
button3.place(relx=0.32, rely=0.50, relwidth=0.3, relheight=0.075)
button5.place(relx=0.32, rely=0.60, relwidth=0.3, relheight=0.075)
button11.place(relx=0.32, rely=0.70, relwidth=0.3, relheight=0.075)
button12.place(relx=0.32, rely=0.80, relwidth=0.3, relheight=0.075)
button_1_sure = Button(root, text="确认", command=fun1_sure)
button_3_sure = Button(root, text="确认", command=fun3_sure)
button_5_sure = Button(root, text="确认", command=fun5_sure)
button_12_sure = Button(root, text="确认", command=lambda : fun_sure(oursparehero))
button_12_finalsure_blue = Button(root, text="确认输入完毕,选择蓝色方", command=lambda : finalsure_blue(oursparehero))
button_12_finalsure_red = Button(root, text="确认输入完毕,选择红色方", command=lambda : finalsure_red(oursparehero))
button_13_sure = Button(root, text="确认", command=lambda : fun13_sure(oursparehero))
button_13_finalsure_first = Button(root, text="确认输入完毕,是先手选取", command=lambda : finalsure_first(oursparehero, enemyhero))
button_13_finalsure_last = Button(root, text="确认输入完毕,是后手选取", command=lambda : finalsure_last(oursparehero, enemyhero))
button_reset = Button(root, text="回归主界面",  command=reset)
textWindow = Text(root, width=80, height=10)





# textr = Text(root,width=60,height=5)
# textr.grid(row=8,column=0)

root.mainloop()
