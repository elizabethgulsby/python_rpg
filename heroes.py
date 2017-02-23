from character import Character
import time; #use tbd

# Heroes are inheriting methods from Character - they all have a name, health and strength
class Hero(Character):
	def __init__(self, name, health, strength, weapon, armor):
		Character.__init__(self);
		self.name = name
		self.health = health
		self.strength = strength
		self.weapon = weapon
		self.armor = armor

liz = Hero("Liz", 5, 5, "sword", "")
# print vars(liz)

##need a companion class to assist the Hero##
class Companion(Character):
	def __init__(self, name, health, strength, weapon, armor, talent):
		Character.__init__(self);
		self.name = name
		self.health = health
		self.strength = strength
		self.weapon = weapon
		self.armor = armor
		self.talent = talent

	# all companions need an assist method
	def assist(self):
		print "%s provides support!" % self.name
	

# Knights are a type of Companion
class Templar(Companion):
	def __init__(self, name, health, strength, weapon, armor, talent):
		Companion.__init__(self, name, health, strength, weapon, armor, talent);

	# Templar needs a revive method (to be called when certain conditions permit - tbd)
	def revive(self):
		print "%s has revived %s!" % (self.name, hero.name)



Aragorn = Templar("Aragorn", 20, 30, "sword", "shield", "healing")
# print vars (Aragorn)

# Thieves are another type of Companion
class Thief(Companion):
	def __init__(self, name, health, strength, weapon, armor, talent):
		Companion.__init__(self, name, health, strength, weapon, armor, talent);

	# Thief needs a method to steal gold from the monster
	def steal(self):
		print "%s stole gold from the monster!" % (self.name)

twistedFate = Thief("Twisted Fate", 10, 10, "shank", "", "stealing")
# print vars(twistedFate)
