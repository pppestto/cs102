class Users:
    def __init__(self):
        self.id = 1
        self.data = {}

    def add(self, user_history: list):
        self.data[self.id] = user_history
        self.id += 1

    def items(self):
        return self.data

    def views(self):
        response = []
        for item in self.data.values():
            response += item
        return response

    def items_set(self):
        return [set(value) for key, value in self.data.items()]

    def get(self, user_id: int):
        return self.data[user_id]


class Movies:
    def __init__(self):
        self.data = {}

    def update(self, movie_id, movie_name):
        self.data[movie_id] = [movie_name, 0]

    def items(self):
        return self.data

    def count_views(self, views):
        for view in views:
            self.data[view][1] += 1

    def get(self, index):
        return self.data[index]


u = Users()
m = Movies()

with open('files/films.txt', encoding='utf-8') as file:
    films = file.readlines()
    for film in films:
        movie_id, movie_name = film.replace('\n', '').split(',')
        m.update(int(movie_id), movie_name)

with open('files/watch_history.txt', encoding='utf-8') as file:
    users = file.readlines()
    for user in users:
        history = list(map(int, user.replace('\n', '').split(',')))
        u.add(history)


def recommend(watched):
    watched = set(watched)
    m.count_views(u.views())
    rec_ids = set()
    for i in u.items_set():
        if len(i & watched) >= len(watched) // 2:
            rec_ids = rec_ids | (i - watched)
    rec = []
    for id in rec_ids:
        rec.append(m.items()[id])
    return max(rec, key=lambda x: x[1])[0]


if __name__ == '__main__':
    print(recommend(list(map(int, input().split(',')))))
