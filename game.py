print(''' 
█▀▀ ▄▀█ █▀▄▀█ █▀▀   █ █▀   █░░ █▀█ ▄▀█ █▀▄ █ █▄░█ █▀▀   █▀█ █░░ █▀▀ ▄▀█ █▀ █▀▀   █░█░█ ▄▀█ █ ▀█▀
█▄█ █▀█ █░▀░█ ██▄   █ ▄█   █▄▄ █▄█ █▀█ █▄▀ █ █░▀█ █▄█   █▀▀ █▄▄ ██▄ █▀█ ▄█ ██▄   ▀▄▀▄▀ █▀█ █ ░█░
''')

from pygame.locals import *
import pygame
import time
import random
import tkinter as tk

print('''
██████╗░██╗░░░██╗  ░██████╗░█████╗░██╗░░██╗░█████╗░██╗░░██╗
██╔══██╗╚██╗░██╔╝  ██╔════╝██╔══██╗██║░░██║██╔══██╗██║░██╔╝
██████╦╝░╚████╔╝░  ╚█████╗░███████║███████║███████║█████═╝░
██╔══██╗░░╚██╔╝░░  ░╚═══██╗██╔══██║██╔══██║██╔══██║██╔═██╗░
██████╦╝░░░██║░░░  ██████╔╝██║░░██║██║░░██║██║░░██║██║░╚██╗
╚═════╝░░░░╚═╝░░░  ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝


#########█▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀█ █░█ █░░ █▀▀ █▀#############
#########█▄█ █▀█ █░▀░█ ██▄   █▀▄ █▄█ █▄▄ ██▄ ▄█#############

''')

print("Շարժվել։ UP arrow, Down arrow, Right arrow, Left arrow")
print("Ձեզ հարկավոր է հասնել կանաչ քառակուսուն")
print("Շարժվելու ընթացքում ձեր մոտ կբացվի տարբեր գույներով քառակուսիներ")
print("Ամեն քառակուսի մի առարկայի հարց է")
print("Դեղին։ Հայոց լեզու")
print("Կանաչ։ Ֆիզիկա")
print("Կապույտ։ Մաթեմատիկա")
print("Սև։ ՏՏ ոլորտ")
print("Դուք ունեք սխալվելու 3 հնարավորություն")
print("Իրար հետևից 5 հարցի ճիշտ պատասխանելու դեքում դուք կստանաք մեկ միավոր։")

pygame.init()
#pygame.mixer.music.load('sound.mp3')
#pygame.mixer.music.play(-1)

pygame.mixer.Channel(0).play(pygame.mixer.Sound('sound1.wav'), loops = -1)

my_maze =[ 2,2,2,2,3,2,2,2,2,2,                                          
           3,1,1,1,1,1,1,1,1,2,
           2,1,1,1,1,1,1,1,1,2,
           2,1,1,1,1,1,1,1,1,2,
           2,1,1,1,1,1,1,1,1,2,
           2,1,1,1,1,1,1,1,1,2,
           2,1,1,1,1,1,1,1,1,2,
           2,1,1,1,1,1,1,1,1,2,
           2,1,1,1,1,1,1,1,1,2,
           2,2,2,2,2,2,2,2,0,2,]

twos = [0, 1, 2, 3, 5, 6, 7, 8, 9, 20, 29, 30, 39, 40, 49, 50, 59, 60, 69, 70, 79, 80, 89, 90, 91, 92, 93, 94, 95, 96, 97, 99]
threes = [4,10]
quests = [11, 22, 33, 44]

my_maze1 =[]

open_quest = 0

heart_life = 3

right_answer = 0

for i in range(100):
    if i in twos:
        my_maze1.append(2)
    elif i in threes:
        my_maze1.append(3)
    elif i == 98:
        my_maze1.append(0) 
    else:
        a = random.choice(quests)
        while a == my_maze1[i - 1] and a == my_maze1[i - 2]:
            a = random.choice(quests)
        try:
            while a == my_maze1[i - 10] and a == my_maze1[i - 20]:
                a = random.choice(quests)
        except:
            pass
        my_maze1.append(a)

my_maze[88] = my_maze1[88]

q1_n = 0
q2_n = 0
q3_n = 0
q4_n = 0

quest1 = ["Քան՞ի հոլով ունի հայերենը։ \n 1/ 7 \n 2/ 6 \n 3/ 8 \n 4/ 5",
          "Քան՞ի համեմատության աստիճան ունի ածականը։ \n 1/ 3 \n 2/ 4 \n 3/ 2 \n 4/ 5",
          "Ո՞վ է գրել <<Թմկաբերդի Առում>>-ը։ \n 1/ Մեսրոպ Մաշտոց \n 2/ Վահան Տերյան \n 3/ Հովհաննես Թումանյան \n 4/ Եղիշե Չարենց",
          "Ո՞վ է գրել <<Ես իմ անուշ Հայաստանի>> բանաստեղծությունը։ \n 1/ Մեսրոպ Մաշտոց \n 2/ Վահան Տերյան \n 3/ Հովհաննես Թումանյան \n 4/ Եղիշե Չարենց",
          "Ո՞րն է ճիշտ։ \n 1/ ութ-անասուն \n 2/ ութանասուն \n 3/ ութսուն",
          "Ո՞ր բառն է գրվում <<Օ>>-ով։ \n 1/ Աման*ր \n 2/ Մեծամ*ր \n 3/ Կես*ր",
          "Ո՞ր բառն է գրվում <<և>>-ով։ \n 1/ տար*երջ \n 2/ կար*որ \n 3/ *րոպա",
          "Ո՞ր թագավորի օրոք է եղել ծովից ծով Հայաստան։ \n 1/ Տիգրան Մեծ \n 2/ Աշոտ Երկաթ \n 3/ Պապ",
          "Քան՞ի տառ ունի հայոց այբուբենը։ \n 1/ 39 \n 2/ 36 \n 3/ 37",
          "Ո՞վ է <<Աշնան Պոետը>>։ \n 1/ Մեսրոպ Մաշտոց \n 2/ Վահան Տերյան \n 3/ Հովհաննես Թումանյան \n 4/ Եղիշե Չարենց",
          "Ո՞վ է Ամենայան Հայոց բանաստեղծը։ \n 1/ Մեսրոպ Մաշտոց \n 2/ Վահան Տերյան \n 3/ Հովհաննես Թումանյան \n 4/ Եղիշե Չարենց",
          "Որտե՞ղ է ճիշտ դրված հարցական նշանը։ \n 1/ ինչը՞ \n 2/ ի՞նչը",
          "Գործողություն ցույց տվող բառերը կոչվում են․․․ \n 1/ Գոյական \n 2/ Ածական \n 3/ Բայ",
          "Առարկա ցույց տվող բառերը կոչվում են․․․ \n 1/ Գոյական \n 2/ Ածական \n 3/ Բայ",
          "Հատկանիշ ցույց տվող բառերը կոչվում են․․․ \n 1/ Գոյական \n 2/ Ածական \n 3/ Բայ",
          "Ո՞րն է սխալ։ \n 1/ ութը \n 2/ ինը \n 3/ տասը",
          "Ո՞ր բառն է գրվում <<և>>-ով։ \n 1/ տար*երջ \n 2/ կար*որ \n 3/ *րոպա",]



quest2 = ["Քան՞ի բնական արբանյակ ունի երկրը։ \n 1/ 1 \n 2/ 2 \n 3/ 3 \n 4/ 4", 
        "Քան՞ի մոլորակ կա արեգակնային համակարգում։ \n 1/ 9 \n 2/ 10 \n 3/ 8 \n 4/ 11",
        "Ո՞րն է զանգվածի չափման միավոր։ \n 1/ կգ \n 2/ գ \n 3/ տ \n 4/ ց",
        "Ո՞րն է արագության չափման միավոր։ \n 1/ կմ/ժ \n 2/ մ/վ \n 3/ ր/վ \n 4/ ր/ժ",
        "Ո՞ր բանաձևով են հաշվում S-ը \n 1/ S=v*t \n S=v/t \n S=t/v \n S=t*t/v",
        "Ո՞վ է հայտնաբերել Երկրի ձգողության ուժը։ \n 1/ Գալիլո Գալիլեյ \n 2/ Վիկտոր Համբարձումյան \n 3/ Նաստրադամուս \n 4/ Իսահակ Նյութոն",
        "Քան՞ի կգ է 1մ*մ*մ ծավալով ջուրը։ \n 1/ 1,4կգ \n 2/ 1,5կգ \n 3/ 2կգ \n 4/ 1կգ",
        "Ո՞ր ջերմաստճանում է եռում ջուրը նորմալ պայմաններում։ \n 1/ 98 \n 2/ 99 \n 3/ 101 \n 4/ 100",
        "Որքա՞ն ժամանակում է երկրը կատարում մեկ պտույտ Արեգակի շուրջը։ \n 1/ 24 ժ \n 2/ 365 օր \n 3/ 12 ամիս \n 4/ 7 օր",
        "Որտե՞ղ է դիֆուզիան կատարվում ավելի արագ։ \n 1/ պինդ \n 2/ հեղուկ \n 3/ գազային \n 4/ պլազմա",
        "Ո՞րն է դիմադրության չափման միավորը։ \n 1/ Վատ \n 2/ Ջոուլ \n 3/ Օհմ \n 4/ Կգ",
        "Որքա՞ն է նեյտրոնի լիցքը։ \n 1/ 0 \n 2/ 1 \n 3/ -1 \n 4/ 0,5",
        "Ո՞րն է Նյութոնի երրկրորդ օրենքը։ \n 1/ F=mg \n 2/ F = ma \n 3/ F=mgh \n 4/ F=mha",
        "Ո՞րն է լարման չափման միավորը։ \n 1/ Վատ \n 2/ Վոլտ \n 3/ Ամպեր \n 4/ Ջոուլ",
        "Ո՞ր ջերմաստճանում է բյուրեղանում ջուրը։ \n 1/ 0 \n 2/ -1 \n 3/ 4 \n 4/ 1",
        "Ո՞ր բանաձևով են հաշվում S-ը \n 1/ S=v*t \n 2/ S=v/t \n 3/ S=t/v \n 4/ S=t*t/v",
        "Որտե՞ղ է դիֆուզիան կատարվում ավելի արագ։ \n 1/ պինդ \n 2/ հեղուկ \n 3/ գազային \n 4/ պլազմա"]


quest3 = ["Քան՞ի նիստ ունի խորհանարդը։ \n 1/ 7 \n 2/ 6 \n 3/ 4", 
        "Քան՞ի աստիճան է հավասարակողմ եռանկյան անկայն աստիճանային չափը։ \n 1/ 180 \n 2/ 60 \n 3/ 90",
        "Ինչի՞ է հավասար եռանկյան անկյունների գումարը։ \n 1/ 180 \n 2/ 90 \n 3/ 360",
        "Ինչե՞րն են իրար հավասար շեղանկյան մեջ։ \n 1/ անկյունները \n 2/ ԱՆկյունագծերը \n 3/ Կողմերը",
        "sin-ի մեծագույն արժեքը։ \n 1/ 1 \n 2/ -1 \n 3/ 0",
        "cos-ի փոքրագույն արժեքը։ \n 1/ 1 \n 2/ -1 \n 3/ 0 ",
        "Քան՞ի նիստ ունի եռանկյուն բուրգը։ \n 1/ 3 \n  2/ 2 \n 3/ 4",
        "Ինչի՞ է հավասար փռված անկյունը։ \n 1/ 180 \n  2/ 360 \n 3/ 90",
        "Ինչի՞ է հավասար արագությունը։ \n  1 / V=S*t \n  2/ V=t/S \n 3/ V=S/t",
        "Ինչի՞ է հավասար sin(90)-ը։ \n 1/ 1 \n 2/ -1 \n 3/ 0 ",
        "Ինչի՞ է հավասար cos(90)-ը։ \n 1/ 1 \n 2/ -1 \n 3/ 0",
        "Ինչի՞ է հավասար 3 և 4 կողմերով ուղղանկյան P-ն։ \n 1/ 12 \n 2/ 14 \n 3/ 24",
        "Ինչի՞ է հավասար 4 կողմով խորհանարդի ծավալը։ \n 1/ 64 \n 2/ 16 \n 3/ 24",
        "Ինչի՞ է հավասար 3+3*3։ \n 1/ 12 \n 2/ 18 \n 3/ 20",
        "Ինչի՞ է հավասար <<պի>>-թիվը։ \n 1/ 3,14 \n 2/ 4,18 \n 3/ 5,06",
        "Քան՞ի նիստ ունի խորհանարդը։ \n 1/ 7 \n 2/ 6 \n 3/ 4",
        "cos-ի փոքրագույն արժեքը։ \n 1/ 1 \n 2/ -1 \n 3/ 0 "]


quest4 = ["Քան՞ի բիթ է մեկ բայթը։ \n 1/ 7 \n 2/ 1024 \n 3/ 8", 
          "Քան՞ի մեգաբայթ է մեկ գիգաբայթը։ \n 1/ 1024 \n 2/ 8 \n 3/ 7",
          "Ո՞րն է ամենամեծ ստեղը համակարգչի ստեղնաշարում։ \n 1/ Space \n 2/ Enter \n 3/ Backspace",
          "Ո՞վ է ստեղծել Macitosh-ը։ \n 1/ Բիլ Գեյթս \n 2/ Իլոն Մաստ \n 3/ Սթիվ Ջոբս",
          "Ո՞վ է ստեղծել Facebook-ը։ \n 1/ Մարկ Ցուկերբերգ \n 2/ Իլոն Մաստ \n 3/ Սթիվ Ջոբս",
          "Ո՞րն է ամենաշատը օգտագործված վեբ կայքը։ \n 1/ youtube.com \n  2/ facebook.com \n 3/ google.com",
          "Ո՞ր ծրագրավորման լեզուն է ստեղծվել Microsoft-ի կողմից։ \n 1/ C++ \n 2/ C# \n 3/ Python",
          "Ո՞րն է ամենաշատը օգտագործված սոցիալական ցանցը։ \n 1/ WhatsApp \n 2/ Facebook \n 3/ Instagram",
          "Ո՞րն է երկուական համակարգ։ \n 1/ 01000 \n 2/ #8FBC8F \n 3/ 16Z7XR7",
          "Ո՞րն է առաջին որոնողական համակարգը։ \n 1/ Google \n 2/ Archie \n 3/ Yandex",
          "Նշվածներից որը՞ օպերացիոն համակարգ չէ։ \n 1/ Windows \n 2/ Linux \n 3/ C++",
          "Ո՞ր ընկերությունն է ստեղծել Mac օպերացիոն համակարգը։ \n 1/ Apple \n 2/ Microsoft \n 3/ Samsung",
          "Քան՞ի բիթ է օգտագործում IPv6 հասցեն։ \n 1/ 32 \n 2/ 128 \n 3/ 256",
          "Ո՞րն է առաջին միկրոպրոցեսորը։ \n 1/ AMD 2901 \n 2/ Intel Pentium III \n 3/ Intel 4004",
          "Ո՞վ է ստեղծել Microsoft ընկերությունը։ \n 1/ Բիլ Գեյթս \n 2/ Իլոն Մաստ \n 3/ Սթիվ Ջոբս",
          "Քան՞ի մեգաբայթ է մեկ գիգաբայթը։ \n 1/ 1024 \n 2/ 8 \n 3/ 7",
          "Ո՞ր ծրագրավորման լեզուն է ստեղծվել Microsoft-ի կողմից։ \n 1/ C++ \n 2/ C# \n 3/ Python",]

quest1_a = [1, 1, 3, 4, 3, 3, 2, 1, 1, 2, 3, 2, 3, 1, 2, 1, 2]
quest2_a = [1, 3, 1, 2, 1, 4, 4, 4, 1, 3, 3, 1, 2, 2, 1, 1, 3]
quest3_a = [2, 2, 1, 3, 1, 2, 3, 1, 3, 1, 3, 2, 1, 1, 1, 2, 2]
quest4_a = [3, 1, 1, 3, 1, 3, 2, 2, 1, 2, 3, 1, 2, 3, 1, 1, 2]

quest1_z = list(zip(quest1, quest1_a))
quest2_z = list(zip(quest2, quest2_a))
quest3_z = list(zip(quest3, quest3_a))
quest4_z = list(zip(quest4, quest4_a))

random.shuffle(quest1_z)
random.shuffle(quest2_z)
random.shuffle(quest3_z)
random.shuffle(quest4_z)

quest1, quest1_a = zip(*quest1_z)
quest2, quest2_a = zip(*quest2_z)
quest3, quest3_a = zip(*quest3_z)
quest4, quest4_a = zip(*quest4_z)

brake_app = 0

quest_ans = None

class Application(tk.Frame):
    def __init__(self, master=None, quest_id=0, done=0):
        super().__init__(master)
        self.master = master
        self.quest_id = quest_id
        self.pack()
        if done == 0:
            self.create_widgets()
        elif done == 1:
            self.winner()
        elif done == 2:
            self.loser()

    def winner(self):
        global app
        tk.Label(self, text='''
░██╗░░░░░░░██╗██╗███╗░░██╗███╗░░██╗███████╗██████╗░
░██║░░██╗░░██║██║████╗░██║████╗░██║██╔════╝██╔══██╗
░╚██╗████╗██╔╝██║██╔██╗██║██╔██╗██║█████╗░░██████╔╝
░░████╔═████║░██║██║╚████║██║╚████║██╔══╝░░██╔══██╗
░░╚██╔╝░╚██╔╝░██║██║░╚███║██║░╚███║███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝''').grid(row=0)
        tk.Button(self, 
          text='Quit', 
          command=self.win_quit).grid(row=3, 
                                    column=4, 
                                    sticky=tk.W, 
                                    pady=4)

    def win_quit(self):
        global brake_app
        brake_app = 1
        self.killme()

    def loser(self):
        global app
        tk.Label(self, text='''
░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░
██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗
██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝''').grid(row=0)
        tk.Button(self, 
          text='Quit', 
          command=self.win_quit).grid(row=3, 
                                    column=4, 
                                    sticky=tk.W, 
                                    pady=4)
    def on_exit(self):
        print("A")

    def create_widgets(self):
        global app
        global my_maze1
        global q1_n
        global q2_n
        global q3_n
        global q4_n
        global quest1_a
        global quest2_a
        global quest3_a
        global quest4_a
        global quest1
        global quest2
        global quest3
        global quest4
        global my_maze
        self.hi_there = tk.Button(self)
        if my_maze1[self.quest_id] == 11:
            tk.Label(self, text="Հարց: " + str(quest1[q1_n])).grid(row=0)
        if my_maze1[self.quest_id] == 22:
            tk.Label(self, text="Հարց: " + str(quest2[q2_n])).grid(row=0)
        if my_maze1[self.quest_id] == 33:
            tk.Label(self, text="Հարց: " + str(quest3[q3_n])).grid(row=0)
        if my_maze1[self.quest_id] == 44:
            tk.Label(self, text="Հարց: " + str(quest4[q4_n])).grid(row=0)
        self.e1 = tk.Entry(self)
        self.e1.grid(row=1, column=0)
        tk.Button(self, 
          text='Submit', 
          command=self.say_hi).grid(row=3, 
                                    column=10, 
                                    sticky=tk.W, 
                                    pady=4)
        #self.hi_there["text"] = "Hello World\n(click me)"
        #self.hi_there["command"] = self.say_hi
        #self.hi_there.pack(side="top")

        #self.quit = tk.Button(self, text="QUIT", fg="red",
        #                     command=self.killme)
        #self.quit.pack(side="bottom")


    def killme(self):
        self.master.destroy()

    def say_hi(self):
        global quest_ans
        global q1_n
        global q2_n
        global q3_n
        global q4_n
        global quest1_a
        global quest2_a
        global quest3_a
        global quest4_a
        global quest1
        global quest2
        global quest3
        global quest4
        if my_maze1[self.quest_id] == 11:
            quest_ans = int(quest1_a[q1_n]) == int(self.e1.get())
            q1_n += 1
        elif my_maze1[self.quest_id] == 22:
            quest_ans = int(quest2_a[q2_n]) == int(self.e1.get())
            q2_n += 1
        elif my_maze1[self.quest_id] == 33:
            quest_ans = int(quest3_a[q3_n]) == int(self.e1.get())
            q3_n += 1
        elif my_maze1[self.quest_id] == 44:
            quest_ans = int(quest4_a[q4_n]) == int(self.e1.get())
            q4_n += 1
        self.killme()



class Player:
    x = 400
    y = 450
    speed = 2

    def add_newblocks(self):
        global my_maze
        global my_maze1
        
        if my_maze[int(self.x / 50 + ((self.y - 50) / 5))] != 2:
            my_maze[int(self.x / 50 + ((self.y - 50) / 5))] = my_maze1[int(self.x / 50 + ((self.y - 50) / 5))]
        if my_maze[int((self.x + 50) / 50 + ((self.y) / 5))] != 2:
            my_maze[int((self.x + 50) / 50 + ((self.y) / 5))] = my_maze1[int((self.x + 50) / 50 + ((self.y) / 5))]
        if my_maze[int((self.x - 50) / 50 + ((self.y) / 5))] != 2:
            my_maze[int((self.x - 50) / 50 + ((self.y) / 5))] = my_maze1[int((self.x - 50) / 50 + ((self.y) / 5))]
    
    def moveRight(self):
        global my_maze
        global open_quest
        global quest_ans
        global heart_life
        global theApp
        global right_answer
        if my_maze[int((self.x + 50) / 50 + ((self.y) / 5))] == 3:
            root = tk.Tk()
            root.geometry("950x150")
            app = Application(master=root, quest_id = int((self.x) / 50 + ((self.y) / 5)), done=1)
            app.mainloop()
            return 0
        if my_maze[int((self.x + 50) / 50 + ((self.y) / 5))] != 2:
            self.x = self.x + 50
            my_maze[int((self.x) / 50 + ((self.y) / 5))] = 0
            self.add_newblocks()
        root = tk.Tk()
        root.geometry("700x200")
        app = Application(master=root, quest_id = int((self.x) / 50 + ((self.y) / 5)))
        app.mainloop()
        if quest_ans is False:
            heart_life -= 1
            right_answer = 0
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('wrong.wav'))
            if heart_life < 0:
                root = tk.Tk()
                root.geometry("950x150")
                app = Application(master=root, quest_id = int((self.x) / 50 + ((self.y) / 5)), done=2)
                app.mainloop()
        else:
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('correct1.wav'))
            right_answer += 1
        quest_ans = None
        time.sleep(0.2)

    def moveLeft(self):
        global my_maze
        global open_quest
        global quest_ans
        global heart_life
        global theApp
        global right_answer
        if my_maze[int((self.x  - 50) / 50 + ((self.y) / 5))] == 3:
            root = tk.Tk()
            root.geometry("950x150")
            app = Application(master=root, quest_id = int((self.x) / 50 + ((self.y) / 5)), done=1)
            app.mainloop()
            return 0
        if my_maze[int((self.x - 50) / 50 + ((self.y) / 5))] != 2:
            self.x = self.x - 50
            my_maze[int((self.x) / 50 + ((self.y) / 5))] = 0
            self.add_newblocks()
        root = tk.Tk()
        root.geometry("700x200")
        app = Application(master=root, quest_id = int((self.x) / 50 + ((self.y) / 5)))
        app.mainloop()
        if quest_ans is False:
            heart_life -= 1
            right_answer = 0
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('wrong.wav'))
            if heart_life < 0:
                root = tk.Tk()
                root.geometry("950x150")
                app = Application(master=root, quest_id = int((self.x) / 50 + ((self.y) / 5)), done=2)
                app.mainloop()
        else:
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('correct1.wav'))
            right_answer += 1
        quest_ans = None
        time.sleep(0.2)
        
    def moveUp(self):
        #global root
        global my_maze
        global open_quest
        global quest_ans
        global heart_life
        global theApp
        global right_answer
        if my_maze[int((self.x ) / 50 + ((self.y - 50) / 5))] == 3:
            print("Win")
            root = tk.Tk()
            root.geometry("950x150")
            app = Application(master=root, quest_id = int((self.x) / 50 + ((self.y) / 5)), done=1)
            app.mainloop()
            return 0
        if my_maze[int(self.x / 50 + ((self.y - 50) / 5))] != 2:
            self.y = self.y - 50
            my_maze[int((self.x) / 50 + ((self.y) / 5))] = 0
            self.add_newblocks()
        root = tk.Tk()
        root.geometry("700x200")
        root.overrideredirect(1)
        app = Application(master=root, quest_id = int((self.x) / 50 + ((self.y) / 5)))
        #app.protocol("WM_DELETE_WINDOW", self.do_smth)
        app.mainloop()
        if quest_ans is False:
            heart_life -= 1
            right_answer = 0
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('wrong.wav'))
            if heart_life < 0:
                root = tk.Tk()
                root.geometry("950x150")
                app = Application(master=root, quest_id = int((self.x) / 50 + ((self.y) / 5)), done=2)
                app.mainloop()
        else:
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('correct1.wav'))
            right_answer += 1
        quest_ans = None
        time.sleep(0.2)

    def do_smth(self):
        print("a")
        
    def moveDown(self):
        global my_maze
        global open_quest
        global quest_ans
        global heart_life
        global theApp
        global right_answer
        if my_maze[int((self.x) / 50 + ((self.y + 50) / 5))] == 3:
            root = tk.Tk()
            root.geometry("950x150")
            app = Application(master=root, quest_id = int((self.x) / 50 + ((self.y) / 5)), done=1)
            app.mainloop()
            return 0
        if my_maze[int(self.x / 50 + ((self.y + 50) / 5))] != 2:
            self.y = self.y + 50
            my_maze[int((self.x) / 50 + ((self.y) / 5))] = 0
            self.add_newblocks()
        root = tk.Tk()
        root.geometry("700x200")
        app = Application(master=root, quest_id = int((self.x) / 50 + ((self.y) / 5)))
        app.mainloop()
        if quest_ans is False:
            heart_life -= 1
            right_answer = 0
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('wrong.wav'))
            if heart_life < 0:
                root = tk.Tk()
                root.geometry("950x150")
                app = Application(master=root, quest_id = int((self.x) / 50 + ((self.y) / 5)), done=2)
                app.mainloop()
        else:
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('correct1.wav'))
            right_answer += 1
        quest_ans = None
        time.sleep(0.2)
    
 
class Maze:
    def __init__(self):
       self.M = 10
       self.N = 10

    def draw(self,display_surf,image_surf, fin, maze_my, q1, q2, q3, q4, bys, heart):
       global heart_life
       global theApp
       global right_answer
       bx = 0
       by = 0
       if right_answer == 5:
           pygame.mixer.Channel(3).play(pygame.mixer.Sound('jacpot.wav'))
           right_answer = 0
           heart_life += 1
       if brake_app:
           theApp.on_cleanup()
       display_surf.blit(bys,( 0 , 510))
       for i in range(heart_life):
           display_surf.blit(heart,( (210 + (i * 50)) , 505))
       for i in range(0,self.M*self.N):
           if maze_my[ bx + (by*self.M) ] == 1 or maze_my[ bx + (by*self.M) ] == 2:
               display_surf.blit(image_surf,( bx * 50 , by * 50))
           if maze_my[ bx + (by*self.M) ] == 3:
               display_surf.blit(fin,( bx * 50 , by * 50))
           if maze_my[ bx + (by*self.M) ] == 11:
               display_surf.blit(q1,( bx * 50 , by * 50))
           if maze_my[ bx + (by*self.M) ] == 22:
               display_surf.blit(q2,( bx * 50 , by * 50))
           if maze_my[ bx + (by*self.M) ] == 33:
               display_surf.blit(q3,( bx * 50 , by * 50))
           if maze_my[ bx + (by*self.M) ] == 44:
               display_surf.blit(q4,( bx * 50 , by * 50))
           bx = bx + 1
           if bx > self.M-1:
               bx = 0 
               by = by + 1


class App:
 
    windowWidth = 500
    windowHeight = 560
    player = 0
 
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self.fin = None
        self.player = Player()
        self.maze = Maze()
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        
        pygame.display.set_caption('Labyrinth by Sahak')
        self._running = True
        self._image_surf = pygame.image.load("player.png").convert()
        self._block_surf = pygame.image.load("block1.png").convert()
        self.q1 = pygame.image.load("q11.png").convert()
        self.q2 = pygame.image.load("q22.png").convert()
        self.q3 = pygame.image.load("q33.png").convert()
        self.q4 = pygame.image.load("q44.png").convert()
        self.fin = pygame.image.load("finish1.png").convert()
        self.bys = pygame.image.load("bysahak1.png").convert()
        self.heart = pygame.image.load("heart1.png").convert()
        
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        pass
    
    def on_render(self):
        global my_maze
        self._display_surf.fill((0,0,0))
        self._display_surf.blit(self._image_surf,(self.player.x,self.player.y))
        self.maze.draw(self._display_surf, self._block_surf, self.fin, my_maze, self.q1, self.q2, self.q3, self.q4, self.bys, self.heart)
        self.maze.draw(self._display_surf, self._block_surf, self.fin, my_maze, self.q1, self.q2, self.q3, self.q4, self.bys, self.heart)
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        global my_maze
        if self.on_init() == False:
            self._running = False
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            try:
                if (keys[K_RIGHT]):
                    self.player.moveRight()
     
                if (keys[K_LEFT]):
                    self.player.moveLeft()
     
                if (keys[K_UP]):
                    self.player.moveUp()
     
                if (keys[K_DOWN]):
                    self.player.moveDown()
     
                if (keys[K_ESCAPE]):
                    self._running = False
            except:
                pass
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 

theApp = App()
theApp.on_execute()

#    app.mainloop()
