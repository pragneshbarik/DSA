# MIT 6.0001 Lecture 6 Recursion

##############################
## Recursive Multiplication ##
##############################

def mult (a,b) :
    if b == 1 :
        return a 
    else :
        return a + mult (a, b-1)

##############################
##### Fibonacci Sequence #####
##############################

def fib(x) :
    if x == 0 or x == 1 :
        return 1
    else :
        return fib(x-1) + fib(x-2)


##############################
#### Recursive Factorial  ####
##############################

def fact (n) :
    if n == 1 :
        return 1
    else :
        return n * fact (n-1)

##############################
######  Towers of Hanoi ######
##############################

def towerHanoi (n):

    def printMove (fr, to) :
        print("Move from" + str(fr) + "to" + str(to))

    def Towers (n, fr, to, spare) :
        if n == 1 :
            printMove(fr, to)
        else :
            Towers (n-1, fr, spare, to)
            Towers (1, fr, to, spare)
            Towers (n-1, spare, to, fr)

##############################
##### Palindrome Checker #####
##############################

def is_palindrome (string) :
    if len(string) <= 1:
        return True
    else :
        return string[0] == string[-1] and is_palindrome (string[1:-1])
