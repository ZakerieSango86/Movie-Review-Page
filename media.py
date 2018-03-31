
import random
import webbrowser


class Video():
    """A title is an individual title, like a specific program or movie, or an episode of a series"""

    def __init__(self, title_name, title_duration, poster_image):
        self.title = title_name
        self.duration = title_duration
        self.poster_image_url = poster_image

class Movie(Video):
    """This code allows you to store movie information"""

    def __init__(self, title_name, title_duration, poster_image, title_quotes, movie_storyline, trailer_youtube):
        Video.__init__(self, title_name, title_duration, poster_image)
        self.quotes = title_quotes
        self.storyline = movie_storyline
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def random_quote(self):
        """ return a randomly selected quote from a list """
        random_number = random.randint(0,1)
        return self.quotes[random_number]

class TV_Show(Video):

    def __init__(self, title_name, title_duration, poster_image, episode_review, season_episode, tv_listing_url):
        Video.__init__(self, title_name, title_duration, poster_image)
        self.review = episode_review
        self.season = season_episode #list
        self.listing = tv_listing_url

#    def get_tv_listing()
#    """Return a full tv listing url based on series and episode number"""
