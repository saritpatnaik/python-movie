import media
import fresh_tomatoes

#instantiating the movie objects
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that comes to life",
                        "https://goo.gl/4ZBxcU",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar0",
                     "alien ki kahani",
                     "https://goo.gl/tyN2TQ",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

bang_bang = media.Movie("Bang Bang",
                        "story of a spy",
                        "https://goo.gl/sg2fzV",
                        "https://www.youtube.com/watch?v=LRARHtMzZQE")


mission_impossible = media.Movie("Mission Impossible",
                                 "Story of a spy",
                                 "https://goo.gl/LUkBxg",
                                 "https://www.youtube.com/watch?v=QBavzf2_ook")

interstellar = media.Movie("Interstellar",
                           "Space exploration",
                           "https://goo.gl/aS9niu",
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

#movie objects stored in a list
movies = [toy_story, avatar, mission_impossible, bang_bang, interstellar]
fresh_tomatoes.open_movies_page(movies)
