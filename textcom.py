#By /u/TachyonNZ
# Van Doorn by /u/net_goblin
#TEXT-COM, V0.1

import random as rd
import time as tm


SEX_FEMALE = 'f'
SEX_MALE = 'm'
XCOM_MALE_FIRSTNAME = [
    'Bob',
    'Grant',
    'Dylan',
    'Fletcher',
    'Daniel',
    'Kav',
    'Jackson',
    'Alex',
    'Tim',
    'Peter',
    'Jeb',
    'Bill',
    'Rune',
    'Jeff',
    'Lee',
    'Iago',
    'Dan',
    'John',
    'Isaac',
    'Pedro',
    'Juan',
    'Rico',
    'David',
    'Andrew',
    'Wilson',
    'James',
    'Richard',
    'Rocky',
    'Adam',
    'Bear',
    'Paul',
    'Guy',
    'Sid',
    'Murray'
]
XCOM_FEMALE_FIRSTNAME = [
    'Becks',
    'Kate',
    'Annetta',
    'Violet',
    'Kim',
    'Iko',
    'Megan',
    'Shelly',
    'Kim',
    'Nina',
    'Olga',
    'Katherina',
    'Anya',
    'Suzie',
    'Rebecca',
    'Joanna',
    'Patricia',
    'Maria',
    'Judith',
    'Carmen',
    'Isabel',
    'Ana',
    'Laura',
    'Sara',
    'Emma',
    'Rachael',
    'Ingrid',
    'Nicole',
    'Chelsea',
    'Chell'
]
XCOM_LASTNAME = [
    'Meier',
    'Durant',
    'Lee',
    'Kerman',
    'Nilsen',
    'Fox',
    'Vern Dern',
    'Beagle',
    'Green',
    'Wolf',
    'Grills',
    'Red',
    'Taa',
    'Tank',
    'Beardly',
    'Sherman',
    'Herman',
    'Nerman',
    'Nuton',
    'Peterson',
    'Clarke',
    'French',
    'Clark',
    'Hayes',
    'Munroe',
    
]
# <http://www.ufopaedia.org/index.php?title=Nicknames_%28EU2012%29>
XCOM_UNISEX_NICKNAMES_ASSAULT = [
    'All Day',
    'Android',
    'Blitz',
    'Bonzai',
    'Boomer',
    'Caper',
    'Chops',
    'Cobra',
    'Coney',
    'Close Range',
    'D.O.A.',
    'DJ',
    'Desperado',
    'Devil Dog',
    'Dice',
    'Double Down',
    'Geronimo',
    'Gonzo',
    'Gunner',
    'Hardcore',
    'Hazard',
    'Loco',
    'Mad Dog',
    'Mustang',
    'Pitbull',
    'Psycho',
    'Rabid',
    'Rhino',
    'Red Fox',
    'Septic',
    'Sheriff',
    'Shotsy',
    'Smash',
    'Socks',
    'Spitfire',
    'Tombstone',
    'Trips',
    'Twitch',
    'Vandal',
    'Wardog',
    'Werewolf',
    'Wildchild',
    'Wolverine',
    'Zilch',
    'Zap'
]
XCOM_MALE_NICKNAMES_ASSAULT = [
    'Bull',
    'Cash',
    'Cowboy',
    'Duke',
    'Mad Man',
    'Nitro',
    'Rascal',
    'Spike',
    'Viking'
]
XCOM_FEMALE_NICKNAMES_ASSAULT = [
    'All In',
    'Freestyle',
    'Wednesday',
]
XCOM_UNISEX_NICKNAMES_HEAVY = [
    '98',
    'Arcade',
    'Boom Boom',
    'Brick',
    'Casino',
    'Collateral',
    'Crash',
    'Crater',
    'Diesel',
    'Disco',
    'Doomsday',
    'Dozer',
    'Flash',
    'Hulk',
    'Leaded',
    'Lights Out',
    'Nova',
    'Nuke',
    'Painbringer',
    'Prototype',
    'Richter',
    'Road Block',
    'Seismic',
    'Sledge',
    'Smokey',
    'Strobe',
    'Terra',
    'Tectonic',
    'Thunder'
]
XCOM_MALE_NICKNAMES_HEAVY = [
    'Buster',
    'Kingpin',
    'Kong',
    'Mack',
    'Moose',
    'Nero',
    'Odin',
    'Papa Bear',
    'Tank',
    'Yeti'
]
XCOM_FEMALE_NICKNAMES_HEAVY = [
    'Big Momma',
    'Mama Bear'
]
XCOM_UNISEX_NICKNAMES_SNIPER = [
    'Alpha',
    'Checkmate',
    'Claymore',
    'Cyclops',
    'Deadbolt',
    'Demon',
    'Drifter',
    'Echo',
    'Emo',
    'Enigma',
    'Garrote',
    'Ghost',
    'Hex',
    'Ice',
    'Lockdown',
    'Long Shot',
    'Longbow',
    'Low Rider',
    'Nightmare',
    'Nix',
    'Omega',
    'Shadow',
    'Snapsight'
    'Snake Eyes',
    'Solo',
    'Specter',
    'Spider',
    'Stalker',
    'Vampire',
    'Xeno',
    'Zero',
    'Zulu'
]
XCOM_MALE_NICKNAMES_SNIPER = [
    'Godfather',
    'Loki',
    'Pharaoh',
    'Ranger',
    'Slim',
    'Walker',
    'Warlock',
    'Zed',
    'Zeus'
]
XCOM_FEMALE_NICKNAMES_SNIPER = [
    'Athena',
    'Baroness',
    'Black Widow',
    'Lady Grey',
    'Raven',
    'Witchy'
]
XCOM_UNISEX_NICKNAMES_SUPPORT = [
    'Angel',
    'Axle',
    'Bonus',
    'Cargo',
    'Carrier',
    'Combo',
    'Congo',
    'Doc',
    'Fast Lane',
    'Missionary',
    'Pox',
    'Prophet',
    'Rogue',
    'Saturn',
    'Scarecrow',
    'Scotch',
    'Sentinel',
    'Shield',
    'Skinner',
    'Smokes',
    'Stacks',
    'Strings',
    'Vita',
    'Voodoo',
    'Whiskey'
]
XCOM_MALE_NICKNAMES_SUPPORT = [
    'Ace',
    'Atlas',
    'Bishop',
    'Deacon',
    'Freud',
    'Hitch',
    'Magic Man',
    'Mr. Clean',
    'Padre',
    'Pops',
    'Romeo',
    'Santa'
]
XCOM_FEMALE_NICKNAMES_SUPPORT = [
    'Cookie',
    'Gypsy',
    'Kitty',
    'Pixie',
    'Vixen'
]
XCOM_MALE_NICKNAMES_MEC = [
    'Big Daddy',
    'Bolts',
    'Caliban',
    'Chip',
    'Clank',
    'Data',
    'Deep Teal',
    'Forklift',
    'Golem',
    'Marvin',
    'Murphy',
    'Olivaw',
    'Ratchet',
    'Robby',
    'Ryle',
    'Stick',
    'Sputnik',
    'Talos',
    'Tik-Tok',
    'Tin Can',
    'Vulcan'
]
XCOM_FEMALE_NICKNAMES_MEC = [
    'Beeps',
    'Big Mommy',
    'Freya',
    'Friday',
    'Gadget',
    'Gizmo',
    'Hadaly',
    'Iris',
    'Maya',
    'Molly',
    'Number Six',
    'Orianna',
    'Rosie',
    'Vanessa',
    'Vesta',
]
bradford = ["CLOSE RANGE?!","WHAT HAVE YOU DONE?!","COMMANDER!","WE'RE PICKING UP MULTIPLE CONTACTS!","CURRENT ENEMY STATUS AT THE SITE IS UNKNOWN!"]
VAN_DOORN_QUOTES = [
    "I'm the Ops team!",
    "Only fair if I have all the fun.",
    "Get down there!",
    "Come on! I won't go down without a fight.",
    # "Thank God you're here. I'm still breathing, but I can't say the same for a lot of my boys. Let's get out of here before any more of those things show up.",
    "I don't know what outfit you're from, but I haven't seen gear like that before.",
    "Come on!",
    "I won't go down without a fight!",
    "It's looking bad...for you!",
    "I owe you one."
]

#Soldier names
VAN_DOORN = "Van Doorn"

bbspecies = ["Sectoid"]
sectoidfName = ["Glip","Gleep","Glup","Glorp","Gloop","Glop","Glump","Glerp","Glurp","Glarp"]
sectoidlName = ["Glop","Glarp","Glupple","Glorple","Gloopley","Glopperson","Glep","Glommery"]
thinfName = ["T.","P.","H.","Z.","K.","A.","F.","X.","P.","L.","W.","S.","V."]
thinlName = ["Hinman","Alium","Van Doom","Lmao","Notanalien","Anderson","Smith","Human","Clark","Warzonager","Iper","Thinmint","Mint","Spear","Infiltrator"]
floaterfName = ["Dirk","Ferdinand","Frederick","Algernon","Angus","King","Cornelius","Francis","Christopher","Gustav","Richard","Ivan","Yuri","Vlad"]
floaterlName = ["Meyer","Mleadeer","Peters","Prince","Vos","Wolf","Schwarz","Frank","Miller","Anderssen","Slavolav","Stroganov","Costarov"]

#Aliem names
mutonfName = ["Pooter","Dave","Holk","Billy","Tim","Jeffery","Leeroy","Jimmy","Hank"]
mutonlName = ["Von Mooter","The Muton","Hugan","Jankins","Jefferson","Higgins","Jenkins"]

RANK_ROOKIE = 0
RANK_SQUADDIE = 1
RANK_CORPORAL = 2
RANK_SERGEANT = 3
RANK_LIEUTENANT = 4
RANK_CAPTAIN = 5
RANK_MAJOR = 6
RANK_COLONEL = 7
RANK_GENERAL = 8 # only for Van Doorn
RANK_CENTRAL_OFFICER = 9 # only for Bradford
XCOM_RANKS = [
    'Rookie',
    'Squaddie',
    'Corporal',
    'Sergeant',
    'Lieutenant',
    'Captain',
    'Major',
    'Colonel',
    # Special ranks
    'General',
    'Central Officer'
]
ALIEN_RANKS = [
    "Peon",
    "Guard",
    "Soldier",
    "Trooper",
    "Warrior",
    "Officer",
    "Commander",
    "Elite",
    "Uber"
]

#when a soldier shoots at an alien
retort = ("Suck on this!","Eat this!","Pick on someone your own size!","Take this!","Welcome to Earth!","AAGGHH!!!","HYAAA!")

#human weapons + items
items = {0:"Frag Grenade",1:"Nano Serum",2:"Scope",3:"Alien Grenade",999:"None"}
drops = {0:"Frag Grenade",1:"Nano Serum",2:"Alien Grenade",3:"Light Plasma Rifle",4:"Plasma Rifle"}

apowers = {0: "Mindfray",1: "Psi Boost"}
aitems = {0:"Alien Grenade",1:"Alloy Plating",2:"Focus Lens",999:"None"}
#aliem weapons, items and powers

pod = []
room = []
roomNo = -0

fragments = 0
elerium = 0
meld = 0
alloy = 0

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


class Weapon:
    '''Base class for all weapon classes'''

    def __init__(self, name, damage, clip_size):
        self.name = name
        self.damage = damage
        self.clip_size = clip_size
        self.ammo = clip_size

    def reload(self):
        self.ammo = self.clip_size

    def shoot(self):
        if (self.ammo == 0):
            print('Out of ammo')
            return 0
        self.ammo -= 1
        return self.damage + rd.randrange(-1, 2)


class AlienWeapon(Weapon):
    '''Base class for alien weapons'''

    def __init__(self, name, damage, clip_size, elerium, fragments):
        super().__init__(name, damage, clip_size)
        self.elerium = elerium
        self.fragments = fragments

    def get_materials(self):
        '''Returns the amount of elerium and weapon fragments retrieved from this weapon'''

        return self.elerium, self.fragments


class BallisticPistol(Weapon):
    def __init__(self):
        super().__init__('Ballistic Pistol', 2, 10)


class Autopistol(Weapon):
    def __init__(self):
        super().__init__('Autopistol', 2, 10)


class PlasmaPistol(Weapon):
    def __init__(self):
        super().__init__('Plasma Pistol', 3, 10) # TODO: values


class AlloyPistol(Weapon):
    def __init__(self):
        super().__init__('Alloy Pistol', 4, 10) # TODO: values


class BallisticCarbine(Weapon):
    def __init__(self):
        super().__init__('Ballistic Carbine', 2, 3)


class BallisticRifle(Weapon):
    def __init__(self):
        super().__init__('Ballistic Rifle', 3, 4)


class LaserRifle(Weapon):
    def __init__(self):
        super().__init__('Beam Rifle', 4, 999)


class LaserCarbine(Weapon):
    def __init__(self):
        super().__init__('Beam Carbine', 3, 999)


class PlasmaCarbine(AlienWeapon):
    def __init__(self):
        super().__init__('Light Plasma Rifle', 4, 4, 1, 2)


class PlasmaRifle(AlienWeapon):
    def __init__(self):
        super().__init__('Plasma Rifle', 6, 5, 2, 4)


class BradfordsPistol(Weapon):
    def __init__(self):
        super().__init__("Bradford's Pistol", 5, 999)


class Unit:
    def __init__(self, hp, aim, mobility, nrank, firstname, lastname,
                 armour, weapon, items, mods):
        self.hp = hp
        self.aim = aim
        self.mobility = mobility
        self.nrank = nrank
        self.firstname = firstname
        self.lastname = lastname
        self.weapon = weapon
        self.items = items
        self.cover = 0
        self.overwatch = False
        self.alive = True
        self.mods = []

    def reload(self):
        self.weapon.reload()

    def shoot(self):
        return self.weapon.shoot()


class Soldier(Unit):
    def __init__(self, sid, sex, hp, aim, mobility, rank, firstname, lastname,
                 armour, weapon, items, mods):
        super().__init__(hp, aim, mobility, rank, firstname, lastname, armour,
                         weapon, items, mods)
        self.sid = sid
        self.sex = sex
        self.xp = 0
        self.aimpenalty = 0
        self.nickname = None
        self.mods = []
        self.hunkerbonus = 0

    def __str__(self):
        middle = ' '
        if self.nickname:
            middle = " '" + self.nickname + "' "
        return XCOM_RANKS[self.nrank] + middle + self.lastname

    def print_summary(self):
        middle = ' '
        if self.nickname:
            middle = " '" + self.nickname + "' "
        p(0, XCOM_RANKS[self.nrank] + ' ' + self.firstname + middle           \
          + self.lastname + ' - ' + str(self.hp) + ' HP' + ' - '              \
          + str(self.aim) + ' Aim'+ ' - ' +str(self.mobility) + ' AP')
        p(0, 'Items: ' + self.weapon.name + ', ' + items[self.items[0]] + ', '\
          + items[self.items[1]])


# Global variables to prevent duplicate hero soldiers
have_bradford = False
have_vdoorn = False


def create_soldier(sid):
    global have_bradford
    global have_vdoorn
    # sid, hp, aim, mobility, rank, firstname, lastname, armour, weapon, items

    items = [(rd.randrange(0, 3)), (rd.randrange(0, 2))]
    mobility = rd.randrange(11, 16)
    armour = 'BDY'
    mods  = []
    if rd.randrange(1,100) < 5:
        if rd.randrange(0, 2) == 0:
            if not have_bradford:
                return Soldier(sid, SEX_MALE, 6, 100, mobility,               \
                               RANK_CENTRAL_OFFICER, '', 'Bradford', armour,  \
                               BradfordsPistol(), items, mods)
        if not have_vdoorn:
            return Soldier(sid, SEX_MALE, 6, 80, mobility, RANK_GENERAL,      \
                           'Peter', VAN_DOORN, armour, BallisticRifle(), items, mods)
    weapon = None
    if rd.randrange(0, 2) == 0:
        weapon = BallisticRifle()
    else:
        weapon = BallisticCarbine()
    sex = None
    if rd.randrange(0, 2) == 0:
        sex = SEX_FEMALE
    else:
        sex = SEX_MALE
    name = None
    if sex == SEX_FEMALE:
        name = rd.choice(XCOM_FEMALE_FIRSTNAME)
    else:
        name = rd.choice(XCOM_MALE_FIRSTNAME)
    return Soldier(sid, sex, rd.randrange(3, 6), rd.randrange(50, 75),        \
                   mobility, RANK_ROOKIE, name, rd.choice(XCOM_LASTNAME),     \
                   armour, weapon, items, mods)


#we define the aliens here. they are initialised as sectoids but this can be changed with the definitions, such
#as thinman(), to convert the alien to a thinman
class Alien(Unit):
    # self, hp, aim, mobility, rank, firstname, lastname, armour, weapon, items
    def __init__(self):
        super().__init__(0, 0, 0, '', '', '', 'BDY', None, [],[])
        self.species = "Sectoid"
        self.firstname = rd.choice(sectoidfName)
        self.aID = len(pod)
        self.lastname = rd.choice(sectoidlName)
        self.nrank = round(rd.randrange(0+round(roomNo/20),2))
        self.hp = 2 + self.nrank
        self.aim = rd.randrange(50, 75) + self.nrank
        self.mobility = rd.randrange(9, 13) + self.nrank
        self.weapon = PlasmaCarbine()
        self.secondary = PlasmaPistol()
        self.item1 = rd.randrange(0,3)
        self.alive = True
    def thinman(self):
        self.ammo = 1
        self.species = "Thin Man"
        self.firstname = rd.choice(thinfName)
        self.aID = len(pod)
        self.lastname = rd.choice(thinlName)
        self.nrank = round(rd.randrange(0, 3))
        self.hp = 3 + self.nrank
        self.aim = rd.randrange(60, 80) + self.nrank
        self.mobility = rd.randrange(12, 15) + self.nrank
        self.item1 = rd.randrange(0,3)
        self.armour = "BDY" #body armour
        self.alive = True
    def floater(self):
        self.ammo = 1
        self.species = "Floater"
        self.firstname = rd.choice(floaterfName)
        self.aID = len(pod)
        self.lastname = rd.choice(floaterlName)
        self.nrank = round(rd.randrange(0 + round(roomNo / 10), 3))
        self.item1 = rd.randrange(0,3)
        self.hp = 4 + self.nrank
        self.aim = rd.randrange(50, 70) + self.nrank
        self.mobility = rd.randrange(12, 15) + self.nrank
        self.armour = "BDY" #body armour
        self.alive = True
    def muton(self):
        self.ammo = 1
        self.species = "Muton"
        self.firstname = rd.choice(mutonfName)
        self.aID = len(pod)
        self.lastname = rd.choice(mutonlName)
        self.nrank = round(rd.randrange(0 + round(roomNo / 10), 3))
        self.item1 = rd.randrange(0,3)
        self.hp = 8 + self.nrank
        self.aim = rd.randrange(50, 60) + self.nrank
        self.mobility = rd.randrange(10, 12) + self.nrank
        self.weapon = PlasmaRifle()
        self.armour = "BDY" #body armour
        self.alive = True
    def refresh(self):
        self.hp += self.nrank * round(rd.random() * 2)
        self.aim  +=  self.nrank * round(rd.random() * 2)

    #gives us names for when we reference the alien in game
    def __str__(self):
        return '(' + self.species + ') ' + ALIEN_RANKS[self.nrank] + ' '      \
               + self.firstname + " " + self.lastname

    #gives us tactical information, like HP and hit chance
    def tactical_info(self, chance):
        return (ALIEN_RANKS[self.nrank] + ' ' + self.firstname + ' '          \
                + self.lastname + ' - ' + str(self.hp) + ' HP - '             \
                + str(chance) + '%')


#scatters the aliens in a room, some won't find any cover.
def scatter(roomNo):
    cover = ["Full","Full","Full","Half","Half","Half","Half","Half","Half","No"]
    covernumber = [40,40,40,20,20,20,20,20,20,-10]
    for i in range(len(room[roomNo])):
        room[roomNo][i].cover = rd.choice(covernumber)
        if not room[roomNo][i].cover == -10:
            p(0, str(room[roomNo][i]) + ' moves to '                          \
              + cover[covernumber.index(room[roomNo][i].cover)] + ' cover!')
        else:
            p(0, str(room[roomNo][i]) + " can't find any cover!")


#could probably be merged in with scatter(). Tells you that you've seen an alien
def checkspot(roomNo):
    for i in range(len(room[roomNo])):
        p(0, str(room[roomNo][i]) + ' spotted!')


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
    soldier.hunkerbonus = 0
    while AP > 0 and soldier.alive == True: #while the player has spare action points left
        p(0,"HP - "+str(soldier.hp))
        p(0,"AP - "+str(AP))
        #displays stats
        if len(room[roomNo]) == 0:
            p("1","Advance")
            if AP > 7 and soldier.weapon.ammo < soldier.weapon.clip_size:
                p("2","(8AP) Reload")
            while out == False:
                action = a("int","#")
                #until they enter valid text, see a(form,q) for more information
            out = False
            if action == "1":
                if soldier.lastname == "Bradford":
                    p(spk, "Commander! I advise you to reconsider!")
                elif soldier.lastname == VAN_DOORN:
                    p(spk, "I'll get over there!")
                else:
                    p(spk, "Roger that, moving up!")
                AP -= 1 #this is redundant because AP is reset the next room anyway
                roomNo += 1
                if not "Drop Zone" in room[roomNo]:
                    checkspot(roomNo)
                    scatter(roomNo)
                    if rd.randrange(0,100) < 30:
                        p(0, str(soldier) + ' is in FULL cover.')
                        soldier.cover = 40
                    else:
                        p(0, str(soldier) + ' is in HALF cover.')
                        soldier.cover = 20
                    playerTurn()

                else:                   
                    p(spk,"Reached an access point, Commander. Requesting additional goods!")
                    p(spk,"We only have a short time before the aliens close it off!")
                    AP = 60
                    while AP != 0:
                        print("Fragments:",fragments)
                        print("Elerium:",elerium)
                        print("Meld:",meld)
                        print("Alloy:",alloy)
                        displayShop()
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
                        if sel == "AimBonus":
                            soldier.mods.append("Aim")
                            soldier.aim += 5
                            meld -= 15
                            AP -= 60
                            print("Depth Perception Insta-Genemod applied!")
                        elif sel == "HPBonus":
                            soldier.mods.append("HP")
                            soldier.hp += 5
                            meld -= 20
                            AP -= 60
                            print("Muscle Regeneration Insta-Genemod applied!")
                        elif sel == "APBonus":
                            soldier.mods.append("HP")
                            soldier.mobility += 2
                            meld -=15
                            AP -= 60
                            print("Micro Servomotors Augment inserted!")
                        elif sel == "NadeBonus":
                            soldier.mods.append("Nade")
                            soldier.item.append(0)
                            soldier.item.append(0)
                            meld -= 20
                            AP -= 60
                            print("Grenade Launcher Augment inserted!")
                        elif sel == "LaserRifle":
                            soldier.weapon = LaserRifle()
                            fragments -= 40
                            elerium -= 20
                            AP -= 40
                            print("Beam Rifle fabricated!")
                        elif sel == "LaserCarbine":
                            soldier.weapon = LaserCarbine()
                            fragments -= 20
                            elerium -= 10
                            AP -= 40
                            print("Beam Carbine fabricated!")
                        elif sel == "Frag":
                            soldier.items.append(0)
                            alloy -= 4
                            fragments -= 20
                            AP -= 20
                            print("Frag Grenade fabricated!")
                        elif sel == "Meds":
                            soldier.items.append(1)
                            meld -= 10
                            fragments -= 10
                            AP -= 20
                            print("Nano Serum fabricated!")
                        elif sel == "Reload":
                            soldier.weapon.ammo = soldier.weapon.clip_size
                            AP -= 20
                            print("Weapon reloaded!")
                        elif sel == "Heal":
                            soldier.hp += 1
                            AP -= 20
                            print("Healed 1HP!")
                        elif sel == "Advance":
                            AP = 0
                    p(spk,"All out of time! I'll have to keep moving!")
                    roomNo += 1
                    checkspot(roomNo)
                    scatter(roomNo)
                    playerTurn()
                        
            if action == "2":
                if AP > 7:
                    soldier.reload()
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
                soldier.reload()
                #depending on what weapon the player has, they will get a certain amount of ammo
                AP -= 8
            if sel == "Overwatch":
                if soldier.lastname == "Bradford":
                    p(spk, "Keep your eyes peeled!")
                elif soldier.lastname == VAN_DOORN:
                    p(spk, "You coming down here or what?")
                else:
                    p(spk, "Got it, on Overwatch.")
                soldier.overwatch = 1
                AP = 0
            if sel == "End Turn":
                AP = 0
            if sel == "Reposition":
                AP -= 3
                if soldier.lastname == "Bradford":
                    p(spk, "Moving to...wait...that's CLOSE RANGE!")
                elif soldier.lastname == VAN_DOORN:
                    p(spk, "Come on! I won't go down without a fight.")
                else:
                    p(spk, "Moving to Full cover!")
                checkForOverwatch("Alium",0)
                soldier.cover = 40

                #if any aliens are on overwatch, check and be shot at if they are

                if rd.randrange(0,100) < 50:
                    alium = rd.choice(room[roomNo])
                    p(0, str(alium) + ' is flanked!')
                    alium.cover = 0
                #chance to flank an alien

            if sel == "Meds":
                AP -= 10
                print("HP restored.")
                soldier.hp += 4
                soldier.items.pop(soldier.items.index(1))
                #heals soldier but consumes the item
            if sel == "Hunker Down":
                soldier.overwatch = 0
                soldier.hunkerbonus = 20
                p(spk,"Taking cover!")
                AP = 0
                #provides extra cover to soldier
            if sel in room[roomNo]: #if sel is an Alien() pointer
                AP -= 6
                damage = soldier.shoot()
                if soldier.lastname == "Bradford":
                    p(spk, rd.choice(bradford))
                elif soldier.lastname == VAN_DOORN:
                    p(spk, rd.choice(VAN_DOORN_QUOTES))
                else:
                    p(spk, rd.choice(retort))
                if type(soldier.weapon) is BallisticCarbine \
                   or type(soldier.weapon) is BallisticRifle:
                    p(0,"*Dakkadakkadakka!*")
                elif type(soldier.weapon) is LaserCarbine \
                   or type(soldier.weapon) is LaserRifle:
                    p(0,"*Zzzaaaaaap!*")
                elif type(soldier.weapon) is BradfordsPistol:
                    p(0,"*Bang!*")
                else:
                    p(0,"*Whap-whap-whap!*")
                chance = (soldier.aim)-(sel.cover)
                if 2 in soldier.items: #scope
                    chance += 0
                # Carbines get an aim bonus
                if type(soldier.weapon) is BallisticCarbine \
                   or type(soldier.weapon) is PlasmaCarbine \
                   or type(soldier.weapon) is LaserCarbine:
                    chance += 10
                roll = rd.randrange(0,100)
                if roll <= chance+10:
                    sel.hp -= damage
                    p(0,str(damage)+" damage!")
                    fragments += getLoot(sel)[0]
                    elerium += getLoot(sel)[1]
                    meld += getLoot(sel)[2]
                    alloy += getLoot(sel)[3]
                    checkDead(sel)
                else:
                    p(0,"Missed!")
            elif sel == "Frag":
                AP -= 10
                p(0,"*BAM!*")
                #grenade, obviously
                soldier.items.pop(soldier.items.index(0))
                affected = room[roomNo]
                for i in range(len(affected)+1):
                    try:
                        alium = affected[i]
                        alium.hp -= 2
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
                soldier.items.pop(soldier.items.index(3))
                affected = room[roomNo]
                for i in range(len(affected)+1):
                    try:
                        alium = affected[i]
                        alium.hp -= 4
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


def displayShop():
    global fragments
    global elerium
    global meld
    global alloy
    global invac
    global invacref
    global AP
    invac = []
    invacref = []
    print("Time: "+str(AP))
    invac.append("Advance")
    p(len(invac),"Advance")
    if AP == 60:
        if meld >= 15:
            if not "Aim" in soldier.mods:
                invac.append("AimBonus")
                p(len(invac),"(60 Time) (15m) Insta-Genemod: Depth Perception (+5 aim)")
            if not "AP" in soldier.mods:
                invac.append("APBonus")
                p(len(invac),"(60 Time) (15m) Micro-Augment: Reflex Servomotors (+2 AP)")
            invac.append("")
        if meld >= 20:
            if not "HP" in soldier.mods:
                invac.append("HPBonus")
                p(len(invac),"(60 Time) (20m) Insta-Genemod: Muscle Regeneration (+5 HP)")
            if not "Nade" in soldier.mods:
                invac.append("NadeBonus")
                p(len(invac),"(60 Time) (20m) Micro-Augment: Grenade Launcher (+2 Frag Grenades)")
    if AP >= 50:
        if not type(soldier.weapon) is LaserRifle() and elerium >= 20 and fragments >= 40:
            invac.append("LaserRifle")
            p(len(invac),"(40 Time) (20e) (40f) Get Laser Rifle")
            print("     (~4dmg), infinite ammo")
        if not type(soldier.weapon) is LaserCarbine() and elerium >= 10 and fragments >= 30:
            invac.append("LaserCarbine")
            p(len(invac),"(40 Time) (10e) (30f) Get Laser Carbine")
            print("     (~3dmg), infinite ammo, +10% aim")
    if AP >= 30:
        if meld >= 10 and fragments >= 10:
            invac.append("Meds")
            p(len(invac),"(30 Time) (10m) (10f) Get Nano Serum")
        if alloy >= 4 and fragments >= 20:
            invac.append("Frag")
            p(len(invac),"(30 Time) (20f) (4a) Get Frag Grenade")
    if AP >= 20:
        if meld >= 5:
            invac.append("Heal")
            p(len(invac),"(20 Time) (5m) Recuperate (+1 HP)")
        invac.append("Reload")
        p(len(invac),"(20 Time) Reload Weapon")
    invac.append("Skip")
    p(len(invac),"("+str(AP)+" Time) Advance (Skip this Drop Zone)")


def checkForOverwatch(who,getalium):
    if who == "Alium": #if it's an alien shooting at soldier
        for i in range(len(room[roomNo])):
            alium = room[roomNo][i]
            cthplayer = alium.aim - soldier.cover + 10
            if alium.overwatch == 1:
                p(0, str(alium) + ' reacts!')
                if alium.item1 == 2:
                    cthplayer += 10
                if rd.randrange(0,100) < cthplayer:
                    dmg = alium.shoot()
                    p(0,str(dmg)+" damage!")
                    soldier.hp -= dmg
                    checkPlayerDead()
                    #did it kill the player?
                else:
                    p(0," Missed!")
                alium.overwatch = 0
    else: #if a soldier is shooting at an alien
        alium = getalium
        cth = soldier.aim - alium.cover + 10
        if soldier.overwatch == 1:
                p(0, str(soldier) + ' reacts!')
                dmg = soldier.shoot()
                if 2 in soldier.items:
                    cth += 10
                if rd.randrange(0,100) < cth:
                    p(0,str(dmg)+" damage!")
                    alium.hp -= dmg
                    checkDead(alium)
                else:
                    if soldier.lastname == "Bradford":
                        p(spk,"How did I miss that?!")
                    else:
                        p(spk,"Shot failed to connect!")
                soldier.overwatch = 0


def fire(alium,cthplayer):
    if alium.alive == True:
        if cthplayer > 0:
            p(0, str(alium) + ' fires at ' + str(soldier) + '(' + str(cthplayer) + '%)')
            dmg = alium.shoot()
            if rd.randrange(0,100) < cthplayer:
                p(0,str(dmg)+" damage!")
                soldier.hp -= dmg
                checkPlayerDead()
                #did you kill the player, alien?
            else:
                p(0,"Missed!")
        else:
            if rd.randrange(0,100) < 80:
                ow(alium)
            else:
                if alium.item1 == 0:
                    nade(alium)


def nade(alium):
    if alium.alive == True:
        if alium.item1 == 0:
            p(0, str(alium) + ' uses Alien Grenade!')
            p(0,"**BLAM!**")
            alium.item1 = 999
            #sets the aliens item to 'none', no more grenades for you
            p(0,"3 damage!")
            soldier.cover = 20
            soldier.hp -= 3
            checkPlayerDead()


def ow(alium):
    if alium.alive == True:

        p(0, str(alium) + ' went on overwatch!')
        alium.overwatch = 1


def move(alium,cover):
    if alium.alive == True:
        if cover == 40:
            p(0, str(alium) + ' runs to Full cover!') #if an alien has no cover, it will run to full cover. same goes if it's flanked
        elif cover == 20:
            p(0, str(alium) + ' runs to Half cover!')
        checkForOverwatch("Soldier",alium)
        alium.overwatch = False
        alium.cover = cover


def alienTurn():
    for i in range(len(room[roomNo])):
        try:
            alium = room[roomNo][i]
        except ( Exception ):
            i = 0
        #because something may have happened that causes an index error
        if alium.alive == True and soldier.alive == True:
            cthplayer = (alium.aim - soldier.cover) - soldier.hunkerbonus
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
                if cthplayer > 50 + rd.randrange(0,20):
                    fire(alium,cthplayer)
                elif rd.randrange(0,100) < 20:
                    if alium.item1 == 0:
                        nade(alium)
                    else:
                        fire(alium,cthplayer)
                elif rd.randrange(0,100) < 20:
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
                if cthplayer > 30 + rd.randrange(0,20):
                    fire(alium,cthplayer)
                elif rd.randrange(0,100) < 80:
                    move(alium,20)
                else:
                    ow(alium)


def checkDead(alium):
    if alium.hp <= 0:
        p(0, str(alium) + ' died!')
        getLoot(alium)
        drop()
        checkXP()
        alium.alive = False
        room[roomNo].pop(room[roomNo].index(alium))
        #kills, loots and removes the alien from the game


def checkPlayerDead():
    if soldier.hp <= 0:
        p(0, str(soldier) + ' was killed!')
        if not soldier.lastname == "Bradford":

            p("Bradford","Commander, our unit was killed.")
            p("Bradford","We were able to recover some materials, however.")
            print("Fragments:",fragments)
            print("Elerium:",elerium)
            print("Meld:",meld)
            print("Alloy:",alloy)
            print('Total Score: ' + str(fragments + elerium + meld + alloy        \
                                 + soldier.xp + roomNo))
        else:
            p("Council Member","Commander...you 'volunteered' your Central Officer to fight on the front lines.")
            p("Council Member","This was a foolish endeavour, and as a result, you lost him.")
            print('Monthly Rating: F')
            p("Council Member","We have negotiated...a deal with the aliens, and so...your services are no longer required.")
            p("Council Member","We are...terminating the XCOM Project, effective...immediately.")


        soldier.alive = False
        quit
        #doesn't want to stop the whole game straight away for some reason


#levels up
def checkXP():
    was_promoted = False
    if soldier.xp >= 25 and soldier.nrank < RANK_SQUADDIE:
        soldier.nrank = RANK_SQUADDIE
        soldier.hp += 1
        soldier.aim += 2
        soldier.mobility += 1
        drop()
        drop()
        was_promoted = True
    elif soldier.xp >= 100 and soldier.nrank < RANK_CORPORAL:
        soldier.nrank = RANK_CORPORAL
        soldier.hp += 1
        soldier.aim += 2
        soldier.mobility += 1
        drop()
        drop()
        was_promoted = True
    elif soldier.xp >= 300 and soldier.nrank < RANK_SERGEANT:
        nicknames = XCOM_UNISEX_NICKNAMES_ASSAULT                             \
                    + XCOM_UNISEX_NICKNAMES_HEAVY                             \
                    + XCOM_UNISEX_NICKNAMES_SNIPER                            \
                    + XCOM_UNISEX_NICKNAMES_SUPPORT
        if soldier.sex == SEX_FEMALE:
            nicknames += XCOM_FEMALE_NICKNAMES_ASSAULT                        \
                         + XCOM_FEMALE_NICKNAMES_HEAVY                        \
                         + XCOM_FEMALE_NICKNAMES_MEC                          \
                         + XCOM_FEMALE_NICKNAMES_SNIPER                       \
                         + XCOM_FEMALE_NICKNAMES_SUPPORT
        else:
            nicknames += XCOM_MALE_NICKNAMES_ASSAULT                          \
                         + XCOM_MALE_NICKNAMES_HEAVY                          \
                         + XCOM_MALE_NICKNAMES_MEC                            \
                         + XCOM_MALE_NICKNAMES_SNIPER                         \
                         + XCOM_MALE_NICKNAMES_SUPPORT
        soldier.nickname = rd.choice(nicknames)
        p(0, XCOM_RANKS[soldier.nrank] + ' ' + soldier.firstname + ' '        \
          + soldier.lastname  + " earned the nickname '" + soldier.nickname   \
          + "'")
        soldier.nrank = RANK_SERGEANT
        soldier.hp += 2
        soldier.aim += 1
        soldier.mobility += 1
        drop()
        drop()
        was_promoted = True
    elif soldier.xp >= 900 and soldier.nrank < RANK_LIEUTENANT:
        soldier.nrank = RANK_LIEUTENANT
        soldier.hp += 1
        soldier.aim += 1
        drop()
        drop()
        was_promoted = True
    elif soldier.xp >= 1500 and soldier.nrank < RANK_CAPTAIN:
        soldier.nrank = RANK_CAPTAIN
        soldier.hp += 2
        soldier.aim += 1
        drop()
        drop()
        drop()
        drop()
        was_promoted = True
    elif soldier.xp >= 2000 and soldier.nrank < RANK_MAJOR:
        soldier.nrank = RANK_MAJOR
        soldier.hp += 1
        soldier.aim += 1
        soldier.mobility += 1
        drop()
        drop()
        drop()
        was_promoted = True
    elif soldier.xp >= 3000 and soldier.nrank < RANK_COLONEL:
        soldier.nrank = RANK_COLONEL
        soldier.hp += 1
        soldier.aim += 1
        drop()
        drop()
        drop()
        drop()
        drop()
        drop()
        was_promoted = True
    if was_promoted:
        p(0, str(soldier) + ' was promoted to ' + XCOM_RANKS[soldier.nrank])


#gets some sweet sweet loot from those aliens
def getLoot(alium):
    fragments = 0
    elerium = 0
    meld = 0
    alloy = 0
    soldier.xp += alium.nrank * abs(alium.hp)
    fragments += abs(alium.hp)
    elerium += alium.nrank
    meld += 2 * alium.nrank
    if alium.item1 == 0:
        elerium += 2
    elif alium.item1 == 1:
        alloy += 2
    elif alium.item1 == 2:
        fragments += 2
    e, f = alium.weapon.get_materials()
    elerium += e
    fragments += f
    return [fragments, elerium, meld, alloy]


def displayOptions():
    global invac
    global invacref
    global AP
    invac = []
    invacref = []

    if soldier.weapon.ammo != 0:
        if AP > 5:
            saywep = '(~{}dmg)(6AP) Fire {}'.format(soldier.weapon.damage, soldier.weapon.name)
            for i in range(len(room[roomNo])):
                alium = room[roomNo][i]
                chance = (soldier.aim)-(alium.cover)
                if 2 in soldier.items:
                    chance += 10
                if 1 in soldier.items:
                    chance += 10
                if chance < 0:
                    chance = 5
                if chance > 100:
                    chance = 95
                invac.append(alium)
                p(len(invac), saywep + ' : ' + alium.tactical_info(chance))
                #displays a list of valid targets
        invac.append("Overwatch")
        p(len(invac),"Overwatch")
    else:
        if AP > 7 and soldier.weapon.ammo < soldier.weapon.clip_size:
            invac.append("Reload")
            p(len(invac),"(8AP) Reload Weapon")
    if 0 in soldier.items:
        if AP > 9:
            invac.append("Frag")
            p(len(invac),"(2dmg)(10AP) Throw Frag Grenade")
    if 3 in soldier.items:
        if AP > 14:
            invac.append("AlienFrag")
            p(len(invac),"(4dmg)(15AP) Throw Alien Grenade")
    if 1 in soldier.items:
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
    if rd.randrange(1,100) <= 5:
        p(spk,"Recovered a "+drops[itemdrop]+"!")
        if itemdrop == 3:
            soldier.weapon = PlasmaCarbine()
        if itemdrop == 4:
            soldier.weapon = PlasmaRifle()
        else:
            soldier.items.append(itemdrop)

def mutate(i):
    if i <= 3:
        pass
    elif i > 3 and i < 10:
        y = options[rd.randrange(0,2)]
        if y == "Thinman":
            x.thinman()
        x.nrank += 1
        x.refresh()
    elif i > 9 and i < 15:
        y = rd.choice(options)
        if y == "Thinman":
            x.thinman()
        if y == "Floater":
            x.floater()
        if y == "Muton":
            x.muton()
            x.nrank -= 2
        x.nrank += 3
        x.refresh()
    elif i > 14:
        y = options[rd.randrange(1,4)]
        if y == "Thinman":
            x.thinman()
        if y == "Floater":
            x.floater()
        if y == "Muton":
            x.muton()
        x.nrank += 4
        x.refresh()
    elif i > 16:
        y = options[rd.randrange(2,4)]
        if y == "Muton":
            x.muton()
        if y == "Floater":
            x.floater()
        x.nrank += 4
        x.refresh()


# def main():
p("Bradford", "Welcome Commander. We've discovered an Alien Base, and it's your job to send someone out to deal with it.")
p("Bradford", "Choose a soldier from the 3 below to go on the mission.")

#generates soldiers
for i in range(3):
    x = create_soldier(i)
    barracks.append(x)

#displays a list of the soldiers
for i in range(len(barracks)):
    p(0,str(i+1)+": ")
    barracks[i].print_summary()
    p(0,"")

#forces you to pick only one soldier
while out == False and int(out) < len(barracks):
    soldier = a("int","#")
    out = True
out = False
soldier = barracks[int(soldier)-1]

spk = soldier.firstname + " " + soldier.lastname
if soldier.lastname == "Bradford":
    p(spk, "What? There must have been a mistake on the sheet, Commander! You can't send --")
elif soldier.lastname == VAN_DOORN:
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
x.nrank = 8
x.refresh()
x.hp = 50

#generates the pods in each room
room.append([])
room[31] = []
room[5] = ["Drop Zone"]
room[10] = ["Drop Zone"]
room[15] = ["Drop Zone"]
room[20] = ["Drop Zone"]

roomNo = 0
AP = soldier.mobility

#game loop, runs until your soldier is killed
while soldier.alive == True:
    try:
        playerTurn()
        p(0, str(soldier) + ' is out of AP!')
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
