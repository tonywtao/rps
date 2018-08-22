import pytest


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

def test_decideWin():
    assert decideWin('r', 's') == 'You Win!'
    assert decideWin('s', 's') == 'Draw!'