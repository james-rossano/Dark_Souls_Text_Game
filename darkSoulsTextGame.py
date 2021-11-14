# A Dark Souls Game By James Rossano
import time
from pynput import keyboard
import random

introText = ["Yes, indeed. It is called Lothric, where the transitory lands of the Lords of Cinder converge.",
	"In venturing north, the pilgrims discover the truth of the old words:",
	"\'The fire fades and the lords go without thrones.\'",
	"When the link of the fire is threatened, the bell tolls, unearthing the old Lords of Cinders from their graves…",
	"Dark Son Gwydolyn...",
	"Leader of Farron's Undead Legion, Executioner Smough…",
	"And the reclusive lord of the Profaned Capital, Artorias the Abysswalker…",
	"Only, in truth... the Lords will abandon their thrones…",
	"And the Unkindled will rise.",
	"Nameless, accursed Undead, unfit even to be cinder. And so it is, that ash seeketh embers.",
]
seigwaldText = ["Hmm…",
	"Mmmmmm…",
	"Hmm... Mmm…",
	"Oh!",
	"Pardon me, I was absorbed in thought.",
	"I am Siegward of Catarina.",
	"Would you join me in this battle?: ",
	"Artorius, old friend.",
	"I, Siegward of the Knights of Catarina, have come to uphold my promise!",
	"Let the sun shine upon this Lord of Cinder.",
	"Forgive me, old friend…",
	"I've failed, in everything..."
]

class Character:
	def __init__(self,name,hp,dmg):
		self.name = name
		self.hp = hp
		self.dmg = dmg

	def lowerHealth(self,dmg):
		self.hp -= dmg
	def maxHealth(self,hp):
		self.hp = hp


UD = Character('Chosen Undead',500,1.4)
SC = Character('Seigward of Catarina',200,0.5)
ES = Character('Executioner Smough',1000,0.5)
AA = Character('Artorias The Abysswalker',1500,0.5)
DG = Character('Dark Son Gwyndolyn',1800,0.5)


animationSet = ['5-','10--','15---','20----','25-----','30------','35-------','40--------','50---------','60----------','70-----------','80------------','90-------------','100-##############']
dmgSet = [5,10,15,20,25,30,35,40,50,60,70,80,90,100]

imageRest = 0.1
hitMiss = 0
spacePress = False

diff = input('Select a difficulty 1-3: ')
if diff == 1:
	prob=10
	npcProb = 12
elif diff == 2:
	prob=13
	npcProb = 10
else:
	prob=15
	npcProb = 8

def charIntro(image):
	f = open(image,'r')
	for i in f:
		x = f.readline()
		time.sleep(imageRest)
		print(x, end="")
	f.close()
	print('\n')

def death():
	input('The fire has failed to ignite...')
	input('The age of dark continues...')
	input('You Died')
	time.sleep(3)
	path = input('Try Again?: ')
	if path == 'y' or path == 'yes':
		UD.maxHealth(500)
		SC.maxHealth(200)
		ES.maxHealth(1000)
		AA.maxHealth(1500)
		DG.maxHealth(1800)
		startGame()

def pressed(key):
	global spacePress
	if str(key) == 'Key.space':
		spacePress = True

def enemyHit():
	rand = random.randint(1,prob)
	if rand > 10:
		rand = 10
	return rand * 10

def npcHit(npcOn):
	if npcOn == True:
		rand = random.randint(1,npcProb)
		if rand > 10:
			rand = 10
		return rand * 10
	else:
		return None

def battle(encounter,rest,npcOn):
	global spacePress
	frame = 1
	negPos = 1
	print('\n')
	print('Ready....')
	time.sleep(1.5)
	print('Begin!')
	listener = keyboard.Listener(on_press=pressed)
	listener.start()
	while True:
		hitOnce = True
		enemyDmg = enemyHit()
		npcDmg = npcHit(npcOn)
		for i in range((len(animationSet)*2)-2):
			print(animationSet[frame])
			if hitOnce == True and spacePress == True:
				print('Hit///Hit///Hit///Hit///Hit///Hit///'+str(dmgSet[frame]))
				UDDamage = dmgSet[frame]
				hitOnce = False
				spacePress = False
			if dmgSet[frame] == enemyDmg and negPos != -1:
				print('EnemyHit///EnemyHit///EnemyHit///EnemyHit///'+str(enemyDmg))
			if dmgSet[frame] == npcDmg and negPos != -1:
				print('NPCHit///NPCHit///NPCHit///NPCHit///'+str(npcDmg))
			if frame >= len(animationSet)-1:
				negPos=negPos*-1
			if frame <= 0:
				negPos=negPos*-1
			frame+=negPos
			time.sleep(rest)
		
		if encounter == 1:
			UD.lowerHealth(ES.dmg * enemyDmg)
			ES.lowerHealth(UD.dmg * UDDamage)
			if ES.hp <= 0:
				print(ES.name + " Health: 0")
				print('Victory Achieved')
				return True
				break
			print(ES.name + " Health: " + str(round(ES.hp)))
		elif encounter == 2:
			UD.lowerHealth(AA.dmg * enemyDmg)
			AA.lowerHealth(UD.dmg * UDDamage)
			if AA.hp <= 0:
				print(AA.name + " Health: 0")
				print('Victory Achieved')
				return True
				break
			print(AA.name + " Health: " + str(round(AA.hp)))
		elif encounter == 3:
			UD.lowerHealth(DG.dmg * enemyDmg)
			DG.lowerHealth(UD.dmg * UDDamage)
			if DG.hp <= 0:
				print(DG.name + " Health: 0")
				print('Victory Achieved')
				return True
				break
			print(DG.name + " Health: " + str(round(DG.hp)))

		UDDamage = 0
		if UD.hp <= 0:
			print('Your Health: 0')
			return False
		print("Your Health: " + str(round(UD.hp)))

def win():
	kindle = input('Would you like to kindle the first flame:')
	if kindle == 'y' or kindle == 'yes':
		input('The age of fire has been restored')
		input('You Win')
	else:
		death()

def startGame():
	for i in range(len(introText)):
		input(introText[i])
	print('\n')
	input('Firelink Shrine stands in the distance...')
	input('You stand on the edge of Lothric, a shell of its previous fire')
	path = input('Continue along the beaten path?: ')
	if path == 'y' or path == 'yes':
		input('You see the gates to the city of light, Anor Londo')
		smn = input('You see a summon sign on the ground. Do you want to summon the phantom?: ')
		if smn == 'y' or smn == 'yes':
			charIntro("Seigwald.txt")
			for i in range(len(seigwaldText)-6):
				input(seigwaldText[i])
			seigDec = input(seigwaldText[6])
			if seigDec == 'y' or seigDec == 'yes':
				npcOn = True
				input('Then lets fight valiantly against this old lord')
			else:
				input('To each their own then unkindled one')
				npcOn = False
		else:
			npcOn = False

		
		charIntro("Smough.txt")
		rest=0.2
		btl1 = battle(1,rest,npcOn)
		if btl1 == True:
			UD.maxHealth(500)
			input('next battle')
			charIntro("Artorius.txt")
			rest=0.17
			btl2 = battle(2,rest,npcOn)
			if btl2 == True:
				UD.maxHealth(500)
				input('next battle')
				charIntro("Gwyndolin.txt")
				rest=0.14
				btl3 = battle(3,rest,npcOn)
				UD.maxHealth(500)
				if btl3 == True:
					return win()
				else:
					return death()
			else:
				return death()
		else:
			return death()
	else:
		return death()

startGame()



