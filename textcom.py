#By /u/TachyonNZ
# Van Doorn by /u/net_goblin
#TEXT-COM, V0.1

import random as rd
import time as tm

########################################################################
# constants                                                            #
########################################################################

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
    'Murray',
    'James',
    'Ethan',
    'Micah',
    'Michael',
    'Mike',
    'Jason',
    'Sam',
    'Reuben'
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
    'Chell',
    'Lexi'
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
    'Scott',
    'Mars',
    'Smith',
    'Connors',
    'Hunt',
    'Bond',
    'Miller',
    'Zhu',
    'Zhang',
    'Li'

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
BRADFORD_RETORTS = [
    'CLOSE RANGE?!',
    'WHAT HAVE YOU DONE?!',
    'COMMANDER!',
    "WE'RE PICKING UP MULTIPLE CONTACTS!",
    'CURRENT ENEMY STATUS AT THE SITE IS UNKNOWN!'
]
VAN_DOORN_RETORTS = [
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
drops = {0:"Frag Grenade",1:"Nano-Serum",2:"Alien Grenade",3:"Light Plasma Rifle",4:"Plasma Rifle"}

#aliem weapons, items and powers
apowers = {0: "Mindfray",1: "Psi Boost"}

#########
# Cover #
#########

COVER_FLANKED = -20
COVER_NONE = 0
COVER_FULL = 40
COVER_HALF = 20

#######
# Map #
#######

NUMBER_OF_ROOMS = 31

########################################################################
# Legacy stuff to be removed                                           #
########################################################################

# to be removed
pod = []
room = [[]]
roomNo = -0

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


########################################################################
# weapon classes                                                       #
########################################################################

class Weapon:
    '''Base class for all weapon classes'''

    def __init__(self, name, damage, clip_size,crit_chance):
        self.name = name
        self.damage = damage
        self.clip_size = clip_size
        self.ammo = clip_size
        self.crit_chance = crit_chance

    def get_sound(self):
        '''Sound interface method'''
        pass

    def reload(self):
        self.ammo = self.clip_size
        s(0.5)

    def shoot(self):
        s(0.5)
        print(self.get_sound())
        s(0.5)
        if (self.ammo == 0):
            print('Out of ammo')
            return 0
        self.ammo -= 1
        return self.damage + rd.randrange(-1, 2)

class AlienWeapon(Weapon):
    '''Base class for alien weapons'''

    def __init__(self, name, damage, clip_size, elerium, fragments,crit_chance):
        super().__init__(name, damage, clip_size,crit_chance)
        self.elerium = elerium
        self.fragments = fragments

    def get_materials(self):
        '''Returns the amount of elerium and weapon fragments retrieved from this weapon'''

        return self.elerium, self.fragments


class BallisticPistol(Weapon):
    def __init__(self):
        super().__init__('Ballistic Pistol', 2, 10,5)

    def get_sound(self):
        return '*Dak*'


class Autopistol(Weapon):
    def __init__(self):
        super().__init__('Autopistol', 2, 10,5)

    def get_sound(self):
        return '*Dakdakdak*'


class PlasmaPistol(AlienWeapon):
    def __init__(self):
        super().__init__('Plasma Pistol', 2, 10,1,1,5)

    def get_sound(self):
        return '*Whap*'


class AlloyPistol(Weapon):
    def __init__(self):
        super().__init__('Alloy Pistol', 4, 10,5)

    def get_sound(self):
        return '*Kchak!*'


class BallisticCarbine(Weapon):
    def __init__(self):
        super().__init__('Ballistic Carbine', 2, 3,15)

    def get_sound(self):
        return '*Dakkadakka!*'


class BallisticRifle(Weapon):
    def __init__(self):
        super().__init__('Ballistic Rifle', 3, 4,10)

    def get_sound(self):
        return '*Dakkadakkadakka!*'


class LaserCarbine(Weapon):
    def __init__(self):
        super().__init__('Beam Carbine', 3, 999,20)

    def get_sound(self):
        return '*Zzaap!*'


class LaserRifle(Weapon):
    def __init__(self):
        super().__init__('Beam Rifle', 4, 999,15)

    def get_sound(self):
        return '*Zzzaaaaaap!*'


class PlasmaCarbine(AlienWeapon):
    def __init__(self):
        super().__init__('Light Plasma Rifle', 4, 4, 1, 2, 15)

    def get_sound(self):
        return '*W-W-Whap!*'


class PlasmaRifle(AlienWeapon):
    def __init__(self):
        super().__init__('Plasma Rifle', 6, 5, 2, 4, 10)

    def get_sound(self):
        return '*Whap-whap-whap!*'


class BradfordsPistol(Weapon):
    def __init__(self):
        super().__init__("Bradford's Pistol", 5, 999, 30)

    def get_sound(self):
        return '*Bang!*'

########################################################################
# item classes                                                         #
########################################################################

class Item:
    '''Base class for items

    Items with an `use_ap_costs` of 0 are passive items.
    '''

    def __init__(self, name, use_ap_costs, effect_descr, key = ""):
        self.name = name
        self.use_ap_costs = use_ap_costs
        self.effect_descr = effect_descr
        self.action_key = key

    def use(self, soldier):
        '''Interface method for active items'''
        pass


class Explosive(Item):
    def __init__(self, name, use_ap_costs, damage, sound_descr, key):
        super().__init__(name, use_ap_costs, '{} dmg'.format(damage), key)
        self.damage = damage
        self.sound_descr = sound_descr

    def use(self, soldier):
        global alloy
        global elerium
        global fragments
        global meld
        global roomNo

        p(0, self.sound_descr)
        #the grenade only affects some of the aliens in the room, but is guaranteed to hit at least 1
        #it's not a bug, it's a feature
        affected = room[roomNo]
        for i in range(len(affected) + 1):
            try:
                alien = affected[i]
                alien.hp -= self.damage
                alien.cover = COVER_NONE
                fragments += getLoot(alien)[0]
                elerium += getLoot(alien)[1]
                meld += getLoot(alien)[2]
                alloy += getLoot(alien)[3]
                alien.check_death()
            except (IndexError):
                i = 0 #reset the loop


class Medkit(Item):
    def __init__(self):
        super().__init__('Nano-Serum', 10, '+4 HP', 's')

    def use(self, soldier):
        print("HP restored.")
        soldier.hp += 4

# XCOM items
ITEM_SCOPE = Item('Scope', 0, 'Increases aim')
ITEM_FRAG_GRENADE = Explosive('Frag Grenade', 10, 2, 'BAM!', 'g')
ITEM_ALLOY_PLATING = Item('Alloy Plating', 0, 'Increases defense')
ITEM_MEDKIT = Medkit()

# Alien items
# Alien grenade is also available to XCOM
ITEM_ALIEN_GRENADE = Explosive('Alien Grenade', 15, 4, '**BLAM**!', 'G')

########################################################################
# unit classes                                                         #
########################################################################

class Unit:
    def __init__(self, hp, aim, mobility, nrank, firstname, lastname,
                 armour, weapon, items, mods):
        self.hp = hp
        self.aim = aim
        self.mobility = mobility
        self.nrank = nrank
        self.firstname = firstname
        self.lastname = lastname
        self.armour = armour
        self.weapon = weapon
        self.items = items
        self.mods = mods
        self.cover = 0
        self.on_overwatch = False
        self.alive = True

    def _handle_overwatch(self, target):
        '''
        Generic overwatch handler which shoots at the target
        '''
        chance = self.aim_at(target)
        return self.shoot_at(target, chance,10)

    def aim_at(self, target):
        hit_chance = self.aim - target.cover
        if ITEM_SCOPE in self.items:
            hit_chance += 10
        # Carbines get an aim bonus
        if type(self.weapon) is BallisticCarbine                              \
           or type(soldier.weapon) is LaserCarbine                            \
           or type(self.weapon) is PlasmaCarbine:
            hit_chance += 10
        if hit_chance < 0:
            hit_chance = 5
        if hit_chance > 100:
            hit_chance = 95
        return hit_chance

    def check_death(self):
        '''
        Check for unit death and call death handler, if unit is dead.

        If the unit is not dead, `False` is returned and nothing
        happens, else the `_handle_death` method implemented by the
        subclass is called.
        '''
        if self.hp <= 0:
            self._handle_death()
            return True
        return False

    def overwatch(self, target):
        '''
        Perform overwatch reaction if unit is on overwatch.

        If the unit is on overwatch, the `_handle_overwatch` method is
        called (overwrite this to customize the overwatch handling) and
        `True` is returned, else `False` is returned and nothing
        happens.
        '''
        if self.on_overwatch:
            self.on_overwatch = False
            p(0, str(self) + ' reacts!')
            self._handle_overwatch(target)
            return True
        return False

    def reload(self):
        self.weapon.reload()

    def shoot_at(self, target, chance, situation_modificator=0):
        '''
        Perform an attack at the target

        Returns `True` if the target was hit, `False` otherwise.  If the
        target was hit, hit points are discounted and the death check is
        performed.
        '''
        crit = self.getCrit(target)
        
        if rd.randrange(0, 100) < chance:
            if rd.randrange(0, 100) < crit:
                p(0, "CRITICAL!")
                damage = self.weapon.shoot()+rd.randint(3,5)
                p(0, str(damage) + ' damage!')
                target.hp -= damage
                target.check_death()
            else:
                damage = self.weapon.shoot()
                p(0, str(damage) + ' damage!')
                target.hp -= damage
                target.check_death()
            return True
        else:
            self.weapon.ammo -= 1
            s(0.5)
            print(self.weapon.get_sound())
            s(0.5)
            p(0, ' Missed!')
        self.on_overwatch = False
        return False
    
    def getCrit(self, target):
        return self.weapon.crit_chance - target.cover/4


class Soldier(Unit):
    def __init__(self, sid, sex, hp, aim, mobility, rank, firstname, lastname,
                 armour, weapon, items, mods):
        super().__init__(hp, aim, mobility, rank, firstname, lastname, armour,
                         weapon, items, mods)
        self.ap = 0
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

    def _handle_death(self):
        soldier.alive = False
        p(0, str(soldier) + ' was killed!')
        if not soldier.lastname == "Bradford":
            p("Bradford", "Commander, our unit was killed.")
            p("Bradford", "We were able to recover some materials, however.")
            print("Fragments:", fragments)
            print("Elerium:", elerium)
            print("Meld:", meld)
            print("Alloy:", alloy)
            print('Total Score: ' + str(fragments + elerium + meld + alloy    \
                                        + soldier.xp + roomNo))
        else:
            p("Council Member",
              "Commander...you 'volunteered' your Central Officer to fight on the front lines.")
            p("Council Member","This was a foolish endeavour, and as a result, you lost him.")
            print('Monthly Rating: F')
            p("Council Member",
              "We have negotiated...a deal with the aliens, and so...your services are no longer required.")
            p("Council Member",
              "We are...terminating the XCOM Project, effective...immediately.")
        quit

    def _handle_overwatch(self, target):
        if super()._handle_overwatch(target) == False:
            p(spk, self.get_overwatch_miss_retort())

    def get_overwatch_confirmation(self):
        return 'Got it, on Overwatch.'

    def get_overwatch_miss_retort(self):
        return 'Shot failed to connect!'

    def get_reposition_confirmation(self):
        return 'Moving to Full cover!'

    def get_retort(self):
        return rd.choice(retort)

    def print_summary(self):
        middle = ' '
        if self.nickname:
            middle = " '" + self.nickname + "' "
        p(0, XCOM_RANKS[self.nrank] + ' ' + self.firstname + middle           \
          + self.lastname + ' - ' + str(self.hp) + ' HP' + ' - '              \
          + str(self.aim) + ' Aim'+ ' - ' +str(self.mobility) + ' AP')
        p(0, 'Items: ' + self.weapon.name + ', ' + self.items[0].name + ', '  \
          + self.items[1].name)


#we define the aliens here. they are initialised as sectoids but this can be changed with the definitions, such
#as thinman(), to convert the alien to a thinman
class Alien(Unit):
    def __init__(self, alien_id, species, hp, aim, mobility, nrank, firstname,\
                 lastname, armour, weapon, items, mods):
        super().__init__(hp, aim, mobility, nrank, firstname, lastname,       \
                         armour, weapon, items, mods)
        self.aid = alien_id
        self.species = species

    #gives us names for when we reference the alien in game
    def __str__(self):
        return '(' + self.species + ') ' + ALIEN_RANKS[self.nrank] + ' '      \
               + self.firstname + " " + self.lastname

    def _handle_death(self):
        #kills, loots and removes the alien from the game
        p(0, str(self) + ' died!')
        getLoot(self)
        drop()
        checkXP()
        self.alive = False
        room[roomNo].pop(room[roomNo].index(self))

    def refresh(self):
        self.hp += self.nrank * round(rd.random() * 2)
        self.aim  +=  self.nrank * round(rd.random() * 2)


SPECIES_RANK_FUNC = 0
SPECIES_HP_BASE = 1
SPECIES_AIM_RANGE = 2
SPECIES_MOBILITY_RANGE = 3
SPECIES_WEAPON_CLASS = 4
SPECIES_FIRSTNAME = 5
SPECIES_LASTNAME = 6

# Species data table, used to construct aliens with the `create_alien`
# function with keywords
# rank function, hp base, aim base range, mobility base range,
#     primary weapon class, firstname table, lastname table
ALIEN_SPECIES = {
    'Sectoid': [
        lambda nroom: round(rd.randrange(round(nroom / 20), 2)),
        2, (50, 75), (9, 13), PlasmaPistol, sectoidfName, sectoidlName
    ],
    'Thinman': [
        lambda nroom: round(rd.randrange(round(nroom / 20), 2)),
        3, (60, 80), (12, 15), PlasmaCarbine, thinfName, thinlName
    ],
    'Floater': [
        lambda nroom: round(rd.randrange(round(nroom / 12), 3)),
        4, (50, 70), (12, 15), PlasmaCarbine, floaterfName, floaterlName
    ],
    'Muton': [
        lambda nroom: round(rd.randrange(round(nroom / 12), 3)),
        8, (50, 60), (10, 12), PlasmaRifle, mutonfName, mutonlName
    ]
}

def create_alien(alien_id, room_index, species, **kwargs):
    '''
    Create a alien with random stats or stats supplied by keywords

    Returns a new alien with the stats read from kwargs, or if the stat
    is not contained in there, random stats according to the
    `ALIEN_SPECIES` table.
    '''
    if species not in ALIEN_SPECIES:
        raise Exception('Unknown alien species')

    # the rank may be used for other values, so it is set differently
    nrank = 0
    if not 'nrank' in kwargs:
        nrank = ALIEN_SPECIES[species][SPECIES_RANK_FUNC](room_index)
        kwargs['nrank'] = nrank
    else:
        nrank = kwargs['nrank']

    if not 'hp' in kwargs:
        kwargs['hp'] = ALIEN_SPECIES[species][SPECIES_HP_BASE] + nrank
    if not 'aim' in kwargs:
        kwargs['aim'] =                                                       \
            rd.randrange(*ALIEN_SPECIES[species][SPECIES_AIM_RANGE]) + nrank
    if not 'mobility' in kwargs:
        kwargs['mobility'] =                                                  \
            rd.randrange(*ALIEN_SPECIES[species][SPECIES_MOBILITY_RANGE])     \
            + nrank
    if not 'firstname' in kwargs:
        kwargs['firstname'] =                                                 \
            rd.choice(ALIEN_SPECIES[species][SPECIES_FIRSTNAME])
    if not 'lastname' in kwargs:
        kwargs['lastname'] =                                                  \
            rd.choice(ALIEN_SPECIES[species][SPECIES_LASTNAME])
    if not 'armour' in kwargs:
        kwargs['armour'] = 'BDY'
    if not 'weapon' in kwargs:
        kwargs['weapon'] = ALIEN_SPECIES[species][SPECIES_WEAPON_CLASS]()
    if not 'items' in kwargs:
        kwargs['items'] = [rd.choice([ITEM_ALIEN_GRENADE,
                                      ITEM_ALLOY_PLATING,
                                      ITEM_SCOPE])
                          ]
    if not 'mods' in kwargs:
        kwargs['mods'] = []

    return Alien(alien_id, species, **kwargs)


###########
# actions #
###########

class Action:
    '''Base class for actions'''

    def __init__(self, soldier, name, ap_costs, ends_turn, key = ''):
        self.soldier = soldier
        self.name = name
        self.ap_costs = ap_costs
        self.ends_turn = ends_turn
        self.action_key = key
    
    def __str__(self):
        return self.name

    def perform(self):
        '''Interface method to perform action'''
        pass

    def _calc_ap(self):
        '''Should be the first thing executed by the perform functions'''
        if self.soldier.ap < self.ap_costs:
            raise Exception("Not enough AP to perform action '{}'".
                            format(self.name))
        if self.ends_turn:
            self.soldier.ap = 0
        else:
            self.soldier.ap -= self.ap_costs


class AdvanceAction(Action):
    def __init__(self, soldier):
        super().__init__(soldier, 'Advance', 1, True, 'a')

    def perform(self):
        global roomNo
        global fragments
        global elerium
        global meld
        global alloy

        self._calc_ap()
        roomNo += 1
        try:
            if not "Drop Zone" in room[roomNo]:
                checkspot(roomNo)
                scatter(roomNo)
            else:
                p(spk,"Reached an access point, Commander. Requesting additional goods!")
                p(spk,"We only have a short time before the aliens close it off!")
                ap = 60
                while ap != 0:
                    print("Fragments:",fragments)
                    print("Elerium:",elerium)
                    print("Meld:",meld)
                    print("Alloy:",alloy)
                    sel = displayShop(ap)

                    if sel == "AimBonus":
                        soldier.mods.append("Aim")
                        soldier.aim += 5
                        meld -= 15
                        ap -= 60
                        print("Depth Perception Insta-Genemod applied!")
                    elif sel == "HPBonus":
                        soldier.mods.append("HP")
                        soldier.hp += 10
                        meld -= 20
                        ap -= 60
                        print("Muscle Regeneration Insta-Genemod applied!")
                    elif sel == "APBonus":
                        soldier.mods.append("HP")
                        soldier.mobility += 2
                        meld -=15
                        ap -= 60
                        print("Micro Servomotors Augment inserted!")
                    elif sel == "NadeBonus":
                        soldier.mods.append("Nade")
                        soldier.item.append(0)
                        soldier.item.append(0)
                        meld -= 20
                        ap -= 60
                        print("Grenade Launcher Augment inserted!")
                    elif sel == "LaserRifle":
                        soldier.weapon = LaserRifle()
                        fragments -= 40
                        elerium -= 20
                        ap -= 40
                        print("Beam Rifle fabricated!")
                    elif sel == "LaserCarbine":
                        soldier.weapon = LaserCarbine()
                        fragments -= 20
                        elerium -= 10
                        ap -= 40
                        print("Beam Carbine fabricated!")
                    elif sel == "Frag":
                        soldier.items.append(ITEM_FRAG_GRENADE)
                        alloy -= 4
                        fragments -= 20
                        ap -= 30
                        print("Frag Grenade fabricated!")
                    elif sel == "Meds":
                        soldier.items.append(ITEM_MEDKIT)
                        meld -= 5
                        fragments -= 5
                        ap -= 30
                        print("Nano Serum fabricated!")
                    elif sel == "Reload":
                        soldier.weapon.ammo = soldier.weapon.clip_size
                        ap -= 20
                        print("Weapon reloaded!")
                    elif sel == "Heal":
                        soldier.hp += 1
                        ap -= 20
                        print("Healed 1HP!")
                    elif sel == "Advance":
                        ap = 0
                    s(.5)
                s(.5)
                p(spk,"All out of time! I'll have to keep moving!")
                s(.5)
                roomNo += 1
                checkspot(roomNo)
                scatter(roomNo)
        except( Exception ):
            pass


class ReloadAdvanceAction(Action):
    def __init__(self, soldier):
        super().__init__(soldier,'Reload + Advance', 9, True, 'd')

    def perform(self):
        reload_action.perform()
        advance_action.perform()


class EndTurnAction(Action):
    def __init__(self, soldier):
        super().__init__(soldier, 'End turn', 0, True, 'e')

    def perform(self):
        self._calc_ap()


class FireAction(Action):
    def __init__(self, soldier, target):
        super().__init__(soldier, 'Fire', 6, False)
        self.target = target
        self.hit_chance = soldier.aim_at(target)

    def __str__(self):
        return '(~{} dmg) Fire {} at {} - {} HP - ({}%)'.\
               format(soldier.weapon.damage, soldier.weapon.name, self.target,\
                      self.target.hp, self.hit_chance)

    def perform(self):
        global alloy
        global elerium
        global fragments
        global meld

        self._calc_ap()
        p(spk, self.soldier.get_retort())
        if self.soldier.shoot_at(self.target, self.hit_chance):
            fragments += getLoot(self.target)[0]
            elerium += getLoot(self.target)[1]
            meld += getLoot(self.target)[2]
            alloy += getLoot(self.target)[3]


class HunkerDownAction(Action):
    def __init__(self, soldier):
        super().__init__(soldier, 'Hunker down', 1, True, 'h')

    def perform(self):
        self._calc_ap()
        if soldier.cover == COVER_HALF or soldier.cover == COVER_FULL:
            soldier.hunkerbonus += 20
        p(spk, 'Taking cover!')
        s(.5)


class OverwatchAction(Action):
    def __init__(self, soldier):
        super().__init__(soldier, 'Overwatch', 6, True, 'o')

    def perform(self):
        self._calc_ap()
        p(spk, self.soldier.get_overwatch_confirmation())
        s(.5)
        self.soldier.ap = 0 # TODO check if this is necessary
        self.soldier.on_overwatch = True


class ReloadAction(Action):
    def __init__(self, soldier):
        super().__init__(soldier, 'Reload', 8, False, 'r')

    def perform(self):
        self._calc_ap()
        soldier.reload()


class RepositionAction(Action):
    def __init__(self, soldier):
        super().__init__(soldier, 'Reposition', 3, False, 'p')

    def perform(self):
        self._calc_ap()
        # if any aliens are on overwatch, check and be shot at if they are
        check_for_alien_overwatch()
        self.soldier.cover = 40 # ?!
        p(spk, self.soldier.get_reposition_confirmation())
        s(.5)
        #chance to flank an alien
        if rd.randrange(0, 100) < 50:
            alien = rd.choice(room[roomNo])

            p(0, str(alien) + ' is flanked!')
            alien.cover = COVER_FLANKED


class UseItemAction(Action):
    def __init__(self, soldier, item):
        super().__init__(soldier, 'Use ' + item.name, item.use_ap_costs, False)
        self.item = item
        self.action_key = item.action_key

    def __str__(self):
        return '({}) ({} AP) {}'.format(self.item.effect_descr,                     \
               self.item.use_ap_costs, self.name)

    def perform(self):
        self._calc_ap()
        items = self.soldier.items
        del items[items.index(self.item)]
        self.item.use(self.soldier)


########################################################################
# globals                                                              #
########################################################################

# Global variables to prevent duplicate hero soldiers
have_bradford = False
have_vdoorn = False

# Global stat counters
fragments = 0
elerium = 0
meld = 0
alloy = 0


########################################################################
# functions                                                            #
########################################################################

def get_action_input(prompt, actions):
    '''Get validated input, and return the chosen action'''
    
    if prompt[-1] != ' ':
        prompt += ' '
    
    while True:
        instr = input(prompt)
        for action in actions:
            if action.action_key == instr:
                return action
        
        print("'" + instr + "' is not a valid action")

# Legacy, can probably be removed
def get_int_input(prompt, vmin, vmax):
    '''Get a range checked integer from the player.'''

    if prompt[-1] != ' ':
        prompt += ' '
    while True:
        instr = input(prompt)
        if instr.isdigit():
            val = int(instr)
            if val < vmin:
                print("That's not an option.")
            elif vmax < val:
                print("That's not an option.")
            else:
                return val
        else:
            print("Please enter the number of the action.")


def create_soldier(sid):
    global have_bradford
    global have_vdoorn

    items = [(rd.choice([ITEM_FRAG_GRENADE, ITEM_MEDKIT, ITEM_SCOPE])),       \
             (rd.choice([ITEM_FRAG_GRENADE, ITEM_MEDKIT]))]
    mobility = rd.randrange(11, 16)
    armour = 'BDY'
    mods  = []
    if rd.randrange(1,100) < 5:
        if rd.randrange(0, 2) == 0:
            if not have_bradford:
                bradford = Soldier(sid, SEX_MALE, 6, 100, mobility,           \
                                   RANK_CENTRAL_OFFICER, '', 'Bradford',      \
                                   armour, BradfordsPistol(), items, mods)
                bradford.get_overwatch_confirmation =                         \
                        lambda: 'Keep your eyes peeled!'
                bradford.get_overwatch_miss_retort =                          \
                        lambda: 'How did I miss that?!'
                bradford.get_reposition_confirmation =                        \
                        lambda: "Moving to...wait...that's CLOSE RANGE!"
                bradford.get_retort = lambda: rd.choice(BRADFORD_RETORTS)
                return bradford
        if not have_vdoorn:
            van_doorn = Soldier(sid, SEX_MALE, 6, 80, mobility, RANK_GENERAL, \
                                'Peter', VAN_DOORN, armour, BallisticRifle(), \
                                items, mods)
            van_doorn.get_overwatch_confirmation =                            \
                    lambda: 'You coming down here or what?'
            van_doorn.get_reposition_confirmation =                           \
                    lambda: "Come on! I won't go down without a fight."
            van_doorn.get_retort = lambda: rd.choice(VAN_DOORN_RETORTS)
            return van_doorn
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


#scatters the aliens in a room, some won't find any cover.
def scatter(roomNo):
    cover = ["Full","Full","Full","Half","Half","Half","Half","Half","Half","No"]
    covernumber = [40,40,40,20,20,20,20,20,20,-10]
    for i in range(len(room[roomNo])):
        room[roomNo][i].cover = rd.choice(covernumber)
        if not room[roomNo][i].cover == -10:
            p(0, str(room[roomNo][i]) + ' moves to '                          \
              + cover[covernumber.index(room[roomNo][i].cover)] + ' cover!')
            s(.5)
        else:
            p(0, str(room[roomNo][i]) + " can't find any cover!")
            s(.5)
    print()


#could probably be merged in with scatter(). Tells you that you've seen an alien
def checkspot(roomNo):
    for i in range(len(room[roomNo])):
        p(0, str(room[roomNo][i]) + ' spotted!')
    s(.5)


def prompt_player(actions):
    for index, action in enumerate(actions):
        ap_str = ''
        ap_costs = action.ap_costs
        if ap_costs > 0:
            ap_str = ' (' + str(ap_costs) + ' AP) '
        action_key = action.action_key
        if len(action_key) < 1:
            action_key = str(index + 1)
            actions[index].action_key = action_key
        print('[' + action_key + '] ' + ap_str + str(action))
    return get_action_input('> ', actions)

reload_action = ""
advance_action = ""
#ah, the player's turn.
def playerTurn():
    global reload_action
    global advance_action
    soldier.ap = soldier.mobility
    soldier.on_overwatch = False
    soldier.hunkerbonus = 0
    

    # currently redundant and inefficient
    advance_action = AdvanceAction(soldier)
    end_turn_action = EndTurnAction(soldier)
    hunker_down_action = HunkerDownAction(soldier)
    overwatch_action = OverwatchAction(soldier)
    reload_action = ReloadAction(soldier)
    reposition_action = RepositionAction(soldier)
    reload_advance_action = ReloadAdvanceAction(soldier)

    #maybe just have these as def's instead of classes?

    # while the player has spare action points left
    while soldier.ap > 0 and soldier.alive == True:
        # displays stats
        p(0, 'HP: ' + str(soldier.hp) + '\tAP: ' + str(soldier.ap)+ '\tAmmo: ' + str(soldier.weapon.ammo))
        if soldier.cover >= 40:
            p(0, str(soldier) + ' is in FULL cover.')
        elif soldier.cover <= 20:
            p(0, str(soldier) + ' is in HALF cover.')
        actions = []
        if len(room[roomNo]) == 0:
            actions.append(advance_action)
            if soldier.ap >= reload_action.ap_costs and soldier.weapon.ammo < soldier.weapon.clip_size:
                actions.append(reload_action)
            if soldier.ap >= reload_advance_action.ap_costs and soldier.weapon.ammo < soldier.weapon.clip_size:
                actions.append(reload_advance_action)
            actions.append(end_turn_action)
        else:
            if soldier.weapon.ammo > 0:
                if soldier.ap >= 6: # TODO make the ap_cost a static member
                    for i in range(len(room[roomNo])):
                        alien = room[roomNo][i]
                        actions.append(FireAction(soldier, alien))
                if soldier.ap >= overwatch_action.ap_costs:
                    actions.append(overwatch_action)
            if soldier.weapon.ammo < soldier.weapon.clip_size                 \
               and soldier.ap >= reload_action.ap_costs:
                actions.append(reload_action)
            for item in soldier.items:
                if item.use_ap_costs > 0 and soldier.ap >= item.use_ap_costs:
                    actions.append(UseItemAction(soldier, item))
            if soldier.ap >= reposition_action.ap_costs:
                actions.append(reposition_action)
            if soldier.cover > COVER_NONE                                     \
               and soldier.ap >= hunker_down_action.ap_costs:
                    actions.append(hunker_down_action)
            actions.append(end_turn_action)
        prompt_player(actions).perform()
    #ends turn by default


def displayShop(ap):
    global fragments
    global elerium
    global meld
    global alloy

    options = []
    print("Time: "+str(ap))
    p(0, 'HP: ' + str(soldier.hp) + '\tAP: ' + str(soldier.ap)+ '\tAmmo: ' + str(soldier.weapon.ammo))
    if ap == 60:
        if meld >= 15:
            if not "Aim" in soldier.mods:
                options.append("AimBonus")
                p(len(options),"(60 Time) (15m) Insta-Genemod: Depth Perception (+5 aim)")
            if not "AP" in soldier.mods:
                options.append("APBonus")
                p(len(options),"(60 Time) (15m) Micro-Augment: Reflex Servomotors (+2 AP)")
            options.append("")
        if meld >= 20:
            if not "HP" in soldier.mods:
                options.append("HPBonus")
                p(len(options),"(60 Time) (20m) Insta-Genemod: Muscle Regeneration (+10 HP)")
            if not "Nade" in soldier.mods:
                options.append("NadeBonus")
                p(len(options),"(60 Time) (20m) Micro-Augment: Grenade Launcher (+2 Frag Grenades)")
    if ap >= 50:
        if not type(soldier.weapon) is LaserRifle() and elerium >= 20 and fragments >= 40:
            options.append("LaserRifle")
            p(len(options),"(40 Time) (20e) (40f) Get Laser Rifle")
            print("     (~4dmg), infinite ammo")
        if not type(soldier.weapon) is LaserCarbine() and elerium >= 10 and fragments >= 30:
            options.append("LaserCarbine")
            p(len(options),"(40 Time) (10e) (30f) Get Laser Carbine")
            print("     (~3dmg), infinite ammo, +10% aim")
    if ap >= 30:
        if meld >= 5 and fragments >= 5:
            options.append("Meds")
            p(len(options),"(30 Time) (10m) (5f) Get Nano Serum")
        if alloy >= 4 and fragments >= 20:
            options.append("Frag")
            p(len(options),"(30 Time) (20f) (4a) Get Frag Grenade")
    if ap >= 20:
        if meld >= 5:
            options.append("Heal")
            p(len(options),"(20 Time) (5m) Recuperate (+1 HP)")
        options.append("Reload")
        p(len(options),"(20 Time) Reload Weapon")
    options.append("Skip")
    p(len(options),"("+str(ap)+" Time) Advance (Skip this Drop Zone)")
    selection = get_int_input('> ', 1, len(options) - 1)
    print('selected option ' + str(selection))
    return options[selection - 1]


def check_for_alien_overwatch():
    for i in range(len(room[roomNo])):
        alium = room[roomNo][i]
        alium.overwatch(soldier)


def fire(alium,cthplayer):
    alium.on_overwatch = False
    if alium.alive == True:
        if cthplayer > 0:
            p(0, str(alium) + ' fires at ' + str(soldier) + ' (' + str(cthplayer) + '%)'+'('+alium.weapon.name+")")
            alium.shoot_at(soldier, cthplayer)
        else:
            if rd.randrange(0,100) < 80:
                ow(alium)
            else:
                if ITEM_ALIEN_GRENADE in alium.items:
                    nade(alium)


def nade(alium):
    alium.on_overwatch = False
    if ITEM_ALIEN_GRENADE not in alium.items:
        raise Exception('No grenade in inventory')
    if alium.alive == True:
        p(0, str(alium) + ' uses Alien Grenade!')
        s(.5)
        p(0, '**BLAM!**')
        s(.5)
        del alium.items[alium.items.index(ITEM_ALIEN_GRENADE)]
        #sets the aliens item to 'none', no more grenades for you
        p(0, '3 damage!')
        soldier.cover = 20
        soldier.hp -= 3

def ow(alium):
    if alium.alive == True:

        p(0, str(alium) + ' went on overwatch!')
        alium.on_overwatch = True


def move(alium,cover):
    if alium.alive == True:
        s(.5)
        if cover == 40:
            p(0, str(alium) + ' runs to Full cover!') #if an alien has no cover, it will run to full cover. same goes if it's flanked
        elif cover == 20:
            p(0, str(alium) + ' runs to Half cover!')
        s(.5)
        soldier.overwatch(alium)
        alium.on_overwatch = False
        alium.cover = cover


def alienTurn(soldier):
    for i in range(len(room[roomNo])):
        try:
            alium = room[roomNo][i]
        except ( Exception ):
            i = 0
        #because something may have happened that causes an index error
        if alium.alive == True and soldier.alive == True:
            cthplayer = (alium.aim - soldier.cover) - soldier.hunkerbonus
            if ITEM_SCOPE in alium.items:
                cthplayer += 10

            if alium.cover < 20:
                if rd.randrange(0,100) < 70:
                    move(alium,40)
                elif rd.randrange(0,100) < 20:
                    fire(alium,cthplayer)
                else:
                    move(alium,20)
            elif alium.cover < 40:
                if cthplayer > 30 + rd.randrange(0,20):
                    fire(alium,cthplayer)
                elif rd.randrange(0,100) < 15:
                    if ITEM_ALIEN_GRENADE in alium.items:
                        nade(alium)
                    else:
                        fire(alium,cthplayer)
                elif rd.randrange(0,100) < 30:
                    if rd.randrange(0,100) < 50:
                        move(alium,40)
                    else:
                        move(alium,20)
                    #randomly moves to different cover sometimes

                else:
                    if rd.randrange(0,100) < 70:
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
        s(.5)


#levels up
def checkXP():
    was_promoted = False
    if soldier.xp >= 25 and soldier.nrank < RANK_SQUADDIE:
        soldier.nrank = RANK_SQUADDIE
        soldier.hp += 2
        soldier.aim += 2
        soldier.mobility += 1
        drop()
        drop()
        was_promoted = True
    elif soldier.xp >= 100 and soldier.nrank < RANK_CORPORAL:
        soldier.nrank = RANK_CORPORAL
        soldier.hp += 2
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
        soldier.hp += 2
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
        soldier.hp += 2
        soldier.aim += 1
        soldier.mobility += 1
        drop()
        drop()
        drop()
        was_promoted = True
    elif soldier.xp >= 3000 and soldier.nrank < RANK_COLONEL:
        soldier.nrank = RANK_COLONEL
        soldier.hp += 2
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
    if ITEM_ALIEN_GRENADE in alium.items:
        elerium += 2
    elif ITEM_ALLOY_PLATING in alium.items:
        alloy += 2
    elif ITEM_SCOPE in alium.items:
        fragments += 2
    e, f = alium.weapon.get_materials()
    elerium += e
    fragments += f
    return [fragments, elerium, meld, alloy]


def drop():
    itemdrop = rd.randrange(0,5)
    if rd.randrange(1,100) <= 5+(soldier.mobility):
        p(spk,"Recovered a "+drops[itemdrop]+"!")
        if itemdrop == 0:
            soldier.items.append(ITEM_FRAG_GRENADE)
        elif itemdrop == 1:
            soldier.items.append(ITEM_MEDKIT)
        elif itemdrop == 2:
            soldier.items.append(ITEM_ALIEN_GRENADE)
        elif itemdrop == 3:
            print("Replace your {}?".format(soldier.weapon.name))
            replace = yn()
            if replace:
                soldier.weapon = PlasmaCarbine()
        elif itemdrop == 4:
            print("Replace your {}?".format(soldier.weapon.name))
            replace = yn()
            if replace:
                soldier.weapon = PlasmaRifle()

def yn():
    chosen = False
    while chosen == False:
        print("[y] Yes")
        print("[n] No")
        selection = input(">> ")
        if selection == "y":
            chosen = True
            return True
        if selection == "n":
            chosen = True
            return False
        else:
            continue
            



def create_map(scripted_levels):
    # the first room is empty, since the player starts there
    options = ['Sectoid', 'Thinman', 'Floater', 'Muton']
    the_map = [[]]
    for i in range(1, NUMBER_OF_ROOMS):
        if i in scripted_levels:
            the_map.append(scripted_levels[i])
        else:
            pod = []
            # more aliens per room the further along you are
            for j in range(3 + rd.randrange(-2, 2 + round(i / 10))):
                # determine alien species
                species = options[0]
                nrank = 0
                if 3 < i and i < 10:
                    species = rd.choice(options[:2])
                elif 10 <= i and i < 20:
                    species = rd.choice(options)
                else:
                    species = rd.choice(options[2:])
                # determine rank
                # if species == 'Sectoid':
                maxrank = 4
                if species == 'Thinman':
                    maxrank = 5
                elif species == 'Floater':
                    maxrank = 6
                elif species == 'Muton':
                    maxrank = 8
                nrank = rd.randrange(round(i / (NUMBER_OF_ROOMS               \
                                                / (maxrank - 1))), maxrank)
                alien = create_alien(j, i, species, nrank=nrank)
                pod.append(alien)
            the_map.append(pod)
    return the_map


def dump_map(the_map):
    for index, location in enumerate(the_map):
        print('#{}:'.format(index))
        for pod in location:
            print('{}'.format(pod))


# def main():
p("Bradford", "Welcome Commander. We've discovered an Alien Base, and it's your job to send someone out to deal with it.")
p("Bradford", "Choose a soldier from the 3 below to go on the mission.")

barracks = []
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
soldier = barracks[get_int_input('# ', 1, 3) - 1]

spk = soldier.firstname + " " + soldier.lastname
if soldier.lastname == "Bradford":
    p(spk, "What? There must have been a mistake on the sheet, Commander! You can't send --")
elif soldier.lastname == VAN_DOORN:
    p(spk, "I'm the Ops team?")
else:
    p(spk, "Ready for duty, Commander!")

scripted_levels = {
    1:  [create_alien(1, 1, 'Sectoid', nrank=0)],
    2:  [
            create_alien(1, 2, 'Sectoid', nrank=0),
            create_alien(1, 2, 'Sectoid', nrank=0)
        ],
    3:  [
            create_alien(1, 3, 'Sectoid', nrank=0),
            create_alien(1, 3, 'Sectoid', nrank=1)
        ],
    5:  ["Drop Zone"],
    10: ["Drop Zone"],
    15: ["Drop Zone"],
    20: ["Drop Zone"],
    30: [create_alien(1, 1, 'Muton', nrank=8, hp=50)]
}

room = create_map(scripted_levels)
# dump_map(room)
roomNo = 0


#game loop, runs until your soldier is killed
while soldier.alive == True:
    try:
        old_room = roomNo
        playerTurn()
        p(0, str(soldier) + ' is out of AP!')

        # Aliens are not allowed to act after the room was changed,
        # because they already scattered when the player entered the new
        # room.  Also, there is no need for an alien turn if there are
        # no more aliens in the room.
        if soldier.alive == True and old_room == roomNo                       \
           and len(room[roomNo]) > 0:
            print()
            print("--------------Alien Activity!--------------")
            print()
            s(1)
            alienTurn(soldier)
            print()
            print("--------------XCOM Turn--------------")
            print()
    except ( ValueError or IndexError ):
        pass
    if roomNo == NUMBER_OF_ROOMS:
        print("Bradford","We did it, Commander! We cleared the Alien Base. We took out their leader - that's a victory in my books!")
        break
