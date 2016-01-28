# table_def.py
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///test.db', echo=True)
Base = declarative_base()


game_players = Table('game_players', Base.metadata,
                     Column('player_name', ForeignKey('players.name'), primary_key=True),
                     Column('game_date', ForeignKey('games.date'), primary_key=True))

########################################################################
class DbPlayer(Base):

    __tablename__ = "players"
 
    name = Column(String, primary_key=True)
    fga  = Column(Integer)  
    fgm  = Column(Integer)  
    three_pa  = Column(Integer)
    three_pm  = Column(Integer)

    rebounds = Column(Integer)
    steals   = Column(Integer)
    blocks   = Column(Integer)

    games = relationship('games',
                         secondary=game_players,
                         back_populates='players')
    
    #----------------------------------------------------------------------
    def __init__(self, name_in, number_in):
        self.name   = name_in
        self.number = number_in


########################################################################
class DbGame(Base):

    __tablename__ = "games"

    date     = Column(Date, primary_key=True)
    opponent = Column(String)

    players = relationship('players',
                           secondary=game_players,
                           back_populates='games')
        
    def __init__(self, date_in, opponent_in):
        self.date     = date_in
        self.opponent = opponent_in

########################################################################
class DbSeason(Base):

    __tablename__ = "season"

    season = Column(String, primary_key=True)

    def __init__(self, season_in):
        self.season = season_in

        
# create tables
Base.metadata.create_all(engine)
