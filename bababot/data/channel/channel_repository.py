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


from typing import list

from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

from bababot.data.channel import Channel

Channels = list[Channel]

class ChannelRepository:
    def __init__(self, engine: Engine):
        self.__session = sessionmaker(bind=engine)

    def add(self, channel: Channel):
        self.__session.add(channel)
        self.__session.commit()

    def add_multiple(self, channels: Channels):
        self.__session.add_all(channels)
        self.__session.commit()
