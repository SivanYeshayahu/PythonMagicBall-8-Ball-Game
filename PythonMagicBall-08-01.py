#sivan yeshayahu
import sys
import random


listRand = ["IT IS CERTAIN","YOU MAY RELY ON IT","AS I SEE IT, YES","MOST LIKELY", "IT IS DECIDELY SO", "WITHOUT A DOUBT","YES, DEFINETLY"]

while True :
    q = input("ask a question. (press ENTER to quit)")

    if q == "":
        exit()
    else:
        print(random.choice(listRand))
        


