import random
# Snake water gun or rock paper Scissors
def gameWin(comp,you):
#    If two values are equal then declare a tie b/w them.
    if comp == you:
            return None
    # Check for all possibilities when computer chose s,w,g.
    elif comp == 's':
       
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print(input("Comp Turn: Snake(s) Water(w) or Gun(g) ?"))
randNo= random.randint(1,3)
#print(randNo)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you= input("your's Turn: Snake(s) Water(w) or Gun(g) ?")
a = gameWin(comp,you)

print(f"Computer chose {comp}")
print(f"you chose {you}")

if a == None:
    print("The game is a Tie!")
elif a:
    print("You Win!")
else:
    print("you Lose!")