from src.lab4.task1.User import User
from math import ceil
import typing


def get_recommendation(user: User, other_users: typing.List[User], count_films: int) -> int:
    """
    @param user: пользователь, для которого мы будем составлять рекомендацию
    @param other_users: список пользователей, на основе просмотров которых мы будем составлять рекомендацию
    @param count_films: количество фильмов
    @return: id фильма, рекомендованного к просмотру
    """
    recommendation = dict()
    for i in user.viewing_history:
        recommendation[i] = -1
    for current_user in other_users:
        general_movies = user.compare_with_other_user(current_user)
        if len(general_movies) >= ceil(len(user.viewing_history) / 2):
            for current_movie in current_user.viewing_history:
                if current_movie not in recommendation:
                    recommendation[current_movie] = len(general_movies) / len(user.viewing_history)
                else:
                    if recommendation[current_movie] != -1:
                        recommendation[current_movie] += len(general_movies) / len(user.viewing_history)
    film_id = -1
    max_recommendation_points = 0
    for id_film, points in recommendation.items():
        if points >= max_recommendation_points:
            max_recommendation_points = points
            film_id = id_film
    return film_id


if __name__ == "__main__":
    films = dict()
    for i in open("films.txt", encoding="UTF-8").readlines():
        film = i.rstrip().split(',')
        films[int(film[0])] = film[1]
    users = []
    for i in open("viewing_history.txt").readlines():
        users.append(User(i.rstrip()))
    user_view = "2,4"
    user = User(user_view)
    print(films[get_recommendation(user, users, len(films))])