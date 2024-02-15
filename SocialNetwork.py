from DataBase import create_user
Users = []
class SocialNetwork:
    __instance = None

    def __new__(cls,*args):
        if cls.__instance is None:
            cls.__instance =super().__new__(cls)
        return cls.__instance

    def __init__(self,nameOfNetwork):
        self.nameOfNetwork=nameOfNetwork
        print("The social network Twitter was created!")

    def log_in(self, username: str, password: str):
        for user in Users:
            if username == user.get_username() and password == user.get_password() and user.is_logged is False:
                user.log_in()
                print(f"{user.get_username()} connected")

    def log_out(self,username):
        for user in Users:
            if user.get_username()== username and user.is_logged is True:
                user.log_out()
                print(f"{user.get_username()} disconnected")

    def __str__(self):
        text=f"{self.nameOfNetwork} social network:\n"
        for user in Users:
            text = text +user.__str__() + "\n"
        return text


    def sign_up(self, name:str,password:str):
        for user in Users:
            if user.get_username()==name:
                return

        return create_user(name,password)
