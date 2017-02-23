from character import Character
import time; #use tbd

class Vampire(Character):
	def __init__(self, name, health, strength, bloodlust):
		Character.__init__(self);
		self.name = name
		self.health = health
		self.strength = strength
		self.bloodlust = bloodlust

	def drain(self, hero_health):
		print "The vampire %s has drained %s!  2x health diminished." % (self.name, hero.name)
		return hero_health.take_damage(self.strength * 2)
		# place if statement to check to see if drain will diminish hero to 0 health - if so, hero dies

		#place if statement in logic to add points to bloodlust when vampire takes attack of a certain point value

vlad = Vampire("Vlad", 10, 15, 20)
# print vars(vlad)

class Goblin(Character):
	def __init__(self, name, health, strength):
		Character.__init__(self);
		self.name = name
		self.health = health
		self.strength = strength

	#only called if hero has a certain percentage of health (< 5?)
	def consume(self, hero_health):
		print "%s has eaten the hero!" % self.name

hoggle = Goblin("Hoggle", 8, 25)
# print vars(hoggle)
