"""
DecodeLabs - Artificial Intelligence Internship
Project 3: AI Recommendation Logic

Goal:
    Create a simple recommendation system based on user preferences.

Key Requirements met:
    - Take user input (choices or interests)
    - Match preferences using logic / similarity
    - Display recommended items

Key Skills:
    Logic building, pattern matching, recommendation concepts.

Approach:
    This is a content-based recommender. Each movie has a set of
    genre "tags". The user picks the genres they like, and we score
    every movie by how many of its tags overlap with the user's
    interests (a simple similarity score). The highest-scoring
    movies are shown as recommendations.

Author: Vinod
"""

# A small movie catalog. Each movie has a name and a set of genre tags.
MOVIES = [
    {"title": "The Dark Knight",         "genres": {"action", "thriller", "crime"}},
    {"title": "Inception",               "genres": {"action", "sci-fi", "thriller"}},
    {"title": "Interstellar",            "genres": {"sci-fi", "drama", "adventure"}},
    {"title": "The Notebook",            "genres": {"romance", "drama"}},
    {"title": "La La Land",              "genres": {"romance", "musical", "drama"}},
    {"title": "The Conjuring",           "genres": {"horror", "thriller"}},
    {"title": "Get Out",                 "genres": {"horror", "thriller", "mystery"}},
    {"title": "The Hangover",            "genres": {"comedy"}},
    {"title": "Superbad",                "genres": {"comedy", "coming-of-age"}},
    {"title": "Avengers: Endgame",       "genres": {"action", "sci-fi", "adventure"}},
    {"title": "Toy Story",               "genres": {"animation", "comedy", "adventure"}},
    {"title": "Spirited Away",           "genres": {"animation", "fantasy", "adventure"}},
    {"title": "John Wick",               "genres": {"action", "thriller", "crime"}},
    {"title": "Knives Out",              "genres": {"mystery", "comedy", "crime"}},
    {"title": "A Quiet Place",           "genres": {"horror", "sci-fi", "thriller"}},
]

ALL_GENRES = sorted({genre for movie in MOVIES for genre in movie["genres"]})


def show_available_genres():
    """Display the list of genres the user can choose from."""
    print("\nAvailable genres:")
    for i, genre in enumerate(ALL_GENRES, start=1):
        print(f"  {i}. {genre}")


def get_user_preferences():
    """
    Ask the user which genres they like. They can type genre names
    separated by commas (e.g. "action, sci-fi").
    """
    show_available_genres()
    raw = input("\nType your favorite genres (comma-separated): ")
    chosen = {g.strip().lower() for g in raw.split(",") if g.strip()}

    # Keep only genres that actually exist in our catalog
    valid_choices = {g for g in chosen if g in ALL_GENRES}
    return valid_choices


def similarity_score(user_genres, movie_genres):
    """
    A simple similarity measure: how many genres the movie shares
    with the user's preferences (set intersection size).
    """
    return len(user_genres & movie_genres)


def recommend_movies(user_genres, top_n=5):
    """
    Score every movie by similarity to the user's preferences and
    return the top_n highest-scoring movies (score > 0 only).
    """
    scored = []
    for movie in MOVIES:
        score = similarity_score(user_genres, movie["genres"])
        if score > 0:
            scored.append((movie["title"], score, movie["genres"]))

    # Sort by score, highest first
    scored.sort(key=lambda item: item[1], reverse=True)
    return scored[:top_n]


def display_recommendations(recommendations):
    """Print the recommended movies in a readable format."""
    if not recommendations:
        print("\nSorry, no matching recommendations found. "
              "Try picking different genres.")
        return

    print("\n" + "=" * 45)
    print(" RECOMMENDED FOR YOU")
    print("=" * 45)
    for rank, (title, score, genres) in enumerate(recommendations, start=1):
        genre_list = ", ".join(sorted(genres))
        print(f"{rank}. {title}  (match score: {score})")
        print(f"   Genres: {genre_list}")


def main():
    print("=" * 45)
    print(" DecodeLabs Project 3: AI Recommendation Logic")
    print("=" * 45)

    user_genres = get_user_preferences()

    while not user_genres:
        print("That didn't match any known genre. Please try again.")
        user_genres = get_user_preferences()

    recommendations = recommend_movies(user_genres, top_n=5)
    display_recommendations(recommendations)


if __name__ == "__main__":
    main()
