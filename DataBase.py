import SocialNetwork
from abc import ABC, abstractmethod
class User:
    def __init__(self, username: str, password: str):
        self.__username = username
        self.__password = password
        self.__following = []
        self.__followers = []
        self.__posts = []

    def get_username(self):
        return self.__username

    def getPosts(self):
        return self.__posts

    def follow(self, user):
        for temp in self.__following:
            if temp.get_username() == user.get_username():
                return
        self.__following.append(user)
        print(f"{self.__username} started following {user.get_username()}")

    def unfollow(self, user):
        for temp in self.__following:
            if temp.get_username() == user.get_username():
                self.__following.remove(user)

    def publish_post(self,*args):
        p = postFactory
        return  p.create_post(self,*args)

    def __str__(self):
        return f"User name:{self.__username}, Number Of posts: {len(self.__posts)} , Number Of followers:{len(self.__followers)}"
class post(ABC):
    @abstractmethod
    def post(self):
        pass

    @abstractmethod
    def like(self,user):
        pass

    @abstractmethod
    def comment(self,user,text):
        pass
class text_post(post):
    def __init__(self,user,text):
        self.__type='Text'
        self.__text = text
        self.__likes = []
        self.__comments = []
        self.__user=user
        print(self.__str__())

    def post(self):
        return self.__text, self.__likes, self.__comments

    def like(self,user):
        self.__likes.append(user)

    def comment(self,user,comment):
        c=Comment(user,comment)
        self.__comments.append(c)

    def __str__(self):
        return (f"{self.__user.get_username()} published a post:\n,"
                f"{self.__text}")
class img_post(post):
    def __init__(self,user, img,):
        self.__type='Image'
        self.__img = img
        self.__likes = []
        self.__comments = []
        self.__user=user
        print(self.__str__())

    def post(self):
        return self.__img, self.__likes, self.__comments

    def like(self,user):
        self.__likes.append(user)

    def comment(self, user, comment):
        c = Comment(user, comment)
        self.__comments.append(c)

    def __str__(self):
        return f"{self.__user.get_username()} posted a picture"
class sale_post(post):
    def __init__(self, product, price, location,user):
        self.__type='Sale'
        self.__product = product
        self.__price = price
        self.__location = location
        self.__likes = []
        self.__comments = []
        self.__user = user

    def post(self):
        return self.__product, self.__price,self.__location,self.__likes,self.__comments

    def like(self,user):
        self.__likes.append(user)

    def comment(self, user, comment):
        c = Comment(user, comment)
        self.__comments.append(c)
class postFactory():
    def create_post(user,*args):
        type = args[0]
        if type == "Text":
            return text_post(user,args[1])
        elif type == "Image":
            return img_post(user,args[1])
        else:
            product = args[1]
            price = args[2]
            location = args[3]
            return sale_post(product, price, location, user)
class Comment:
    def __init__(self, user: User, text: str):
        self.user = user
        self.text = text

def create_user(username: str, password: str):
    user = User(username, password)
    SocialNetwork.Users.append(user)
    return user
def find_user(username: str):
    for user in SocialNetwork.Users:
        if user.username == username:
            return user
