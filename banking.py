import json
import time
import os
import pickle
from getpass import getpass
def main_menu():
    os.system('cls')
    time.sleep(1)
    s='''\n1.Signup\n2.Login\n3.Exit'''
    print(s)
    ch=int(input('Choose any option from above'))
    if ch==1:
        signup()
    elif ch==2:
        login()
    else:
        exit()
def exit():
    os.system('cls')
    print('Thanks for using our service')
    for i in '..........Exciting..........':
        time.sleep(0.1)
        print(i,end='')
def signup():
    print('\n')
    print('Now you are at signup page')
    print('\n')
    d={'Name':input('Enter Name'),'Bal':int(input('Enter Balance')),'Pwd':getpass('Enter Password')}
    last_acc=int(os.listdir('Bank/')[-1][0:4])
    path=f'bank/{last_acc+1}'+'.json'
    f=open(path,'w')
    json.dump(d,f)
    f.close()
    print('Account Created Successfully')
    print(f'Your Account Number is: {last_acc+1}')
    print('Now You Can Login')
    time.sleep(2)
    main_menu()
def login():
    acc=input('enter account number')
    path=acc+'.json'
    if path in os.listdir('Bank/'):
        f=open(f'Bank/{path}','r')
        data=json.load(f)
        pwd=getpass('Enter Password')
        if pwd==data['Pwd']:
            s='''1.Withdrawl\n2.Deposit\n3.Check Balance\n4.Update Password\n5.main menu'''
            print(s)
            ch=int(input('Choose any option from above'))
            if ch==1:
                withdrawl(acc,pwd)
            elif ch==2:
                deposit(acc,pwd)
            elif ch==3:
                check_bal(acc,pwd)
            elif ch==4:
                update_pwd(acc,pwd)
            else:
                main_menu()
        else:
            print('Invalid Password')
            login()
    else:
        print('Account Not Exist')
        main_menu()
def withdrawl(acc,pwd):
    print('\n')
    print('You are at Debit Transaction page')
    f=open(f"Bank/{acc}.json")
    data=json.load(f)
    f.close()
    bal=int(input('Enter the Balance amount which you want to withdrawl'))
    if data['Bal']>=bal:
        data['Bal']-=bal
        time.sleep(1)
        print(f"Withdrawl Successful\nYour Updated Balance is :{data['Bal']}")
        f=open(f"Bank/{acc}.json",'w')
        json.dump(data,f)
        f.close()
        time.sleep(1)
        login()
    else:
        print('Insufficient Balance Amount')
        f.close()
        time.sleep(2)
        main_menu()
def deposit(acc,pwd):
    print('\n')
    print('You are at Credit Transaction page')
    f=open(f"Bank/{acc}.json",'r')
    data=json.load(f)
    f.close()
    bal=int(input('Enter the Balance amount which you want to deposit'))
    data['Bal']+=bal
    time.sleep(1)
    print(f"Deposit Successful\nYour Updated Balance is :{data['Bal']}")
    f=open(f"Bank/{acc}.json",'w')
    json.dump(data,f)
    f.close()
    time.sleep(2)
    main_menu()
def check_bal(acc,pwd):
    print('\n')
    print('You are at Check Balance page')
    f=open(f"Bank/{acc}.json",'r')
    data=json.load(f)  
    f.close()
    print(f"Your Account Balance is {data['Bal']}")
    time.sleep(3)
    main_menu()
def update_pwd(acc,pwd):
    print('\n')
    print('You are at Update Password page')
    f=open(f"Bank/{acc}.json",'r')
    data=json.load(f)  
    f.close()
    pass1=getpass('Enter New Password: ')
    pass2=input('Confirm Password: ')
    if pass1==pass2:
        data['Pwd']=pass1
        print('Password Updated Successfully')
        f=open(f"Bank/{acc}.json",'w')
        json.dump(data,f)  
        f.close()
        time.sleep(2)
        main_menu()
    else:
        update_pwd(acc,pwd)
main_menu()
