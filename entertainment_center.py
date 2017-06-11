import fresh_tomatoes
import media
#create Movie instance "me_before_you" using media.py file
me_before_you = media.Movie ("Me Before You",
                             "A girl in a small town forms an unlikely bond "
                             "with a recently-paralyzed man she's taking "
                             "care of",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ2NjE4NDE2NV5BMl5BanBnXkFtZTgwOTcwNDE5NzE@._V1_UY1200_CR90,0,630,1200_AL_.jpg", #NOQA
                             "https://www.youtube.com/watch?v=Eh993__rOxA")
#create Movie instance "avatar"
avatar = media.Movie ("Avatar",
                      "A marine on an alien planet",
                      "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp", #NOQA
                      "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#create Movie instance "gladiator"
gladiator = media.Movie ("Gladiator",
                         "a general becomes a slave, become a gladiator and "
                         "defy the emperor",
                         "http://t3.gstatic.com/images?q=tbn:ANd9GcRuhegCaGHfcQc-Owpib9vGSO0hUlSUMTojO2s4ih8oXqHBw2ks", #NOQA
                         "https://www.youtube.com/watch?v=owK1qxDselE")
#create Movie instance "last_king_of_scotland"
last_king_of_scotland = media.Movie ("Last King Of Scotland",
                                     "A scottish doctor going to Ugunda "
                                     "influencing the political system",
                                     "https://englishessaysfred.files.wordpress.com/2011/11/the-last-king-of-scotland-original-1.jpg?w=348&h=510", #NOQA
                                     "https://www.youtube.com/watch?v=iV_QgKJFZP0")
#create Movie instance "ip_man"
ip_man = media.Movie ("Ip man",
                      "The beauty and philosophy of Chinese Martial arts",
                      "http://www.gstatic.com/tv/thumb/movieposters/3586588/p3586588_p_v8_ac.jpg", #NOQA
                      "https://www.youtube.com/watch?v=1AJxXQ7xojE")
#create Movie instance "if_only"
if_only = media.Movie ("If Only",
                       "A man waking up finding his dead wife back to life "
                       "and having a second chance",
                       "http://www.gstatic.com/tv/thumb/movieposters/160181/p160181_p_v8_ae.jpg", #NOQA
                       "https://www.youtube.com/watch?v=3z5XDNHmBco")
#append all Movie instances into "movies" list
movies = [me_before_you, avatar, gladiator, last_king_of_scotland, ip_man,
          if_only]
#call open_movies_page function from fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
