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
while True:
      
      random_choise = ["rock", "paper", "scissors"]
      player = input("Hey player! Enter Your Choise: ")
      computer = random.choice(random_choise)
      print(f"You chose {player} and computer chose {computer}:")

      if computer == player:
            print("It's Tie: Let's play again:")
      elif computer == "rock":
            if player == "paper":
                  print("You Won! Because paper wraps the rock:")
            else:
                  print("You Lost! Because rock smashes the scissors:")
      elif computer == "paper":
            if player == "scissors":
                  print("You Won! Because scissors cut the paper:")
            else:
                  print("You Lost! Because paper wraps the rock:")
      elif computer == "scissors":
            if player == "rock":
                  print("You Won! Because rock smashes the scissors:")
            else:
                  print("You Lost! Because scissors cut the paper:")
      print("")

# Library Management System using "if, else" and "Loops"
from time import  sleep
book_list = ["Geeta", "Ramayan", "Mahabharat", "Darshan", "Vedas", "Vyakaran"]
options = """
 === Welcome to our Library ===
  options are:
    1. Show book list
    2. Borrow the book
    3. Return the book
    4. Exit the program
     """
while True:
    print(options)
    opt =int(input("Select from the options: "))
    if opt==1:
        for book in book_list:
            print("=> " + book)
            sleep(0.5)
        print("")
            
    elif opt==2:
        book_borrowed = input("Enter book-name you want to borrow: ")
        print(f"You have borrowed the book named '{book_borrowed}'")
        book_list.remove(book_borrowed)
        sleep(1)
        print("")
        
    elif opt == 3:
        book_returned = input("Enter book-name you want to return: ")
        print(f"You have returned the book named '{book_returned}'")
        book_list.append(book_returned)
        sleep(1)
        print("")
        
    elif opt == 4:
        break
print("Thanks for using the our Library")

# Library Management System using "functions"
from time import  sleep

lst = ["Geeta", "Ramayan", "Mahabharat", "Darshan", "Vedas", "Vyakaran"]
def book_list():
    """will list available  books"""
    for i in lst:
        print("=>" + i)
        sleep(0.5)
def book_borrow():
    """will list borrowed book"""
    book_borrowed = input("Enter book-name you want to borrow: ")
    print(f"You have borrowed the book named '{book_borrowed}'")
    lst.remove(book_borrowed)
    sleep(1)
def book_return():
    """will list returned book"""
    book_returned = input("Enter book-name you want to return: ")
    print(f"You have returned the book named '{book_returned}'")
    lst.append(book_returned)
    sleep(1)
options = """
 === Welcome to our Library ===
  options are:
    1. Show book list
    2. Borrow the book
    3. Return the book
    4. Exit the program
     """
while True:
    print(options)
    opt =int(input("Select from the options: "))
    
    if opt==1:
        book_list()
    elif opt==2:
        book_borrow()
    elif opt == 3:
        book_return()
    elif opt == 4:
        break
print("Thanks for using the our Library")
    


# Library Management System using "OOPs" without "constructor"
from time import  sleep

lst = ["Geeta", "Ramayan", "Mahabharat", "Darshan", "Vedas", "Vyakaran"]
class LibraryManagementSystem:
    def book_list(self):
        """will list available  books"""
        for i in lst:
            print("=>" + i)
            sleep(0.5)
    def book_borrow(self):
        """will list borrowed book"""
        book_borrowed = input("Enter book-name you want to borrow: ")
        print(f"You have borrowed the book named '{book_borrowed}'")
        lst.remove(book_borrowed)
        sleep(1)
    def book_return(self):
        """will list returned book"""
        book_returned = input("Enter book-name you want to return: ")
        print(f"You have returned the book named '{book_returned}'")
        lst.append(book_returned)
        sleep(1)
options = """
 === Welcome to our Library ===
  options are:
    1. Show book list
    2. Borrow the book
    3. Return the book
    4. Exit the program
    """
LMS = LibraryManagementSystem()
while True:
    print(options)
    opt =int(input("Select from the options: "))
    
    if opt==1:
        LMS.book_list()
    elif opt==2:
        LMS.book_borrow()
    elif opt == 3:
        LMS.book_return()
    elif opt == 4:
        break
print("Thanks for using the our Library")


# Library Management System using "OOPs" with "constructor"
from time import  sleep

class LibraryManagementSystem:
    """this is our Library class"""
    def __init__(self, bookList):
        self.bookList = bookList
    def book_list(self):
        """will list available  books"""
        for i in self.bookList:
            print("=>" + i)
            sleep(0.5)
    def book_borrow(self):
        """will list borrowed book"""
        book_borrowed = input("Enter book-name you want to borrow: ")
        print(f"You have borrowed the book named '{book_borrowed}'")
        self.bookList.remove(book_borrowed)
        sleep(1)
    def book_return(self):
        """will list returned book"""
        book_returned = input("Enter book-name you want to return: ")
        print(f"You have returned the book named '{book_returned}'")
        self.bookList.append(book_returned)
        sleep(1)
options = """
 === Welcome to our Library ===
  options are:
    1. Show book list
    2. Borrow the book
    3. Return the book
    4. Exit the program
    """
LMS = LibraryManagementSystem(["Geeta", "Ramayan", "Mahabharat", "Darshan", "Vedas", "Vyakaran"])
while True:
    print(options)
    opt =int(input("Select from the options: "))
    
    if opt==1:
        LMS.book_list()
    elif opt==2:
        LMS.book_borrow()
    elif opt == 3:
        LMS.book_return()
    elif opt == 4:
        break
print("Thanks for using the our Library")

# Tic-Tac-Toe game with little bug when player2 selects place
import random
from time import sleep
dic = {
    "1":" ","2":" ","3":" ",
    "4":" ","5":" ","6":" ",
    "7":" ","8":" ","9":" ",
    }

def Board():
    print(dic["1"] + "|" + dic["2"] + "|" + dic["3"] )
    print("-+-+-")
    print(dic["4"] + "|" + dic["5"] + "|" + dic["6"] )
    print("-+-+-")
    print(dic["7"] + "|" + dic["8"] + "|" + dic["9"] )
Board()
def PlayTicTacToe():
    for i in dic:
        player1 = input("\nHey player1! Enter value: ")
        if dic[player1] == " ":
            dic[player1] = "x"
            Board()
        else:
            print("Already Selected!! Chose Another Place:")
            continue
        if dic["1"] == dic["2"] == dic["3"]  == "x":
            print("Congratulations!!! player1 wins........")
            break
        elif dic["4"] == dic["5"] == dic["6"]  == "x":
            print("Congratulations!!! player1 wins........")
            break
        elif dic["7"] == dic["8"] == dic["9"]  == "x":
            print("Congratulations!!! player1 wins........")
            break
        elif dic["1"] == dic["4"] == dic["7"]  == "x":
            print("Congratulations!!! player1 wins........")
            break
        elif dic["2"] == dic["5"] == dic["8"]  == "x":
            print("Congratulations!!! player1 wins........")
            break
        elif dic["3"] == dic["6"] == dic["9"]  == "x":
            print("Congratulations!!! player1 wins........")
            break
        elif dic["1"] == dic["5"] == dic["9"]  == "x":
            print("Congratulations!!! player1 wins........")
            break
        elif dic["3"] == dic["5"] == dic["7"]  == "x":
            print("Congratulations!!! player1 wins........")
            break

    
        computer = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        print("\nNow it's turn of player2: ")
        sleep(1)
        player2 = random.choice(computer)
        print(f"player2 selected place: {player2}")
        if dic[player2] == " ":
            dic[player2] = "o"
            
        else:
            print("Already Selected!! Chose Another Place:")
            player2 = random.choice(computer)
            print(f"player2 selected place: {player2}")
            if dic[player2] == " ":
                dic[player2] = "o"
        Board()      
        
        if dic["1"] == dic["2"] == dic["3"]  == "o":
            print("player2 wins..... Sorry you Lost....Good Luck Ahead")
            break
        elif dic["4"] == dic["5"] == dic["6"]  == "o":
            print("player2 wins..... Sorry you Lost....Good Luck Ahead")
            break
        elif dic["7"] == dic["8"] == dic["9"]  == "o":
            print("player2 wins..... Sorry you Lost....Good Luck Ahead")
            break
        elif dic["1"] == dic["4"] == dic["7"]  == "o":
            print("player2 wins..... Sorry you Lost....Good Luck Ahead")
            break
        elif dic["2"] == dic["5"] == dic["8"]  == "o":
            print("player2 wins..... Sorry you Lost....Good Luck Ahead")
            break
        elif dic["3"] == dic["6"] == dic["9"]  == "o":
            print("player2 wins..... Sorry you Lost....Good Luck Ahead")
            break
        elif dic["1"] == dic["5"] == dic["9"]  == "o":
            print("player2 wins..... Sorry you Lost....Good Luck Ahead")
            break
        elif dic["3"] == dic["5"] == dic["7"]  == "o":
            print("player2 wins..... Sorry You Lost....Good Luck Ahead")
            break
PlayTicTacToe()


      
   





