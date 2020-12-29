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


from typing import str

from sqlalchemy import Column, String, Integer, Table
from sqlalchemy.orm import relationship

member_association = Table(
      'guild_member_association', Base.metadata,
      Column('guild_id', Integer, ForeignKey('guild.id')),
      Column('member_id', Integer, ForeignKey('member.id'))
)

class Guild(Base):
      """Represents a Discord Guild"""

      __tablename__ = 'guild'

      id = Column(Integer, primary_key = True, unique = True)
      name = Column(String, unique = True)
      owner_id = Column(Integer, ForeignKey('member.id'))

      members = relationship('Member', secondary = member_association,
                             back_populates = 'guilds')
      channels = relationship('Channel')

      def __repr__(self) -> str:
            return f"<Guild(name='{self.name}')>"
