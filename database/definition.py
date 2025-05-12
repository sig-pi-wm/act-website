from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.orm import mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    user_id = mapped_column(Integer, primary_key=True, autoincrement=True)
    username = mapped_column(String, nullable=False)

    race_players = relationship("RacePlayer", back_populates="user")
    team_players = relationship("TeamPlayer", back_populates="user")

class ACT(Base):
    __tablename__ = "acts"
    act_id = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    date = mapped_column(Date, nullable=False)

    races = relationship("Race", back_populates="act")
    race_players = relationship("RacePlayer", back_populates="act")
    teams = relationship("Team", back_populates="act")

class Map(Base):
    __tablename__ = "maps"
    map_id = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    map_name = mapped_column(String, nullable=False)

    races = relationship("Race", back_populates="map")

class Race(Base):
    __tablename__ = "races"
    race_id = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    act_id = mapped_column(Integer, ForeignKey('acts.act_id'), nullable=False)
    map_id = mapped_column(Integer, ForeignKey('maps.map_id'), nullable=False)
    race_number = mapped_column(Integer, nullable=False)

    act = relationship("ACT", back_populates="races")
    map = relationship("Map", back_populates="races")

class RacePlayer(Base):
    __tablename__ = "race_players"
    act_id = mapped_column(Integer, ForeignKey('acts.act_id'), primary_key=True, nullable=False)
    user_id = mapped_column(Integer, ForeignKey('users.user_id'), primary_key=True, nullable=False)
    points = mapped_column(Integer, nullable=False)

    act = relationship("ACT", back_populates="race_players")
    user = relationship("User", back_populates="race_players")

class Character(Base):
    __tablename__ = "characters"
    character_id = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    character_name = mapped_column(String, nullable=False)

    teams = relationship("Team", back_populates="character")

class Team(Base):
    __tablename__ = "teams"
    team_id = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    act_id = mapped_column(Integer, ForeignKey('acts.act_id'), nullable=False)
    character_id = mapped_column(Integer, ForeignKey('characters.character_id'), nullable=False)

    act = relationship("ACT", back_populates="teams")
    character = relationship("Character", back_populates="teams")
    players = relationship("TeamPlayer", back_populates="team")

class TeamPlayer(Base):
    __tablename__ = "team_players"
    team_id = mapped_column(Integer, ForeignKey('teams.team_id'), primary_key=True, nullable=False)
    user_id = mapped_column(Integer, ForeignKey('users.user_id'), primary_key=True, nullable=False)

    team = relationship("Team", back_populates="players")
    user = relationship("User", back_populates="team_players")

