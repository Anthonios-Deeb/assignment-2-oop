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

    def sign_up(self, name:str,password:str):
        return create_user(name,password)
