import SocialNetwork
import matplotlib.image as mpimage
import matplotlib.pyplot as plt

from abc import ABC, abstractmethod

class Sender(ABC):
    def __init__(self):
        self.followers=[]

    def notify(self,notification):
        for follower in self.followers:
            follower.update(notification)

class Member(ABC):
    @abstractmethod
    def update(self,notification):
        pass


class User(Sender,Member):
    def __init__(self, username: str, password: str):
        self.is_logged=True
        self.__username = username
        self.__password = password
        self.__following = []
        self.__posts = []
        self.__notifications = []
        super().__init__()


    def get_password(self):
        return self.__password

    def log_in(self):
         self.is_logged=True

    def log_out(self):
        self.is_logged=False

    def get_username(self):
        return self.__username

    def getPosts(self):
        return self.__posts

    def follow(self, user):
        if self.is_logged is False:
            return

        for temp in self.__following:
            if temp.get_username() == user.get_username():
                return
        self.__following.append(user)
        user.followers.append(self)
        print(f"{self.__username} started following {user.get_username()}")

    def unfollow(self, user):
        if self.is_logged is False:
            return

        for temp in self.__following:
            if temp.get_username() == user.get_username():
                self.__following.remove(user)
                temp.followers.remove(self)
                print(f"{self.get_username()} unfollowed {temp.get_username()}")

    def publish_post(self,*args):
        p = postFactory
        post=p.create_post(self, *args)
        print(post)
        self.__posts.append(post)
        self.notify(f"{self.__username} has a new post")
        return post

    def update(self,notification):
        self.__notifications.append(notification)

    def print_notifications(self):
        print(f"{self.__username}'s notifications:")
        for notification in self.__notifications:
            print(notification)

    def __str__(self):
        return f"User name: {self.__username}, Number of posts: {len(self.__posts)}, Number of followers: {len(self.followers)}"


class post(ABC):
    @abstractmethod
    def post(self):
        pass


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

    def post(self):
        return self.__text, self.__likes, self.__comments

    def like(self,user):
        if self.__user.is_logged is False:
            return
        if user.get_username() == self.__user.get_username():
            self.__likes.append(user)
            return
        text = f"{user.get_username()} liked your post"
        print(f"notification to {self.__user.get_username()}: {text}")
        self.__user.update(text)
        self.__likes.append(user)

    def comment(self,user,comment):
        if self.__user.is_logged is False:
            return
        if user.get_username() == self.__user.get_username():
            c = Comment(user, comment)
            self.__comments.append(c)
            return
        text = f"{user.get_username()} commented on your post: {comment}"
        print(f"notification to {self.__user.get_username()}: {text}")
        self.__user.update(f"{user.get_username()} commented on your post")
        c=Comment(user,comment)
        self.__comments.append(c)

    def __str__(self):
        return (f"{self.__user.get_username()} published a post:\n"
                 f"\"{self.__text}\"\n")

class img_post(post):
    def __init__(self,user, img,):
        self.__type='Image'
        self.__img = img
        self.__likes = []
        self.__comments = []
        self.__user=user

    def post(self):
        return self.__img, self.__likes, self.__comments

    def like(self,user):
        if self.__user.is_logged is False:
            return
        if user.get_username() == self.__user.get_username():
            self.__likes.append(user)
            return
        text=f"{user.get_username()} liked your post"
        print(f"notification to {self.__user.get_username()}: {text}")
        self.__user.update(text)
        self.__likes.append(user)

    def comment(self, user, comment):
        if self.__user.is_logged is False:
            return
        if user.get_username() == self.__user.get_username():
            c = Comment(user, comment)
            self.__comments.append(c)
            return
        text = f"{user.get_username()} commented on your post: {comment}"
        print(f"notification to {self.__user.get_username()}: {text}")
        self.__user.update(f"{user.get_username()} commented on your post")
        c = Comment(user, comment)
        self.__comments.append(c)

    def display(self):
        print("Shows picture")
        img=mpimage.imread(self.__img)
        plt.imshow(img)
        plt.show()

    def __str__(self):
        return f"{self.__user.get_username()} posted a picture\n"
class sale_post(post):
    def __init__(self, product, price, location,user):
        self.__isSold=False
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
        if self.__user.is_logged is False:
            return
        if user.get_username() == self.__user.get_username():
            self.__likes.append(user)
            return
        text = f"{user.get_username()} liked your post"
        print(f"notification to {self.__user.get_username()}: {text}")
        self.__user.update(text)
        self.__likes.append(user)

    def comment(self, user, comment):
        if self.__user.is_logged is False:
            return
        if user.get_username() == self.__user.get_username():
            c = Comment(user, comment)
            self.__comments.append(c)
            return
        text = f"{user.get_username()} commented on your post: {comment}"
        print(f"notification to {self.__user.get_username()}: {text}")
        self.__user.update(f"{user.get_username()} commented on your post")
        c = Comment(user, comment)
        self.__comments.append(c)

    def sold(self,password):
        if self.__user.is_logged is False:
            return
        if   self.__isSold is True:
            return
        if self.__user.get_password()!= password:
            return
        print(f"{self.__user.get_username()}'s product is sold")
        self.__isSold=True

    def discount(self,percentage,password):
        if self.__user.is_logged is False:
            return
        if self.__user.get_password()!=password:
            return
        self.__price= (self.__price*(100-percentage))/100
        print(f"Discount on {self.__user.get_username()} product! the new price is: {self.__price}")

    def __str__(self):
        if(self.__isSold==False):
            sold="For sale!"
        else:
            sold="Sold!"

        return f"{self.__user.get_username()} posted a product for sale:\n{sold} {self.__product}, price: {self.__price}, pickup from: {self.__location}\n"

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
