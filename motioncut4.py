import random
import time
flag=True
while flag:
    print("Welcome to the game of 'Heads' or 'Tails'")
    print("-------------------------------------------------")
    no_of_flips=int(input("Enter the number of flips you want to make:"))
    heads=0
    tails=0
    for i in range(no_of_flips):
        flip=random.choice(['Tails','Heads'])
        print("3...")
        time.sleep(1)
        print("3...2...")
        time.sleep(1)
        print("3...2...1")
        time.sleep(1)
        print(f"You got {flip}")   
        print("--------------------") 
        if flip=='Tails':
            tails+=1
        else:
            heads+=1
    print(f"Total number of heads and percentage obtained out of {no_of_flips} are {heads} and {((heads/no_of_flips)*100):.2f} %")
    print(f"Total number of tails and percentage obtained out of {no_of_flips} are {tails} and {((tails/no_of_flips)*100):.2f} %")
    print("---------------------------------------------------------------")
    ch=input("Do you want to play another session of 'Heads' or 'Tails'? [Y/N]").upper()
    print("---------------------------------------------------------------")
    if ch=='N':
        print("Hope you enjoyed your session!!")
        flag=False
    else:
        flag=True
