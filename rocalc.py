import math 
import os 


def start():
    os.system("cls")
    amnt_rbx = input("enter amount of robux: ")

    formula = math.floor(0.3 * int(amnt_rbx))

    print(f"amount after calculations: {formula}")
    print("\n\ntype return to make another calculation")
    a = input()
    if a == "return":
        start()
    

start()