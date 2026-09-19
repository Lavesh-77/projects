import mysql.connector as mc
import random

#Create Database
try:
    mycon=mc.connect(host='localhost',user='root',password='root@123')
    cur=mycon.cursor()
    cur.execute("CREATE DATABASE QUIZ")
    mycon.close()
except mc.Error as e:
    pass


#Create Tables
mycon=mc.connect(host='localhost',user='root',password='root@123',database='QUIZ')
cur=mycon.cursor()
cur.execute('create table if not exists Questions(Question varchar(200) unique,A varchar(100),B varchar(100),C varchar(100),D varchar(100),Answer varchar(10))')
cur.execute('create table if not exists users(user varchar(100) unique,score int)')
mycon.commit()
mycon.close()

#User Login
Name=input('Enter your name:')
mycon=mc.connect(host='localhost',user='root',password='root@123',database='QUIZ')
cur=mycon.cursor()
cur.execute('select user from users;')
data=cur.fetchall()
if data==[]:
    cur.execute("insert into users(user,score) values('{}',0)".format(Name.lower()))
    mycon.commit()
    cur.execute('select user from users;')
    data=cur.fetchall()
for i in data:
    if (Name.lower(),) not in data:
        cur.execute("insert into users(user,score) values('{}',0)".format(Name.lower))
        mycon.commit()
        print('=============================================================================================')
        print('welcome',Name.capitalize(),'to the quiz')
        break
    else:
        print('=============================================================================================')
        print('welcome back',Name.capitalize(),'to the quiz')
        break

#Menu
def start():
    print('=============================================================================================')   
    print('1.Start the Quiz\n2.Enter Question\n3.Exit')
    ch=int(input('Enter choice:'))
    if ch==1:
        Quiz()
    elif ch==2:
        Question()
    else:
        print('Thank you for using our Quiz application')
        exit()
        mycon.close()

#Enter Questions
def  Question():
    mycon=mc.connect(host='localhost',user='root',password='root@123',database='QUIZ')
    cur=mycon.cursor()
    ch='y'
    print('=============================================================================================')
    while ch=='y' or ch=='Y':
        Question=input('Enter Question:')
        Optiona=input('Enter option a:')
        Optionb=input('Enter option b:')
        Optionc=input('Enter option c:')
        Optiond=input('Enter option d:')
        Answer=input('Enter answer:')
        ch=input('Do you wish to add more questions(y/n):')
        print('=============================================================================================')
        cur.execute("insert into Questions(Question,A,B,C,D,Answer) values('{}','{}','{}','{}','{}','{}')".format(str(Question),Optiona,Optionb,Optionc,Optiond,Answer))
        mycon.commit()
    start()


#Take Quiz
def Quiz():   
    mycon=mc.connect(host='localhost',user='root',password='root@123',database='QUIZ')
    cur=mycon.cursor()
    cur.execute('select * from Questions')
    data=cur.fetchall()
    cur.execute('select score from users where user="{}"'.format(Name.lower()))
    score=cur.fetchall()
    random.shuffle(data)
    a=0
    ch='y'
    for i in data:
        if ch=='n':
            break
        print('=============================================================================================')
        print('Question:',i[0])
        print('a.',i[1])
        print('b.',i[2]) 
        print('c.',i[3])
        print('d.',i[4])
        ans=input('Enter your answer:')
        if ans==i[5]:
            print('Correct answer')
            a+=4
        else:
            print('Wrong answer')
            a-=1
        print('Your current score is:',score[0][0]+a)
        cur.execute('update users set score={} where user="{}"'.format(score[0][0]+a,Name.lower()))
        mycon.commit()
        ch=input('Do you want to continue(y/n):')
        print('=============================================================================================')

    start()
start()
mycon.close()
