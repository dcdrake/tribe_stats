from lxml import html
import requests
import re


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

		print player_name	
		print '====================================================\n'

		for game in player_info:
			game = game.strip()
			beginning_of_date_index_exists = re.search('\d', game)

			if (beginning_of_date_index_exists):
				first_digit_index = beginning_of_date_index_exists.start()

				# Split the venue and stats into two separate lists to be parsed into database
				venue = game[:first_digit_index]
				game  = game[first_digit_index:]


				game = game.split()
				print game

				# Check if there is a star after the date that indicates the player started that game.
				# If there is, then that list will be one element longer than a player who didn't start.
				#player_started_game = re.search('\*', game)

				#if (player_started_game):
					#Do something


		print '\n'
		print '\n'
		print '\n'
		print '\n'
		print '\n'
