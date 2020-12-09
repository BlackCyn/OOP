class Ferma(object):
    def __str__(self):
        rep="Объект класса Ferma\n"
        rep+= "имя: " + self.name + "\n"
        rep+= "настроение: " + self.mood + "\n"
        rep+= "голод:" + str(self.hunger) + "\n"
        rep+= "показатель скуки:" + str(self.boredom) + "\n"
        return rep
        
    def __init__(self, name, hunger=0, boredom = 0):
        print("Появилась на свет новая зверюшка!")
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger +=1
        self.boredom += 1

    def talk(self):
        print('Привет! Меня зовут ', self.name, " . Сейчас я чувствую себя ", self.mood, "\n")
        self.__pass_time()

    def eat(self, food = 4):
        food=int(input("Сколько еды ты хочешь мне дать? (дай 4 пожалуйста)"))
        print("Спасибо!")
        self.hunger-=food
        if self.hunger<0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        fun=int(input("Сколько времени ты хочешь со мной поиграть?"))
        print("ОМАГАД!!1!")
        self.boredom-=fun
        if self.boredom<0:
            self.boredom = 0
        self.__pass_time()

    @property
    def mood(self):
        unhappiness = self.hunger +self.boredom
        if unhappiness <5:
            m = "прекрасно"
        elif 5<=unhappiness<=10:
            m = "норм"
        elif 10<unhappiness<=15:
            m = "пойдет"
        else:
            m = "ужасно"
        return m

def main():
    import random
    print("Добро пожаловать не ферму. На данный момент она пустая")
    ferma=[]
    crit_kol=input("Введите количество животных которых вы хотите завести: ")
    for i in range(int(crit_kol)):
        crit_name=input("На ферме появилось новое животное. Как вы его назовете? ")
        crit=Ferma(crit_name, hunger = random.randint(1,10),boredom=random.randint(1,10))
        ferma.append(crit)

    choice=None
    while choice != "0":
        print \
        ("""
        Моя зверюшка
        0 - Выйти
        1 - Узнать о самочувствиии зверюшки
        2 - Покормить зверюшку
        3 - Поиграть со зверюшкой
        Здесь также был добавлен секретный черный ход чтобы посмотреть информацию о каждой зверюшке
        """)
        choice = input("Ваш выбор: ")
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            for crit in ferma:
                crit.talk()
        elif choice == "2":
            for crit in ferma:
                crit.eat()
        elif choice == "3":
            for crit in ferma:
                crit.play()
        elif choice == "123qwe":
            for crit in ferma:
                print(crit)
        else:
            print("Извините, в меню игры нет такого пункта ", choice)
                

main()

input("\n\nНажмите Enter, чтобы выйти")
