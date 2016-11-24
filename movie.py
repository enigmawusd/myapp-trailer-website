#movie.py
#Movies for movie trailer website.

import media
import fresh_tomatoes

movie1 = media.Movie("Toy Story (1995)",
    "Animation, Adventure, Comedy",
    "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

movie2 = media.Movie("Avtaar (2009)",
    "Action, Adventure, Fantasy",
    "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

movie3 = media.Movie("Megamind (2010)",
    "Animation, Action, Comedy",
    "The supervillain Megamind finally defeats his nemesis, the superhero Metro Man. But without a hero, he loses all purpose and must find new meaning to his life.",
    "https://upload.wikimedia.org/wikipedia/en/8/89/Megamind2010Poster.jpg",
    "https://www.youtube.com/watch?v=Xu42-p6_5RE")

movie4 = media.Movie("Prometheus (2012)",
    "Adventure, Mystery, Sci-Fi",
    "Following clues to the origin of mankind a team journey across the universe and find a structure on a distant moon containing a monolithic statue of a humanoid head and stone cylinders of alien blood but they soon find they are not alone.",
    "https://upload.wikimedia.org/wikipedia/en/a/a3/Prometheusposterfixed.jpg",
    "https://www.youtube.com/watch?v=34cEo0VhfGE")

movie5 = media.Movie("Shrek (2001)",
    "Animation, Adventure, Comedy",
    "After his swamp is filled with magical creatures, an ogre agrees to rescue a princess for a villainous lord in order to get his land back.",
    "https://upload.wikimedia.org/wikipedia/en/3/39/Shrek.jpg",
    "https://www.youtube.com/watch?v=ooJJX3R42WM")

movie6 = media.Movie("Lucy (2014)",
    "Action, Sci-Fi, Thriller",
    "A woman, accidentally caught in a dark deal, turns the tables on her captors and transforms into a merciless warrior evolved beyond human logic.",
    "https://upload.wikimedia.org/wikipedia/en/1/14/Lucy_%282014_film%29_poster.jpg",
    "https://www.youtube.com/watch?v=6Vu081NOorA")

#Creating list of instances of movies.
movies = [movie1, movie2, movie3, movie4, movie5, movie6]

#Uses list of movie instances as input to generate an HTML file and open it in the browser.
fresh_tomatoes.open_movies_page(movies)
