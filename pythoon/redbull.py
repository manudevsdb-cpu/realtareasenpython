import os 
import time 
import random 

GREN = "\033[32m"
END = "\033[0m"

def buses(n1, n2):
    output = []
    output.append(115 * "-")
    output.append((n1 * " ")"__________________"((100 - n1) * " " ) + "|")
    output.append((n1 * " "))"|_|_|_|_|_|_|_|_|_|_|_"((97 - n1) * " ") + "|")
    output.append((n1 * " "))"|    red bull        |)"((96 - n1) * " ") + "|")
    output.append((n1 * " "))"|~~~~@~~~~~~~~~~@~~~~|)"((95 - n1) * " ") + "|")
    output.append((115 * "-"))
    output.append((n2 * " "))
    output.append((n2 * " "))
    output.append((n2 * " "))
    output.append((n2 * " ") )
    output.append((n2 * " "))
    output.append((115 * "-"))
    return "\n". join(output)

a = 0     
b = 0
gano = none
 
os.system("cls" if os.name == "nr" else "clear" ) 