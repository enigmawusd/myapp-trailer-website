#media.py
#Class defination for movie trailer website.

import webbrowser

class Movie():
    '''Provides way to store movie related information.'''
	
    def __init__(self, m_title, m_genre, m_storyline, m_poster_url, m_trailer_url):
	'''[ Iniatialise and create memory space for instance variables. ]'''

        self.title = m_title
        self.genre = m_genre
        self.storyline = m_storyline 
        self.poster_url = m_poster_url 
        self.trailer_url = m_trailer_url

    def show_trailer(self):
	'''[ Open youtube trailer webpage in web-browser. ]'''

        webbrowser.open(self.trailer_url)
        

