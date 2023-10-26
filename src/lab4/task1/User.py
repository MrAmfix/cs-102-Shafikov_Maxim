class User:
    viewing_history: set

    def __init__(self, history: str):
        """
        @param history: история просмотра
        """
        self.viewing_history = set(map(int, history.split(',')))

    def compare_with_other_user(self, other_user: "User") -> list:
        """
        @param other_user: пользователь, с которым будет сравниваться список просмотров
        @return: список id совпадающих фильмов
        """
        general_movies = []
        for i in self.viewing_history:
            if i in other_user.viewing_history:
                general_movies.append(i)
        return general_movies
