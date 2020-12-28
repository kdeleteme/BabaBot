from sqlalchemy import Column, String, Integer

class Member(Base):
    """Represents a Discord Guild Member"""

    __tablename__ = 'member'

    id = Column(Integer, primary_key = True, unique = True)
    username = Column(String, unique = True)
    nick = Column(String)
    # Number of times ?slap was attempted
    times_tried_slapping = Column(Integer)
    # The last time ?slap was attempted
    last_time_tried_slapping = Column(Integer)
    
