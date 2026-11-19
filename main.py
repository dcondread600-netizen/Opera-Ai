import sys
import time
import random
import string
import subprocess

logo = [
    "\033[35m ██████╗ ██████╗ ███████╗██████╗  █████╗      █████╗ ██╗\033[0m",
    "\033[35m██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗    ██╔══██╗██║\033[0m",
    "\033[35m██║   ██║██████╔╝█████╗  ██████╔╝███████║    ███████║██║\033[0m",
    "\033[35m██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗██╔══██║    ██╔══██║██║\033[0m",
    "\033[35m╚██████╔╝██║     ███████╗██║  ██║██║  ██║    ██║  ██║██║\033[0m",
    "\033[35m ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝\033[0m",
    ]
for line in logo:
    print(line)

blue= "\033[34m"
green = '\033[32m'  
red = '\033[31m'  
end = '\033[0m' 
soft = 'Opera AI: '
white = '\033[37m'
ai = soft
vers = "1.3" #VERSION IS HERE -----------------------------------------------------------------------------------------------

print(f"{red}                          -- IMPORTANT NOTE -- {end}")
print(f"{blue}{soft}Type 'command' in chat to access commands, type back to exit any centre{end}")
print(f"{blue}{soft}WHEN YOU ARE IN A PROGRAM TYPE 'BACK' TO LEAVE THE PROGRAM{end}")
print(f"{blue}{soft}WHEN YOU ARE IN A PROGRAM TYPE 'EXIT' TO LEAVE THE WHOLE SCRIPT{end}")
print(f"{green}{soft}What Should I Call You For This Session?{end}")
name = input(f"You:  ")
pic = name
user = pic
 
print(f"{green}{soft}Hello {pic}! What Is Your Search Today?{end}")
 
while True:

    choice = input(f"{user}: ").lower().strip()

    if choice == "larp":
        
        larp_logo=[
    "\033[35m   ██╗       █████╗  ██████╗  ██████╗ \033[0m",
    "\033[35m   ██║      ██╔══██╗ ██╔══██╗ ██╔══██╗\033[0m",
    "\033[35m   ██║      ███████║ ██████╔╝ ██████╔╝\033[0m",
    "\033[35m   ██║      ██╔══██║ ██╔══██╗ ██╔═══╝ \033[0m",
    "\033[35m   ███████╗ ██║  ██║ ██║  ██║ ██║     \033[0m",
    "\033[35m   ╚══════╝ ╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚═╝     \033[0m"
                ]
        for line in larp_logo:
            print(line)

        while True:
            print(f"{red}{soft} LARP MODE HAS BEEN ACTIVATED {end}")
            print(f"{green}{soft} Hacker{end}")

            larp_choice=(input(f"{pic}: "))
            if larp_choice == "Hacker" or larp_choice == "hacker":
                subprocess.Popen("start cmd /k cls", shell=True)
                


    elif choice == '':
        print(f"{green}{soft} Input has to be something {end}")
 
    elif choice == 'who are you':
        print(f"{green}{soft}Thanks for asking {pic}! I am a strict question AI made by speed!{end}")

    elif choice == "units" or choice == "unit":
        units_logo = [
    "\033[35m   ██╗   ██╗  ███╗   ██╗  ██╗  ████████╗  ███████╗\033[0m",
    "\033[35m   ██║   ██║  ████╗  ██║  ██║  ╚══██╔══╝  ██╔════╝\033[0m",
    "\033[35m   ██║   ██║  ██╔██╗ ██║  ██║     ██║     ███████╗\033[0m",
    "\033[35m   ██║   ██║  ██║╚██╗██║  ██║     ██║     ╚════██║\033[0m",
    "\033[35m   ╚██████╔╝  ██║ ╚████║  ██║     ██║     ███████║\033[0m",
    "\033[35m    ╚═════╝   ╚═╝  ╚═══╝  ╚═╝     ╚═╝     ╚══════╝\033[0m",
            ]

        for line in units_logo:
            print(line)

        while True:

            print(f"{blue}{soft}km to miles{end}")#domr
            print(f"{blue}{soft}miles to km{end}")#done
            print(f"{blue}{soft}cm to inches{end}")#done
            print(f"{blue}{soft}inches to cm{end}")#done
            print(f"{blue}{soft}kg to pounds{end}")#done
            print(f"{blue}{soft}pounds to kg{end}")#done
            print(f"{blue}{soft}celsius to fahrenheit{end}")#done
            print(f"{blue}{soft}fahrenheit to celsius{end}")
            print(f"{blue}{soft}km/h to mph{end}")
            print(f"{blue}{soft}mph to km/h{end}")
        
            unit = (input(f"{pic}: "))

            if unit == "km to miles":
                    print(f"{green}{soft}Enter km:{end}")
                    km_text = input(f"{pic}: ").lower().strip()#euro = km
                    try:
                        km_val = float(km_text)
                        miles_val = km_val * 0.621371
                        print(f'{green}{soft}{km_val} is roughly {miles_val:.2f}{end}')
                    except ValueError:
                        print(f"{red}{soft}Hey {pic}, try entering a number!{end}")
            
            elif unit == "miles to km":
                print(f"{green}{soft}Enter miles:{end}")
                miles_text = input(f"{pic}: ").lower().strip()#km = inches
                try:
                    miles_val = float(miles_text)
                    km_val = miles_val * 1.60934
                    print(f'{green}{soft}{miles_val}miles  is roughly {km_val:.2f}km{end}')
                except ValueError:
                        print(f"{red}{soft}Hey {pic}, try entering a number!{end}")

            elif unit == "cm to inches":
                print(f"{green}{soft}Enter cm:{end}")
                cm_text = input(f"{pic}: ").lower().strip()#euro = km
                try:
                    cm_val = float(cm_text)
                    inches_val = cm_val * 0.393701
                    print(f'{green}{soft}{cm_val}cm is roughly {inches_val:.2f}inches{end}')
                except ValueError:
                        print(f"{red}{soft}Hey {pic}, try entering a number!{end}")

            elif unit == "inches to cm":
                print(f"{green}{soft}Enter inches:{end}")
                inches_text = input(f"{pic}: ").lower().strip()
                try:
                    inches_val = float(inches_text)
                    cm_val = inches_val * 2.54
                    print(f'{green}{soft}{inches_val}inches is roughly {cm_val:.2f}cm{end}')
                except ValueError:
                        print(f"{red}{soft}Hey {pic}, try entering a number!{end}")
            
            elif unit == "kg to pounds":
                print(f"{green}{soft}Enter kg:{end}")
                kg_text = input(f"{pic}: ").lower().strip()
                try:
                    kg_val = float(kg_text)
                    pounds_val = kg_val * 2.20462
                    print(f'{green}{soft}{kg_val}kg is roughly {pounds_val:.2f}lbs{end}')
                except ValueError:
                        print(f"{red}{soft}Hey {pic}, try entering a number!{end}")

            elif unit == "pounds to kg":
                print(f"{green}{soft}Enter pounds:{end}")
                pounds_text = input(f"{pic}: ").lower().strip()
                try:
                    pounds_val = float(pounds_text)
                    kg_val = pounds_val *  0.453592
                    print(f'{green}{soft}{pounds_val}lbs is roughly {kg_val:.2f}kg{end}')
                except ValueError:
                        print(f"{red}{soft}Hey {pic}, try entering a number!{end}")

            elif unit == "celsius to fahrenheit":
                print(f"{green}{soft}Enter celsius:{end}")
                celsius_text = input(f"{pic}: ").lower().strip()
                try:
                    celsius_val = float(celsius_text)
                    fahrenheit_val = (celsius_val * 9/5) + 32
                    print(f'{green}{soft}{celsius_val}°C  is roughly {fahrenheit_val:.2f}°F{end}')
                except ValueError:
                        print(f"{red}{soft}Hey {pic}, try entering a number!{end}")

            elif unit == "fahrenheit to celsius":
                print(f"{green}{soft}Enter fahrenheit:{end}")
                fahrenheit_text = input(f"{pic}: ").lower().strip()
                try:
                    fahrenheit_val = float(fahrenheit_text)
                    celsius_val = (fahrenheit_val - 32) * 5/9
                    print(f'{green}{soft}{fahrenheit_val}°F is roughly {celsius_val:.2f}°C{end}')
                except ValueError:
                        print(f"{red}{soft}Hey {pic}, try entering a number!{end}")

            elif unit == "km/h to mph":
                print(f"{green}{soft}Enter km/h:{end}")
                kmh_text = input(f"{pic}: ").lower().strip()
                try:
                    kmh_val = float(kmh_text)
                    mph_val = kmh_val *  0.621371
                    print(f'{green}{soft}{kmh_val}km/h is roughly {mph_val:.2f}mph{end}')
                except ValueError:
                        print(f"{red}{soft}Hey {pic}, try entering a number!{end}")

            elif unit == "mph to km/h":
                print(f"{green}{soft}Enter mph:{end}")
                mph_text = input(f"{pic}: ").lower().strip()
                try:
                    mph_val = float(mph_text)
                    kmh_val = mph_val *  1.60934
                    print(f'{green}{soft}{mph_val}mph is roughly {kmh_val:.2f}km/h{end}')
                except ValueError:
                        print(f"{red}{soft}Hey {pic}, try entering a number!{end}")

            elif unit == "back":
                print(f"{green}{soft}Exiting unit prompt centre...{end}")
                break
    elif choice == "settings":
        set_logo = [
    "\033[35m   ███████╗  ███████╗  ████████╗  ████████╗  ██╗  ███╗   ██╗  ██████╗    ███████╗\033[0m",
    "\033[35m   ██╔════╝  ██╔════╝  ╚══██╔══╝  ╚══██╔══╝  ██║  ████╗  ██║  ██╔════╝   ██╔════╝\033[0m",
    "\033[35m   ███████╗  █████╗       ██║        ██║     ██║  ██╔██╗ ██║  ██║  ███╗  ███████╗\033[0m",
    "\033[35m   ╚════██║  ██╔══╝       ██║        ██║     ██║  ██║╚██╗██║  ██║   ██║  ╚════██║\033[0m",
    "\033[35m   ███████║  ███████╗     ██║        ██║     ██║  ██║ ╚████║  ╚██████╔╝  ███████║\033[0m",
    "\033[35m   ╚══════╝  ╚══════╝     ╚═╝        ╚═╝     ╚═╝  ╚═╝  ╚═══╝   ╚═════╝  ╚══════╝\033[0m",
            ]
        for line in set_logo:
            print(line)
        print(f"{blue}{soft}name{end}")
        print(f"{blue}{soft}about{end}")

        while True:
            
            set = input(f"{pic}: ")

            if set == 'about':
                print(f"{green}{soft}Opera Ai version: {vers}{end}")#version here ================================================-
                print(f"{green}{soft}Last Update: 09.05.2026{end}")
            elif set == "name":
                print(f"{green}{soft}Enter the new name{end}")
                new = input(f'{pic}: ')
                old = pic
                pic = new
                user = pic
                print(f"{green}{soft}Nice name {new}! I will now call you '{new}' instead of {old}!{end}")

            elif set == "back":
                print(f"{green}{soft}Exiting settings prompt centre...{end}")
                break

    elif choice == "math":
        math_logo = [
                "\033[35m   ███╗   ███╗   █████╗  ████████╗   ██╗  ██╗\033[0m",
                "\033[35m   ████╗ ████║  ██╔══██╗ ╚══██╔══╝   ██║  ██║\033[0m",
                "\033[35m   ██╔████╔██║  ███████║    ██║      ███████║\033[0m",
                "\033[35m   ██║╚██╔╝██║  ██╔══██║    ██║      ██╔══██║\033[0m",
                "\033[35m   ██║ ╚═╝ ██║  ██║  ██║    ██║      ██║  ██║\033[0m",
                "\033[35m   ╚═╝     ╚═╝  ╚═╝  ╚═╝    ╚═╝      ╚═╝  ╚═╝\033[0m",
                ]
        for line in math_logo:
                print(line)

        print(f"{blue}{soft}radius{end}")
        print(f"{blue}{soft}diameter{end}")
        print(f"{blue}{soft}triangle{end}")#
        print(f"{blue}{soft}area circle{end}")#
 
        while True:
 
            math = input(f"{pic}: ")
 
            if math == "triangle":
                print(f"{green}{soft}Enter the measure of the first angle{end}")
                ang1 = int(input(f"{pic}: "))
 
                print(f"{green}{soft}Enter the measure of the second angle{end}")
                ang2 = int(input(f"{pic}: "))
                ang = 180 - (ang1 + ang2)
                print(f"{green}{soft}The third angle is {ang}{end}")
 
            elif math == "area circle":
                print(f"{green}{soft}Enter Radius lenght{end}")
                r = int(input(f"{pic}: "))
                area_result = 3.14 * r * r
                print(area_result)

            elif math == "diameter":

                    print(f"{green}{soft}Enter the radius:{end}")
                    rad_text = input(f"{pic}: ").lower().strip()
                    try:
                        rad_val = float(rad_text)
                        diam_val = rad_val * 2
                        print(f'{green}{soft}A {rad_val}cm radius is a {diam_val}cm diameter{end}')
                    except ValueError:
                        print(f"{red}{soft}Hey {pic}, try entering a number!{end}")

            elif math == "radius":

                    print(f"{green}{soft}Enter the diameter:{end}")
                    dia_text = input(f"{pic}: ").lower().strip()
                    try:
                        dia_val = float(dia_text)
                        rado_val = dia_val / 2
                        print(f'{green}{soft}A {dia_val}cm diameter is a {rado_val}cm radius{end}')
                    except ValueError:
                        print(f"{red}{soft}Hey {pic}, try entering a number!{end}")
 
            elif math == "back":
                print(f"{green}{soft}Exiting math prompt centre...{end}")
                break
 
    elif choice == 'currency':
            currency_logo = [
                    "\033[35m   ██████╗   ██╗   ██╗  ██████╗   ██████╗  ███████╗  ███╗   ██╗  ██████╗   ██╗   ██╗\033[0m",
                    "\033[35m   ██╔════╝  ██║   ██║  ██╔══██╗  ██╔══██╗ ██╔════╝  ████╗  ██║  ██╔════╝  ╚██╗ ██╔╝\033[0m",
                    "\033[35m   ██║       ██║   ██║  ██████╔╝  ██████╔╝ █████╗    ██╔██╗ ██║  ██║        ╚████╔╝\033[0m",
                    "\033[35m   ██║       ██║   ██║  ██╔══██╗  ██╔══██╗ ██╔══╝    ██║╚██╗██║  ██║         ╚██╔╝\033[0m",
                    "\033[35m   ╚██████╗  ╚██████╔╝  ██║  ██║  ██║  ██║ ███████╗  ██║ ╚████║  ╚██████╗     ██║\033[0m",
                    "\033[35m    ╚═════╝   ╚═════╝   ╚═╝  ╚═╝  ╚═╝  ╚═╝ ╚══════╝  ╚═╝  ╚═══╝   ╚═════╝     ╚═╝\033[0m",
                    ]
            for line in currency_logo:
                print(line)

            print(f"{green}{soft}Available exchanges are:{end}")
            print(f"{blue}{soft}Euro to USD{end}")
            print(f"{blue}{soft}USD to Euro{end}")
            print(f"{blue}{soft}RON to MDL{end}")
            print(f"{blue}{soft}MDL to RON{end}")
            print(f"{blue}{soft}Euro to MDL{end}")
 
            while True:

                what = input(f"{soft}Enter needed exchange: ").lower().strip()

                if what == 'euro to usd':
                    print(f"{green}{soft}Enter Euro amount:{end}")
                    euro_text = input(f"{pic}: ").lower().strip()
                    try:
                        euro_val = float(euro_text)
                        usd_val = euro_val * 1.17
                        print(f'{green}{soft}{euro_val}€ is roughly ${usd_val:.2f}{end}')
                    except ValueError:
                        print(f"{red}{soft}Hey {pic}, try entering a number!{end}")
 
                elif what == 'usd to euro':
                    print(f"{green}{soft}Enter USD amount:{end}")
                    usd_text = input(f"{pic}: ").lower().strip()
                    try:
                        usd_val = float(usd_text)
                        euro_val = usd_val * 0.85
                        print(f'{green}{soft}${usd_val} is roughly {euro_val:.2f}€{end}')
                    except ValueError:
                        print(f"{red}{soft}Hey {pic}, try entering a number!{end}")
        
                elif what == 'ron to mdl':
                    print(f"{green}{soft}Enter RON amount:{end}")
                    ron_text = input(f"{pic}: ").lower().strip()
                    try:
                        ron_val = float(ron_text)
                        mdl_val = ron_val * 3.99
                        print(f'{green}{soft}{ron_val}RON is roughly {mdl_val:.2f}MDL{end}')
                    except ValueError:
                        print(f"{red}{soft}Hey {pic}, try entering a number!{end}")
 
                elif what == 'mdl to ron':
                    print(f"{green}{soft}Enter MDL amount:{end}")
                    mdl_text = input(f"{pic}: ").lower().strip()
                    try:
                        mdl_val = float(mdl_text)
                        ron_val = mdl_val * 0.25
                        print(f'{green}{soft}{mdl_val}MDL is roughly {ron_val:.2f}RON{end}')
                    except ValueError:
                        print(f"{red}{soft}Hey {pic}, try entering a number!{end}")
 
                elif what == 'euro to mdl':
                    print(f"{green}{soft}Enter Euro amount:{end}")
                    euro_text = input(f"{pic}: ").lower().strip()
                    try:
                        euro_val = float(euro_text)
                        mdl_val = euro_val * 20.35
                        print(f'{green}{soft}{euro_val}€ is roughly {mdl_val:.2f}MDL{end}')
                    except ValueError:
                        print(f"{red}{soft}Hey {pic}, try entering a number!{end}")

                elif what == 'back':
                    print(f"{green}{soft}Exiting currency prompt centre...{end}")
                    break
 
                else:
                    print(f"{red}{soft}Sorry {pic}, I dont understand that currency pair!{end}")
 
    elif choice == 'chance':
        chance_logo = [
            "\033[35m   ██████╗  ██╗  ██╗  █████╗  ███╗   ██╗  ██████╗  ███████╗\033[0m",
            "\033[35m  ██╔════╝  ██║  ██║ ██╔══██╗ ████╗  ██║ ██╔════╝  ██╔════╝\033[0m",
            "\033[35m  ██║       ███████║ ███████║ ██╔██╗ ██║ ██║       █████╗\033[0m",
            "\033[35m  ██║       ██╔══██║ ██╔══██║ ██║╚██╗██║ ██║       ██╔══╝\033[0m",
            "\033[35m  ╚██████╗  ██║  ██║ ██║  ██║ ██║ ╚████║ ╚██████╗  ███████╗\033[0m",
            "\033[35m   ╚═════╝  ╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚═╝  ╚═══╝  ╚═════╝  ╚══════╝\033[0m",
                ]
        
        for line in chance_logo:
            print(line)
        print(f"{green}{soft}flip a coin{end}")
        print(f"{green}{soft}roll a 6 sided cube{end}")
        print(f"{green}{soft}pick a random number{end}")
 
        while True:
            chance = input(f"{pic}: ").lower().strip()
 
            if chance == "flip a coin":
                outcomes = {1: "Heads", 2: "Tails"}
                event = random.randint(1, 2)
                print(f"{green}{soft}Nice {pic}!, You'r coin landed on {outcomes[event]}")
 
            elif chance == "roll a 6 sided cube":
                outcomes1= {1: "1", 2:'2', 3:'3', 4:'4', 5:'5' , 6:'6'}
                event = random.randint(1, 6)
                print(f"{green}{soft}Nice {pic}!, Your cube landed on {outcomes1[event]}")
 
            elif chance == 'pick a random number':
 
                print(f"{green}{soft}Enter the minimum number!{end}")
                min_choice = int(input(f'{pic}: ').strip().lower())
                print(f"{green}{soft}Enter the maximum number!{end}")
                max_choice = int(input(f"{pic}: ").strip().lower())
 
                result=random.randint(min_choice, max_choice)
 
                print(f"{green}{soft}You'r random number is {result}!{end}")
 
            elif chance == 'back':
                print(f"{green}{soft}Exiting chance prompt centre...{end}")
                break
                
    elif choice == 'timer':
        timer_logo = [
            "\033[35m   ████████╗  ██╗  ███╗   ███╗  ███████╗  ██████╗\033[0m",
            "\033[35m   ╚══██╔══╝  ██║  ████╗ ████║  ██╔════╝  ██╔══██╗\033[0m",
            "\033[35m      ██║     ██║  ██╔████╔██║  █████╗    ██████╔╝\033[0m",
            "\033[35m      ██║     ██║  ██║╚██╔╝██║  ██╔══╝    ██╔══██╗\033[0m",
            "\033[35m      ██║     ██║  ██║ ╚═╝ ██║  ███████╗  ██║  ██║\033[0m",
            "\033[35m      ╚═╝     ╚═╝  ╚═╝     ╚═╝  ╚══════╝  ╚═╝  ╚═╝\033[0m",
                ]

        for line in timer_logo:
            print(line)

        print(f"{green}{soft}{pic}, enter the number of second you want the timer to be{end}")
        while True:
            sleep1 = input(f'{white}{pic}{end}: ')
            if sleep1.lower() == "back":
                print(f"{green}{soft}Exiting timer prompt centre...{end}")
                break
            try:
                sleep = int(sleep1)
                time.sleep(sleep)
                print(f"{green}{soft}Hey {pic}, your timer is up!{end}")
            except ValueError:
                print(f"{green}{soft}Hey {pic}, try entering a number or 'back'{end}")

    elif choice == "back":
        print(f"{green}{soft}User {pic} is not in any active centre, did you mean 'exit'?{end}")

    elif choice == "tools" or choice == "tool":
        tools_logo = [
    "\033[35m   ████████╗  ██████╗   ██████╗  ██╗      ███████╗\033[0m",
    "\033[35m   ╚══██╔══╝ ██╔═══██╗ ██╔═══██╗ ██║      ██╔════╝\033[0m",
    "\033[35m      ██║    ██║   ██║ ██║   ██║ ██║      ███████╗\033[0m",
    "\033[35m      ██║    ██║   ██║ ██║   ██║ ██║      ╚════██║\033[0m",
    "\033[35m      ██║    ╚██████╔╝ ╚██████╔╝ ███████╗ ███████║\033[0m",
    "\033[35m      ╚═╝     ╚═════╝   ╚═════╝  ╚══════╝ ╚══════╝\033[0m",
        ]

        for line in tools_logo:
            print(line)
        print(f"{green}{soft}generate{end}")

        while True:
            
            tool = input(f"{white}{pic}: {end}")

            if tool == "generate":
                print(f"{green}{ai}Enter the lenght of the password:")

                try:
                    lenght = int(input(f"{white}{pic}: {end}").lower())
                    chars = string.ascii_letters + string.digits + string.punctuation
                    passw = ''
                    for i in range(lenght):
                        passw = passw + random.choice(chars)
                    print(f"{green}{ai}You'r generated password is {passw}")
                except ValueError:
                    print(f"{green}{soft}Hey {pic}, try entering a number{end}")

            elif tool == "back":
                print(f"{green}{soft}Exititng tool prompt centre...{end}")
                break


    elif choice == "command":
        command_logo = [
        "\033[35m   ██████╗  ██████╗  ███╗   ███╗ ███╗   ███╗  █████╗  ███╗   ██╗ ██████╗\033[0m",
        "\033[35m  ██╔════╝ ██╔═══██╗ ████╗ ████║ ████╗ ████║ ██╔══██╗ ████╗  ██║ ██╔══██╗\033[0m",
        "\033[35m  ██║      ██║   ██║ ██╔████╔██║ ██╔████╔██║ ███████║ ██╔██╗ ██║ ██║  ██║\033[0m",
        "\033[35m  ██║      ██║   ██║ ██║╚██╔╝██║ ██║╚██╔╝██║ ██╔══██║ ██║╚██╗██║ ██║  ██║\033[0m",
        "\033[35m  ╚██████╗ ╚██████╔╝ ██║ ╚═╝ ██║ ██║ ╚═╝ ██║ ██║  ██║ ██║ ╚████║ ██████╔╝\033[0m",
        "\033[35m   ╚═════╝  ╚═════╝  ╚═╝     ╚═╝ ╚═╝     ╚═╝ ╚═╝  ╚═╝ ╚═╝  ╚═══╝ ╚═════╝\033[0m",
        ]

        for line in command_logo:
            print(line)
    print(f"{red}{soft}Type 1 for exchange commands{end}")
    print(f"{red}{soft}Type 2 for chance commands{end}") 
    print(f"{red}{soft}Type 3 for math commands{end}")
    print(f"{red}{soft}Type 4 for timer commands{end}")
    print(f"{red}{soft}Type 5 for setting commands{end}")
 
    while True:
            ch = input(f"{pic}: ")

            if ch == "5":
                set_logo = [
                "\033[35m   ███████╗  ███████╗  ████████╗  ████████╗  ██╗  ███╗   ██╗  ██████╗    ███████╗\033[0m",
                "\033[35m   ██╔════╝  ██╔════╝  ╚══██╔══╝  ╚══██╔══╝  ██║  ████╗  ██║  ██╔════╝   ██╔════╝\033[0m",
                "\033[35m   ███████╗  █████╗       ██║        ██║     ██║  ██╔██╗ ██║  ██║  ███╗  ███████╗\033[0m",
                "\033[35m   ╚════██║  ██╔══╝       ██║        ██║     ██║  ██║╚██╗██║  ██║   ██║  ╚════██║\033[0m",
                "\033[35m   ███████║  ███████╗     ██║        ██║     ██║  ██║ ╚████║  ╚██████╔╝  ███████║\033[0m",
                "\033[35m   ╚══════╝  ╚══════╝     ╚═╝        ╚═╝     ╚═╝  ╚═╝  ╚═══╝   ╚═════╝  ╚══════╝\033[0m",
                    ]
                for line in set_logo:
                    print(line)
                print(f"{blue}{soft}name{end}")
                print(f"{blue}{soft}about{end}")

                while True:

                    set = input(f"{pic}: ")

                    if set == 'about':
                        print(f"{green}{soft}Opera Ai version: {vers}{end}")#version here ================================================-
                        print(f"{green}{soft}Last Update: 09.05.2026{end}")
                    elif set == "name":
                        print(f"{green}{soft}Enter the new name{end}")
                        new = input(f'{pic}: ')
                        old = pic
                        pic = new
                        user = pic
                        print(f"{green}{soft}Nice name {new}! I will now call you '{new}' instead of {old}!{end}")

                    elif set == "back":
                        print(f"{green}{soft}Exiting settings prompt centre...{end}")
                        command_logo = [
                            "\033[35m   ██████╗  ██████╗  ███╗   ███╗ ███╗   ███╗  █████╗  ███╗   ██╗ ██████╗\033[0m",
                            "\033[35m  ██╔════╝ ██╔═══██╗ ████╗ ████║ ████╗ ████║ ██╔══██╗ ████╗  ██║ ██╔══██╗\033[0m",
                            "\033[35m  ██║      ██║   ██║ ██╔████╔██║ ██╔████╔██║ ███████║ ██╔██╗ ██║ ██║  ██║\033[0m",
                            "\033[35m  ██║      ██║   ██║ ██║╚██╔╝██║ ██║╚██╔╝██║ ██╔══██║ ██║╚██╗██║ ██║  ██║\033[0m",
                            "\033[35m  ╚██████╗ ╚██████╔╝ ██║ ╚═╝ ██║ ██║ ╚═╝ ██║ ██║  ██║ ██║ ╚████║ ██████╔╝\033[0m",
                            "\033[35m   ╚═════╝  ╚═════╝  ╚═╝     ╚═╝ ╚═╝     ╚═╝ ╚═╝  ╚═╝ ╚═╝  ╚═══╝ ╚═════╝\033[0m",
                                ]
                        for line in command_logo:
                            print (line)
                        print(f"{red}{soft}Type 1 for exchange commands{end}")
                        print(f"{red}{soft}Type 2 for chance commands{end}") 
                        print(f"{red}{soft}Type 3 for math commands{end}")
                        print(f"{red}{soft}Type 4 for timer commands{end}")
                        print(f"{red}{soft}Type 5 for setting commands{end}")
                        break
#-----------------------------------------------------------------------------------------------------------------------------

            elif ch == "4":
                timer_logo = [
                    "\033[35m   ████████╗  ██╗  ███╗   ███╗  ███████╗  ██████╗\033[0m",
                    "\033[35m   ╚══██╔══╝  ██║  ████╗ ████║  ██╔════╝  ██╔══██╗\033[0m",
                    "\033[35m      ██║     ██║  ██╔████╔██║  █████╗    ██████╔╝\033[0m",
                    "\033[35m      ██║     ██║  ██║╚██╔╝██║  ██╔══╝    ██╔══██╗\033[0m",
                    "\033[35m      ██║     ██║  ██║ ╚═╝ ██║  ███████╗  ██║  ██║\033[0m",
                    "\033[35m      ╚═╝     ╚═╝  ╚═╝     ╚═╝  ╚══════╝  ╚═╝  ╚═╝\033[0m",
                        ]

                for line in timer_logo:
                    print(line)

                print(f"{green}{soft}{pic}, enter the number of second you want the timer to be{end}")

                while True:
                    sleep1 = input(f'{white}{pic}{end}: ')

                    if sleep1.lower() == "back":
                        print(f"{green}{soft}Exiting timer prompt centre...{end}")
                        command_logo = [
                            "\033[35m   ██████╗  ██████╗  ███╗   ███╗ ███╗   ███╗  █████╗  ███╗   ██╗ ██████╗\033[0m",
                            "\033[35m  ██╔════╝ ██╔═══██╗ ████╗ ████║ ████╗ ████║ ██╔══██╗ ████╗  ██║ ██╔══██╗\033[0m",
                            "\033[35m  ██║      ██║   ██║ ██╔████╔██║ ██╔████╔██║ ███████║ ██╔██╗ ██║ ██║  ██║\033[0m",
                            "\033[35m  ██║      ██║   ██║ ██║╚██╔╝██║ ██║╚██╔╝██║ ██╔══██║ ██║╚██╗██║ ██║  ██║\033[0m",
                            "\033[35m  ╚██████╗ ╚██████╔╝ ██║ ╚═╝ ██║ ██║ ╚═╝ ██║ ██║  ██║ ██║ ╚████║ ██████╔╝\033[0m",
                            "\033[35m   ╚═════╝  ╚═════╝  ╚═╝     ╚═╝ ╚═╝     ╚═╝ ╚═╝  ╚═╝ ╚═╝  ╚═══╝ ╚═════╝\033[0m",
                                ]
                        for line in command_logo:
                            print (line)
                        print(f"{red}{soft}Type 1 for exchange commands{end}")
                        print(f"{red}{soft}Type 2 for chance commands{end}") 
                        print(f"{red}{soft}Type 3 for math commands{end}")
                        print(f"{red}{soft}Type 4 for timer commands{end}")
                        print(f"{red}{soft}Type 5 for setting commands{end}")
                        break
                    try:
                        sleep = int(sleep1)
                        time.sleep(sleep)
                        print(f"{green}{soft}Hey {pic}, your timer is up!{end}")
                    except ValueError:
                        print(f"{green}{soft}Hey {pic}, try entering a number or 'back'{end}")
#---------------------------------------------------------------------------------------------------------------
            elif ch == "3":
                math_logo = [
                    "\033[35m   ███╗   ███╗   █████╗  ████████╗   ██╗  ██╗\033[0m",
                    "\033[35m   ████╗ ████║  ██╔══██╗ ╚══██╔══╝   ██║  ██║\033[0m",
                    "\033[35m   ██╔████╔██║  ███████║    ██║      ███████║\033[0m",
                    "\033[35m   ██║╚██╔╝██║  ██╔══██║    ██║      ██╔══██║\033[0m",
                    "\033[35m   ██║ ╚═╝ ██║  ██║  ██║    ██║      ██║  ██║\033[0m",
                    "\033[35m   ╚═╝     ╚═╝  ╚═╝  ╚═╝    ╚═╝      ╚═╝  ╚═╝\033[0m",
                        ]
                for line in math_logo:
                        print(line)

                print(f"{blue}{soft}radius{end}")
                print(f"{blue}{soft}diameter{end}")
                print(f"{blue}{soft}triangle{end}")
                print(f"{blue}{soft}area circle{end}")
 
                while True:

                    math = input(f"{pic}: ")
 
                    if math == "triangle":
                        print(f"{green}{soft}Enter the measure of the first angle{end}")
                        ang1 = int(input(f"{pic}: "))
 
                        print(f"{green}{soft}Enter the measure of the second angle{end}")
                        ang2 = int(input(f"{pic}: "))
                        ang = 180 - (ang1 + ang2)
                        print(f"{green}{soft}The third angle is {ang}{end}")
 
                    elif math == "area circle":
                        print(f"{green}{soft}Enter Radius lenght{end}")
                        r = int(input(f"{pic}: "))
                        area_result = 3.14 * r * r
                        print(area_result)
 
                    elif math == "back":
                        print(f"{green}{soft}Exiting math prompt centre...{end}")
#---------------------------------============================================----------------------------------------
                        command_logo = [
                            "\033[35m   ██████╗  ██████╗  ███╗   ███╗ ███╗   ███╗  █████╗  ███╗   ██╗ ██████╗\033[0m",
                            "\033[35m  ██╔════╝ ██╔═══██╗ ████╗ ████║ ████╗ ████║ ██╔══██╗ ████╗  ██║ ██╔══██╗\033[0m",
                            "\033[35m  ██║      ██║   ██║ ██╔████╔██║ ██╔████╔██║ ███████║ ██╔██╗ ██║ ██║  ██║\033[0m",
                            "\033[35m  ██║      ██║   ██║ ██║╚██╔╝██║ ██║╚██╔╝██║ ██╔══██║ ██║╚██╗██║ ██║  ██║\033[0m",
                            "\033[35m  ╚██████╗ ╚██████╔╝ ██║ ╚═╝ ██║ ██║ ╚═╝ ██║ ██║  ██║ ██║ ╚████║ ██████╔╝\033[0m",
                            "\033[35m   ╚═════╝  ╚═════╝  ╚═╝     ╚═╝ ╚═╝     ╚═╝ ╚═╝  ╚═╝ ╚═╝  ╚═══╝ ╚═════╝\033[0m",
                                ]
                        for line in command_logo:
                            print (line)
                        print(f"{red}{soft}Type 1 for exchange commands{end}")
                        print(f"{red}{soft}Type 2 for chance commands{end}") 
                        print(f"{red}{soft}Type 3 for math commands{end}")
                        print(f"{red}{soft}Type 4 for timer commands{end}")
                        print(f"{red}{soft}Type 5 for setting commands{end}")
                        print(f"{red}{soft}Type 6 for unit commands{end}")
                        break
            elif ch == "1":
                currency_logo = [
                    "\033[35m   ██████╗   ██╗   ██╗  ██████╗   ██████╗  ███████╗  ███╗   ██╗  ██████╗   ██╗   ██╗\033[0m",
                    "\033[35m   ██╔════╝  ██║   ██║  ██╔══██╗  ██╔══██╗ ██╔════╝  ████╗  ██║  ██╔════╝  ╚██╗ ██╔╝\033[0m",
                    "\033[35m   ██║       ██║   ██║  ██████╔╝  ██████╔╝ █████╗    ██╔██╗ ██║  ██║        ╚████╔╝\033[0m",
                    "\033[35m   ██║       ██║   ██║  ██╔══██╗  ██╔══██╗ ██╔══╝    ██║╚██╗██║  ██║         ╚██╔╝\033[0m",
                    "\033[35m   ╚██████╗  ╚██████╔╝  ██║  ██║  ██║  ██║ ███████╗  ██║ ╚████║  ╚██████╗     ██║\033[0m",
                    "\033[35m    ╚═════╝   ╚═════╝   ╚═╝  ╚═╝  ╚═╝  ╚═╝ ╚══════╝  ╚═╝  ╚═══╝   ╚═════╝     ╚═╝\033[0m",
                        ]
                for line in currency_logo:
                    print(line)

                print(f"{green}{soft}Available exchanges are:{end}")
                print(f"{blue}{soft}Euro to USD{end}")
                print(f"{blue}{soft}USD to Euro{end}")
                print(f"{blue}{soft}RON to MDL{end}")
                print(f"{blue}{soft}MDL to RON{end}")
                print(f"{blue}{soft}Euro to MDL{end}")
 
                while True:

                    what = input(f"{soft}Enter needed exchange: ").lower().strip()

                    if what == 'euro to usd':
                        print(f"{green}{soft}Enter Euro amount:{end}")
                        euro_text = input(f"{pic}: ").lower().strip()
                        try:
                            euro_val = float(euro_text)
                            usd_val = euro_val * 1.17
                            print(f'{green}{soft}{euro_val}€ is roughly ${usd_val:.2f}{end}')
                        except ValueError:
                            print(f"{red}{soft}Hey {pic}, try entering a number!{end}")
 
                    elif what == 'usd to euro':
                        print(f"{green}{soft}Enter USD amount:{end}")
                        usd_text = input(f"{pic}: ").lower().strip()
                        try:
                            usd_val = float(usd_text)
                            euro_val = usd_val * 0.85
                            print(f'{green}{soft}${usd_val} is roughly {euro_val:.2f}€{end}')
                        except ValueError:
                            print(f"{red}{soft}Hey {pic}, try entering a number!{end}")
        
                    elif what == 'ron to mdl':
                        print(f"{green}{soft}Enter RON amount:{end}")
                        ron_text = input(f"{pic}: ").lower().strip()
                        try:
                            ron_val = float(ron_text)
                            mdl_val = ron_val * 3.99
                            print(f'{green}{soft}{ron_val}RON is roughly {mdl_val:.2f}MDL{end}')
                        except ValueError:
                            print(f"{red}{soft}Hey {pic}, try entering a number!{end}")
 
                    elif what == 'mdl to ron':
                        print(f"{green}{soft}Enter MDL amount:{end}")
                        mdl_text = input(f"{pic}: ").lower().strip()
                        try:
                            mdl_val = float(mdl_text)
                            ron_val = mdl_val * 0.25
                            print(f'{green}{soft}{mdl_val}MDL is roughly {ron_val:.2f}RON{end}')
                        except ValueError:
                            print(f"{red}{soft}Hey {pic}, try entering a number!{end}")
 
                    elif what == 'euro to mdl':
                        print(f"{green}{soft}Enter Euro amount:{end}")
                        euro_text = input(f"{pic}: ").lower().strip()
                        try:
                            euro_val = float(euro_text)
                            mdl_val = euro_val * 20.35
                            print(f'{green}{soft}{euro_val}€ is roughly {mdl_val:.2f}MDL{end}')
                        except ValueError:
                            print(f"{red}{soft}Hey {pic}, try entering a number!{end}")

                    elif what == 'back':
                        print(f"{green}{soft}Exiting currency prompt centre...{end}")
                        command_logo = [
                            "\033[35m   ██████╗  ██████╗  ███╗   ███╗ ███╗   ███╗  █████╗  ███╗   ██╗ ██████╗\033[0m",
                            "\033[35m  ██╔════╝ ██╔═══██╗ ████╗ ████║ ████╗ ████║ ██╔══██╗ ████╗  ██║ ██╔══██╗\033[0m",
                            "\033[35m  ██║      ██║   ██║ ██╔████╔██║ ██╔████╔██║ ███████║ ██╔██╗ ██║ ██║  ██║\033[0m",
                            "\033[35m  ██║      ██║   ██║ ██║╚██╔╝██║ ██║╚██╔╝██║ ██╔══██║ ██║╚██╗██║ ██║  ██║\033[0m",
                            "\033[35m  ╚██████╗ ╚██████╔╝ ██║ ╚═╝ ██║ ██║ ╚═╝ ██║ ██║  ██║ ██║ ╚████║ ██████╔╝\033[0m",
                            "\033[35m   ╚═════╝  ╚═════╝  ╚═╝     ╚═╝ ╚═╝     ╚═╝ ╚═╝  ╚═╝ ╚═╝  ╚═══╝ ╚═════╝\033[0m",
                                ]
                        for line in command_logo:
                            print (line)
                        print(f"{red}{soft}Type 1 for exchange commands{end}")
                        print(f"{red}{soft}Type 2 for chance commands{end}") 
                        print(f"{red}{soft}Type 3 for math commands{end}")
                        print(f"{red}{soft}Type 4 for timer commands{end}")
                        print(f"{red}{soft}Type 5 for setting commands{end}")
                        print(f"{red}{soft}Type 6 for units commands{end}")
                        break
 
                    else:
                        print(f"{red}{soft}Sorry {pic}, I dont understand that currency pair!{end}")
            elif ch == "6":
                units_logo = [
                        "\033[35m   ██╗   ██╗  ███╗   ██╗  ██╗  ████████╗  ███████╗\033[0m",
                        "\033[35m   ██║   ██║  ████╗  ██║  ██║  ╚══██╔══╝  ██╔════╝\033[0m",
                        "\033[35m   ██║   ██║  ██╔██╗ ██║  ██║     ██║     ███████╗\033[0m",
                        "\033[35m   ██║   ██║  ██║╚██╗██║  ██║     ██║     ╚════██║\033[0m",
                        "\033[35m   ╚██████╔╝  ██║ ╚████║  ██║     ██║     ███████║\033[0m",
                        "\033[35m    ╚═════╝   ╚═╝  ╚═══╝  ╚═╝     ╚═╝     ╚══════╝\033[0m",
                            ]

                for line in units_logo:
                    print(line)

                print(f"{blue}{soft}km to miles{end}")#domr
                print(f"{blue}{soft}miles to km{end}")#done
                print(f"{blue}{soft}cm to inches{end}")#done
                print(f"{blue}{soft}inches to cm{end}")#done
                print(f"{blue}{soft}kg to pounds{end}")#done
                print(f"{blue}{soft}pounds to kg{end}")#done
                print(f"{blue}{soft}celsius to fahrenheit{end}")#done
                print(f"{blue}{soft}fahrenheit to celsius{end}")
                print(f"{blue}{soft}km/h to mph{end}")
                print(f"{blue}{soft}mph to km/h{end}")

                while True:
                 
                    unit = (input(f"{pic}: "))

                    if unit == "km to miles":
                        print(f"{green}{soft}Enter km:{end}")
                        km_text = input(f"{pic}: ").lower().strip()#euro = km
                        try:
                            km_val = float(km_text)
                            miles_val = km_val * 0.621371
                            print(f'{green}{soft}{km_val} is roughly {miles_val:.2f}{end}')
                        except ValueError:
                            print(f"{red}{soft}Hey {pic}, try entering a number!{end}")
            
                    elif unit == "miles to km":
                        print(f"{green}{soft}Enter miles:{end}")
                        miles_text = input(f"{pic}: ").lower().strip()#km = inches
                        try:
                            miles_val = float(miles_text)
                            km_val = miles_val * 1.60934
                            print(f'{green}{soft}{miles_val}miles  is roughly {km_val:.2f}km{end}')
                        except ValueError:
                                print(f"{red}{soft}Hey {pic}, try entering a number!{end}")

                    elif unit == "cm to inches":
                        print(f"{green}{soft}Enter cm:{end}")
                        cm_text = input(f"{pic}: ").lower().strip()#euro = km
                        try:
                            cm_val = float(cm_text)
                            inches_val = cm_val * 0.393701
                            print(f'{green}{soft}{cm_val}cm is roughly {inches_val:.2f}inches{end}')
                        except ValueError:
                            print(f"{red}{soft}Hey {pic}, try entering a number!{end}")

                    elif unit == "inches to cm":
                        print(f"{green}{soft}Enter inches:{end}")
                        inches_text = input(f"{pic}: ").lower().strip()
                        try:
                            inches_val = float(inches_text)
                            cm_val = inches_val * 2.54
                            print(f'{green}{soft}{inches_val}inches is roughly {cm_val:.2f}cm{end}')
                        except ValueError:
                            print(f"{red}{soft}Hey {pic}, try entering a number!{end}")
            
                    elif unit == "kg to pounds":
                        print(f"{green}{soft}Enter kg:{end}")
                        kg_text = input(f"{pic}: ").lower().strip()
                        try:
                            kg_val = float(kg_text)
                            pounds_val = kg_val * 2.20462
                            print(f'{green}{soft}{kg_val}kg is roughly {pounds_val:.2f}lbs{end}')
                        except ValueError:
                            print(f"{red}{soft}Hey {pic}, try entering a number!{end}")

                    elif unit == "pounds to kg":
                        print(f"{green}{soft}Enter pounds:{end}")
                        pounds_text = input(f"{pic}: ").lower().strip()
                        try:
                            pounds_val = float(pounds_text)
                            kg_val = pounds_val *  0.453592
                            print(f'{green}{soft}{pounds_val}lbs is roughly {kg_val:.2f}kg{end}')
                        except ValueError:
                            print(f"{red}{soft}Hey {pic}, try entering a number!{end}")

                    elif unit == "celsius to fahrenheit":
                        print(f"{green}{soft}Enter celsius:{end}")
                        celsius_text = input(f"{pic}: ").lower().strip()
                        try:
                            celsius_val = float(celsius_text)
                            fahrenheit_val = (celsius_val * 9/5) + 32
                            print(f'{green}{soft}{celsius_val}°C  is roughly {fahrenheit_val:.2f}°F{end}')
                        except ValueError:
                            print(f"{red}{soft}Hey {pic}, try entering a number!{end}")

                    elif unit == "fahrenheit to celsius":
                        print(f"{green}{soft}Enter fahrenheit:{end}")
                        fahrenheit_text = input(f"{pic}: ").lower().strip()
                        try:
                            fahrenheit_val = float(fahrenheit_text)
                            celsius_val = (fahrenheit_val - 32) * 5/9
                            print(f'{green}{soft}{fahrenheit_val}°F is roughly {celsius_val:.2f}°C{end}')
                        except ValueError:
                            print(f"{red}{soft}Hey {pic}, try entering a number!{end}")

                    elif unit == "km/h to mph":
                        print(f"{green}{soft}Enter km/h:{end}")
                        kmh_text = input(f"{pic}: ").lower().strip()
                        try:
                            kmh_val = float(kmh_text)
                            mph_val = kmh_val *  0.621371
                            print(f'{green}{soft}{kmh_val}km/h is roughly {mph_val:.2f}mph{end}')
                        except ValueError:
                            print(f"{red}{soft}Hey {pic}, try entering a number!{end}")

                    elif unit == "mph to km/h":
                        print(f"{green}{soft}Enter mph:{end}")
                        mph_text = input(f"{pic}: ").lower().strip()
                        try:
                            mph_val = float(mph_text)
                            kmh_val = mph_val *  1.60934
                            print(f'{green}{soft}{mph_val}mph is roughly {kmh_val:.2f}km/h{end}')
                        except ValueError:
                            print(f"{red}{soft}Hey {pic}, try entering a number!{end}")

                    elif unit == "back":
                        print(f"{green}{soft}Exiting unit prompt centre...{end}")
                        command_logo = [
                            "\033[35m   ██████╗  ██████╗  ███╗   ███╗ ███╗   ███╗  █████╗  ███╗   ██╗ ██████╗\033[0m",
                            "\033[35m  ██╔════╝ ██╔═══██╗ ████╗ ████║ ████╗ ████║ ██╔══██╗ ████╗  ██║ ██╔══██╗\033[0m",
                            "\033[35m  ██║      ██║   ██║ ██╔████╔██║ ██╔████╔██║ ███████║ ██╔██╗ ██║ ██║  ██║\033[0m",
                            "\033[35m  ██║      ██║   ██║ ██║╚██╔╝██║ ██║╚██╔╝██║ ██╔══██║ ██║╚██╗██║ ██║  ██║\033[0m",
                            "\033[35m  ╚██████╗ ╚██████╔╝ ██║ ╚═╝ ██║ ██║ ╚═╝ ██║ ██║  ██║ ██║ ╚████║ ██████╔╝\033[0m",
                            "\033[35m   ╚═════╝  ╚═════╝  ╚═╝     ╚═╝ ╚═╝     ╚═╝ ╚═╝  ╚═╝ ╚═╝  ╚═══╝ ╚═════╝\033[0m",
                                ]
                        for line in command_logo:
                            print (line)

                        print(f"{red}{soft}Type 1 for exchange commands{end}")
                        print(f"{red}{soft}Type 2 for chance commands{end}") 
                        print(f"{red}{soft}Type 3 for math commands{end}")
                        print(f"{red}{soft}Type 4 for timer commands{end}")
                        print(f"{red}{soft}Type 5 for setting commands{end}")
                        break

            elif ch == '2':
                chance_logo = [
                    "\033[35m   ██████╗  ██╗  ██╗  █████╗  ███╗   ██╗  ██████╗  ███████╗\033[0m",
                    "\033[35m  ██╔════╝  ██║  ██║ ██╔══██╗ ████╗  ██║ ██╔════╝  ██╔════╝\033[0m",
                    "\033[35m  ██║       ███████║ ███████║ ██╔██╗ ██║ ██║       █████╗\033[0m",
                    "\033[35m  ██║       ██╔══██║ ██╔══██║ ██║╚██╗██║ ██║       ██╔══╝\033[0m",
                    "\033[35m  ╚██████╗  ██║  ██║ ██║  ██║ ██║ ╚████║ ╚██████╗  ███████╗\033[0m",
                    "\033[35m   ╚═════╝  ╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚═╝  ╚═══╝  ╚═════╝  ╚══════╝\033[0m",
                    ]
        
                for line in chance_logo:
                    print(line)

                print(f"{green}{soft}flip a coin{end}")
                print(f"{green}{soft}roll a 6 sided cube{end}")
                print(f"{green}{soft}pick a random number{end}")
 
                while True:
                    chance = input(f"{pic}: ").lower().strip()
 
                    if chance == "flip a coin":
                            outcomes = {1: "Heads", 2: "Tails"}
                            event = random.randint(1, 2)
                            print(f"{green}{soft}Nice {pic}!, You'r coin landed on {outcomes[event]}")
 
                    elif chance == "roll a 6 sided cube":
                            outcomes1= {1: "1", 2:'2', 3:'3', 4:'4', 5:'5' , 6:'6'}
                            event = random.randint(1, 6)
                            print(f"{green}{soft}Nice {pic}!, Your cube landed on {outcomes1[event]}")
 
                    elif chance == 'pick a random number':
 
                            print(f"{green}{soft}Enter the minimum number!{end}")
                            min_choice = int(input(f'{pic}: ').strip().lower())
                            print(f"{green}{soft}Enter the maximum number!{end}")
                            max_choice = int(input(f"{pic}: ").strip().lower())
 
                            result=random.randint(min_choice, max_choice)
 
                            print(f"{green}{soft}You'r random number is {result}!{end}")
 
                    elif chance == 'back':
                            print(f"{green}{soft}Exiting chance prompt centre...{end}")

                            command_logo = [
                                "\033[35m   ██████╗  ██████╗  ███╗   ███╗ ███╗   ███╗  █████╗  ███╗   ██╗ ██████╗\033[0m",
                                "\033[35m  ██╔════╝ ██╔═══██╗ ████╗ ████║ ████╗ ████║ ██╔══██╗ ████╗  ██║ ██╔══██╗\033[0m",
                                "\033[35m  ██║      ██║   ██║ ██╔████╔██║ ██╔████╔██║ ███████║ ██╔██╗ ██║ ██║  ██║\033[0m",
                                "\033[35m  ██║      ██║   ██║ ██║╚██╔╝██║ ██║╚██╔╝██║ ██╔══██║ ██║╚██╗██║ ██║  ██║\033[0m",
                                "\033[35m  ╚██████╗ ╚██████╔╝ ██║ ╚═╝ ██║ ██║ ╚═╝ ██║ ██║  ██║ ██║ ╚████║ ██████╔╝\033[0m",
                                "\033[35m   ╚═════╝  ╚═════╝  ╚═╝     ╚═╝ ╚═╝     ╚═╝ ╚═╝  ╚═╝ ╚═╝  ╚═══╝ ╚═════╝\033[0m",
                                ]
                            for line in command_logo:
                                print (line)
                            print(f"{red}{soft}Type 1 for exchange commands{end}")
                            print(f"{red}{soft}Type 2 for chance commands{end}") 
                            print(f"{red}{soft}Type 3 for math commands{end}")
                            print(f"{red}{soft}Type 4 for timer commands{end}")
                            print(f"{red}{soft}Type 5 for setting commands{end}")
                            break

            elif ch == 'back':
                print(f"{green}{ai}Exiting command prompt centre... {end}")
                break

            elif ch not in [ "1", "2", "3", "4", "5" , "6", "back"]:
                print(f"{red}{soft}Sorry {pic}, I don't recognize that command!{end}")
            

            elif ch == 'back':
                print(f"{green}{ai}Exiting command prompt centre... {end}")
                break

            elif choice == 'exit':
                print(f"{green}{soft}Hey {pic}, this action will entirely close the program, are you sure?{end}")
                print(f"{green}{soft}y(yes)   n(no) {end}")
                ext = input(f"{pic}: ")
                if ext == "n" or ext == "no":
                    print(f"{green}{soft}You have not exited the program, and aren't in any active centres{end}")

            elif ext == "y" or ext == "yes":
                print(f"{green}{soft}Bye {pic}!{end}")
                sys.exit()

            else: 
                print(f"\n{red}{soft}Sorry {pic}, I don't understand that yet!{end}")