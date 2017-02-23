import random;
import time;
from heroes import Hero, Companion, Templar, Thief;
from monsters import Goblin, Vampire;

def coinToss():
	number = input("Okay, heads or tails?")
	headsOrTails = ""
	heads = 0
	tails = 0
	for amount in range(number):
		flip = random.randint(0,1)
		if (flip == 0):
			headsOrTails = "Heads!"
			print "Heads!"
		else:
			headsOrTails = "Tails!"
			print "Tails!"
	return headsOrTails

companions = [Templar("Gabriel", 20, 30, "sword", "shield", "holy light"), Thief("Twisted Fate", 13, 15, "lockpick", "bracers", "charismatic evasion")]

enemies = [Vampire("Vlad", 10, 20, 15), Goblin("Hoggle", 15, 25)];

Thorin = Hero("Thorin", 10, 22, "axe", "");

for enemy in enemies:
	while Thorin.alive() and enemy.alive():
		print "Hello, Hero!  An adventure awaits you! Do you dare roam these woods and brave the peril that surely awaits you at every turn?"
		print "1. It's been a while since my last adventure.  Sign me up!"
		print "2. Hell no, Netflix and coffee are back at the house.  How did I get here, anyway?"
		print "3. Adventure?  I dunno.....can I flip a coin?"
		print "> "
		input = int(raw_input());
		if input == 1:
			print "Excellent!  Aaaaaaaand we're off!"
		elif input == 2:
			print "Awww, okay.  Another time, then."
			break;
		elif input == 3:
			print "Okay.  Heads, you go on the adventure.  Tails, you get your coffee and Netflix.  Here we go."
			x = coinToss();
			if x == "Heads!":
				print "Whee!  Let's go!"
			else:
				print "Womp womp.  See you next time, then."
		else:
			print "I'm not a string!"



