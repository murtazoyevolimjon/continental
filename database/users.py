class User:
    def __init__(username: str, password: float):
        self.username = username
        self.password = password

        def add_user(username,password):
            users.append(User(username, password))


            def authenticate(username,password):
                return any(user.username == username and user.password == password for user in users)
            
