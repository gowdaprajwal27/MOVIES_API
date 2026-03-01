# 🎬 Movie Recommendation API

A cloud-deployed FastAPI application that provides movie recommendations using collaborative filtering and sentiment analysis.

## 🌐 Live Demo
👉 https://moviesapi-d5gscphbdqpaxcb.centralus-01.azurewebsites.net/docs

---

## 🚀 Features
- Add and retrieve movies
- User ratings support
- Sentiment analysis on movie reviews
- Personalized movie recommendations
- Interactive Swagger API documentation
- Fully containerized with Docker
- Deployed on Microsoft Azure App Service

---

## 🛠 Tech Stack
- **Backend**: FastAPI
- **Database**: SQLite (SQLAlchemy ORM)
- **Machine Learning**: Collaborative Filtering
- **NLP**: TextBlob (Sentiment Analysis)
- **Containerization**: Docker
- **Cloud**: Azure App Service
- **Version Control**: Git & GitHub

---

## 📌 API Endpoints
| Method | Endpoint | Description |
|------|--------|-------------|
| POST | `/movies` | Add a new movie |
| GET | `/movies` | Get all movies |
| POST | `/ratings` | Add a rating |
| POST | `/reviews` | Add a review with sentiment analysis |
| GET | `/recommendations/{user_id}` | Get personalized recommendations |

---

## 🐳 Run Locally with Docker

```bash
docker build -t movie-recommendation-api .
docker run -p 8000:8000 movie-recommendation-api
