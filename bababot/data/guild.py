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
