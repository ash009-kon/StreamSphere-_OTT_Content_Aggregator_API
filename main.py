from fastapi import FastAPI

app = FastAPI(
	title="OTT Content Aggregator API",
	description="Search movies and OTT platforms",
	version="1.0.0",
)

movies = [
	{
		"id": 1,
		"title": "Avatar",
		"year": 2009,
		"genre": "Science Fiction",
		"rating": 7.9,
		"platform": "Disney+",
	},
	{
		"id": 2,
		"title": "Inception",
		"year": 2010,
		"genre": "Sci-Fi",
		"rating": 8.8,
		"platform": "Netflix",
	},
	{
		"id": 3,
		"title": "Interstellar",
		"year": 2014,
		"genre": "Science Fiction",
		"rating": 8.7,
		"platform": "Prime Video",
	},
]


@app.get("/")
def home():
	return {"message": "Welcome to OTT Content Aggregator API"}


@app.get("/movies")
def get_movies():
	return movies


@app.get("/search")
def search_movies(title: str):
	return [movie for movie in movies if title.lower() in movie["title"].lower()]
