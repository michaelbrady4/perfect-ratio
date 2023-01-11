# !pip install instaloader
import instaloader


def get_big_timers(username: str, password: str) -> list:
    # Username and password
    USERNAME = username
    PASSWORD = password

    if USERNAME == "nathanwisherd":
        return "MEME"

    # Get instance
    L = instaloader.Instaloader()

    # Login
    # Using strings as login info
    L.login(USERNAME, PASSWORD)
    # Using terminal login to type in password (when you type in a letter it will not show up in the terminal but it is recording it)
    # L.interactive_login(USERNAME)  # Prompts for password in terminal

    # Create an instance of a profile
    profile = instaloader.Profile.from_username(L.context, USERNAME)

    # Add each username that you follow to a list
    followees = []
    for followee in profile.get_followees():
        followees.append(followee.username)

    # Add each username that follows you to a list
    followers = []
    for follower in profile.get_followers():
        followers.append(follower.username)

    # print(f"Number of people you follow: {len(followees)}")
    # print(f"Number of people who follow you: {len(followers)}")

    # People who don't follow you back
    big_timers = []
    # print("These are the people who do not follow you back:")
    for name in followees:
        if name not in followers:
            big_timers.append(name)
            # print(name)
    
    return big_timers