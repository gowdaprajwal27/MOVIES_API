from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
from models import Movie, Rating, Review
from sentiments import analyze_sentiment
from recommender import recommend_movies
import os

ROOT_PATH = os.getenv("ROOT_PATH", "")

app = FastAPI(
    title="Movie Recommendation API",
    root_path=ROOT_PATH,
    docs_url="/docs",
    openapi_url="/openapi.json"
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🎬 Movies
@app.post("/movies")
def add_movie(title: str, genre: str, db: Session = Depends(get_db)):
    movie = Movie(title=title, genre=genre)
    db.add(movie)
    db.commit()
    return movie

@app.get("/movies")
def get_movies(db: Session = Depends(get_db)):
    return db.query(Movie).all()

# ⭐ Ratings
@app.post("/ratings")
def add_rating(user_id: int, movie_id: int, rating: float, db: Session = Depends(get_db)):
    r = Rating(user_id=user_id, movie_id=movie_id, rating=rating)
    db.add(r)
    db.commit()
    return {"message": "Rating added"}

# 🧠 Reviews + Sentiment
@app.post("/reviews")
def add_review(user_id: int, movie_id: int, review: str, db: Session = Depends(get_db)):
    sentiment = analyze_sentiment(review)
    r = Review(user_id=user_id, movie_id=movie_id, review=review, sentiment=sentiment)
    db.add(r)
    db.commit()
    return {"sentiment_score": sentiment}

# 🎯 Recommendations
@app.get("/recommendations/{user_id}")
def get_recommendations(user_id: int, db: Session = Depends(get_db)):
    ratings = db.query(Rating).all()
    rating_data = [
        {"user_id": r.user_id, "movie_id": r.movie_id, "rating": r.rating}
        for r in ratings
    ]

    recommended_ids = recommend_movies(rating_data)
    movies = db.query(Movie).filter(Movie.id.in_(recommended_ids)).all()
    return movies