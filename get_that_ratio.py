import instaloader


def get_big_timers(username: str, password: str) -> list:
    USERNAME = username
    PASSWORD = password

    # Create instance
    L = instaloader.Instaloader()
    # Login using strings passed in
    L.login(USERNAME, PASSWORD)
    # Create an instance of a the user's profile
    profile = instaloader.Profile.from_username(L.context, USERNAME)

    # Add each username that you follow to a list
    followees = set()
    for followee in profile.get_followees():
        followees.add(followee.username)
    # Add each username that follows you to a list
    followers = set()
    for follower in profile.get_followers():
        followers.add(follower.username)
    
    return list(followees - followers)
