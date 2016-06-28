from xml.dom.minidom import parse

DOMTree = parse("movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print("Root Element: %s"%collection.getAttribute("shelf"))

movies = collection.getElementsByTagName("movie")

for movie in movies:
    print("******Movie******")

    movie_type = movie.getElementsByTagName('type')
    print(movie_type[-1].childNodes[-1].data)
    movie_format = movie.getElementsByTagName('format')
    print(movie_format[-1].childNodes[-1].data)
    movie_format = movie.getElementsByTagName('rating')
    print(movie_format[-1].childNodes[-1].data)
    movie_format = movie.getElementsByTagName('description')
    print(movie_format[-1].childNodes[-1].data)
