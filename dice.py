import random 
import keyboard
import time
def dice():
    print("this dice simulation are created by HK")
    while True:
        print('Rolling the dice Please wait...')
        time.sleep(0.3)
        dice_number = random.randint(1, 6)
        # print(dice_number)
        if dice_number == 1:
            print("_____________")
            print("|           |")
            print("|           |")
            print("|     1     |")
            print("|           |")
            print("|___________|")
        elif dice_number == 2:
            print("_____________")
            print("|           |")
            print("|     2     |")
            print("|           |")
            print("|     2     |")
            print("|___________|")
        elif dice_number == 3:
            print("_____________")
            print("|           |")
            print("|  3     3  |")
            print("|           |")
            print("|     3     |")
            print("|___________|")
        elif dice_number == 4:
            print("_____________")
            print("|           |")
            print("|  4     4  |")
            print("|           |")
            print("|  4     4  |")
            print("|___________|")
        elif dice_number == 5:
            print("_____________")
            print("|           |")
            print("|  5     5  |")
            print("|     5     |")
            print("|  5     5  |")
            print("|___________|")
        elif dice_number == 6:
            print("_____________")
            print("|           |")
            print("|  6     6  |")
            print("|  6     6  |")
            print("|  6     6  |")
            print("|___________|")
        print("press ENTER to continue or Ctrl+C to exit or just cross the window")
        keyboard.wait('enter')

if __name__ == '__main__':
    dice()
