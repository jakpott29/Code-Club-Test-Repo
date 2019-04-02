from random import randint
while True:
    pla = input("(R)ock, (P)aper, or (S)cissors: ")
    p = 0
    if pla == "r" or pla == "R":
        p = 1
    elif pla == "p" or pla == "P":
        p = 2
    else:
        p = 3
    c = randint(1,3)
    if c == 1:
        com = "R"
    elif c == 2:
        com = "P"
    else:
        com = "S"
    print(pla + " vs. " + com)
    if p == 3 and c == 1:
        print("You Lose")
    elif p > c:
        print("You Win")
    elif c == 3 and p == 1:
        print("You Win")
    elif c > p:
        print("You Lose")
    else:
        print("Is a tie")
    if pla == "exit" or pla == "Exit":
        break
