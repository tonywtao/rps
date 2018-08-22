import random

rps_choice = ['r', 'p', 's']

def askInput():
    response = input('Type your input and press ENTER:\n')
    return response

def makeChoice():
    return random.choice(rps_choice)
    
def decideWin(user, cpu):
    if(user==cpu):
        return('Draw!')
    elif(user=='r' and cpu=='p'):
        return('You lose!')
    elif(user=='r' and cpu=='s'):
        return('You Win!')
    elif(user=='p' and cpu=='s'):
        return('You Lose!')
    elif(user=='p' and cpu=='r'):
        return('You Win!')
    elif(user=='s' and cpu=='p'):
        return('You Win!')
    elif(user=='s' and cpu=='r'):
        return('You Lose!')
    print('\n')
        
    

def main():
    print('Welcome to my Rock, Papers, Scissors Game!')
    print('Make your choice by inputing r, p, or s\n') 
    while(True):
        user_input = askInput()
        if(user_input.lower() not in rps_choice):
            print('Not a valid choice, try again!')
        else:
            print('Calculating...')
            cpu_choice = makeChoice()
            print('The CPU has made this choice: ', cpu_choice)
            print('\n')
            print(decideWin(user_input, cpu_choice))
            print('\n')


if __name__== "__main__":
    main()
