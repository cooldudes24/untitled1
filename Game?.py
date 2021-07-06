import time
import PIL

heads=["(~- -~)", "(▔ ▔)"]
playercostumes=[]
x=0
xpos=0


#(- -)
#ο||ο
# ΤΤ

playercostumes.append(
"""          
{}(- -)
{}ο||ο
 {}ΤΤ"""
)

playercostumes.append(
"""          
{}(- -)
 {}ο||o
  {}Τ Τ"""
)

playercostumes.append(
"""          
{}(- -)
{}ο||o
{}Τ Τ"""
)
print(playercostumes[0].format("  ", "  ", "  "))
print(" ")

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

def speak(stuff, char):
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

walk(10)
time.sleep(0.5)
speak("Yea I kool, I'm really cool, so cool that I'm cool.", "You")
