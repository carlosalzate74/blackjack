from random import shuffle
import sys
from time import sleep

class Blackjack:
	def __init__(self):
		self.deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']*4
		self.player = []
		self.dealer = []
		self.stand = False
		self.first_hand = True
		return

	def deal(self):
		print("Shuffling...")
		sleep(2)
		shuffle(self.deck)
		for _ in range(2):
		    self.player.append(self.deck.pop())
		    self.dealer.append(self.deck.pop())
		return

	def score(self, hand):
		non_aces = [c for c in hand if c != 'A']
		aces = [c for c in hand if c == 'A']

		total = 0

		for card in non_aces:
		    if card in 'JQK':
		        total += 10
		    else:
		        total += int(card)

		for card in aces:
		    if total <= 10:
		        total += 11
		    else:
		        total += 1

		return total

	def results(self):
	    if self.score(self.player) == 21 and self.hand:
	        print("Blackjack! You won!")
	        sys.exit()
	    elif self.score(self.player) > 21:
	        print("You lost!")
	        sys.exit()
	    if self.stand:
	        if self.score(self.dealer) > 21:
	            print("You won!")
	        elif self.score(self.player) > self.score(self.dealer):
	            print("You won!")
	        elif self.score(self.player) < self.score(self.dealer):
	            print("You lost!")
	        else:
	            print("Push. Nobody wins.")
	        sys.exit()


	def hit_stand(self):
	    print("[H] - Hit\n[S] - Stand")
	    choice = input("> ").upper()
	    self.hand = False
	    if choice == 'H':
	        self.player.append(self.deck.pop())
	    elif choice == 'S':
	        self.stand = True
	        while self.score(self.dealer) <= 16:
	            self.dealer.append(self.deck.pop())
	        self.display_info()
	        self.results()


	def display_info(self):
		print("You   : {} = {}".format(' '.join(self.player), self.score(self.player)))
		if self.stand:
		    print("Dealer: {} = {}".format(' '.join(self.dealer), self.score(self.dealer)))
		else:
		    print("Dealer: {} X".format(self.dealer[0]))


