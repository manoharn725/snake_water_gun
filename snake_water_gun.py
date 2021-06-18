import random

def gamewin(comp , you):

    if(comp == you):
        return None

    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True

    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True

    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True

print(f"comp turn: Snake(s),Water(w),Gun(g)?")
randomNo= random.randint(1,3)
if randomNo == 1:
    comp ='s'
elif randomNo == 2:
    comp ='w'
elif randomNo == 3:
    comp ='g'

you =input(f"your turn: Snake(s),Water(w),Gun(g): ")
a =gamewin(comp,you)

print(f"computer choose: {comp}")
print(f"your choose: {you}")

if(a==None):
    print("the match is tie")
elif(a):
    print("you won!")
else:
    print("you loose!")        