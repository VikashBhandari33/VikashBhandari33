import random as rn

def rps():
    choice = rn.randint(1,3)
    return choice
def check(x, y):
    wins =  [[1,3],[3,2],[2,1]]
    loss = [[1,2], [2,3],[3,1]]
    ls = [x , y]
    if ls in wins:
        print("\nyou won this round !")
        return 0
    elif ls in loss:
        print("\nyou lost this round !")
        return 1
    else:
        print("\nthis round is draw !")

if __name__ == "__main__":
    print("welcome to the Rock paper scissors Game !")
    won = 0
    lost = 0
    rnd = 0
    while (rnd < 3):
        print(f"\nROUND {rnd+1}\n")
        print("1 for rock \n2 for paper \n3 for scissor")
        p_choice = int(input("\nenter your choice :"))
        c_choice = rps()
        if c_choice == 1:
            print("\ncomputer had chosen Rock")
        elif c_choice == 2:
            print("\ncomputer had chosen Paper")
        else:
            print("\ncomputer had chosen Scissors")

        cwk = check(p_choice, c_choice)
        print("_"*25)
        if cwk == 0:
            won += 1
        if cwk == 1:
            lost += 1
        rnd += 1
    print("\n Final Score")
    print(f"\n you -{won} ")
    print(f" computer -{lost}")
    if won > lost:
        print("\nyou won the game!")
    elif lost > lost:
        print("\nyou lost the game!")
    else:
        print("\n this game is draw !")

            





