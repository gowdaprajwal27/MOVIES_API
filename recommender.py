import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def recommend_movies(ratings_data):
    """
    ratings_data: list of dicts
    [
      {"user_id": 1, "movie_id": 2, "rating": 4.5},
      ...
    ]
    """

    if not ratings_data:
        return []

    df = pd.DataFrame(ratings_data)

    # Create user-movie matrix
    user_movie_matrix = df.pivot_table(
        index="user_id",
        columns="movie_id",
        values="rating"
    ).fillna(0)

    # Compute similarity
    similarity_matrix = cosine_similarity(user_movie_matrix)
    similarity_df = pd.DataFrame(
        similarity_matrix,
        index=user_movie_matrix.index,
        columns=user_movie_matrix.index
    )

    # Pick the last user (demo purpose)
    target_user = user_movie_matrix.index[-1]

    similar_users = (
        similarity_df[target_user]
        .sort_values(ascending=False)
        .iloc[1:3]
        .index
    )

    recommended_movies = set()

    for user in similar_users:
        movies = df[df["user_id"] == user]["movie_id"].tolist()
        recommended_movies.update(movies)

    return list(recommended_movies)