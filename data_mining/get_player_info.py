from lxml import html
import datetime
import requests
import re
from Game import Game
from Player import Player

for i in range(0, 100):

	player_page_url = 'http://www.tribeathletics.com/custompages/files/mbb/2015/stats/plyr_%02d.htm' % (i)


	page = requests.get(player_page_url)

	if (page.status_code != 404):
		tree = html.fromstring(page.content)

		player_name = tree.xpath('/html/head/title/text()')
		player_info = tree.xpath('/html/body/font/pre/text()')

		# Get the big chart of stats, and get rid of most of the junk
		player_info = player_info[1].strip().split('\n')
		del player_info[0:3]

		player_name = player_name[0].split(',')

		# Get the number, first and last name
		player_number     = player_name[0].split()[0].strip()
		player_last_name  = player_name[0].split()[1].strip()
		player_first_name = player_name[1].strip()

		# Create a new player 
		new_player = Player(player_first_name, 
							player_last_name, 
							player_number)


		for game in player_info:

			# Create a new game
			new_game = Game()

			game = game.strip()
			beginning_of_date_index_exists = re.search('\d', game)

			if (beginning_of_date_index_exists):
				first_digit_index = beginning_of_date_index_exists.start()

				# Split the venue and stats into two separate lists to be parsed into database
				venue = game[:first_digit_index]
				game  = game[first_digit_index:]
					
				# Split each game line into a list of individual stats
				game = game.split()

				# There are excess lines at the end of the chart, and they should be excluded.
				if not (len(game) < 4):
					date_string = game[0]
					date_list = date_string.split('/')

					# There is a garbage date with one value for each player, exclude it.
					if (len(date_list) > 1):
						month = int(date_list[0])
						day   = int(date_list[1])
						year  = 2000 + int(date_list[2]) # Inexplicably doesn't do two digit years

						game_date = datetime.date(year, month, day)


						new_game.date = game_date

						if "at" in venue:
							new_game.away = True

						if (game[1] == '*'):
							new_game.started = True

						new_game.avg_points = game[-1]
						new_game.points     = game[-2]
						new_game.steals     = game[-3]
						new_game.blocks     = game[-4]
						new_game.turnovers  = game[-5]
						new_game.assists    = game[-6]
						new_game.fouled_out = game[-7]
						new_game.personal_fouls = game[-8]
						new_game.avg_rebound = game[-9]
						new_game.tot_rebound = game[-10]
						new_game.def_rebound = game[-11]
						new_game.off_rebound = game[-12]
						new_game.ft_percent  = game[-13]

						ft  = game[-14].split('-')[1]
						fta = game[-14].split('-')[0]
						
						new_game.fta         = fta
						new_game.ft          = ft
						new_game.fg_3_percent = game[-15]

						fg_3  = game[-16].split('-')[0]
						fga_3 = game[-16].split('-')[1]
						
						new_game.fga_3       = fga_3
						new_game.fg_3        = fg_3

						new_game.fg_percent  = game[-17]

						fg  = game[-18].split('-')[0]
						fga = game[-18].split('-')[1]

						new_game.fga         = fga
						new_game.fg          = fg
						new_game.minutes_played = game[-19]
						
						# Add this game to the list of each of the player's games
						new_player.addGame(new_game)

						print new_game.date
