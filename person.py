from country import Country


class Person:
    def __init__(self, age: int, height: int, sex: bool, weight: int, name: str):
        self.age = age
        self.height = height
        self.sex = sex
        self.weight = weight
        self.name = name

    def greeting(self):
        pass

    def is_alco_buyer(self, country: Country) -> bool:
        return self.age >= country.age_for_alco

    def get_imt(self) -> float:
        return self.height/self.weight
