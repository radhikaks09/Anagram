import tkinter as tk
from PIL import ImageTk, Image

import mysql.connector as sql
import random
import threading
import time
import pickle

mycon=sql.connect(host='localhost', user='root', passwd='MySQL_R@d_B0okworm', database='projects')
cursor=mycon.cursor()

root=tk.Tk()
root.title('ANAGRAM')
root.configure(bg='light blue')
root.geometry('1500x800')
root.iconbitmap('Anagram Logo.ico')

screen1=tk.Tk()
screen2=tk.Tk()
screen3=tk.Tk()
playscreen=tk.Tk()
statscreen=tk.Tk()

screen1.withdraw()
screen2.withdraw()
screen3.withdraw()
playscreen.withdraw()
statscreen.withdraw()

root.protocol('WM_DELETE_WINDOW', lambda:buttonquit_click())
screen1.protocol('WM_DELETE_WINDOW', lambda:buttonquit_click())
screen2.protocol('WM_DELETE_WINDOW', lambda:buttonquit_click())
screen3.protocol('WM_DELETE_WINDOW', lambda:buttonquit_click())
playscreen.protocol('WM_DELETE_WINDOW', lambda:buttonquit_click())
statscreen.protocol('WM_DELETE_WINDOW', lambda:buttonquit_click())

home=ImageTk.PhotoImage(Image.open('Anagram Logo.png'))
button_home=tk.Button(root, image=home, font=('Arial Bold', 10), bg='lavender', command=lambda:buttonhome_click())
button_home.grid(row=0, column=0)

button_howtoplay=tk.Button(root, text='How to Play', height=5, width=40, font=('Arial Bold', 10), bg='lavender', command=lambda:buttonhtp_click())
button_howtoplay.place(x=625, y=350)

button_login=tk.Button(root, text='Login', height=5, width=13, font=('Arial Bold', 10), bg='lavender', command=lambda:buttonlogin_click())
button_signup=tk.Button(root, text='Sign Up', height=5, width=13, font=('Arial Bold', 10), bg='lavender', command=lambda:buttonsignup_click())
button_login.place(x=1225, y=1)
button_signup.place(x=1350, y=1)

button_play=tk.Button(root, text='Play as Guest', height=5, width=40, font=('Arial Bold', 10), bg='lavender', command=lambda:buttonplay_click())
button_play.place(x=625, y=250)

button_stats=tk.Button(root, text='Statistics', height=5, width=40, font=('Arial Bold', 10), bg='lavender', command=lambda:buttonstats_click())
button_stats.place(x=625, y=450)

button_quit=tk.Button(root, text='EXIT', height=2, width=10, font=('Arial Bold', 10), bg='lavender', command=lambda:buttonquit_click())
button_quit.place(x=750, y= 600)

def buttonquit_click():
    global screen1, screen2, screen3, playscreen, statscreen

    screen1.destroy()
    screen2.destroy()
    screen3.destroy()
    playscreen.destroy()
    statscreen.destroy()
    root.destroy()
    root.quit()

def buttonhome_click():
    root.deiconify()

    global screen1, screen2, screen3, playscreen, statscreen

    if screen1.wm_state()=='normal':
        screen1.withdraw()
    if screen2.wm_state()=='normal':
        screen2.withdraw()
    if screen3.wm_state()=='normal':
        screen3.withdraw()
    if playscreen.wm_state()=='normal':
        playscreen.withdraw()
    if statscreen.wm_state()=='normal':
        statscreen.withdraw()

def buttonhtp_click():
    global screen1, screen2, screen3, playscreen, statscreen

    if screen2.wm_state()=='normal':
        screen2.withdraw()
    if screen3.wm_state()=='normal':
        screen3.withdraw()
    if playscreen.wm_state()=='normal':
        playscreen.withdraw()
    if statscreen.wm_state()=='normal':
        statscreen.withdraw()

    screen1=tk.Tk()
    screen1.title('HOW TO PLAY')
    screen1.configure(bg='light blue')
    screen1.iconbitmap('Anagram Logo.ico')
    screen1.geometry('1500x800')

    root.withdraw()

    button_home=tk.Button(screen1, text='HOME', font=('Arial Bold', 10), bg='lavender', command=lambda:buttonhome_click())
    button_home.grid(row=0, column=0)

    l1=tk.Label(screen1, width=110, borderwidth=40, text='''Welcome to ANAGRAM!

How to play:

You can Play as Guest or Login if you have an account. If you are a new user you may Sign Up.

You can pick the topic and the difficulty level.
You will be given jumbled words from the topic and you will have to figure out what the word is.
You will be given five words and you have one hint for each word.
(The Hint will appear on the screen for 5 seconds. Don't worry, you can click the button to view it again.)

If you want to quit the game, you can click on the EXIT button or the X button.
ALL THE BEST!''', bg='lavender', fg='black', font=('Arial Bold', 15))

    l1.grid(row=1, column=1, padx=20, pady=20)

    button_login=tk.Button(screen1, text='Login', height=5, width=13, font=('Arial Bold', 10), bg='lavender', command=lambda:buttonlogin_click())
    button_signup=tk.Button(screen1, text='Sign Up', height=5, width=13, font=('Arial Bold', 10), bg='lavender', command=lambda:buttonsignup_click())
    button_login.place(x=675, y=600)
    button_signup.place(x=800, y=600)

    button_play=tk.Button(screen1, text='Play as Guest', height=5, width=40, font=('Arial Bold', 10), bg='lavender', command=lambda:buttonplay_click())
    button_play.place(x=625, y=500)

    button_quit=tk.Button(screen1, text='EXIT', height=2, width=10, font=('Arial Bold', 10), bg='lavender', command=lambda:buttonquit_click())
    button_quit.place(x=750, y= 700)

    screen1.mainloop()

def buttonplay_click():
    global screen1, screen2, screen3, playscreen, statscreen

    if screen1.wm_state()=='normal':
        screen1.withdraw()
    if screen2.wm_state()=='normal':
        screen2.withdraw()
    if screen3.wm_state()=='normal':
        screen3.withdraw()
    if statscreen.wm_state()=='normal':
        statscreen.withdraw()
    if playscreen.wm_state()=='normal':
        playscreen.withdraw()

    playscreen=tk.Tk()
    playscreen.title('PLAY')
    playscreen.configure(bg='light blue')
    playscreen.iconbitmap('Anagram Logo.ico')
    playscreen.geometry('1500x800')

    root.withdraw()

    button_home=tk.Button(playscreen, text='HOME', font=('Arial Bold', 10), bg='lavender', command=lambda:buttonhome_click())
    button_home.grid(row=0, column=0)

    button_quit=tk.Button(playscreen, text='EXIT', height=2, width=10, font=('Arial Bold', 10), bg='lavender', command=lambda:buttonquit_click())
    button_quit.place(x=750, y= 600)

    label_topics=tk.Label(playscreen, width=100, borderwidth=20, text='Choose a topic:', bg='lavender', fg='black', font=('Arial Bold', 15))
    label_topics.place(x=150, y=1)

    button_1=tk.Button(playscreen, text='COUNTRIES', height=2, width=40, font=('Arial Bold', 10), bg='lavender', command=lambda:button_click(1))
    button_2=tk.Button(playscreen, text='ANIMALS', height=2, width=40, font=('Arial Bold', 10), bg='lavender', command=lambda:button_click(2))
    button_3=tk.Button(playscreen, text='FAMOUS PERSONALITIES', height=2, width=40, font=('Arial Bold', 10), bg='lavender', command=lambda:button_click(3))
    button_4=tk.Button(playscreen, text='CARS', height=2, width=40, font=('Arial Bold', 10), bg='lavender', command=lambda:button_click(4))
    button_5=tk.Button(playscreen, text='CELESTIAL BODIES', height=2, width=40, font=('Arial Bold', 10), bg='lavender', command=lambda:button_click(5))
    button_6=tk.Button(playscreen, text='BUSINESS COMPANIES', height=2, width=40, font=('Arial Bold', 10), bg='lavender', command=lambda:button_click(6))
    button_7=tk.Button(playscreen, text='ELECTRONIC GADGETS/APPLIANCES', height=2, width=40, font=('Arial Bold', 10), bg='lavender', command=lambda:button_click(7))
    button_8=tk.Button(playscreen, text='BOOKS(CLASSICS)', height=2, width=40, font=('Arial Bold', 10), bg='lavender', command=lambda:button_click(8))
    button_9=tk.Button(playscreen, text='FLOWERS', height=2, width=40, font=('Arial Bold', 10), bg='lavender', command=lambda:button_click(9))
    button_10=tk.Button(playscreen, text='ELEMENTS FROM PERIODIC TABLE', height=2, width=40, font=('Arial Bold', 10), bg='lavender', command=lambda:button_click(10))

    button_1.place(x=625,y=100)
    button_2.place(x=625,y=150)
    button_3.place(x=625,y=200)
    button_4.place(x=625,y=250)
    button_5.place(x=625,y=300)
    button_6.place(x=625,y=350)
    button_7.place(x=625,y=400)
    button_8.place(x=625,y=450)
    button_9.place(x=625,y=500)
    button_10.place(x=625,y=550)

    def button_click(n):
        label_topics.place_forget()
        button_1.place_forget()
        button_2.place_forget()
        button_3.place_forget()
        button_4.place_forget()
        button_5.place_forget()
        button_6.place_forget()
        button_7.place_forget()
        button_8.place_forget()
        button_9.place_forget()
        button_10.place_forget()

        label_lod=tk.Label(playscreen, width=100, borderwidth=20, text='Choose your Level of Difficulty:', bg='lavender', fg='black', font=('Arial Bold', 15))
        button_easy=tk.Button(playscreen, text='EASY', height=2, width=40, font=('Arial Bold', 10), bg='lavender', command=lambda:threading.Thread(target=lambda:buttonlod_click('a')).start())
        button_diff=tk.Button(playscreen, text='DIFFICULT', height=2, width=40, font=('Arial Bold', 10), bg='lavender', command=lambda:threading.Thread(target=lambda:buttonlod_click('b')).start())

        label_lod.place(x=150, y=1)
        button_easy.place(x=625,y=100)
        button_diff.place(x=625,y=150)

        if n==1:
            f=open(r'WordsCountries.dat','rb')
        elif n==2:
            f=open(r'WordsAnimals.dat','rb')
        elif n==3:
            f=open(r'WordsFamousPersonalities.dat','rb')
        elif n==4:
            f=open(r'WordsCars.dat','rb')
        elif n==5:
            f=open(r'WordsCelestialBodies.dat','rb')
        elif n==6:
            f=open(r'WordsCompanies.dat','rb')
        elif n==7:
            f=open(r'WordsGadgets.dat','rb')
        elif n==8:
            f=open(r'WordsBooks.dat','rb')
        elif n==9:
            f=open(r'WordsFlowers.dat','rb')
        elif n==10:
            f=open(r'WordsElements.dat','rb')

        def buttonlod_click(m):
            label_lod.place_forget()
            button_easy.place_forget()
            button_diff.place_forget()

            easywords=pickle.load(f)
            diffwords=pickle.load(f)
            f.close()
            if m=='a':
                words=easywords
            elif m=='b':
                words=diffwords

            Lkeys=[y for y in words]
            randomkeys=random.sample(Lkeys, 5)

            score=0
            shuffL=[]
            wordL=[]
            hintL=[]
            for key in randomkeys:
                word=words[key][0]
                hint=words[key][1]
                wordshuff=word
                wordL+=[word]
                hintL+=[hint]
                while wordshuff==word:
                    splitwrd=word.split()
                    L=[]
                    for k in splitwrd:
                        x=k
                        if len(k)!=1:
                            while x==k:
                                l=list(k)
                                random.shuffle(l)
                                x=''.join(l)
                        L+=[x]
                    wordshuff=' '.join(L)
                shuffL+=[wordshuff]

            label_question=tk.Label(playscreen, width=100, borderwidth=20, text=shuffL[0], bg='lavender', fg='black', font=('Arial Bold', 15))
            label_question.place(x=150, y=1)

            entry_answer=tk.Entry(playscreen, width=80, borderwidth=5, font=('Arial Bold', 10))
            entry_answer.place(x=500, y=100)

            button_submit=tk.Button(playscreen, text='Submit', height=2, width=40, font=('Arial Bold', 10), bg='lavender', command=lambda:threading.Thread(target=lambda:buttonsubmit_click(0)).start())
            button_submit.place(x=1100, y=100)

            button_hint=tk.Button(playscreen, text='Hint', height=2, width=20, font=('Arial Bold', 10), bg='lavender', command=lambda:threading.Thread(target=lambda:buttonhint_click(0)).start())
            button_hint.place(x=400, y=150)

            u=0
            def buttonsubmit_click(v):
                nonlocal score, u
                u+=1
                ans=entry_answer.get()
                ANS=ans.upper()
                if ANS==wordL[v]:
                    if m=='a':
                        score+=30
                    elif m=='b':
                        score+=60
                    label_correct=tk.Label(playscreen, width=60, borderwidth=20, text='Hooray! Your answer is correct!', bg='lavender', fg='black', font=('Arial Bold', 15))
                    label_correct.place(x=400, y=300)
                    time.sleep(5)
                    label_correct.place_forget()
                    if v<4:
                        label_question.configure(text=shuffL[v+1])
                        ansl=len(ans)
                        entry_answer.delete(0, ansl)
                        button_submit.configure(command=lambda:threading.Thread(target=lambda:buttonsubmit_click(v+1)).start())
                        button_hint.configure(command=lambda:threading.Thread(target=lambda:buttonhint_click(v+1)).start())
                else:
                    label_incorrect=tk.Label(playscreen, width=60, borderwidth=20, text='Sorry, your answer is incorrect!', bg='lavender', fg='black', font=('Arial Bold', 15))
                    label_incorrect.place(x=400, y=300)
                    time.sleep(5)
                    label_incorrect.place_forget()
                    if v<4:
                        label_question.configure(text=shuffL[v+1])
                        ansl=len(ans)
                        entry_answer.delete(0, ansl)
                        button_submit.configure(command=lambda:threading.Thread(target=lambda:buttonsubmit_click(v+1)).start())
                        button_hint.configure(command=lambda:threading.Thread(target=lambda:buttonhint_click(v+1)).start())

                if u==5:
                    label_question.place_forget()
                    entry_answer.place_forget()
                    button_submit.place_forget()
                    button_hint.place_forget()

                    label_score=tk.Label(playscreen, width=60, borderwidth=20, text=('Score:', score), bg='lavender', fg='black', font=('Arial Bold', 15))
                    label_score.place(x=400, y=100)

                    global p
                    if p!='':
                        cursor.execute("select High_Score from anagram where Username='{}';".format(p))
                        data=cursor.fetchone()
                        if score>data[0]:
                            highscore=score
                            cursor.execute("update anagram set High_Score={} where Username='{}';".format(highscore, p))
                            mycon.commit()
                            label_highscore=tk.Label(playscreen, width=60, borderwidth=20, text=('New Highscore:', highscore), bg='lavender', fg='black', font=('Arial Bold', 15))
                            label_highscore.place(x=400, y=200)

                    button_play=tk.Button(playscreen, text='Play Again', height=2, width=40, font=('Arial Bold', 10), bg='lavender', command=lambda:buttonplay_click())
                    button_play.place(x=625, y=300)

                    button_home.grid_forget()
                    button_home.configure(height=2, width=40)
                    button_home.place(x=625, y=350)

                    button_stats=tk.Button(playscreen, text='Statistics', height=2, width=40, font=('Arial Bold', 10), bg='lavender', command=lambda:buttonstats_click())
                    button_stats.place(x=625, y=400)

            def buttonhint_click(w):
                label_hint=tk.Label(playscreen, width=180, borderwidth=20, text=hintL[w], bg='lavender', fg='black', font=('Arial Bold', 10))
                label_hint.place(x=20, y=200)
                time.sleep(5)
                label_hint.place_forget()

            cursor.execute("select * from anagram;")
            data=cursor.fetchall()
            for i in data:
                if i[0]==p:
                    cursor.execute("update anagram set No_of_Games=No_of_Games+1 where Username='{}';".format(p))
                    mycon.commit()

    playscreen.mainloop()

p=q=''
def buttonlogin_click():
    global screen1, screen2, screen3, playscreen, statscreen

    if screen1.wm_state()=='normal':
        screen1.withdraw()
    if screen3.wm_state()=='normal':
        screen3.withdraw()
    if playscreen.wm_state()=='normal':
        playscreen.withdraw()
    if statscreen.wm_state()=='normal':
        statscreen.withdraw()

    screen2=tk.Tk()
    screen2.title('LOGIN')
    screen2.configure(bg='light blue')
    screen2.iconbitmap('Anagram Logo.ico')
    screen2.geometry('1500x800')

    root.withdraw()

    button_home=tk.Button(screen2, text='HOME', font=('Arial Bold', 10), bg='lavender', command=lambda:buttonhome_click())
    button_home.grid(row=0, column=0)

    label_name=tk.Label(screen2, width=20, borderwidth=10, text='User Name', bg='lavender', fg='black', font=('Arial Bold', 15))
    entry_name=tk.Entry(screen2, width=40, borderwidth=5, font=('Arial Bold', 10))

    label_passwd=tk.Label(screen2, width=20, borderwidth=10, text='Password', bg='lavender', fg='black', font=('Arial Bold', 15))
    entry_passwd=tk.Entry(screen2, show='*', width=40, borderwidth=5, font=('Arial Bold', 10))

    label_name.place(x=500, y=5)
    entry_name.place(x=800, y=15)
    label_passwd.place(x=500, y=100)
    entry_passwd.place(x=800, y=110)
    button_log=tk.Button(screen2, text='Login', height=2, width=40, font=('Arial Bold', 10), bg='lavender', command=lambda:buttonlog_click())
    button_log.place(x=625, y=180)

    button_quit=tk.Button(screen2, text='EXIT', height=2, width=10, font=('Arial Bold', 10), bg='lavender', command=lambda:buttonquit_click())
    button_quit.place(x=750, y= 600)

    cnt=0
    def buttonlog_click():
        global p
        nonlocal cnt
        p=entry_name.get()
        q=entry_passwd.get()
        cursor.execute("select * from anagram;")
        data=cursor.fetchall()
        for i in data:
            if p==i[0] and q==i[1]:
                label_name.place_forget()
                entry_name.place_forget()
                label_passwd.place_forget()
                entry_passwd.place_forget()
                button_log.place_forget()
                button_play=tk.Button(screen2, text='Play', height=5, width=40, font=('Arial Bold', 10), bg='lavender', command=lambda:buttonplay_click())
                button_play.place(x=625, y=250)

                if cnt>0:
                    label_tryagain.place_forget()
                break
            elif (p!=i[0] and q==i[1]) or (p==i[0] and q!=i[1]):
                label_tryagain=tk.Label(screen2, width=60, borderwidth=10, text='Incorrect username or password! Try again', bg='lavender', fg='black', font=('Arial Bold', 15))
                label_tryagain.place(x=400, y=250)
                l1=len(entry_name.get())
                l2=len(entry_passwd.get())
                entry_name.delete(0,l1)
                entry_passwd.delete(0,l2)
                cnt+=1

    screen2.mainloop()

def buttonsignup_click():
    global screen1, screen2, screen3, playscreen, statscreen

    if screen1.wm_state()=='normal':
        screen1.withdraw()
    if screen2.wm_state()=='normal':
        screen2.withdraw()
    if playscreen.wm_state()=='normal':
        playscreen.withdraw()
    if statscreen.wm_state()=='normal':
        statscreen.withdraw()

    screen3=tk.Tk()
    screen3.title('SIGN UP')
    screen3.configure(bg='light blue')
    screen3.iconbitmap('Anagram Logo.ico')
    screen3.geometry('1500x800')

    root.withdraw()

    button_home=tk.Button(screen3, text='HOME', font=('Arial Bold', 10), bg='lavender', command=lambda:buttonhome_click())
    button_home.grid(row=0, column=0)

    label_name=tk.Label(screen3, width=20, borderwidth=10, text='User Name', bg='lavender', fg='black', font=('Arial Bold', 15))
    entry_name=tk.Entry(screen3, width=40, borderwidth=5, font=('Arial Bold', 10))

    label_passwd=tk.Label(screen3, width=20, borderwidth=10, text='Password', bg='lavender', fg='black', font=('Arial Bold', 15))
    entry_passwd=tk.Entry(screen3, show='*', width=40, borderwidth=5, font=('Arial Bold', 10))

    label_name.place(x=500, y=5)
    entry_name.place(x=800, y=15)
    label_passwd.place(x=500, y=100)
    entry_passwd.place(x=800, y=110)
    button_sign=tk.Button(screen3, text='Sign Up', height=2, width=40, font=('Arial Bold', 10), bg='lavender', command=lambda:buttonsign_click())
    button_sign.place(x=625, y=180)

    button_quit=tk.Button(screen3, text='EXIT', height=2, width=10, font=('Arial Bold', 10), bg='lavender', command=lambda:buttonquit_click())
    button_quit.place(x=750, y= 600)

    def buttonsign_click():
        global p
        p=entry_name.get()
        q=entry_passwd.get()
        cursor.execute("select * from anagram;")
        data=cursor.fetchall()
        accountl=[]

        for i in data:
            accountl+=[i[0], i[1]]
        if [p,q] not in accountl:
            query="insert into anagram values ('{}','{}',{},{});"
            cursor.execute(query.format(p, q, 0, 0))
            mycon.commit()
            label_name.place_forget()
            entry_name.place_forget()
            label_passwd.place_forget()
            entry_passwd.place_forget()
            button_sign.place_forget()

            button_play=tk.Button(screen3, text='Play', height=5, width=40, font=('Arial Bold', 10), bg='lavender', command=lambda:buttonplay_click())
            button_play.place(x=625, y=250)

    screen3.mainloop()

def buttonstats_click():
    global screen1, screen2, screen3, playscreen, statscreen

    if screen1.wm_state()=='normal':
        screen1.withdraw()
    if screen2.wm_state()=='normal':
        screen2.withdraw()
    if screen3.wm_state()=='normal':
        screen3.withdraw()
    if playscreen.wm_state()=='normal':
        playscreen.withdraw()

    statscreen=tk.Tk()
    statscreen.title('STATISTICS')
    statscreen.configure(bg='light blue')
    statscreen.iconbitmap('Anagram Logo.ico')
    statscreen.geometry('1500x800')

    root.withdraw()

    button_home=tk.Button(statscreen, text='HOME', font=('Arial Bold', 10), bg='lavender', command=lambda:buttonhome_click())
    button_home.grid(row=0, column=0)

    button_quit=tk.Button(statscreen, text='EXIT', height=2, width=10, font=('Arial Bold', 10), bg='lavender', command=lambda:buttonquit_click())
    button_quit.place(x=750, y= 600)

    cursor.execute("select Username, No_of_Games, High_Score from anagram;")
    data=cursor.fetchall()
    list=[('USERNAME','NO. OF GAMES', 'HIGH SCORE')]+data
    total_rows=len(list)
    total_columns=len(list[0])

    for i in range(total_rows):
        for j in range(total_columns):
            entry_table=tk.Entry(statscreen, width=50, font=('Arial Bold', 10))
            entry_table.grid(row=i+3, column=j+5)
            entry_table.insert(len(entry_table.get()), list[i][j])
            entry_table.configure(state='disabled')

    statscreen.mainloop()

root.mainloop()
