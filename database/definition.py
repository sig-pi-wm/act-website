from sqlalchemy.orm import DeclarativeBase
import helpers as helpers
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.orm import mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    user_id = mapped_column(Integer, primary_key=True, autoincrement=True)
    username = mapped_column(String, nullable=False)

class ACT(Base):
    __tablename__ = "acts"
    act_id = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    date = mapped_column(Date, nullable=False)

class Map(Base):
    __tablename__ = "maps"
    map_id = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    map_name = mapped_column(String, nullable=False)

class Race(Base):
    __tablename__ = "races"
    race_id = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    act_id = mapped_column(Integer, ForeignKey('acts.act_id'), nullable=False)
    map_id = mapped_column(Integer, nullable=False)
    race_number = mapped_column(Integer, nullable=False)

    act = relationship("ACT", back_populates="races")

class RacePlayer(Base):
    __tablename__ = "race_players"
    act_id = mapped_column(Integer, ForeignKey('acts.act_id'), primary_key=True, nullable=False)
    user_id = mapped_column(Integer, ForeignKey('users.user_id'), primary_key=True, nullable=False)
    points = mapped_column(Integer, nullable=False)

    act = relationship("ACT", back_populates="acts")
    user = relationship("User", back_populates="users")

class Character(Base):
    __tablename__ = "characters"
    character_id = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    character_name = mapped_column(String, nullable=False)

class Team(Base):
    __tablename__ = "teams"
    team_id = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    act_id = mapped_column(Integer, ForeignKey('acts.act_id'), nullable=False)
    character_id = mapped_column(Integer, ForeignKey('characters.character_id'), nullable=False)

    act = relationship("ACT", back_populates="acts")
    character = relationship("Character", back_populates="characters")

class TeamPlayer(Base):
    __tablename__ = "team_players"
    team_id = mapped_column(Integer, ForeignKey('teams.team_id'), primary_key=True, nullable=False)
    user_id = mapped_column(Integer, ForeignKey('users.user_id'), primary_key=True, nullable=False)

    team = relationship("Team", back_populates="teams")
    user = relationship("User", back_populates="users")
