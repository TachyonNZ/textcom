#By /u/TachyonNZ
# Van Doorn by /u/net_goblin
#TEXT-COM, V0.1

import random as rd
import time as tm

fnm = ["Bob","Becks","Kate","Alex","Tim","Peter","Annetta","Violet","Jeb","Bill","Rune","Jeff","Kim","Lee","Iago","Soylent","Iko","Dan","John","Pedro","Juan","Rico","David","Andrew","Wilson","James","Richard","Rocky","Adam","Megan","Shelly","Kim","Bear"]
lnm = ["Meier","Dan Voorn","Durant","Lee","Kerman","Nilsen","Possible","Fox","Vin Diern","Vern Dern","Friendly","Civilian","Snek","Advint","Firaxi","Beegle","Green","Wolf","Grills","Red","Taa","Tank","Beardly","Sherman","Herman","Nerman","Nuton"]
bradford = ["CLOSE RANGE?!","WHAT HAVE YOU DONE?!","COMMANDER!","WE'RE PICKING UP MULTIPLE CONTACTS!","CURRENT ENEMY STATUS AT THE SITE IS UNKNOWN!"]
VAN_DOORN_QUOTES = [
    "I'm the Ops team! I'll get over there!",
    "I'll get down there! Just fair if I have all the fun.",
    "I'm getting down there or what?",
    "Come on! I won't go down without a fight.",
    # "Thank God you're here. I'm still breathing, but I can't say the same for a lot of my boys. Let's get out of here before any more of those things show up.",
    # "I don't know what outfit you're from, but I haven't seen gear like that before.",
    "I just hope I get another shot at these alien bastards... I owe it to my men.",
    "I just wish I could have done more for my people, I lost some good men.",
    "It's looking bad out there; I might not make if you don't show up.",
    "I owe you one... seriously... I wouldn't be here without your help."
]

#Soldier names
VAN_DOORN = "Van Doorn"

bbspecies = ["Sectoid"]
sectoidfName = ["Glip","Gleep","Glup","Glorp","Gloop","Glop","Glump","Glerp","Glurp","Glarp"]
sectoidlName = ["Glop","Glarp","Glupple","Glorple","Gloopley","Glopperson","Glep","Glommery"]
thinfName = ["T.","P.","H.","Z.","K.","A.","F.","X.","P.","L.","W.","S.","V."]
thinlName = ["Hinman","Alium","Van Doom","Lmao","Notanalien","Anderson","Smith","Human","Clark","Warzonager","Iper","Thinmint","Mint","Spear"]
floaterfName = ["Dirk","Ferdinand","Frederick","Algernon","Angus","King","Cornelius","Francis","Christopher","Gustav","Richard","Ivan","Yuri","Vlad"]
floaterlName = ["Meyer","Mleadeer","Peters","Prince","Vos","Wolf","Schwarz","Frank","Miller","Anderssen","Slavolav","Stroganov","Costarov"]

mutonfName = ["Pooter","Dave","Holk","Billy","Tim","Jeffery","Leeroy","Jimmy","Hank",""]
mutonlName = ["Von Mooter","The Muton","Hugan","Jankins","Jefferson"]
#Aliem names

aranks = {0:"Peon",1:"Soldier",2:"Trooper",3:"Officer",4:"Commander",5:"Overseer",6:"Supreme Commander",7:"Uber",8:"Trancendant"}
#alien ranks

retort = ("Suck on this!","Eat this!","Pick on someone your own size!","Take this!","Welcome to Earth!")

#when a soldier shoots at an alien

priwep = {0:"Ballistic Rifle",1:"Ballistic Carbine",2:"Light Plasma Rifle",3:"Plasma Rifle",4:"Bradford's Pistol"}
secwep = {0:"Ballistic Pistol",1:"Autopistol"}
items = {0:"Frag Grenade",1:"Nano Serum",2:"Scope",3:"Alien Grenade",999:"None"}
drops = {0:"Frag Grenade",1:"Nano Serum",2:"Alien Grenade",3:"Light Plasma Rifle",4:"Plasma Rifle"}
#human weapons + items



apriwep = {0:"Light Plasma Rifle",1:"Plasma Rifle"}
asecwep = {0:"Plasma Pistol",1:"Alloy Pistol"}
apowers = {0: "Mindfray",1: "Psi Boost"}
aitems = {0:"Alien Grenade",1:"Alloy Plating",2:"Focus Lens",999:"None"}
#aliem weapons, items and powers

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
#unused

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
#get input and check against wanted type

def p(spk,q): #print with speaker and possibly delay
    if spk != 0:
        print(str(spk)+': "'+str(q)+'"')
    else:
        print(q)
    #s(len(q)/50)
    #if uncommented, this will add delay to all instances of 'print' from this def

def s(t):
    tm.sleep(t)
#go to sleep for t seconds

def c(q, chatID):
    picked = a(q)
    picked = int(picked)
    chatmatrix(picked, chatID)
#unused, relic of another TBG I was making

#########

barracks = []

#here we define all the variables for a soldier (could probably all be stored in an array)
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
    alive = True
    aimpenalty = 0

    def __init__(self):
        if rd.randrange(1,100) < 5:
            if rd.randrange(1, 3) == 1:
                # CO Bradford
                self.HP = 6
                self.fName = "Central Officer"
                self.lName = "Bradford"
                self.aim = 100
                self.weapon = 4
                self.ammo = 999
                self.dmgp = 5
            else:
                # Gen. Van Doorn
                self.HP = 6
                self.rank = "General"
                self.fName = "Peter"
                self.lName = VAN_DOORN
                self.aim = 100
                self.weapon = 0
        else:
            self.HP = rd.randrange(3,6)
            self.fName = rd.choice(fnm)
            self.lName =  rd.choice(lnm)
            self.aim = rd.randrange(50,75)
            self.weapon = rd.randrange(0,2)
            self.rank = "Rookie"
        self.sID = len(barracks)
        self.mobility = rd.randrange(11,16)
        if self.weapon == 0:
            self.ammo = 4
            self.dmgp = 3
        elif self.weapon == 1:
            self.ammo = 3
            self.dmgp = 2
        self.secondary = rd.randrange(0,2)

        self.dmgs = 2
        self.item = [(rd.randrange(0,3)),(rd.randrange(0,2))]
        self.armour = "BDY" #body armour


    def summon(self):
        p(0,self.rank+" "+self.fName+" "+self.lName+" -  "+str(self.HP)+" HP"+" - "+str(self.aim)+ " Aim")
        p(0,"Items: "+priwep[self.weapon]+", "+items[self.item[0]]+", "+items[self.item[1]])
    def deets(self):
        return(self.rank+" "+self.lName)
    #randomisation of the starting rookies
    def updateWep(self):
        if soldier.weapon == 2:
            self.dmgp = 5
            self.ammo = 4
        if soldier.weapon == 3:
            self.dmgp = 7
            self.ammo = 5


#we define the aliens here. they are initialised as sectoids but this can be changed with the definitions, such
#as thinman(), to convert the alien to a thinman
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
    alive = False
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
        self.item1 = rd.randrange(0,3)
        self.armour = "BDY" #body armour
        self.alive = True
    def thinman(self):
        self.ammo = 1
        self.species = "Thin Man"
        self.fName = rd.choice(thinfName)
        self.aID = len(pod)
        self.lName = rd.choice(thinlName)
        self.rank = round(rd.randrange(0,3))
        self.HP = 3+self.rank
        self.aim = rd.randrange(60,80)+self.rank
        self.mobility = rd.randrange(12,15)+self.rank
        self.weapon = 0
        self.secondary = 0
        self.dmgp = 4
        self.dmgs = 3
        self.item1 = rd.randrange(0,3)
        self.armour = "BDY" #body armour
        self.alive = True
    def floater(self):
        self.ammo = 1
        self.species = "Floater"
        self.fName = rd.choice(floaterfName)
        self.aID = len(pod)
        self.lName = rd.choice(floaterlName)
        self.rank = round(rd.randrange(0+round(roomNo/10),3))
        self.item1 = rd.randrange(0,3)
        self.HP = 4+self.rank
        self.aim = rd.randrange(50,70)+self.rank
        self.mobility = rd.randrange(12,15)+self.rank
        self.weapon = 0
        self.secondary = 0
        self.dmgp = 4
        self.dmgs = 3
        self.armour = "BDY" #body armour
        self.alive = True
    def muton(self):
        self.ammo = 1
        self.species = "Muton"
        self.fName = rd.choice(mutonfName)
        self.aID = len(pod)
        self.lName = rd.choice(mutonlName)
        self.rank = round(rd.randrange(0+round(roomNo/10),3))
        self.item1 = rd.randrange(0,3)
        self.HP = 8+self.rank
        self.aim = rd.randrange(50,60)+self.rank
        self.mobility = rd.randrange(10,12)+self.rank
        self.weapon = 1
        self.secondary = 0
        self.dmgp = 6
        self.dmgs = 4
        self.armour = "BDY" #body armour
        self.alive = True
    def refresh(self):
        self.HP += self.rank*round(rd.random()*2)
        self.aim  +=  self.rank*round(rd.random()*2)

    def summon(self):
        p(0,aranks[self.rank]+" "+self.fName+" "+self.lName+" - "+str(self.HP)+" HP"+" - "+str(self.aim)+" Aim")
        p(0,"Items: "+apriwep[self.weapon]+", "+aitems[self.item1])
    #used if we want to get valuable data about an alien
    def name(self):
        return (" ("+self.species+") "+aranks[self.rank]+" "+self.fName+" "+self.lName)
    #gives us names for when we reference the alien in game
    def deets(self, chance):
        return (aranks[self.rank]+" "+self.fName+" "+self.lName+" - "+str(self.HP)+" HP - "+ str(chance) +"%")
    #gives us tactical information, like HP and hit chance


def scatter(roomNo):
    cover = ["Full","Full","Full","Half","Half","Half","Half","Half","Half","No"]
    covernumber = [40,40,40,20,20,20,20,20,20,-10]
    for i in range(len(room[roomNo])):
        room[roomNo][i].cover = rd.choice(covernumber)
        if not room[roomNo][i].cover == -10:
            p(0,room[roomNo][i].name()+" moves to "+cover[covernumber.index(room[roomNo][i].cover)]+" cover!")
        else:
            p(0,room[roomNo][i].name()+" can't find any cover!")
#scatters the aliens in a room, some won't find any cover.

def checkspot(roomNo):
    for i in range(len(room[roomNo])):
        p(0,room[roomNo][i].name()+" spotted!")
#could probably be merged in with scatter(). Tells you that you've seen an alien


#ah, the player's turn.
def playerTurn():
    global out
    global AP
    global roomNo
    global fragments
    global elerium
    global meld
    global alloy
    AP = soldier.mobility
    soldier.overwatch = 0
    while AP > 0 and soldier.alive == True: #while the player has spare action points left
        p(0,"HP - "+str(soldier.HP))
        p(0,"AP - "+str(AP))
        #displays stats
        if len(room[roomNo]) == 0:
            p("1","Advance")
            if AP > 7:
                p("2","(8AP) Reload")
            while out == False:
                action = a("int","#")
                #until they enter valid text, see a(form,q) for moer information
            out = False
            if action == "1":
                if soldier.lName == "Bradford":
                    p(spk, "Commander! I advise you to reconsider!")
                elif soldier.lName == VAN_DOORN:
                    p(spk, "I'll get over there!")
                else:
                    p(spk, "Roger that, moving up!")
                AP -= 1 #this is redundant because AP is reset the next room anyway
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
            if action == "2":
                if AP > 7:
                    if soldier.weapon == 0:
                        soldier.ammo = 4
                    elif soldier.weapon == 1:
                        soldier.ammo = 3
                    elif soldier.weapon == 2:
                        soldier.ammo = 4
                    elif soldier.weapon == 3:
                        soldier.ammo = 5
                    elif soldier.weapon == 4:
                        soldier.ammo = 999
                    AP -= 8
                    playerTurn()
        else:
            displayOptions()
            #now the player will choose an action
            while out == False:
                action = a("int","#")
            out = False

            try:
                sel = invac[int(action)-1]
            except ( IndexError ):
                while out == False:
                    action = a("int","#")
                out = False
            sel = invac[int(action)-1]


            if sel == "Reload":
                if soldier.weapon == 0:
                    soldier.ammo = 4
                elif soldier.weapon == 1:
                    soldier.ammo = 3
                elif soldier.weapon == 2:
                    soldier.ammo = 4
                elif soldier.weapon == 3:
                    soldier.ammo = 5
                elif soldier.weapon == 4:
                    soldier.ammo = 999
                #depending on what weapon the player has, they will get a certain amount of ammo
                AP -= 8
            if sel == "Overwatch":
                if soldier.lName == "Bradford":
                    p(spk, "Keep your eyes peeled!")
                elif soldier.lName == VAN_DOORN:
                    p(spk, "You coming down here or what?")
                else:
                    p(spk, "Got it, on Overwatch.")
                soldier.overwatch = 1
                AP = 0
            if sel == "End Turn":
                AP = 0
            if sel == "Reposition":
                AP -= 3
                checkForOverwatch("Alium",0)
                #if any aliens are on overwatch, check and be shot at if they are
                soldier.cover = 40
                if soldier.lName == "Bradford":
                    p(spk, "Moving to...wait...that's CLOSE RANGE!")
                elif soldier.lName == VAN_DOORN:
                    p(spk, "Come on! I won't go down without a fight.")
                else:
                    p(spk, "Moving to Full cover!")
                if rd.randrange(0,100) < 50:
                    alium = rd.choice(room[roomNo])
                    p(0,alium.name()+" is flanked!")
                    alium.cover = 0
                #chance to flank an alien

            if sel == "Meds":
                AP -= 10
                print("HP restored.")
                soldier.HP += 4
                soldier.item.pop(soldier.item.index(1))
                #heals soldier but consumes the item
            if sel == "Hunker Down":
                soldier.overwatch = 0
                if soldier.cover == 20 or soldier.cover == 40:
                    soldier.cover+=20
                p(spk,"Taking cover!")
                AP = 0
                #provides extra cover to soldier
            if sel in room[roomNo]: #if sel is an Alien() pointer
                AP -= 6
                if soldier.lName == "Bradford":
                    p(spk, rd.choice(bradford))
                elif soldier.lName == VAN_DOORN:
                    p(spk, rd.choice(VAN_DOORN_QUOTES))
                else:
                    p(spk, rd.choice(retort))
                if soldier.weapon <= 1:
                    p(0,"*Dakkadakkadakka*")
                if soldier.weapon == 4:
                    p(0,"*Bang*")
                else:
                    p(0,"*Whap-whap-whap*")
                chance = (soldier.aim)-(sel.cover)
                if 2 in soldier.item: #scope
                    chance += 0
                if soldier.weapon == 1 or soldier.weapon == 2 : #carbine
                    chance += 10
                roll = rd.randrange(0,100)
                if roll <= chance+10:
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
                p(0,"BAM!")
                #grenade, obviously
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
                        i = 0 #reset the loop
                #the grenade only affects some of the aliens in the room, but is guaranteed to hit at least 1
                #it's not a bug, it's a feature
            elif sel == "AlienFrag":
                AP -= 15
                p(0,"**BLAM!**")
                #grenade, obviously
                soldier.item.pop(soldier.item.index(3))
                affected = room[roomNo]
                for i in range(len(affected)+1):
                    try:
                        alium = affected[i]
                        alium.HP -= 4
                        alium.cover = 0
                        fragments += getLoot(alium)[0]
                        elerium += getLoot(alium)[1]
                        meld += getLoot(alium)[2]
                        alloy += getLoot(alium)[3]
                        checkDead(alium)
                    except ( IndexError ):
                        i = 0 #reset the loop
                #the grenade only affects some of the aliens in the room, but is guaranteed to hit at least 1
                #it's not a bug, it's a feature
    #ends turn by default


def checkForOverwatch(who,getalium):
    if who == "Alium": #if it's an alien shooting at soldier
        for i in range(len(room[roomNo])):
            alium = room[roomNo][i]
            cthplayer = alium.aim - soldier.cover + 10
            if alium.overwatch == 1:
                p(0,alium.name()+" reacts!")
                if alium.item1 == 2:
                    cthplayer += 10
                if rd.randrange(0,100) < cthplayer:
                    dmg = alium.dmgp + rd.randrange(-2, 1)
                    p(0,str(dmg)+" damage!")
                    soldier.HP -= dmg
                    checkPlayerDead()
                    #did it kill the player?
                else:
                    p(0," Missed!")
                alium.overwatch = 0
    else: #if a soldier is shooting at an alien
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
                    if soldier.lName == "Bradford":
                        p(spk,"How did I miss that?!")
                    else:
                        p(spk,"Shot failed to connect!")
                soldier.ammo -= 1
                soldier.overwatch = 0

def fire(alium,cthplayer):
    p(0,alium.name()+" fires at "+soldier.deets()+"("+str(cthplayer)+"%)")
    if rd.randrange(0,100) < cthplayer:
        dmg = alium.dmgp + rd.randrange(-2, 1)
        p(0,str(dmg)+" damage!")
        soldier.HP -= dmg
        checkPlayerDead()
        #did you kill the player, alien?
    else:
        p(0,"Missed!")

def nade(alium):
    p(0,alium.name()+" uses Alien Grenade!")
    p(0,"**BLAM!**")
    alium.item1 = 999
    #sets the aliens item to 'none', no more grenades for you
    p(0,"3 damage!")
    soldier.HP -= 3
    checkPlayerDead()


def ow(alium):
    p(0,alium.name()+" went on overwatch!")
    alium.overwatch = 1


def move(alium,cover):
    if cover == 40:
        p(0,alium.name()+" runs to Full cover!") #if an alien has no cover, it will run to full cover. same goes if it's flanked
    elif cover == 20:
        p(0,alium.name()+" runs to Half cover!")
    checkForOverwatch("Soldier",alium)
    alium.cover = cover


def alienTurn():
    for i in range(len(room[roomNo])):
        try:
            alium = room[roomNo][i]
        except ( Exception ):
            i = 0
        #because something may have happened that causes an index error
        if alium.alive != 0 and soldier.alive == True:
            cthplayer = alium.aim - soldier.cover
            if alium.item1 == 2: #focusing lens
                cthplayer += 20

            if alium.cover < 20:
                if rd.randrange(0,100) < 80:
                    move(alium,40)
                elif rd.randrange(0,100) < 40:
                    fire(alium,cthplayer)
                else:
                    move(alium,20)
            if alium.cover < 40:
                if cthplayer > 50 + rd.randrange(0,40):
                    fire(alium,cthplayer)
                elif rd.randrange(0,100) < 20:
                    if alium.item1 == 0:
                        nade(alium)
                elif rd.randrange(0,100) < 40:
                    if rd.randrange(0,100) < 50:
                        move(alium,40)
                    else:
                        move(alium,20)
                    #randomly moves to different cover sometimes

                else:
                    if rd.randrange(0,100) < 20:
                        ow(alium)
                    else:
                        fire(alium,cthplayer)

            else:
                if cthplayer > 80 + rd.randrange(0,20):
                    fire(alium,cthplayer)
                elif rd.randrange(0,100) < 80:
                    move(alium,20)
                else:
                    ow(alium)


def checkDead(alium):
    if alium.HP <= 0:
        p(0,alium.name()+" died!")
        getLoot(alium)
        drop()
        checkXP()
        room[roomNo].pop(room[roomNo].index(alium))
        #kills, loots and removes the alien from the game

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
        soldier.alive = False
        quit
        #doesn't want to stop the whole game straight away for some reason

#levels up
def checkXP():
    if soldier.XP >= 25 and not soldier.rank == "Squaddie" and soldier.XP < 100:
        soldier.rank = "Squaddie"
        soldier.HP += 1
        soldier.aim += 2
        soldier.mobility += 1
        drop()
        drop()
        p(0,"LEVEL UP! "+soldier.deets())
    elif soldier.XP >= 100 and not soldier.rank == "Corporal" and soldier.XP < 300:
        soldier.rank = "Corporal"
        soldier.HP += 1
        soldier.aim += 2
        soldier.mobility += 1
        drop()
        drop()
        p(0,"LEVEL UP! "+soldier.deets())
    elif soldier.XP >= 300 and not soldier.rank == "Sergeant" and soldier.XP < 900:
        soldier.rank = "Sergeant"
        soldier.HP += 2
        soldier.aim += 1
        soldier.mobility += 1
        drop()
        drop()
        p(0,"LEVEL UP! "+soldier.deets())
    elif soldier.XP >= 900 and not soldier.rank == "Lieutenant" and soldier.XP < 1500:
        soldier.rank = "Lieutenant"
        soldier.HP += 1
        soldier.aim += 1
        drop()
        drop()
        p(0,"LEVEL UP! "+soldier.deets())
    elif soldier.XP >= 1500 and not soldier.rank == "Captain" and soldier.XP < 2000:
        soldier.rank = "Captain"
        soldier.HP += 2
        soldier.aim += 1
        drop()
        drop()
        drop()
        drop()
        p(0,"LEVEL UP! "+soldier.deets())
    elif soldier.XP >= 2000 and not soldier.rank == "Major" and soldier.XP < 3000:
        soldier.rank = "Major"
        soldier.HP += 1
        soldier.aim += 1
        soldier.mobility += 1
        drop()
        drop()
        drop()
        p(0,"LEVEL UP! "+soldier.deets())
    elif soldier.XP >= 3000 and not soldier.rank == "Colonel":
        soldier.rank = "Colonel"
        soldier.HP += 1
        soldier.aim += 1
        drop()
        drop()
        drop()
        drop()
        drop()
        drop()
        p(0,"LEVEL UP! "+soldier.deets())


def getLoot(alium):
    fragments = 0
    elerium = 0
    meld = 0
    alloy = 0
    soldier.XP += alium.rank*abs(alium.HP)
    fragments += abs(alium.HP)
    elerium += alium.rank
    meld += 2*alium.rank
    if alium.item1 == 0:
        elerium += 2
    elif alium.item1 == 1:
        alloy += 2
    elif alium.item1 == 2:
        fragments += 2
    if alium.weapon == 0:
        elerium += 1
        fragments += 2
    elif alium.weapon == 1:
        elerium += 2
        fragments += 4
    return [fragments, elerium, meld, alloy]
    #gets some sweet sweet loot from those aliens




def displayOptions():
    global invac
    global invacref
    global AP
    invac = []
    invacref = []

    if soldier.ammo != 0:
        if AP > 5:
            if soldier.weapon == 0: #if we have the rifle
                saywep = "(~3dmg)(6AP) Fire Ballistic Rifle"
            elif soldier.weapon == 1: #if we have the carbine
                saywep = "(~2dmg)(6AP) Fire Ballistic Carbine"
            elif soldier.weapon == 2:
                saywep = "(~5dmg)(6AP) Fire Light Plasma Rifle"
            elif soldier.weapon == 3:
                saywep = "(~6dmg)(6AP) Fire Plasma Rifle"
            elif soldier.weapon == 4: #if we have the rifle
                saywep = "(~3dmg)(6AP) Fire Bradford's Pistol"
            for i in range(len(room[roomNo])):
                alium = room[roomNo][i]
                chance = (soldier.aim)-(alium.cover)
                if 2 in soldier.item:
                    chance += 10
                if 1 in soldier.item:
                    chance += 10
                if chance < 0:
                    chance = 5
                if chance > 100:
                    chance = 95
                invac.append(alium)
                p(len(invac),saywep+" : "+alium.deets(chance))
                #displays a list of valid targets
        invac.append("Overwatch")
        p(len(invac),"Overwatch")
    else:
        if AP > 7:
            invac.append("Reload")
            p(len(invac),"(8AP) Reload Weapon")
    if 0 in soldier.item:
        if AP > 9:
            invac.append("Frag")
            p(len(invac),"(2dmg)(10AP) Throw Frag Grenade")
    if 3 in soldier.item:
        if AP > 14:
            invac.append("AlienFrag")
            p(len(invac),"(4dmg)(15AP) Throw Alien Grenade")
    if 1 in soldier.item:
        if AP > 9:
            invac.append("Meds")
            p(len(invac),"(+4HP)(10AP) Use Nano Serum")

    #other default actions which are almost always available

    if AP > 2:
        invac.append("Reposition")
        p(len(invac),"(3AP) Reposition")
    if soldier.cover == 20 or soldier.cover == 40:
        invac.append("Hunker Down")
        p(len(invac),"Hunker Down")
    invac.append("End Turn")
    p(len(invac),"End Turn")


def drop():
    itemdrop = rd.randrange(0,5)
    if rd.randrange(1,100) < 5:
        p(spk,"Recovered a "+drops[itemdrop]+"!")
        if itemdrop == 3:
            soldier.weapon = 2
            soldier.updateWep()
        if itemdrop == 4:
            soldier.weapon = 3
            soldier.updateWep()
        else:
            soldier.item.append(itemdrop)

def craft(item):
    pass

def mutate(i):
    if i <= 3:
        pass
    elif i > 3 and i < 10:
        y = options[rd.randrange(0,2)]
        if y == "Thinman":
            x.thinman()
        x.rank += 1
        x.refresh()
    elif i > 9 and i < 15:
        y = rd.choice(options)
        if y == "Thinman":
            x.thinman()
        if y == "Floater":
            x.floater()
        if y == "Muton":
            x.muton()
            x.rank -= 2
        x.rank += 3
        x.refresh()
    elif i > 14:
        y = options[rd.randrange(1,4)]
        if y == "Thinman":
            x.thinman()
        if y == "Floater":
            x.floater()
        if y == "Muton":
            x.muton()
        x.rank += 4
        x.refresh()
    elif i > 16:
        y = options[rd.randrange(2,4)]
        if y == "Muton":
            x.muton()
        if y == "Floater":
            x.floater()
        x.rank += 4
        x.refresh()


# def main():
p("Bradford", "Welcome Commander. We've discovered an Alien Base, and it's your job to send someone out to deal with it.")
p("Bradford", "Choose a soldier from the 3 below to go on the mission.")

#generates soldiers
for i in range(3):
    x = Soldier()
    barracks.append(x)

#displays a list of the soldiers
for i in range(len(barracks)):
    p(0,str(i+1)+": ")
    barracks[i].summon()
    p(0,"")

#forces you to pick only one soldier
while out == False and int(out) < len(barracks):
    soldier = a("int","#")
    out = True
out = False
soldier = barracks[int(soldier)-1]

spk = soldier.fName + " " + soldier.lName
if soldier.lName == "Bradford":
    p(spk, "What? There must have been a mistake on the sheet, Commander! You can't send --")
elif soldier.lName == VAN_DOORN:
    p(spk, "I'm the Ops team?")
else:
    p(spk, "Ready for duty, Commander!")
room = [[]]
options = ["Sectoid","Thinman","Floater","Muton"]

for i in range(30):
    pod = []
    for j in range(3+rd.randrange(-2,2)):
        x = Alien()
        pod.append(x)
    room.append(pod)
    for j in range(len(room[i])):
        if i < 10:
            x = rd.choice(room[i])
            mutate(i)
        elif i < 15:
            x = rd.choice(room[i])
            mutate(i)
            x = rd.choice(room[i])
            mutate(i)
        elif i < 20:
            x = rd.choice(room[i])
            mutate(i)
            x = rd.choice(room[i])
            mutate(i)
            x = rd.choice(room[i])
            mutate(i)
        else:
            x = rd.choice(room[i])
            mutate(i)
            x = rd.choice(room[i])
            mutate(i)
            x = rd.choice(room[i])
            mutate(i)

room[30] = []
x = Alien()
x.muton()
x.rank = 8
x.refresh()
x.HP = 20

#generates the pods in each room
room.append([])
room[31] = []

roomNo = 0
AP = soldier.mobility

#game loop, runs until your soldier is killed
while soldier.alive == True:
    try:
        playerTurn()
        p(0,soldier.deets()+" is out of AP!")
        print("Alien Activity!")
        s(2)

        if soldier.alive == True:
            alienTurn()
    except ( ValueError or IndexError ):
        pass
    if roomNo == 31:
        print("You have won the game!")
        break
quit

