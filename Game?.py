import time

# xpos is a string
# badspace is also a string



heads=["(~- -~)", "(▔ ▔)"]
bold_start = '\033[1m'
bold_end = '\033[0m'
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

def getx(minus=0):
    global xpos
    lst=[]
    for num in range(len(xpos)-minus):
        lst.append(" ")

    return "".join(lst)

def getbadx(minus=0):
    global badspace
    lst=[]
    for num in range(len(badspace)-minus):
        lst.append(" ")

    return "".join(lst)

def speak(stuff, char):
    global bold_start
    global bold_end
    print(playercostumes[0].format(xpos, xpos, xpos))
    print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")
    tick=0
    comped=[]
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

print(" ")

walk(10)

time.sleep(0.5)
speak("Yea I kool, I'm really cool, so cool that I'm cool.", "You")
time.sleep(1)

arrival(0, 0.1) # because it's costume 0, AKA idle

time.sleep(0.5)

speak("Actually, I beg to differ!", "???")

time.sleep(1)

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
        print(antacostumes[antanum].format(badspace, badspace, badspace, getx(len(getbadx(4)))+"(0 0)", getx(len(getbadx(4)))+"o||o", getx(len(getbadx(3)))+"ΤΤ"))
    except:
        antanum = 0
        print(antacostumes[antanum].format(badspace, badspace, badspace, getx(len(getbadx(4)))+"(0 0)", getx(len(getbadx(4)))+"o||o", getx(len(getbadx(3)))+"ΤΤ"))

    print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")
    time.sleep(0.24)

#print(playercostumes[0].format(xpos, xpos, xpos))
#print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")
