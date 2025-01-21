from colorama import Fore, Style
from models.user import User
from models.room import Room
from models.book import Book

def booking(user: User, rooms: list[Room]) -> Book:
    room_number = int(input("room number: "))
    room_number = int(input(f"{Style.DIM},{Fore.LIGHTRED_EX}Xona raqamini kiriting --> {Style.RESET_ALL} "))
    for room in rooms:
        if room.number == room_number:
            return Book(user, room)

def available_rooms(rooms: list[Room], bookings: list[Book]):
    return [room for room in rooms if not room in bookings]
def book_room():
    room_number = int(input(f"{Style.DIM},{Fore.LIGHTRED_EX}Bron qilish uchun xona raqamini kiriting {Style.RESET_ALL}"))