from src.lab4.task2.Person import Person
from src.lab4.task2.Group import Group

if __name__ == "__main__":
    borders = list(map(int, input().rstrip().split(' ')))
    groupClass = Group(borders)
    data = input()
    while data != "END":
        data_form = data.rstrip().split(' ')
        groupClass.add_person(Person(data_form[0] + " " + data_form[1] + " " + data_form[2], int(data_form[3])))
        data = input()

    for i in range(0, len(borders) + 1):
        print(groupClass.get_print_group(i), end="")
