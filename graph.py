from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
import json
from io import BytesIO

fig = Figure()
ax = fig.subplots()
ratings = {}
allEpisodes = []
allRatings = []
array = {'imDbId': 'tt0903747', 'title': 'Breaking Bad', 'fullTitle': 'Breaking Bad (TV Series 2008–2013)', 'type': 'TVSeries', 'year': '2008', 'episodes': [{'id': 'tt0959621', 'seasonNumber': '1', 'episodeNumber': '1', 'title': 'Pilot', 'image': 'https://m.media-amazon.com/images/M/MV5BNTZlMGY1OWItZWJiMy00MTZlLThhMGItNDQ2ODM3YzNkOWU5XkEyXkFqcGdeQXVyNzgyOTQ4MDc@._V1_Ratio1.7778_AL_.jpg', 'year': '2008', 'released': '20 Jan. 2008', 'plot': 'Diagnosed with terminal lung cancer, chemistry teacher Walter White teams up with former student Jesse Pinkman to cook and sell crystal meth.', 'imDbRating': '9.0', 'imDbRatingCount': '33850'}, {'id': 'tt1054724', 'seasonNumber': '1', 'episodeNumber': '2', 'title': "Cat's in the Bag...", 'image': 'https://m.media-amazon.com/images/M/MV5BNmI5MTU3OTAtYTczMC00MDE5LTg3YjMtMjA3NWEyMmYyZWQwXkEyXkFqcGdeQXVyNjk1MzkzMzM@._V1_Ratio1.7778_AL_.jpg', 'year': '2008', 'released': '27 Jan. 2008', 'plot': "After their first drug deal goes terribly wrong, Walt and Jesse are forced to deal with a corpse and a prisoner. Meanwhile, Skyler grows suspicious of Walt's activities.", 'imDbRating': '8.6', 'imDbRatingCount': '24777'}, {'id': 'tt1054725', 'seasonNumber': '1', 'episodeNumber': '3', 'title': "...And the Bag's in the River", 'image': 'https://m.media-amazon.com/images/M/MV5BMjI4NjIxOTkwMl5BMl5BanBnXkFtZTgwNTAwOTc5MjE@._V1_Ratio1.7778_AL_.jpg', 'year': '2008', 'released': '10 Feb. 2008', 'plot': 'Walt and Jesse clean up after the bathtub incident before Walt decides what course of action to take with their prisoner Krazy-8.', 'imDbRating': '8.7', 'imDbRatingCount': '24031'}, {'id': 'tt1054726', 'seasonNumber': '1', 'episodeNumber': '4', 'title': 'Cancer Man', 'image': 'https://m.media-amazon.com/images/M/MV5BM2ExYjhjMTEtYTEzMy00MjQyLTg2MjYtODQ0N2ZkZDRhZjgwXkEyXkFqcGdeQXVyNjkyNDM2MDc@._V1_Ratio1.7778_AL_.jpg', 'year': '2008', 'released': '17 Feb. 2008', 'plot': 'Walt tells the rest of his family about his cancer. Jesse tries to make amends with his own parents.', 'imDbRating': '8.2', 'imDbRatingCount': '23208'}, {'id': 'tt1054727', 'seasonNumber': '1', 'episodeNumber': '5', 'title': 'Gray Matter', 'image': 'https://m.media-amazon.com/images/M/MV5BNTgwOTE0ODYtMDEwNC00MjY1LWJjZDctNTU2MjRlNTgzY2NkXkEyXkFqcGdeQXVyNjg0Nzk2Nzc@._V1_Ratio1.7778_AL_.jpg', 'year': '2008', 'released': '24 Feb. 2008', 'plot': "Walt rejects everyone who tries to help him with the cancer. Jesse tries his best to create Walt's meth, with the help of an old friend.", 'imDbRating': '8.3', 'imDbRatingCount': '22794'}, {'id': 'tt1054728', 'seasonNumber': '1', 'episodeNumber': '6', 'title': "Crazy Handful of Nothin'", 'image': 'https://m.media-amazon.com/images/M/MV5BOGU0YTA2ZGItNDFjNi00NWM1LTk5NzAtYjFkYTk2MzFhY2YyXkEyXkFqcGdeQXVyNjc0NTIwNTU@._V1_Ratio1.7778_AL_.jpg', 'year': '2008', 'released': '2 Mar. 2008', 'plot': 'With the side effects and cost of his treatment mounting, Walt demands that Jesse finds a wholesaler to buy their drugs - which lands him in trouble.', 'imDbRating': '9.3', 'imDbRatingCount': '26682'}, {'id': 'tt1054729', 'seasonNumber': '1', 'episodeNumber': '7', 'title': 'A No-Rough-Stuff-Type Deal', 'image': 'https://m.media-amazon.com/images/M/MV5BNzM1OTA1NzgxOV5BMl5BanBnXkFtZTgwMjg2MDU5NTM@._V1_Ratio1.7778_AL_.jpg', 'year': '2008', 'released': '9 Mar. 2008', 'plot': 'Walt and Jesse try to up their game by making more of the crystal every week for Tuco. Unfortunately, some of the ingredients they need are not easy to find. Meanwhile, Skyler realizes that her sister is a shoplifter.', 'imDbRating': '8.8', 'imDbRatingCount': '23226'}], 'errorMessage': ''}
for i in array["episodes"]:
    ratings[f'S1E{i["episodeNumber"]}'] = i["imDbRating"]
episodeNumber = []
rating = []
for i in ratings:
                episodeNumber.append(i)
                rating.append(float(ratings[i]))
                # Collecting all episodes and ratings for overall trend
                allEpisodes.append(i)
                allRatings.append(float(ratings[i]))
x = episodeNumber
y = rating

a = []
for i in range(len(y)):
    a.append(i)
test_x = np.array(a)
test_y = np.array(y)

#z = np.polyfit(test_x, test_y, 1)
#p = np.poly1d(z)
#ax.plot(test_x,p(test_x),"r--")
#mean = sum(rating)/len(rating)
ax.stem(x,y,linefmt='C7--', markerfmt='C1o-', bottom=0, basefmt='none')
ax.set_xlabel('Episode')
ax.set_ylabel('ImDB Rating')
ax.set_yticks([0,2,4,6,8,10])
ax.axis(ymin=0,ymax=10*1.1,xmin=-1,xmax=len(allRatings))
fig.suptitle(f'Breaking Bad', fontsize=16)
fig.savefig("./test.png", format="png")