import random;

noOfGuesses = 1
no = random.randint(0, 10)
def inputFromUser():
    global noOfGuesses
    guess = int(input("enter a number:"))
    check(guess)

def check(guess):
    global noOfGuesses
    if(guess==no):
        print('congrats! you did it! so proud of you! yay honey!')
        return 0
    elif(guess>no):
        print('try a smaller number hon')
        inputFromUser()
        noOfGuesses += 1
    else:
        print('try a larger number hon')
        inputFromUser()
        noOfGuesses += 1

inputFromUser()
if noOfGuesses != 1:
    print('you took', noOfGuesses, 'guesses')
