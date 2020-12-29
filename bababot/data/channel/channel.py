# Copyright (C) 2020  Kent Delante <kdeleteme@tutanota.com>

# This file is part of BabaBot

# BabaBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# BabaBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with BabaBot.  If not, see <https://www.gnu.org/licenses/>.


from enum import Enum
from typing import str

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
    
    def __repr__(self) -> str:
        if self.channel_type is ChannelType.TEXT:
            channel_type = 'text'
        elif self.channel_type is ChannelType.VOICE:
            channel_type = 'voice'
        elif self.channel_type is ChannelType.CATEGORY:
            channel_type = 'category'
        else:
            channel_type = 'undefined'

        return f"<Channel(name='{self.name}', channel_type='{channel_type}')>"
            
            
