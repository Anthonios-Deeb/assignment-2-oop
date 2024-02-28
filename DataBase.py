import SocialNetwork
import matplotlib.image as mpimage
import matplotlib.pyplot as plt

from abc import ABC, abstractmethod


#this is an abstarct class
class Sender(ABC):
    def __init__(self):
        self.followers = []

    # this function goes over all the followers of a user and adds a notification to that follower using the function
    # update
    def notify(self, notification):
        for follower in self.followers:
            follower.update(notification)

    # this is an abstract class that has the function update
class Member(ABC):
    @abstractmethod
    def update(self, notification):
        pass


    # this is the user class
class User(Sender, Member):
    def __init__(self, username: str, password: str):
        self.is_logged = True
        self.__username = username
        self.__password = password
        self.__following = []
        self.__posts = []
        self.__notifications = []
        super().__init__()

    # this is a get function for the password of the user
    def get_password(self):
        return self.__password

    # this function makes the user logged in
    def log_in(self):
        self.is_logged = True

    # this function makes the user log out
    def log_out(self):
        self.is_logged = False

    # this is a get function for the username of the user
    def get_username(self):
        return self.__username

    # this is a get function for the posts that the user that has posted
    def getPosts(self):
        return self.__posts

    # this function receives a user and checks if the self.user is following this user if not it follows
    # and sends a notification to the user that it followed,
    # if self.user does follow the user that the function received it returns
    # the user can not do this action if logged out, the function checks if logged out and it exits
    def follow(self, user):
        if self.is_logged is False:
            return

        for temp in self.__following:
            if temp.get_username() == user.get_username():
                return

        self.__following.append(user)
        user.followers.append(self)
        print(f"{self.__username} started following {user.get_username()}")

    # this function receives a user and checks if the self.user is following this user if it does it unfollow,
    # if self.user doesn't follow the user that the function received it returns
    # the user can not do this action if logged out, the function checks if logged out and it exits
    def unfollow(self, user):
        if self.is_logged is False:
            return

        for temp in self.__following:
            if temp.get_username() == user.get_username():
                self.__following.remove(user)
                temp.followers.remove(self)
                print(f"{self.get_username()} unfollowed {temp.get_username()}")

    # this function publishes a post and returns it,
    # after adding the post to the array that contains all the posts for the user.
    # the user can not do this action if logged out, the function checks if logged out and it exits
    def publish_post(self, *args):
        if self.is_logged is False:
            return
        p = postFactory
        post = p.create_post(self, *args)
        print(post)
        self.__posts.append(post)
        self.notify(f"{self.__username} has a new post")
        return post

    # this function adds a notification for the user by adding it to the notifications array
    def update(self, notification):
        self.__notifications.append(notification)

    # this function prints all the notifications of the user
    def print_notifications(self):
        print(f"{self.__username}'s notifications:")
        for notification in self.__notifications:
            print(notification)

    # this function prints the name, number of posts and the number of followers of the user
    def __str__(self):
        return f"User name: {self.__username}, Number of posts: {len(self.__posts)}, Number of followers: {len(self.followers)}"

    # this is the post class it contains the likes and comments and who posted this post and the type of the post
    # this class is part of the factory
class post():
    def __init__(self, type, user):
        self.__type = type
        self.__likes = []
        self.__comments = []
        self._user = user

    # this function receives a user and checks if the user likes this post if it does exits, if not the function
    # likes by adding the user to the like lists and sends a notification to the user that posted the post
    # the user can not do this action if logged out, the function checks if logged out and it exits
    def like(self, user):
        if self._user.is_logged is False:
            return
        for temp in self.__likes:
            if temp.get_username() == user.get_username():
                return

        if user.get_username() == self._user.get_username():
            self.__likes.append(user)
            return

        text = f"{user.get_username()} liked your post"
        print(f"notification to {self._user.get_username()}: {text}")
        self._user.update(text)
        self.__likes.append(user)

    # comments by generating a comment and adding it to the comments array
    # then sends a notification to the user that posted the post
    # the user can not do this action if logged out, the function checks if logged out and it exits
    def comment(self, user, comment):
        if self._user.is_logged is False:
            return
        if user.get_username() == self._user.get_username():
            c = Comment(user, comment)
            self.__comments.append(c)
            return
        text = f"{user.get_username()} commented on your post: {comment}"
        print(f"notification to {self._user.get_username()}: {text}")
        self._user.update(f"{user.get_username()} commented on your post")
        c = Comment(user, comment)
        self.__comments.append(c)

# class is part of the factory, this is the text post class, it inherits from the post class.
class text_post(post):
    # this is the constructor where the test post is made.
    def __init__(self, user, text):
        super().__init__('Text', user)
        self._text = text

    # this function prints who posted the post and the text that he posted
    def __str__(self):
        return (f"{self._user.get_username()} published a post:\n"
                f"\"{self._text}\"\n")

# class is part of the factory, this is the image post class, it inherits from the post class.
class img_post(post):
    # this is the constructor where the image post is made.
    def __init__(self, user, img, ):
        super().__init__('Image', user)
        self.__img = img

    # this function displays the image that the user posted using a library
    def display(self):
        print("Shows picture")
        img = mpimage.imread(self.__img)
        plt.imshow(img)
        plt.show()

    # this function prints that a certain user posted a picture
    def __str__(self):
        return f"{self._user.get_username()} posted a picture\n"

# class is part of the factory, this is the sale post class, it inherits from the post class.
class sale_post(post):
    # this is the constructor where the sale post is made
    def __init__(self, product, price, location, user):
        super().__init__('Sale', user)
        self.__isSold = False
        self.__product = product
        self.__price = price
        self.__location = location

    # this function makes the items sold if it is not sold yet
    # it checks if the user is logged in and if the password is the same as the password of the user
    def sold(self, password):
        if self._user.is_logged is False:
            return
        if self.__isSold is True:
            return
        if self._user.get_password() != password:
            return
        print(f"{self._user.get_username()}'s product is sold")
        self.__isSold = True

    # this function makes a discount
    # it checks if the user is logged in and if the password is the same as the password of the user
    # also checks if the item is not sold then it makes the discount and prints the new price
    def discount(self, percentage, password):
        if self._user.is_logged is False:
            return
        if self.__isSold is True:
            return
        if self._user.get_password() != password:
            return
        self.__price = (self.__price * (100 - percentage)) / 100
        print(f"Discount on {self._user.get_username()} product! the new price is: {self.__price}")

    # this function prints the info about the sale post
    def __str__(self):
        if self.__isSold is False:
            sold = "For sale!"
        else:
            sold = "Sold!"

        return f"{self._user.get_username()} posted a product for sale:\n{sold} {self.__product}, price: {self.__price}, pickup from: {self.__location}\n"

# this is the post factory
class postFactory():

    # this function creates the post
    # it checks by the type and creates the post of the same time
    def create_post(user, *args):
        type = args[0]
        if type == "Text":
            return text_post(user, args[1])
        elif type == "Image":
            return img_post(user, args[1])
        else:
            product = args[1]
            price = args[2]
            location = args[3]
            return sale_post(product, price, location, user)

# this is a comment class that contains a text and the user that posted the comment
class Comment:
    def __init__(self, user: User, text: str):
        self.user = user
        self.text = text

# this function helps to create the user
# after generating the user it adds it to the list of users
def create_user(username: str, password: str):
    user = User(username, password)
    SocialNetwork.Users.append(user)
    return user
