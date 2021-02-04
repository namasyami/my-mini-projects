# table of any number:
while True:
    num = int(input("Enter num: "))
    table = [i * num for i in range(1,11)]
    print(table)
    
# calculator-1
while True:
    num1, num2, sign = map(input, ["Enter num1: ", "Enter num2: ", "Enter sign: "])
    if sign in ("+", "-", "*", "**", "/", "//", "%"):
        try:
            print(eval("%s%s%s" % (float(num1), sign, float(num2))))
        except Exception as e:
            print(f"ERROR IS: {e} ")

# calculator-2
while True:
    calci = (input("Enter 'num + sign': "))
    try:
        print(eval(calci))
    except Exception as e:
        print(f"error is: {e}")

# calculator-3
while True:
    num1 = float(input("Enter Your First Number: "))
    num2 = float(input("Enter Your second Number: "))
    opp = input("Enter Your operator: ")

    if opp == "+":
        print (num1 + num2)
    elif opp == "-":
        print(num1 - num2)
    elif opp == "*":
        print(num1 * num2)
    elif opp == "/":
        print(num1 / num2)
    else: 
        print("enter valid values")   


# digital clock
from datetime import datetime
import time
while(True):
    now = datetime.now()
    print(now.strftime("%d-%m-%Y and %I:%M:%S"), end="\r")
    # time.sleep(2)

# alarm
import datetime
import os
alarm = False
while alarm==False:
    now = str(datetime.datetime.now().time())
    print(now)
    if now>="09:30:00-000000":
        alarm = True
        os.system("Ring4Python.mp3")

def square(num):
     return num*num
l = [2,3,4]
print(list(map(square, l)))
print(list(filter(square, l)))
print(list(reduce(square, l)))

# perfect guess game:
answer = 35
for i in range(5):
      guess = int(input("guess your answer: "))
      if guess == answer:
            print("you won!")
            break
      elif guess<=20:
            print("answer is more than 30;")
      elif guess>=40:
            print("answer is less than 40;")
      else: 
            print("guess again...")
print("thanks for playing game!!!")


# rock, paper, scissors
import random

lst = ["rock", "paper", "scissors"]
computer = random.choice(lst)
print(computer)

player = input("enter your choise: ")

if computer == player:
    print("it's tie: play again: ")
elif computer == "rock":
    if player == "paper":
        print("you won! ")
    else:
        print("you lost!")
elif computer == "paper":
    if player == "scissors":
        print("you won!")
    else:
        print("you lost!")
elif computer == "scissors":
    if player == "rock":
        print("you won!")
    else:
        print("you lost!")














