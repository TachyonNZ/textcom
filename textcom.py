#By /u/TachyonNZ
#TEXT-COM, V0.1

import random as rd
import time as tm

fnm = ["Bob","Becks","Kate","Alex","Tim","Peter","Chilling","Annetta","Violet","Jeb","Bill","Rune","Jeff","Kim","Lee","Iago"]
lnm = ["Van Doorn","Meier","Dan Voorn","Durant","Lee","Kerman","Nilsen","Possible","Fox","Vin Diern","Vern Dern","Friendly","Civilian","Snek","Advint","Eggsalt"]


bbspecies = ["Sectoid"]
sectoidfName = ["Glip","Gleep","Glup","Glorp","Gloop","Glop","Glump","Glerp","Glurp","Glarp"]
sectoidlName = ["Glop","Glarp","Glupple","Glorple","Gloopley","Glopperson","Glep","Glommery"]
thinfName = ["T.","P.","H.","Z.","K.","A.","F.","X.","P.","L.","W.","S"]
thinlName = ["Hinman","Alium","Van Doom","Lmao","Notanalien","Anderson","Smith","Human","Clark","Warzonager"]
mutonfName = ["Pooter","Dave","Holk","Billy","Tim","Jeffery","Leeroy"]
mutonlName = ["Von Mooter","The Muton","Hugan","Jankins","Jefferson"]

aranks = {0:"Peon",1:"R1",2:"R2",3:"R3",4:"Commander"}

retort = ("Suck on this!","Eat lead!","Pick on someone your own size!","Take this!","Welcome to Earth!")

priwep = {0:"Ballistic Rifle",1:"Ballistic Carbine"}
secwep = {0:"Ballistic Pistol",1:"Autopistol"}
items = {0:"Frag Grenade",1:"Nano Serum",2:"Scope",999:"None"}

apriwep = {0:"Light Plasma Rifle",1:"Plasma Rifle"}
asecwep = {0:"Plasma Pistol",1:"Alloy Pistol"}
apowers = {0: "Mindfray",1: "Psi Boost"}
aitems = {0:"Alien Grenade",1:"Alloy Plating",2:"Focus Lens",999:"None"}

pod = []
room = []
roomNo = -1


fragments = 0
elerium = 0
meld = 0
alloy = 0

def stocktake(soldier):
    if soldier.weapon == priwep[0]:
        pass

out = False
def a(form, q): #ask
    global out
    out = input(q)
    if form == "int":
        if out.isdigit() == 1:
            pass
        else:
            out = False
    if form == "str":
        if out.isalpha() == 1:
            pass
        else:
            out = False
    return out

def p(spk,q): #print with speaker and possibly delay
    if spk != 0:
        print(str(spk)+': "'+str(q)+'"')
    else:
        print(q)
    #s(len(q)/50)

def s(t):
    tm.sleep(t)

def c(q, chatID):
    picked = a(q)
    picked = int(picked)
    chatmatrix(picked, chatID)

#########

barracks = []

class Soldier():
    sID = 0
    rank  =""
    fName = ""
    lName = ""
    HP = 0
    aim = 0
    mobility = 0
    weapon = ""
    secondary = ""
    item = [""]
    armour = 0
    dmgp = 0
    dmgs = 0
    cover = 0
    ammo = 0
    overwatch = 0
    XP = 0
    alive = 1
    def __init__(self):
        self.fName = rd.choice(fnm)
        self.sID = len(barracks)
        self.lName =  rd.choice(lnm)
        self.rank = "Rookie"
        self.HP = rd.randrange(3,6)
        self.aim = rd.randrange(50,75)
        self.mobility = rd.randrange(11,16)
        self.weapon = rd.randrange(0,2)
        if self.weapon == 0:
            self.ammo = 4
        elif self.weapon == 1:
            self.ammo = 3
        self.secondary = rd.randrange(0,2)
        self.dmgp = 3
        self.dmgs = 2
        self.item = [(rd.randrange(0,3))]
        self.armour = "BDY" #body armour
    def summon(self):
        p(0,self.rank+" "+self.fName+" "+self.lName+" -  "+str(self.HP)+" HP"+" - "+str(self.aim)+ " Aim")
        p(0,"Items: "+priwep[self.weapon]+", "+secwep[self.secondary]+", "+items[self.item[0]])
    def deets(self):
        return(self.rank+" "+self.lName)
        
class Alien():
    species = ""
    aID = 0
    rank  =""
    fName = ""
    lName = ""
    HP = 0
    aim = 0
    mobility = 0
    weapon = ""
    secondary = ""
    item1 = ""
    item2 = ""
    armour = 0
    dmgp = 0
    dmgs = 0
    alive = 0
    cover = 0
    ammo = 0
    overwatch = 0
    def __init__(self):
        self.ammo = 1
        self.species = "Sectoid"
        self.fName = rd.choice(sectoidfName)
        self.aID = len(pod)
        self.lName =  rd.choice(sectoidlName)
        self.rank = round(rd.randrange(0+round(roomNo/20),2))
        self.HP = 2+self.rank
        self.aim = rd.randrange(50,75)+self.rank
        self.mobility = rd.randrange(9,13)+self.rank
        self.weapon = 0
        self.secondary = 0
        self.dmgp = 4
        self.dmgs = 3
        self.item1 = rd.randrange(0,2)
        self.armour = "BDY" #body armour
        self.alive = 1
    def thinman(self):
        self.ammo = 1
        self.species = "Thin Man"
        self.fName = rd.choice(thinfName)
        self.aID = len(pod)
        self.lName = rd.choice(thinlName)
        self.rank = round(rd.randrange(0+round(roomNo/30),2))
        self.HP = 3+self.rank
        self.aim = rd.randrange(60,80)+self.rank
        self.mobility = rd.randrange(12,15)+self.rank
        self.weapon = 0
        self.secondary = 0
        self.dmgp = 4
        self.dmgs = 3
        self.item1 = rd.randrange(0,2)
        self.armour = "BDY" #body armour
        self.alive = 1        
        
    def summon(self):
        p(0,aranks[self.rank]+" "+self.fName+" "+self.lName+" - "+str(self.HP)+" HP"+" - "+str(self.aim)+" Aim")
        p(0,"Items: "+apriwep[self.weapon]+", "+aitems[self.item1])
    def name(self):
        return (" ("+self.species+") "+aranks[self.rank]+" "+self.fName+" "+self.lName)
    def deets(self, chance):
        return (aranks[self.rank]+" "+self.fName+" "+self.lName+" - "+str(self.HP)+" HP - "+ str(chance) +"%")


def scatter(roomNo):
    cover = ["Full","Full","Full","Half","Half","Half","Half","Half","Half","No"]
    covernumber = [40,40,40,20,20,20,20,20,20,-10]
    for i in range(len(room[roomNo])):
        room[roomNo][i].cover = rd.choice(covernumber)
        if not room[roomNo][i].cover == -10:
            p(0,room[roomNo][i].name()+" moves to "+cover[covernumber.index(room[roomNo][i].cover)]+" cover!")
        else:
            p(0,room[roomNo][i].name()+" can't find any cover!")


def checkspot(roomNo):
    for i in range(len(room[roomNo])):
        p(0,room[roomNo][i].name()+" spotted!")

def playerTurn():
    global out
    global AP
    global roomNo
    global fragments
    global elerium
    global meld
    global alloy
    AP = soldier.mobility
    while AP > 0:
        p(0,"HP - "+str(soldier.HP))
        p(0,"AP - "+str(AP))
        if len(room[roomNo]) == 0:
            p("1","Advance")
            while out == False:
                action = a("int","#")
            out = False
            if action == "1":
                p(spk,"Roger that, moving up!")
                AP -= 1
                roomNo += 1
                checkspot(roomNo)
                scatter(roomNo)
                if rd.randrange(0,100) < 30:
                    p(0,soldier.deets()+" is in FULL cover.")
                    soldier.cover = 40
                else:
                    p(0,soldier.deets()+" is in HALF cover.")
                    soldier.cover = 20
                playerTurn()
        else:
            displayOptions()
            while out == False:
                action = a("int","#")
            out = False
            sel = invac[int(action)-1]

            if sel == "Reload":
                if soldier.weapon == 0:
                    soldier.ammo = 3
                elif soldier.weapon == 1:
                    soldier.ammo = 2
                AP -= 8
            if sel == "Overwatch":
                p(spk,"Got it, on Overwatch.")
                soldier.overwatch = 1
                AP = 0
            if sel == "End Turn":
                AP = 0
            if sel == "Reposition":
                AP -= 3
                checkForOverwatch("Alium",0)
                soldier.cover = 40
                p(spk,"Moving to Full cover!")
                if rd.randrange(0,100) < 50:
                    alium = rd.choice(room[roomNo])
                    p(0,alium.name()+" is flanked!")
                    alium.cover = 0
                
            if sel == "Meds":
                AP -= 10
                print("HP restored.")
                soldier.HP += 4
                soldier.item.pop(soldier.item.index(1))
            if sel == "Hunker Down":
                soldier.cover+=20
                p(spk,"Taking cover!")
                AP = 0
            if sel in room[roomNo]:
                AP -= 6
                p(spk,rd.choice(retort))
                p(0,"*Dakkadakkadakka*")
                chance = (soldier.aim)-(sel.cover)
                if 2 in soldier.item:
                    chance += 10
                if soldier.weapon == 1:
                    chance += 10
                if rd.randrange(0,100) <= chance:
                    damage = soldier.dmgp+rd.randrange(-1,2)
                    sel.HP -= damage
                    soldier.ammo -= 1
                    p(0,str(damage)+" damage!")
                    fragments += getLoot(sel)[0]
                    elerium += getLoot(sel)[1]
                    meld += getLoot(sel)[2]
                    alloy += getLoot(sel)[3]
                    checkDead(sel)
                else:
                    p(0,"Missed!")
                    soldier.ammo -= 1
            elif sel == "Frag":
                AP -= 10
                p(0,"BOOM!")
                soldier.item.pop(soldier.item.index(0))
                affected = room[roomNo]
                for i in range(len(affected)+1):
                    try:
                        alium = affected[i]
                        alium.HP -= 2
                        alium.cover = 0
                        fragments += getLoot(alium)[0]
                        elerium += getLoot(alium)[1]
                        meld += getLoot(alium)[2]
                        alloy += getLoot(alium)[3]
                        checkDead(alium)
                    except ( IndexError ):
                        i = 0
    p(0,soldier.deets()+" is out of AP!")


def checkForOverwatch(who,getalium):
    if who == "Alium":
        for i in range(len(room[roomNo])):
            alium = room[roomNo][i]
            cthplayer = alium.aim - soldier.cover + 10
            if alium.overwatch == 1:
                p(0,alium.name()+" reacts!")
                if alium.item1 == 2:
                    chance += 10
                if rd.randrange(0,100) < cthplayer:
                    dmg = alium.dmgp + rd.randrange(-2, 1)
                    p(0,str(dmg)+" damage!")
                    soldier.HP -= dmg
                    checkPlayerDead()
                else:
                    p(0," Missed!")
    else:
        alium = getalium
        cth = soldier.aim - alium.cover + 10
        if soldier.overwatch == 1:
                p(0,soldier.deets()+" reacts!")
                if 2 in soldier.item:
                    cth += 10
                if rd.randrange(0,100) < cth:
                    dmg = soldier.dmgp + rd.randrange(-2, 1)
                    p(0,str(dmg)+" damage!")
                    alium.HP -= dmg
                    checkDead(alium)
                else:
                    p(spk," Shot failed to connect!")


def alienTurn():
    for i in range(len(room[roomNo])):
        try:
            alium = room[roomNo][i]
        except ( Exception ):
            i = 0
        cthplayer = alium.aim - soldier.cover
        if alium.item1 == 2:
            chance += 10
        
        if alium.cover < 20:
            p(0,alium.name()+" runs to Full cover!")
            checkForOverwatch("Soldier",alium)
            alium.cover = 40
        if alium.cover < 40:
            if cthplayer > 30 + rd.randrange(0,40):
                p(0,alium.name()+" fires at "+soldier.deets()+"("+str(cthplayer)+"%)")
                if rd.randrange(0,100) < cthplayer:
                    dmg = alium.dmgp + rd.randrange(-2, 1)
                    p(0,str(dmg)+" damage!")
                    soldier.HP -= dmg
                    checkPlayerDead()
                else:
                    p(0,"Missed!")
            elif rd.randrange(0,100) < 20:
                if alium.item1 == 0:
                    p(0,alium.name()+" uses Alien Grenade!")
                    alium.item1 = 999
                    p(0,"3 damage!")
                    soldier.HP -= 3
                    checkPlayerDead()
            elif rd.randrange(0,100) < 40:
                if rd.randrange(0,100) < 50:
                    p(0,alium.name()+" runs to Full cover!")
                    checkForOverwatch("Soldier",alium)
                    alium.cover = 40
                else:
                    p(0,alium.name()+" runs to Half cover!")
                    checkForOverwatch("Soldier",alium)
                    alium.cover = 20
                
            else:
                if rd.randrange(0,100) < 30:
                    p(0,alium.name()+" went on overwatch!")
                    alium.overwatch = 1
                else:
                    p(0,alium.name()+" fires at "+soldier.deets()+"("+str(cthplayer)+"%)")
                    if rd.randrange(0,100) < cthplayer:
                        dmg = alium.dmgp + rd.randrange(-2, 1)
                        p(0,str(dmg)+" damage!")
                        soldier.HP -= dmg
                        checkPlayerDead()
                    else:
                        p(0,"Missed!")
                    
        else:
            if cthplayer > 10 + rd.randrange(0,40):
                p(0,alium.name()+" fires at "+soldier.deets()+"("+str(cthplayer)+"%)")
                if rd.randrange(0,100) < cthplayer:
                    dmg = alium.dmgp
                    p(0,str(dmg)+" damage!")
                    soldier.HP -= dmg
                    checkPlayerDead()
                else:
                    print("Missed!")
            else:
                p(0,alium.name()+" went on overwatch!")
                alium.overwatch = 1
                    
def checkDead(alium):
    if alium.HP <= 0:
        p(0,alium.name()+" died!")
        getLoot(alium)
        checkXP()
        room[roomNo].pop(room[roomNo].index(alium))

def checkPlayerDead():
    if soldier.HP <= 0:
        p(0,soldier.deets()+" was killed!")
        p("Bradford","Commander, our unit was killed.")
        p("Bradford","We were able to recover some materials, however.")
        print("Fragments:",fragments)
        print("Elerium:",elerium)
        print("Meld:",meld)
        print("Alloy:",alloy)
        print("Total Score:",(fragments+elerium+meld+alloy+soldier.XP+roomNo))
        soldier.alive = 0
        quit
   

def checkXP():
    if soldier.XP >= 25 and not soldier.rank == "Squaddie" and soldier.XP < 50:
        soldier.rank = "Squaddie"
        soldier.HP += 1
        soldier.aim += 2
        soldier.mobility += 1
        p(0,"LEVEL UP! "+soldier.deets())
    elif soldier.XP >= 50 and not soldier.rank == "Corporal" and soldier.XP < 100:
        soldier.rank = "Corporal"
        soldier.HP += 1
        soldier.aim += 2
        soldier.mobility += 1
        soldier.item.append(0)
        p(spk,"Recovered a Frag Grenade!")
        p(0,"LEVEL UP! "+soldier.deets())
    elif soldier.XP >= 100 and not soldier.rank == "Sergeant" and soldier.XP < 200:
        soldier.rank = "Sergeant"
        soldier.HP += 2
        soldier.aim += 1
        soldier.mobility += 1
        soldier.item.append(1)
        p(spk,"Recovered Nano Serum!")
        p(0,"LEVEL UP! "+soldier.deets())
    elif soldier.XP >= 200 and not soldier.rank == "Sergeant" and soldier.XP < 400:
        soldier.rank = "Liutenant"
        soldier.HP += 1
        soldier.aim += 1
        soldier.item.append(0)
        p(spk,"Recovered a Frag Grenade!")
        p(0,"LEVEL UP! "+soldier.deets())
    
        
def getLoot(alium):
    fragments = 0
    elerium = 0
    meld = 0
    alloy = 0
    soldier.XP += alium.rank + -(alium.HP)+2
    fragments += -(alium.HP)
    elerium += alium.rank
    meld += 1*alium.rank
    if alium.item1 == 0:
        elerium += 1
    elif alium.item1 == 1:
        alloy += 3
    elif alium.item1 == 2:
        fragments += 2
    return [fragments, elerium, meld, alloy]

            

        
def displayOptions():
    global invac
    global invacref
    global AP
    invac = []
    invacref = []
    
    if soldier.ammo != 0:
        if AP > 5:
            if soldier.weapon == 0:
                saywep = "(~3dmg)(6AP) Fire Ballistic Rifle"
            elif soldier.weapon == 1:
                saywep = "(~2dmg)(6AP) Fire Ballistic Carbine"
            for i in range(len(room[roomNo])):
                alium = room[roomNo][i]
                chance = (soldier.aim)-(alium.cover)
                if 2 in soldier.item:
                    chance += 10
                if 1 in soldier.item:
                    chance += 10
                invac.append(alium)
                p(len(invac),saywep+" "+alium.deets(chance))
    else:
        if AP > 7:
            invac.append("Reload")
            p(len(invac),"(8AP) Reload Weapon")
    if 0 in soldier.item:
        if AP > 9:
            invac.append("Frag")
            p(len(invac),"(2dmg)(10AP) Throw Frag Grenade")
    if 1 in soldier.item:
        if AP > 9:
            invac.append("Meds")
            p(len(invac),"(+4HP)(10AP) Use Nano Serum")
    invac.append("Overwatch")
    p(len(invac),"Overwatch")
    if AP > 2:
        invac.append("Reposition")
        p(len(invac),"(3AP) Reposition")
    invac.append("Hunker Down")
    p(len(invac),"Hunker Down")
    invac.append("End Turn")
    p(len(invac),"End Turn")
    
def craft(item):
    pass

p(0,"Welcome Commander. We've discovered an Alien Base, and it's your job to send someone out to deal with it.")
p(0,"Choose a soldier from the 3 below to go on the mission.")

for i in range(3):
    x = Soldier()
    barracks.append(x)

for i in range(len(barracks)):
    p(0,str(i+1)+": ")
    barracks[i].summon()
    p(0,"")

while out == False and int(out) < len(barracks):
    soldier = a("int","#")
    out = True
out = False
soldier = barracks[int(soldier)-1]

spk = soldier.fName + " " + soldier.lName
p(spk, "Ready for duty, Commander!")
room = [[]]
for i in range(11):
    for j in range(3+rd.randrange(-2,2)):
        x = Alien()
        pod.append(x)
    room.append(pod)
    pod = []
    if i > 3:
        for j in range(3+rd.randrange(-2,2)):
            x = Alien()
            if rd.randrange(0,100) < 50:
                x.thinman()
            pod.append(x)
        room.append(pod)
        pod = []
    


roomNo = 0
AP = soldier.mobility


while soldier.alive == 1:
    try:
        playerTurn()
        alienTurn()
    except ( ValueError or IndexError):
        pass
    if roomNo == 11:
        print("You win!")
        break
quit
