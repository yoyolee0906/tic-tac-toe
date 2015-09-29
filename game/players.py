import random
from django.utils.module_loading import import_string

class RandomPlayer(object):

	def play(self, game):
		open_indexes = [i for i, v in enumerate(game.board) if v == ' ']

		if not open_indexes:
			return
		return random.choice(open_indexes) # return a index number including 0 to 8


def get_player(player_type):
	cls = import_string(player_type)
	return cls()

