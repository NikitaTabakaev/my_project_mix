import random


class Tobacco:

    def __init__(self, brand, strength):
        self.brand = brand
        self.strength = strength
        self.fresh_taste = ["Супернова", "Лимон", "Цитрусовый микс", "Лайм"]
        self.berry_taste = ["Лесные ягоды", "Ежевика", "Черная смородина", "Красная смородина", "Черника",
                            "Овсянка с ягодами", "Малина", "Клубника"]
        self.fruit_taste = ["Грейпфрут", "Пина каладо", "Апельсин", "Сливочный кокос", "Лайм", "Гуава", "Гранат"]
        self.desert_taste = ["Чизкейк", "Тирамису", "Пряник", "Шоколадное печенье", "Шоколадное мороженное",
                             "Сливочный кокос", "Клубничный джем"]

    def get_mix(self, first, second, fresh=""):

        choice_1 = ""
        choice_2 = ""
        if first == "ягоды":
            choice_1 = random.choice(self.berry_taste)
        elif first == "фрукты":
            choice_1 = random.choice(self.fruit_taste)
        elif first == "десерты":
            choice_1 = random.choice(self.desert_taste)

        if second == "ягоды":
            choice_2 = random.choice(self.berry_taste)
        elif second == "фрукты":
            choice_2 = random.choice(self.fruit_taste)
        elif second == "десерты":
            choice_2 = random.choice(self.desert_taste)

        if choice_1 != choice_2 and fresh == "да":
            return f"Твой микс готов!: {choice_1} + {choice_2} и {random.choice(self.fresh_taste)}"
        elif choice_1 != choice_2:
            return f"Твой микс готов!: {choice_1} + {choice_2}"

        while choice_1 == choice_2:
            if first == "ягоды":
                choice_1 = random.choice(self.berry_taste)
            elif first == "фрукты":
                choice_1 = random.choice(self.fruit_taste)
            elif first == "десерты":
                choice_1 = random.choice(self.desert_taste)
            if choice_1 != choice_2:
                return f"Твой микс готов!: {choice_1} + {choice_2}"


tobacco_1 = Tobacco("Дарк Сайд", "Средний")

q_1 = input("Привет! я помогу тебе подобрать микс! первый вкус: ягоды, фрукты, свежесть, десерты?: ").lower()
q_2 = input("Что добавить?: ягоды, фрукты, свежесть, десерты?: ").lower()
q_3 = input("Добавить свежести?: ").lower()
print(tobacco_1.get_mix(q_1, q_2, q_3))






