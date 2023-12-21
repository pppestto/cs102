class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} ({self.age})'

    def __eq__(self, other):
        return self.age == other

    def __gt__(self, other):
        return self.age > other

    def __lt__(self, other):
        return self.age < other

    def __ge__(self, other):
        return self.age >= other

    def __le__(self, other):
        return self.age <= other


class People:
    def __init__(self, *args):
        self.data = {}
        args = (-1,) + args + (args[-1],)
        for i in range(0, len(args) - 1):
            if i == len(args) - 2:
                key = (args[-1] + 1, float('inf'))
            else:
                key = (args[i] + 1, args[i + 1])
            self.data[key] = []

    def add(self, item):
        for a, b in self.data.keys():
            if a <= item <= b:
                self.data[(a, b)].append(item)

    def items(self):
        return self.data


def main():
    people = People(18, 25, 35, 45, 60, 80, 100)

    with open('files/people.txt', encoding='utf-8') as file:
        array = file.readlines()
        for line in array:
            name, age = line.replace('\n', '').split(',')
            people.add(Person(name, int(age)))

    items = people.items()
    answer = ''
    for group in list(items.keys())[::-1]:
        current = items[group]
        if current:
            if group[1] == float('inf'):
                answer += f'{group[0]}+: ' + ', '.join(map(str, current))  + '\n'
            else:
                answer += f'{group[0]}-{group[1]}: ' + ', '.join(map(str, current)) + '\n'
    return answer[:-1]


if __name__ == '__main__':
    print(main())
