import webbrowser


class Movie():
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
     #constructor to create instance of the movie
    def __init__(self, movie_title, movie_story, poster, trailer):
        self.title = movie_title
        self.story = movie_story
        self.poster_url = poster
        self.trailer_youtube = trailer
        
    #function to show the trailer
    def show_trailer(self, ):
        webbrowser.open(self.trailer_youtube)
