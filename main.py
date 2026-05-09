import sys
import time
import random

# Color definitions
blue= "\033[34m"
nig = '\033[32m'  # Green
red = '\033[31m'  # Red
ger = '\033[0m'   # Reset
soft = 'Opera AI: '
white = '\033[37m'

print(f"{nig}{soft}Type 'command' in chat to access commands, type back to exit any centre{ger}")

print(f"{nig}{soft}What Should I Call You For This Session?{ger}")
name = input(f"You:  ")
pic = name
user = pic

print(f"{nig}{soft}Hello {pic}! What Is Your Search Today?{ger}")

while True:
    # Main Input Loop
    choice = input(f"{user}: ").lower().strip()

    if choice == '':
        print(f"{nig}{soft} Input has to be something {ger}")

    elif choice == 'who are you':
        print(f"{nig}{soft}Thanks for asking {pic}! I am a strict question AI made by speed!{ger}")

    elif choice == 'exit':
        print(f"{nig}{soft}Bye!{ger}")
        sys.exit()

    elif choice == "settings":
        print(f"{nig}{soft} ---SETTING CENTRE--- {ger}")
        settings = input(f"{pic}: ")

    elif choice == "math":
        print(f"{red}-- MATH CENTRE --{ger}")
        print(f"{red}{soft}radius{ger}")
        print(f"{red}{soft}diameter{ger}")
        print(f"{red}{soft}triangle{ger}")
        print(f"{red}{soft}area circle{ger}")

        while True:

            math = input("You: ")

            if math == "triangle":
                print(f"{nig}{soft}Enter the measure of the first angle{ger}")
                ang1 = int(input("You: "))

                print(f"{nig}{soft}Enter the measure of the second angle{ger}")
                ang2 = int(input("You: "))
                ang = 180 - (ang1 + ang2)
                print(f"{nig}{soft}The third angle is {ang}{ger}")

            elif math == "area circle":
                print(f"{nig}{soft}Enter Radius lenght{ger}")
                r = int(input("You: "))
                area_result = 3.14 * r * r
                print(area_result)

            if math == "exit":
                print(f"{nig}{soft}Exiting math prompt centre...{ger}")
                break

    elif choice == 'currency':
        print(f"{nig}{soft}Available exchanges are:{ger}")
        print(f"{blue}{soft}Euro to USD{ger}")
        print(f"{blue}{soft}USD to Euro{ger}")
        print(f"{blue}{soft}RON to MDL{ger}")
        print(f"{blue}{soft}MDL to RON{ger}")
        print(f"{blue}{soft}Euro to MDL{ger}")

        what = input(f"{soft}Enter needed exchange: ").lower().strip()

        while True:

            if what == 'euro to usd':
                print(f"{nig}{soft}Enter Euro amount:{ger}")
                euro_text = input(f"{pic}: ")
                try:
                    euro_val = float(euro_text)
                    usd_val = euro_val * 1.17
                    print(f'{nig}{soft}{euro_val}€ is roughly ${usd_val:.2f}{ger}')
                except ValueError:
                    print(f"{red}{soft}Hey {pic}, try entering a number!{ger}")

            elif what == 'usd to euro':
                print(f"{nig}{soft}Enter USD amount:{ger}")
                usd_text = input(f"{pic}: ")
                try:
                    usd_val = float(usd_text)
                    euro_val = usd_val * 0.85
                    print(f'{nig}{soft}${usd_val} is roughly {euro_val:.2f}€{ger}')
                except ValueError:
                    print(f"{red}{soft}Hey {pic}, try entering a number!{ger}")
        
            elif what == 'ron to mdl':
                print(f"{nig}{soft}Enter RON amount:{ger}")
                ron_text = input(f"{pic}: ")
                try:
                    ron_val = float(ron_text)
                    mdl_val = ron_val * 3.99
                    print(f'{nig}{soft}{ron_val}RON is roughly {mdl_val:.2f}MDL{ger}')
                except ValueError:
                    print(f"{red}{soft}Hey {pic}, try entering a number!{ger}")

            elif what == 'mdl to ron':
                print(f"{nig}{soft}Enter MDL amount:{ger}")
                mdl_text = input(f"{pic}: ")
                try:
                    mdl_val = float(mdl_text)
                    ron_val = mdl_val * 0.25
                    print(f'{nig}{soft}{mdl_val}MDL is roughly {ron_val:.2f}RON{ger}')
                except ValueError:
                    print(f"{red}{soft}Hey {pic}, try entering a number!{ger}")

            elif what == 'euro to mdl':
                print(f"{nig}{soft}Enter Euro amount:{ger}")
                euro_text = input(f"{pic}: ")
                try:
                    euro_val = float(euro_text)
                    mdl_val = euro_val * 20.35
                    print(f'{nig}{soft}{euro_val}€ is roughly {mdl_val:.2f}MDL{ger}')
                except ValueError:
                    print(f"{red}{soft}Hey {pic}, try entering a number!{ger}")

                else:
                    print(f"{red}{soft}Sorry, I don't recognize that currency pair.{ger}")

            elif what == 'back':
                print(f"{nig}{soft}Exiting currency prompt centre...{ger}")
            break

    elif choice == 'chance':
        print(f"{nig}{soft}Available chances are:{ger}")
        print(f"{nig}{soft}flip a coin{ger}")
        print(f"{nig}{soft}roll a 6 sided cube{ger}")
        print(f"{nig}{soft}pick a random number{ger}")

        while True:
            chance = input(f"{pic}: ").lower().strip()

            if chance == "flip a coin":
                outcomes = {1: "Heads", 2: "Tails"}
                event = random.randint(1, 2)
                print(f"{nig}{soft}Nice {pic}!, You'r coin landed on {outcomes[event]}")

            elif chance == "roll a 6 sided cube":
                outcomes1= {1: "1", 2:'2', 3:'3', 4:'4', 5:'5' , 6:'6'}
                event = random.randint(1, 6)
                print(f"{nig}{soft}Nice {pic}!, Your cube landed on {outcomes1[event]}")

            elif chance == 'pick a random number':

                print(f"{nig}{soft}Enter the minimum number!{ger}")
                min_choice = int(input(f'{pic}: ').strip().lower())
                print(f"{nig}{soft}Enter the maximum number!{ger}")
                max_choice = int(input(f"{pic}: ").strip().lower())

                result=random.randint(min_choice, max_choice)

                print(f"{nig}{soft}You'r random number is {result}!{ger}")

            elif chance == 'back':
                print(f"{nig}{soft}Exiting chance prompt centre...{ger}")
            break
                    #TIMER
    elif choice == 'timer':
        print(f"{blue}{soft} ---TIMER CENTRE--- {ger}")
        print(f"{nig}{soft}{pic}, enter the number of second you want the timer to be")
        sleep = int(input(f'{white}{pic}{ger}:').strip().lower())
        time.sleep(sleep)
        print(f"{nig}{soft}Hey {pic}, your {sleep} second timer is up!{ger}")

    elif choice == "back":
        print(f"{nig}{soft}User {pic} is not in any active server!{ger}")

    elif choice == "command":
        print(f"{blue}{soft} ---COMMAND CENTRE--- {ger}")
        print(f"{red}{soft}Type 1 for exchange commands{ger}")
        print(f"{red}{soft}Type 2 for system commands{ger}")
        print(f"{red}{soft}Type 3 for chance commands{ger}")

        while True:
            ch = input(f"{pic}: ")
            if ch == "1":
                print(f"{blue}{soft} ---EXCHANGE CENTRE--- {ger}")
                print(f"{red}{soft}USD to Euro{ger}")
                print(f"{red}{soft}Euro to USD{ger}")
                print(f"{red}{soft}RON to MDL{ger}")
                print(f"{red}{soft}MDL to RON{ger}")
                print(f"{red}{soft}Euro to MDL{ger}")

            elif ch == "2":
                print(f"{blue}{soft} ---SYSTEM CENTRE--- {ger}")
                print(f"{red}{soft}exit{ger}")
                print(f"{red}{soft}who are you{ger}")
                print(f"{red}{soft}back(exits the centre you are currently in{ger}")

            elif ch == '3':
                print(f"{blue}{soft}CHANCE:{ger}")
                print(f"{red}{soft}flip a coin{ger}")
                print(f"{red}{soft}roll a 6 sided cube{ger}")
                print(f"{red}{soft}pick a random number{ger}")

            elif ch == 'back':
                print(f"{nig}{soft}Exititng command prompt centre...{ger}")
                break
            
    else: 
        print(f"\n{red}{soft}Sorry {pic}, I don't understand that yet!{ger}")