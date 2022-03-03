import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Get content from Empire website.
response = requests.get(url=URL)
content = response.text
# Create soup.
soup = BeautifulSoup(content, "html.parser")
# Break down soup to include only lines with the specified restraints.
movie_titles = soup.find_all(name="h3", class_="title")
# Use list comprehension to get the text which is movie rank and movie title.
titles = [title.getText() for title in movie_titles]
# Slice the list so its reverse order.
movies = titles[::-1]
# Create or open the file movies.txt then write to it the top 100 movies we scrapped from the Empire website.
with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
