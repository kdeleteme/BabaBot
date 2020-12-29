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


import os

from typing import str

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

class Database:
    engine: Engine

    def __init__(self):
        self.__pg_user = os.getenv('POSTGRES_USER')
        self.__pg_pass = os.getenv('POSTGRES_PASSWORD')
        self.__pg_db = os.getenv('POSTGRES_DB')
        self.__pg_host = os.getenv('POSTGRES_HOST')
        uri = f"postgresql://{self.__pg_user}:" \
            f"{self.__pg_pass}@{self.__pg_host}:" \
            f"{self.pg_port}/{self.pg_db}"
            
        self.engine = create_engine(uri) 
