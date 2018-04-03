
import random
import webbrowser


class Video():
    
    """Superclass for all video content.
    
    Both the Movie and TV_Show subclasses inherit the base attributes of a Video. 
    These attributes are 'things' that both Movies and TV Shows share. 
    
    Attributes:
    title (str): Describes the title of the video content
    duration (str): Describes the duration of the video content
    poster_image_url (str): Describes a link to a poster for the video content
   
    """

    def __init__(self, title_name, title_duration, poster_image):      
        """Init class constructor.
        
        Params: 
        title_name (str): Provide a title 
        title_duration (str): Provide a duration 
        poster_image (str): Provides poster url 
        """
        self.title = title_name
        self.duration = title_duration
        self.poster_image_url = poster_image

class Movie(Video):
    
    """Sub-class that represents a single feature title e.g. Batman: The Dark Knight.
    
    The Movie class inherits base attributes from Video and includes additional attributes
    that are unique to a user's interest, in a feature film. 
    
    Attributes: 
    quotes (list): Describes a set of quotes (strings) from the feature film
    storyline (str): Describes the storyline of the feature film
    trailer_youtube_url (str): Describes a link to the YouTube trailer
    
    """
    
    def __init__(self, title_name, title_duration, poster_image, title_quotes, movie_storyline, trailer_youtube):
        """Init class constructor.
        
        Params: 
        title_quotes (list): Provide a list of quotes
        movie_storyline (str): Provide a storyline
        trailer_youtube (str): Provides trailer url 
        """       
        Video.__init__(self, title_name, title_duration, poster_image)
        self.quotes = title_quotes
        self.storyline = movie_storyline
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Open the movie's trailer in the default browser."""
        webbrowser.open(self.trailer_youtube_url)

    def random_quote(self):
        """Return a randomly selected quote from a list of quotes."""
        random_number = random.randint(0,1)
        return self.quotes[random_number]

class TV_Show(Video):
    """Sub-class that represents a TV brand e.g. Breaking Bad.
    
    The TV Show class inherits base attributes from Video and includes additional attributes
    that are unique to a user's interest, in a television brand. 
    
    Attributes: 
    review (str): Describes a set of quotes (strings) from the feature film
    listing (str): Describes a link to listings for where to watch the show 
    
    """
    
    def __init__(self, title_name, title_duration, poster_image, tv_review, tv_listing_url):
        """Init class constructor.
        
        Params: 
        tv_review (str): Provide a brand review
        tv_listing_url (str): Provide a tv listing url 
        """       
        Video.__init__(self, title_name, title_duration, poster_image)
        self.review = tv_review
        self.listing = tv_listing_url

