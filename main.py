from colorama import Style, Fore
import json
from pprint import pprint
from services.authentications import register, login
from models.user import User
from models.room import Room
from models.book import Book
from services import authentications, booking, filters
from models.room import Room
from services.menyu import menu, book_user


def show_menu(menu: list[tuple[int, str]]):
    for option in menu:
        print(f"{option[0]} - {option[1]}")

def main():
    choice = 0
    user: User = None
    rooms: list[Room] = []
    users: list[User] = []
    session: list[User] = []
    users: list[User]    = [] 
    rooms: list[Room]    = []
    session: list[User]  = []
    bookings: list[Book] = []
    

    guest_menu = [
        (1, "Register"),
        (2, "Login"),
        (3, "Exit")
    ]
    user_menu = [
        (1, "See available rooms"),
        (2, "Book a room"),
        (3, "Filter rooms"),
        (4, "Logout"),
        (5, "Exit")
    ]
    with open("files/rooms.json", "r", encoding="utf-8") as fayl:
        rooms = json.load(fayl)  

    while True:

        a_rooms = booking.available_rooms(rooms, bookings)
        menu()
        choose = input(f"{Style.DIM},{Fore.LIGHTRED_EX}Buyruqni kiriting --> {Style.RESET_ALL} ")

        while user:
            show_menu(user_menu)
            choice = input("choice: ")
        if choose == '1':
           
            users_new = register(users)
            bookings.append(book_user(rooms, users_new))
            users.append(users_new)

            if choice == "1":
                for a_room in a_rooms:
                    print(f"Room number: {a_room.number}, Size: {a_room.size}, Price: {a_room.price}, Type: {a_room.type}")
            elif choose == '2':
                book = booking.booking(user, a_rooms)
                bookings.append(book)
                a_rooms.remove(book.room)
                user_booking = login(users)

            elif choice == "3":
                size = int(input("size: "))
                price = float(input("price: "))
            if user_booking:

                filtered_rooms = filters.filter_rooms(a_rooms, size, price)
                for room in filtered_rooms:
                    print(f"Room number: {room.number}, Size: {room.size}, Price: {room.price}, Type: {room.type}")
                print(f"{Style.DIM},{Fore.LIGHTRED_EX}Mexmonxonaga hush kelibsi! {Style.RESET_ALL}")
                bookings.append(book_user(rooms, user_booking))

            elif choice == "4":
                session = authentications.logout(user, session)
                user = None
            elif choice == "5":
                exit()
            else:
                print("invalid option")
        while user == None:
            show_menu(guest_menu)
            choice = input("choice: ")
            print(f"{Style.DIM},{Fore.LIGHTRED_EX}Login yoki parol xato! {Style.RESET_ALL}")

            if choice == "1":
                user = authentications.register(users)
                users.append(user)
                session.append(user)
            elif choose == '3':

            
                user = authentications.login(users)
                if user:
                    session.append(user)
            print("Buncha tez ketyabsiz?\n")
            exit()

            elif choice == "3":
                exit()
            else:
                print("invalid option")
            else:
        print(f"{Style.DIM},{Fore.LIGHTRED_EX}Bunday buyrug` mavjud emas, iltimos tekshirib qaytadan kiriting! {Style.RESET_ALL}")
if __name__ == "__main__":
    main()
main()

