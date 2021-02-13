import random


def game():
    user=input("Choose between rock(r) or paper(p) or scissor(s)\n")
    computer=random.choice(['r','p','s'])

    if user==computer:
        print("The computer cho se the same as you ,ITS A TIE")

    if is_win(user,computer):
        return 'you won !'

    return 'you Lost !'


def is_win(player,opponent):
    if (player=='r' and opponent=='s') or (player=='p' and opponent=='s') or (player=='s'and opponent=='p'):
        return True


print(game())
