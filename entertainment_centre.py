import media
import fresh_tomatoes3

hidden_figures = media.Movie("Hidden Figures",
                            "120m",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMzg2Mzg4YmUtNDdkNy00NWY1LWE3NmEtZWMwNGNlMzE5YzU3XkEyXkFqcGdeQXVyMjA5MTIzMjQ@._V1_UX182_CR0,0,182,268_AL_.jpg",
                            ["Here at NASA we all pee the same color",
                            "Every time we get a chance to get ahead they move the finish line. Every time."],
                            "Creating the future, requires change in the present",
                            "https://youtu.be/5wfrDhgUMGI")

spotlight = media.Movie("Spotlight",
                        "120m",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIyOTM5OTIzNV5BMl5BanBnXkFtZTgwMDkzODE2NjE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        ["If it takes a village to raise a child, it takes a village to abuse one",
                        "How do you say 'no' to God, right?"],
                        "To break the story, they broke the silence",
                        "https://youtu.be/t8P2TUI7yJw")


three_billboards = media.Movie("Three Billboards",
                                "120m",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BZTZjYzU2NTktNTdmNi00OTM0LTg5MDgtNGFjOGMzNjY0MDk5XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX675_CR0,0,675,999_AL_.jpg",
                                ["All this anger, man, it just begets greater anger",
                                "My daughter Angela was murdered 7 months ago, it seems to me the police department is too busy torturing black folk to solve actual crimes"],
                                "A story of retribution born from a mother's desire, for justice",
                                "https://youtu.be/Jit3YhGx5pU")

thor_ragnorak = media.Movie("Thor: Ragnorak",
                            "120m",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMjMyNDkzMzI1OF5BMl5BanBnXkFtZTgwODcxODg5MjI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                            ["<b>Loki:</b> I have been falling ...for 30 minutes!",
                            "Last time we saw you, you were trying to kill everyone. What are you up to these days?"],
                            "Thor must fight for survival and race against time to prevent the all-powerful Hela from destroying his home and the Asgardian civilization.",
                            "https://www.youtube.com/watch?v=ue80QwXMRHg")

lost_translation = media.Movie("Lost in Translation",
                                "120m",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BMTI2NDI5ODk4N15BMl5BanBnXkFtZTYwMTI3NTE3._V1_UX182_CR0,0,182,268_AL_.jpg",
                                ["Let's never come here again because it would never be as much fun",
                                "I just don't know what I'm supposed to be"],
                                "It takes a new friendship for two people to realise they're lost in more than just a new country.",
                                "https://youtu.be/W6iVPCRflQM")

walking_dead = media.TV_Show("The Walking dead",
                        "25m",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMzNkMWNmZGUtNWFlZi00MTYwLWIwMjQtOGViN2QzNmI2MWYwXkEyXkFqcGdeQXVyODA1MDc5NjM@._V1_UY268_CR0,0,182,268_AL_.jpg",
                        "'The Zombies are stupid' - Ian Walker : 2017",
                        ["3", "9"],
                        "http://www.radiotimes.com/tv-programme/2yh/the-walking-dead/")



movies = [hidden_figures, spotlight, three_billboards, thor_ragnorak, lost_translation]
tv_shows = [walking_dead]

fresh_tomatoes3.open_movies_page(movies, tv_shows)

#print media.Movie.__doc__
