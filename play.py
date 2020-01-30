from blackjack import Blackjack
from functions import clear

clear()
blackjack = Blackjack()
blackjack.deal()

while True:
	blackjack.display_info()
	blackjack.results()
	blackjack.hit_stand()