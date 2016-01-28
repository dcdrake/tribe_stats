class Game(object):

	def __init__(self):
		self.date           = 0
		
		self.started        = False
		self.fouled_out     = False
		self.away           = False

		self.minutes_played  = 0
		self.fg              = 0
		self.fga             = 0
		self.fg_percent      = 0
		self.fg_3            = 0
		self.fga_3           = 0
		self.fg_3_percent    = 0
		self.ft              = 0
		self.fta             = 0
		self.ft_percent      = 0
		self.off_rebound     = 0
		self.def_rebound     = 0
		self.tot_rebound     = 0
		self.avg_rebound     = 0
		self.personal_fouls  = 0
		self.assists         = 0
		self.turnovers       = 0
		self.blocks          = 0
		self.steals          = 0
		self.points          = 0
		self.avg_points      = 0
