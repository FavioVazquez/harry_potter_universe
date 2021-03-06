import datetime
from typing import NamedTuple

class HogwartsMember:
    """
    Creates a member of the Hogwarts School of Witchcraft and Wizardry
    """

    def __init__(self, name:str, birthyear:int, sex:str):
        self._name = name
        self.birthyear = birthyear
        self.sex = sex
        self._traits = {}

    def says(self, words):
        return f"{self._name} says {words}"

    def add_trait(self, trait, value=True):
        self._traits[trait] = value

    def print_traits(self):
        true_traits = [trait for trait, value in self._traits.items() if value]
        false_traits = [trait for trait, value in self._traits.items() if not value]

        print(f"{self._name} is {', '.join(true_traits)} "
              f"but not {', '.join(false_traits)}")

    def exhibits_trait(self, trait):
        try:
            value = self._traits[trait]
        except KeyError:
            print(f"{self._name} does not have a character trait with the name '{trait}'")
            return

        if value:
            print(f"Yes, {self._name} is {trait}!")
        else:
            print(f"No, {self._name} is not {trait}!")

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        now = datetime.datetime.now().year
        return now - self.birthyear

    @staticmethod
    def school_headmaster():
        return HogwartsMember('Albus Percival Wulfric Brian Dumbledore', 1881, 'male')

    def __repr__(self):
        return f"{self.__class__.__name__}({self._name}, birthyear: {self.birthyear})"


class Professor(HogwartsMember):
    """
    Creates a Hogwarts professor
    """

    def __init__(self, name:str, birthyear:int, sex:str, subject:str, house: str = None):
        super().__init__(name, birthyear, sex)
        self.subject = subject
        if house is not None:
            self.house = house

    @classmethod
    def mcgonagall(cls):
        return cls('Minerva McGonagall', 1935, 'female', 'Transfiguration', house='Griffindor')

    @classmethod
    def snape(cls):
        return cls('Severus Snape', 1960, 'male', 'Potions', house='Slytherin')


    def __repr__(self):
        return (f"{self.__class__.__name__}({self._name}, "
                f"birthyear: {self.birthyear}, subject: {self.subject})")



class Ghost(HogwartsMember):
    """
    Creates a Hogwarts ghost
    """

    def __init__(self, name:str, birthyear:int, sex:str, year_of_death:int, house: str = None):
        super().__init__(name, birthyear, sex)

        self.year_of_death = year_of_death

        if house is not None:
            self.house = house

    @property
    def age(self):
        now = datetime.datetime.now().year
        return now - self.birthyear

    def __repr__(self):
        return (f"{self.__class__.__name__}({self._name}, "
                f"birthyear: {self.birthyear}, year of death: {self.year_of_death})")

    @classmethod
    def nearly_headless_nick(cls):
        return cls('Sir Nicholas de Mimsy-Porpington', 1401, 'male', '1492', 'Gryffindor')


class Pupil(HogwartsMember):
    """
    Create a Hogwarts Pupil
    """

    def __init__(self, name:str, birthyear:int, sex:str, house:str, start_year:int, pet: tuple = None):
        super().__init__(name, birthyear, sex)
        self.house = house
        self.start_year = start_year

        if pet is not None:
            self.pet_name, self.pet_type = pet

        self._owls = {
                'Study of Ancient Runes': False,
                'Arithmancy': False,
                'Astronomy': False,
                'Care of Magical Creatures': False,
                'Charms': False,
                'Defence Against the Dark Arts': False,
                'Divination': False,
                'Herbology': False,
                'History of Magic': False,
                'Muggle Studies': False,
                'Potions': False,
                'Transfiguration': False}

        self._friends = []

    @classmethod
    def harry(cls):
        return cls('Harry James Potter', 1980, 'male', 'Griffindor', start_year=1991, pet=('Hedwig', 'owl'))

    @classmethod
    def ron(cls):
        return cls('Ronald Bilius Weasley', 1980, 'male', 'Griffindor', 1991, pet=('Pigwidgeon', 'owl'))

    @classmethod
    def hermione(cls):
        return cls('Hermione Jean Granger', 1979, 'female', 'Griffindor', 1991, pet=('Crookshanks', 'cat'))

    @classmethod
    def malfoy(cls):
        return cls('Draco Lucius Malfoy', 1980, 'male', 'Slytherin', 1991, pet=('Unnamed', 'owl') )

    @property
    def current_year(self):
        now = datetime.datetime.now().year
        return (now - self.start_year) + 1

    @property
    def owls(self):
        return self._owls

    @property
    def friends(self):
        return f"{self._name}'s current friends are: {[person.name for person in self._friends]}"

    @owls.setter
    def owls(self, subject_and_grade):

        try:
            subject, grade = subject_and_grade
        except ValueError:
            raise ValueError("Pass and iterable with two items: subject and grade")

        passed = self.passed(grade)

        if passed:
            self._owls[subject] = True
        else:
            print('The exam was not passed so no OWL was awarded!')

    @owls.deleter
    def owls(self):
        print("Caution, you are deleting this students' OWL's! "
              "You should only do that if she/he dropped out of school without passing any exam!")
        del self._owls


    @staticmethod
    def passed(grade):
        """
        Given a grade, determine if an exam was passed.
        """
        grades = {
                'O': True,
                'Ordinary': True,
                'P': True,
                'Passed': True,
                'A': True,
                'Acceptable': True,
                'P': False,
                'Poor': False,
                'D': False,
                'Dreadful': False,
                'T': False,
                'Troll': False,
                }

        return grades.get(grade, False)

    def befriend(self, person):
        """Adds another person to your list of friends"""
        if (person.__class__.__name__ != 'HogwartsMember'
            and self.house != 'Slyterhin'
            and person.house == 'Slytherin'):
            print("Are you sure you want to be friends with someone from Slytherin?")

        self._friends.append(person)
        print(f"{person.name} is now your friend!")

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"({self._name}, birthyear: {self.birthyear}, house: {self.house})")

class Charm:
    """ Creates a charm """
    def __init__(self, incantation:str, difficulty: str = None, effect: str = None):
        self.incantation = incantation
        self.difficulty = difficulty
        self.effect = effect

    def cast(self):
        print(f"{self.incantation}!")

    @classmethod
    def lumos(cls):
        return cls('Lumos', 'simple', 'Illuminates the wand tip')

    @classmethod
    def wingardium_leviosa(cls):
        return cls('Wingardium Leviosa', 'simple', 'Makes objects fly')

    def __repr__(self):
        return f"{self.__class__.__name__}({self.incantation}, {self.difficulty}, {self.effect})"


class DeathEater(NamedTuple):
    """ Creates a death eater """
    name: str
    birthyear: str

    @property
    def leader(self):
        voldemort = DeathEater('Voldemort', 1926)
        return voldemort

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, birthyear: {self.birthyear})"

if __name__ == "__main__":
    now = 1995

    lucius = DeathEater('Lucius Malfoy', 1953)
    print('Lucius: ', lucius)
    print('Leader: ', lucius.leader)

    bellatrix = DeathEater('Bellatrix Lestrange', 1951)
    print('Bellatrix: ', bellatrix)






