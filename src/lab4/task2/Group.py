from src.lab4.task2.Person import Person
import typing
from functools import cmp_to_key


class Group:
    groups: typing.List[typing.List[Person]]
    borders: typing.List[int]

    def __init__(self, borders: typing.List[int]):
        """
        @param borders: границы возрастных групп
        """
        self.borders = borders
        self.groups = [[] for i in range(len(borders) + 1)]

    def add_person(self, person: Person):
        """
        @param person: человек, которого, мы добавляем
        """
        for i in range(0, len(self.borders) + 1):
            if i == 0:
                if person.age <= self.borders[i]:
                    self.groups[i].append(person)
                    break
            elif i == len(self.borders):
                if person.age > self.borders[-1]:
                    self.groups[-1].append(person)
                    break
            else:
                if self.borders[i - 1] < person.age <= self.borders[i]:
                    self.groups[i].append(person)

    def get_print_group(self, num_group: int) -> str:
        """
        @param num_group: номер выводимой группы (группы нумеруются с 0)
        @return: строка с информацией
        """
        print_string = ""
        arr_people = []

        def comparator(obj1: (int, str), obj2: (int, str)) -> int:
            if obj1[0] > obj2[0]:
                return -1
            elif obj1[0] < obj2[0]:
                return 1
            else:
                if obj1[1] < obj2[1]:
                    return -1
                elif obj1[1] > obj2[1]:
                    return 1
                else:
                    return 0

        if len(self.groups[num_group]) != 0:
            for person in self.groups[num_group]:
                arr_people.append((person.age, person.name))
            arr_people = sorted(arr_people, key=cmp_to_key(comparator))
            if num_group == 0:
                print_string += f"0-{self.borders[0]}: "
            elif num_group == len(self.borders):
                print_string += f"{self.borders[-1]}+: "
            else:
                print_string += f"{self.borders[num_group - 1]}-{self.borders[num_group]}: "
            for age, name in arr_people:
                print_string += f"{name} ({age}), "

        if print_string == "":
            return ""
        else:
            return print_string[: -2] + '\n'
