# table_def.py
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///test.db', echo=True)
Base = declarative_base()


#game_players = Table('game_players', Base.metadata,
                    #Column('player_name', ForeignKey('players.name'), primary_key=True),
                    #Column('game_date', ForeignKey('games.date'), primary_key=True))


#player_stats = Table('player_stats', Base.metadata,
#Column('player_id', ForeignKey('player.player_id'), primary_key=True),
#Column('game_id', ForeignKey('game.game_id'), primary_key=True)
#Column()            )

########################################################################
class DbPlayerStats(Base):

    __tablename__ = 'player_stats'

    player_id   = Column(Integer, ForeignKey('player.player_id'), primary_key=True)
    game_id     = Column(Integer, ForeignKey('game.game_id'), primary_key=True)

    minutes_played = Column(Integer)

    field_goals_made      = Column(Integer)
    field_goals_attempted = Column(Integer)
    field_goal_percentage = Column(Float)

    three_point_field_goals_made      = Column(Integer)
    three_point_field_goals_attempted = Column(Integer)
    three_point_field_goal_percentage = Column(Float)

    free_throws_made      = Column(Integer)
    free_throws_attempted = Column(Integer)
    free_throw_percentge  = Column(Float)

    offensive_rebounds = Column(Integer)
    defensive_rebounds = Column(Integer)
    total_rebounds     = Column(Integer)

    personal_fouls = Column(Integer)
    assists        = Column(Integer)
    turnovers      = Column(Integer)
    blocks         = Column(Integer)
    steals         = Column(Integer)
    points         = Column(Integer)

########################################################################
class DbPlayer(Base):

    __tablename__ = "player"

    player_id = Column(Integer, primary_key=True)
    name      = Column(String(50))
    number    = Column(Integer)
    #fga  = Column(Integer)
    #fgm  = Column(Integer)
    #three_pa  = Column(Integer)
    #three_pm  = Column(Integer)

    #rebounds = Column(Integer)
    #steals   = Column(Integer)
    #blocks   = Column(Integer)

    #games = relationship('games',
                         #secondary=game_players,
                         #back_populates='players')

    #----------------------------------------------------------------------
    def __init__(self, name_in, number_in):
        self.name   = name_in
        self.number = number_in


########################################################################
class DbGame(Base):

    __tablename__ = "game"

    game_id  = Column(Integer, primary_key=True)
    date     = Column(Date)
    opponent = Column(String(50))

    #players = relationship('players',
                           #secondary=game_players,
                           #back_populates='games')

    def __init__(self, date_in, opponent_in):
        self.date     = date_in
        self.opponent = opponent_in

########################################################################
class DbSeason(Base):

    __tablename__ = "season"

    season_id = Column(Integer, primary_key=True)
    season    = Column(String(25))

    def __init__(self, season_in):
        self.season = season_in


# create tables
Base.metadata.create_all(engine)
