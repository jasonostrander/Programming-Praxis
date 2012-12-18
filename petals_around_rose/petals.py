from random import randint
petals = {1:0, 2:0, 3:2, 4:0, 5:4, 6:0}
num_correct = 0

def roll_dice():
    return [randint(1, 6) for i in range(5)]

def get_petals(li):
    return sum([petals[i] for i in li])

print '''
Let's play 'Petals Around The Rose.'
The name of the game is significant.
At each turn I will roll five dice,
then ask you for the score, which
will always be zero or an even number.
After you guess the score, I will tell
you if you are right, or tell you the
correct score if you are wrong. The game
ends when you prove that you know the
secret by guessing the score correctly
six times in a row.
'''

while True:
    dice = roll_dice()
    correct = get_petals(dice)
    
    print 'The five dice are:', ' '.join([str(i) for i in dice])
    guess = int(raw_input('What is the score? '))

    if guess == get_petals(dice):
        print 'Correct'
        num_correct += 1
    else:
        print 'The correct score is', correct
        num_correct = 0

    if num_correct == 1:
        break

print '''
Congratulations! You are now a member
of the Fraternity of the Petals Around
The Rose. You must pledge never to
reveal the secret to anyone.'''
