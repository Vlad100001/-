class Animal:
    def __init__(self, name, date_of_birth, skills, animal_class_id):
        self.name = name
        self.date_of_birth = date_of_birth
        self.skills = skills
        self.animal_class_id=animal_class_id

    def get_info(self):
        return f"Имя: {self.name}, День рождения: {self.date_of_birth}, Команды: {self.skills} Класс животных {self.animal_class_id}"

class Dog(Animal):
    def __init__(self, name, date_of_birth, skills, animal_class_id):
        super().__init__(name, date_of_birth, skills,animal_class_id)
        self.animal_type = "Собака"

class Cat(Animal):
    def __init__(self, name, date_of_birth, skills, animal_class_id):
        super().__init__(name, date_of_birth, skills,animal_class_id)
        self.animal_type = "Кошка"

class Hamster(Animal):
    def __init__(self, name, date_of_birth, skills, animal_class_id):
        super().__init__(name, date_of_birth, skills,animal_class_id)
        self.animal_type = "Хомяк"

class Horse(Animal):
     def __init__(self, name, date_of_birth, skills, animal_class_id):
        super().__init__(name, date_of_birth, skills,animal_class_id)
        self.animal_type = "Лощадь"

class Camel(Animal):
     def __init__(self, name, date_of_birth, skills, animal_class_id):
        super().__init__(name, date_of_birth, skills,animal_class_id)
        self.animal_type = "Верблюд"

class Donkey(Animal):
     def __init__(self, name, date_of_birth, skills, animal_class_id):
        super().__init__(name, date_of_birth, skills, animal_class_id)
        self.animal_type = "Осел"

class DomesticAnimalRegistry:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def list_animals(self):
        for animal in self.animals:
            print(animal.get_info())

class Counter:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.count > 0:
            raise ValueError("Ресурс не управляется должным образом в блоке try-with-resources")

def main():
    registry = DomesticAnimalRegistry()

    while True:
        print("Реестр домашних животных:")
        print("1. Добавьте новое животное")
        print("2. Регист животных")
        print("3. Выход")

        choice = input("Сделайте выбор: ")

        if choice == "1":
            with Counter() as counter:
                name = input("Введите имя животного ")
                date_of_birth = input("Введите дату рождения(ГГГГ-ММ-ДД): ")
                skills = input("Введите команды: ")
                animal_class_id= input("Введите класс 1- Домашние животные, 2 Вьючные животные: ")

                animal_type = input("Введите вид животного (Собака, Кошка, Хомяк, Лошадь, Верблюд или Осел).: ")
                if animal_type == "Собака":
                    animal = Dog(name, date_of_birth, skills, animal_class_id)
                elif animal_type == "Кошка":
                    animal = Cat(name, date_of_birth, skills, animal_class_id)
                elif animal_type == "Хомяк":
                    animal = Hamster(name, date_of_birth, skills, animal_class_id)
                elif animal_type == "Лощадь":
                    animal = Horse(name, date_of_birth, skills, animal_class_id)
                elif animal_type == "Верблюд":
                    animal = Camel(name, date_of_birth, skills, animal_class_id)
                elif animal_type == "Осел":
                    animal = Donkey(name, date_of_birth, skills, animal_class_id)
                else:
                    print("Недопустимый вид животного.")
                    continue

                registry.add_animal(animal)
                counter.add()
                print("Животное внесено в реестр.")

        elif choice == "2":
            print("Список животных, внесенных в реестр:")
            registry.list_animals()

        elif choice == "3":
            print("Выход из реестра животных.")
            break

        else:
            print("Неверный вариант. Пожалуйста, укажите правильный вариант")

if __name__ == "__main__":
    main()
