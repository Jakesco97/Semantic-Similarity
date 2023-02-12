import spacy
# I read into spacy more and found out about model sizes
# using sm small gives movie g as the recommended
# using lg large gives movie c which is interesting to see the difference
nlp = spacy.load("en_core_web_sm")


movies = [{"title": "Movie A", "description": "When Hiccup discovers Toothless isn't the only Night Fury, he must seek \"The Hidden World\", a secret Dragon Utopia before a hired tyrant named Grimmel finds it first."},
          {"title": "Movie B", "description": "After the death of Superman, several new people present themselves as possible successors."},
          {"title": "Movie C", "description": "A darkness swirls at the center of a world-renowned dance company, one that will engulf the artistic director, an ambitious young dancer, and a grieving psychotherapist. Some will succumb to the nightmare. Others will finally wake up."},
          {"title": "Movie D", "description": "A humorous take on Sir Arthur Conan Doyle's classic mysteries featuring Sherlock Holmes and Doctor Watson."},
          {"title": "Movie E", "description": "A 16-year-old girl and her extended family are left reeling after her calculating grandmother unveils an array of secrets on her deathbed."},
          {"title": "Movie F", "description": "In the last moments of World War II, a young German soldier fighting for survival finds a Nazi captain's uniform. Impersonating an officer, the man quickly takes on the monstrous identity of the perpetrators he is trying to escape from."},
          {"title": "Movie G", "description": "The world at an end, a dying mother sends her young son on a quest to find the place that grants wishes."},
          {"title": "Movie H", "description": "A musician helps a young singer and actress find fame, even as age and alcoholism send his own career into a downward spiral."},
          {"title": "Movie I", "description": "Corporate analyst and single mom, Jen, tackles Christmas with a business-like approach until her uncle arrives with a handsome stranger in tow."},
          {"title": "Movie J", "description": "Adapted from the bestselling novel by Madeleine St John, Ladies in Black is an alluring and tender-hearted comedy drama about the lives of a group of department store employees in 1959 Sydney."},]

def get_similar_movie(description):
    # processes the movies description into spacy
    query = nlp(description)
    # initialises the most_similar variable and highest_similarity
    most_similar = None
    highest_similarity = 0
    # iterates over the movies list
    for movie in movies:
        # processes the descriptions into a spacy document
        movie_description = nlp(movie["description"])
        # works out the similarity between the input and the current movie
        similarity = query.similarity(movie_description)
        # uses if statments to replace the most_similar movie with the current highest and returns it
        if similarity > highest_similarity:
            highest_similarity = similarity
            most_similar = movie["title"]
    return most_similar

planet_hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# prints the movie with the highest similarity to planet hulk
print(get_similar_movie(planet_hulk))
