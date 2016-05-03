#!/usr/bin/env python

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///test.db', echo=True)
Base = declarative_base()


########################################################################
class DbGameStats(Base):

    __tablename__ = 'game_stats'

    player_id   = Column(Integer, ForeignKey('players.player_id'), primary_key=True)
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

    def __init__(self, minutes_played, field_goals_made, field_goals_attempted,
        field_goal_percentage, three_point_field_goals_made,
        three_point_field_goals_attempted, three_point_field_goal_percentage,
        free_throws_made, free_throws_attempted, free_throw_percentge,
        offensive_rebounds, defensive_rebounds, total_rebounds,
        personal_fouls, assists, turnovers, blocks, steals, points):

        self.minutes_played = minutes_played
        self.field_goals_made = field_goals_made
        self.field_goals_attempted = field_goals_attempted
        self.field_goal_percentage = field_goal_percentage
        self.three_point_field_goals_made = three_point_field_goals_attempted
        self.three_point_field_goal_percentage = three_point_field_goal_percentage
        self.free_throws_made = free_throws_made
        self.free_throws_attempted = free_throws_attempted
        self.free_throw_percentge = free_throw_percentge
        self.offensive_rebounds = offensive_rebounds
        self.defensive_rebounds = defensive_rebounds
        self.total_rebounds = total_rebounds
        self.personal_fouls = personal_fouls
        self.assists = assists
        self.turnovers = turnovers
        self.blocks = blocks
        self.steals = steals
        self.point = points


########################################################################
class DbPlayers(Base):

    __tablename__ = "players"

    player_id = Column(Integer, primary_key=True)
    name      = Column(String(50))
    number    = Column(Integer)

    def __init__(self, name_in, number_in):
        self.name   = name_in
        self.number = number_in


########################################################################
class DbGame(Base):

    __tablename__ = "game"

    game_id  = Column(Integer, primary_key=True)
    date     = Column(Date)
    opponent = Column(String(50))

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
