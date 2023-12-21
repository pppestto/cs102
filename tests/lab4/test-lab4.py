import unittest
from src.lab4.app import main
from src.lab4.rec import recommend


class Test(unittest.TestCase):
    def test_first_task(self):
        self.assertEqual(recommend((2, 4)), 'Дюна')

    def test_second_task(self):
        self.assertEqual(main(), '''101+: Кошельков Захар Брониславович (105)
81-100: Дьячков Нисон Иринеевич (88), Иванов Варлам Якунович (88)
46-60: Старостин Ростислав Ермолаевич (50)
26-35: Ярилова Розалия Трофимовна (29)
0-18: Соколов Андрей Сергеевич (15), Егоров Алан Петрович (7)''')
