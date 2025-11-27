import os

Operation = input("Choose an operation you would like to use (+ , - , * , / , **):") #Variable wat gedefine is
num = int(input("Choose a number between 1-100: ")) #Variable wat gedefine word

def clear_screen(): #Funksie om die Terminal te verwyder
    if os.name == 'nt':  
        os.system('cls')
    else:                
        os.system('clear')

Continuation = "Y"

while Continuation == "Y": #Jou sentinal variable wat toelaat om die loop te einding
    clear_screen()
    Operation = input("Choose an operation you would like to use (+ , - , * , / , **):")

    num = int(input("Choose a number between 1-100: ")) #int Funksie staan vir Integers wat nommers soos jou floats
    while num < 1 or num > 100:
        print("Your number does not meet the criteria")
        num = int(input("Choose a number between 1-100: "))

    num2 = int(input("Choose a number between 1-100: "))
    while num2 < 1 or num2 > 100:
        print("Your number does not meet the criteria")
        num2 = int(input("Choose a number between 1-100: "))

    if Operation == "+": #if Funksie wat se dat n sekere kode gespeel moet word as (if) n sekere kriteria ge-ontmoet word
        result = num + num2
    elif Operation == "-": #elif Funksie wat gespeel word as die user input , fals is of nie die kriteria is van die if funksie nie
        result = num - num2
    elif Operation == "*":
        result = num * num2
    elif Operation == "/":
        result = num / num2
    elif Operation == "**":
        result = num ** num2
    else: #else Funksie wat gespeel word as die if funksie fals is
        result = "Invalid Operation"

    print(f"{num} {Operation} {num2} = {result}") #Vertoon die antwoord of display om die display skerm
                                                  #F-strings word gebruik met "Curly Brackets" vir die variables
    Continuation = input("Would you like to continue (Y/N)? ").upper() #upper.() Maak die input a hoofletter

print("Have a GREAT day!!!")

