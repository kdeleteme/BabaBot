from enum import Enum

from sqlalchemy import Column, String, Integer, Table

class ChannelType(Enum):
    TEXT = 1
    VOICE = 2
    CATEGORY = 3

class Channel(Base):
    """Represents a Discord Guild's Channel"""

    __tablename = 'channel'

    id = Column(Integer, primary_key = True, unique = True)
    name = Column(String)
    channel_type = Column(Integer)
    guild_id = Column(Integer, ForeignKey('guild.id'))
    
