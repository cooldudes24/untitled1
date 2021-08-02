import time

# xpos is a string
# badspace is also a string



heads=["(~- -~)", "(▔ ▔)"]
bold_start = '\33[1m'
bold_end = '\33[0m'
x=0
xpos=0

poses=["""          
{}(0 0)
{}ο||ο
 {}ΤΤ""",
"""          
{}(0 0)
 {}ο||ο
  {}ΤΤ"""
]

playercostumes=[ #disclaimer: should be called "walkanimation"
"""          
{}(- -)
{}ο||ο
 {}ΤΤ""",
"""          
{}(- -)
 {}ο||o
  {}Τ Τ""",
"""          
{}(- -)
{}ο||o
{}Τ Τ"""]

antatrans="🕶) |oΤ"

antacostumes=[ #disclaimer: should be called "walkanimation"
"""          
{}(-🕶){}
{}ο||o{}
 {}ΤΤ {}""",
"""          
{}(-🕶){}
 {}ο||o{}
  {}Τ Τ{}""",
"""          
{}(-🕶){}
{}ο||o{}
{}Τ Τ{}"""]

antaposes=[ #disclaimer: should be called "walkanimation"
"""          
{}(-🕶){}
{}ο||o{}
 {}ΤΤ {}""",
"""          
{}(-🕶)x{}
 {}ο||o{}
  {}ΤΤ {}""",
"""          
{}(-🕶)⭐{}
{}ο||o{}
 {}ΤΤ {}""",
"""          
{}(-🕶) {}
{}ο||o{}
 {}ΤΤ {}""",
"""          
{}╬(-🕶){}
{}ο||o{}
 {}ΤΤ {}"""
]

def wait(): ################################################################
    time.sleep(1)

def walk(steps):
    global x
    csnum = 0
    xlst=[]
    for num in range(steps): #each screen xlength is 14
        x+=1
        csnum+=1
        for num in range(x):
            xlst.append(" ")
        global xpos
        xpos="".join(xlst)
        try:
            print(playercostumes[csnum].format(xpos, xpos, xpos))
        except:
            csnum=0
            print(playercostumes[csnum].format(xpos, xpos, xpos))

        print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")
        time.sleep(0.24)

    print(playercostumes[0].format(xpos, xpos, xpos))
    print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")

def getx(minus=0): # returns a string . . . of spaces
    global xpos
    lst=[]
    for num in range(len(xpos)-minus):
        lst.append(" ")

    return "".join(lst)

def getbadx(minus=0): # same thing
    global badspace
    lst=[]
    for num in range(len(badspace)-minus):
        lst.append(" ")

    return "".join(lst)

def options(a, b):
    print(playercostumes[0].format(xpos, xpos, xpos))
    print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")
    tick=0
    comped=[]
    bold_start = '\033[1m'
    bold_end = '\033[0m'
    for val in range(len(char)):
        comped.append(char[tick])
        print(bold_start, "".join(comped)+":", bold_end, end="\r")
        tick+=1
        time.sleep(0.024)
    tick=0
    speakernametext="".join(comped)+":"
    punctuation=stuff[len(stuff)-1]
    comped=[]
    for val in range(len(stuff)-1):
        comped.append(stuff[tick])
        print(bold_start, speakernametext, bold_end, "".join(comped)+punctuation, end="\r")
        tick+=1
        time.sleep(0.024)

def arrival(costumenum, wait): # MAKE SURE THAT THERE'S NOTHING ONSCREEN EXCEPT GROUND + YOU.
    print(playercostumes[costumenum].format("-"+getx(1), xpos, xpos))
    print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")
    time.sleep(wait)
    print(playercostumes[costumenum].format(" -"+getx(2), xpos, xpos))
    print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")
    time.sleep(wait)
    print(playercostumes[costumenum].format(" - !" +getx(4), xpos, xpos))
    print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")
    time.sleep(wait)
    print(playercostumes[costumenum].format(" -!" +getx(3), xpos, xpos))
    print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")
    time.sleep(wait)
    print(playercostumes[costumenum].format(" - !" +getx(4), xpos, xpos))
    print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")

def allspeak(stuff, char): ###################################################################################################################
    tick = 0
    comped = []
    for val in range(len(char)):
        comped.append(char[tick])
        print(bold_start, "".join(comped) + ":", bold_end, end="\r")
        tick += 1
        time.sleep(0.024)

    tick = 0
    speakernametext = "".join(comped) + ":"
    punctuation = stuff[len(stuff) - 1]
    comped = []
    for val in range(len(stuff) - 1):
        comped.append(stuff[tick])
        print(bold_start, speakernametext, bold_end, "".join(comped) + punctuation, end="\r")
        tick += 1
        time.sleep(0.024)


print(" ")

walk(10)

time.sleep(0.5)
allspeak("Yea I be kool, I so kool that I kool.", "You")

wait()

arrival(0, 0.1) # because it's costume 0, AKA idle

wait()

allspeak("Actually, I beg to differ!", "???")

wait()

#print( bold_start,
#"""
# {}____________
#{}|            |
#{} ▔▔▔▔▔▔▔
#""".format(" "," "," "), bold_end)

print(poses[0].format(xpos, xpos, xpos))
print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")

time.sleep(0.4)

print(poses[1].format(xpos, xpos, xpos))
print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")

print(poses[1].format(antatrans[0]+antatrans[1]+getx(3), antatrans[3]+antatrans[4]+getx(2), antatrans[5]+getx(2)))
print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")
time.sleep(0.24)

antanum = 0
xlst = []
badx=0

for thing in range(5):
    badx += 1
    antanum += 1
    for thing in range(badx):
        xlst.append(" ")
    badspace = "".join(xlst)
    try:
        print(antacostumes[antanum].format(badspace, getx(len(getbadx(2)))+"(0 0)", badspace, getx(len(getbadx(4)))+"o||o", badspace, getx(len(getbadx(5)))+"ΤΤ"))

    except:
        antanum = 0
        print(antacostumes[antanum].format(badspace, getx(len(getbadx(2)))+"(0 0)", badspace, getx(len(getbadx(4)))+"o||o", badspace, getx(len(getbadx(5)))+"ΤΤ"))


    print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")
    time.sleep(0.24)

antanum = 0
print(antacostumes[antanum].format(badspace, getx(len(getbadx(2)))+"(0 0)", badspace, getx(len(getbadx(4)))+"o||o", badspace, getx(len(getbadx(5)))+"ΤΤ"))
print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")

wait()

allspeak("It is I, Lautus, the coolest dude known to man!", "???")
wait()
allspeak("I differ from your opinion because if I didn't, that would imply that you were almost as cool as I was.", "Lautus")

time.sleep(2)

tick=0
for thing in range(3):
    print(antaposes[tick].format(badspace, getx(len(getbadx(2))) + "(0 0)", badspace, getx(len(getbadx(4))) + "o||o", badspace, getx(len(getbadx(5))) + "ΤΤ"))
    print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")
    tick+=1
    time.sleep(0.1)

wait()


print(antaposes[2].format(badspace, getx(len(getbadx())) + "(0 0)", badspace,
                          getx(len(getbadx(4))) + "o||o",
                          badspace, getx(len(getbadx(5))) + "ΤΤ"))
print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")

allspeak("Which, of course, simply can't be true!", "Lautus")

wait()

choice=1 ##################################################################################################3
if choice==1:
    print(antaposes[2].format(badspace, getx(len(getbadx())) + "(> <)", badspace, getx(len(getbadx(4))) + "o||o", badspace, getx(len(getbadx(5))) + "ΤΤ"))
    print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")
    time.sleep(0.1)
    print(antaposes[2].format(badspace, getx(len(getbadx())) + " (> <)", badspace, getx(len(getbadx(4))) + "o||o", badspace, getx(len(getbadx(5))) + "ΤΤ"))
    print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")
    time.sleep(0.1)
    print(antaposes[2].format(badspace, getx(len(getbadx())) + "  (> <)", badspace, getx(len(getbadx(4))) + "o||o", badspace, getx(len(getbadx(5))) + "ΤΤ"))
    print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")
    time.sleep(0.1)
    print(antaposes[2].format(badspace, getx(len(getbadx())) + " (> <)", badspace, getx(len(getbadx(4))) + "o||o", badspace, getx(len(getbadx(5))) + "ΤΤ"))
    print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")
    time.sleep(0.1)

    print(antaposes[3].format(badspace, getx(len(getbadx())) + " (≧ ≦)╬", badspace, getx(len(getbadx(4))) + "o||o", badspace, getx(len(getbadx(5))) + "ΤΤ"))
    print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")
    wait()
    print(antaposes[3].format(badspace, getx(len(getbadx())) + "(≧ ≦)╬", badspace, getx(len(getbadx(4))) + "o||o", badspace, getx(len(getbadx(5))) + "ΤΤ"))
    print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")
    allspeak("Hey, that's not fair!", "You")
    wait()
    allspeak("How come you get to proclaim yourself the coolest guy ever and we have to just agree?", "You")
    wait()
    print(antaposes[3].format(badspace, getx(len(getbadx())) + " (≧ ≦)🌩", badspace, getx(len(getbadx(4))) + "o||o", badspace, getx(len(getbadx(5))) + "ΤΤ"))
    print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")
    allspeak("Because I'm the coolest guy ever, of course!", "Lautus")

wait()
print(antaposes[3].format(badspace, getx(len(getbadx())) + "(≧ ≦)╬", badspace, getx(len(getbadx(4))) + "o||o", badspace, getx(len(getbadx(5))) + "ΤΤ"))
print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")
allspeak("Grr!! That's it! I'll show you that I'm cooler than you!", "You")
wait()
allspeak("Hmph! You've made me mad too!", "Lautus")
wait()
print(antaposes[4].format(badspace, getx(len(getbadx())) + "(≧ ≦)╬", badspace, getx(len(getbadx(4))) + "o||o", badspace, getx(len(getbadx(5))) + "ΤΤ"))
print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")
allspeak("I'll whup you hard, short stuff - mark my words!!", "Lautus")
wait()
print(antaposes[4].format(">"+getbadx(1), getx(len(getbadx())) + "(≧ ≦)╬", ">"+getbadx(1), getx(len(getbadx(4))) + "o||o", ">"+getbadx(2), getx(len(getbadx(5))) + "ΤΤ"))
print(bold_start, "[battle music starts]", bold_end, end="\r")
