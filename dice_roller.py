import random

def compete():

    dice_rolls = int(input('How many dice would you like to roll? '))
    dice_size = int(input('How many sides are the dice? '))
    stats = list()
    gamers = int(input('How many players are gonna play? '))
    for _ in range(gamers):
        nameg = input("What's your name? ")
        score = roller(dice_rolls, dice_size)
        stats.append([nameg, score])

    size = len(stats)
    for p in range(size):
        for i in range(p + 1, size):
            if stats[p][1] > stats[i][1]:
                stats[p], stats[i] =  stats[i], stats[p]

    for _ in range(size - 1, -1, -1):
        print(*stats[_])



def roller(dice_rolls, dice_size):
    dice_sum = 0

    for _ in range(0,dice_rolls):

        roll = random.randint(1, dice_size)
        dice_sum += roll
        if roll == 1:
            print(f'You rolled a {roll}! Critical Fail')
        elif roll == dice_size:
            print(f'You rolled a {roll}! Critical Success!')
        else:
            print(f'You rolled a {roll}')

    print(f'You rolled a total of {dice_sum}')
    return dice_sum




if __name__== "__main__":
  compete()
