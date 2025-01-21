from .user import User
from .room import Room

class Book:
    def __init__(self, user: User, room: Room):
        self.user = user
        self.room = room
    
        self.room = room
    