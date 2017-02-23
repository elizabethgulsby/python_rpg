# Character class - characters have name, health, and strength, given to them in the Hero/Monsters classes
class Character(object):
	# def __init__(self, name, health, strength):
	# 	self.name = name
	# 	self.health = health
	# 	self.strength = strength

	# all characters can take damage
	def take_damage(self, points_of_damage):
		self.health -= points_of_damage

	# all characters can attack, regardless of role
	def attack(self, nameOfCharacter):
		print "%s attacks %s!" % (self.name, nameOfCharacter.name)
		nameOfCharacter.take_damage(self.strength)

	def alive(self):
		return self.health > 0


