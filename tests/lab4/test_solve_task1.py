import unittest
from src.lab4.task1.User import User
from src.lab4.task1.solve_task1 import get_recommendation
from src.lab4.task2.Group import Group
from src.lab4.task2.Person import Person


class TestTasks(unittest.TestCase):

    def test_compare(self):
        user_1 = User("1,2,3,4,5,6,7,8,9,3,3,5")
        user_2 = User("5,7,3,1,10,15,2")
        self.assertEqual(user_2.compare_with_other_user(user_1), list([1, 2, 3, 5, 7]))
        user_1 = User("1,3,5,7,9")
        user_2 = User("2,4,6,8,10")
        self.assertEqual(user_2.compare_with_other_user(user_1), list())

    def test_recommendation(self):
        user_1 = User("1,2,3")
        users = list([User("1,2,4,5"), User("1,3,6,7,5"), User("1,2,3,4"), User("1,6,7"), User("2,6,7")])
        self.assertEqual(get_recommendation(user_1, users, 7), 4)

    def test_group(self):
        group = Group(list([18, 40, 70, 100]))
        group.add_person(Person("Абдула А А", 17))
        group.add_person(Person("Красный Б А", 18))
        group.add_person(Person("Карл Б А", 18))
        group.add_person(Person("Карл А А", 18))
        group.add_person(Person("Джордж М А", 110))
        self.assertEqual(group.get_print_group(0), "0-18: Карл А А (18), Карл Б А (18), Красный Б А (18), Абдула А А (17)\n")
        self.assertEqual(group.get_print_group(1), "")
        self.assertEqual(group.get_print_group(3), "")
        self.assertEqual(group.get_print_group(4), "100+: Джордж М А (110)\n")