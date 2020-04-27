#import random to give random moves from machine
import random

#codes for output in different colours
CEND    = '\33[0m'
CGREEN  = '\33[32m'
CRED    = '\33[31m'
CGREEN  = '\33[32m'
CYELLOW = '\33[33m'
CBLUE   = '\33[5m'

#moves allowed
moves= ['r','p','s']


#functions
def guess():
    '''
    This function is used to give the output from computer's side

    '''
    computer_move= random.randint(0,len(moves))
    return computer_move

def pos():
    '''
   This function will return the position of your move from the moves list 
    '''
    for i in range(len(moves)):
        if my_move==moves[i]:
            return i

def status():
    if my_move in moves:
        '''
        Checks if the input you gave is allowed or not'''

        if guess() == pos():
            '''
            Checks if your move and computer's move is same. If true then it returns "TIE"
            As we know it will be a tie
            '''
            return CYELLOW + "TIE" + CEND


        elif (guess()==0 and pos()==2) or (guess()==1 and pos()==0) or (guess()==2 and pos()==1):
            '''
            All winning condition
            '''
            return CGREEN + "YOU WON!" + CEND
        '''
        if none of these matches then you must have lost '''
        return CRED + "YOU LOST, TRY AGAIN!" + CEND
    return CYELLOW + "INVALID INPUT!" + CEND

'''
drivr function starts here
'''

while True:
    try:
        my_move= input(CBLUE + "Enter Your Move (rock , paper, scissor) :  " + CEND)[0]
        print("\n" +status()+ "\n_____________________\n" )
    except IndexError:
        print(CRED + "You did not entered anything" + CEND)


