class TV():
    def __init__(self, volume=5, channel=""):
        self.volume=volume
        self.channel=channel
        
    def plus(self):
        zvp=int(input("На сколько вы хотите увеличить громкость телевизора?"))
        self.volume+=zvp
        if self.volume>30:
            print("Рекомендуется снизить громкость телевизора")
        print("Громкость была увеличена")
        print("Громкость стала равна:" + str(self.volume))
        
    def minus(self):
        zvm=int(input("На сколько вы хотите уменьщить громкость телевизора?"))
        self.volume-=zvm
        if self.volume<0:
            self.volume=0
        print("Громкость была уменьшена")
        print("Громкость стала равна:" + str(self.volume))
        
    def change(self):
        print ("""
        1-Новостной канал
        2-Развлекательный канал
        3-Спортивный канал
        4-Канал с грустными фильмами
        5-Канал с аниме
        """)
        
        change=int(input("На какой канал вы хотите переключиться?"))
        if change == 1:
            print("Вы переключились на новостной канал")
        elif change == 2:
            print("Вы переключились на развлекательный канал")
        elif change == 3:
            print("Вы переключились на спортивный канал")
        elif change == 4:
            print("Вы переключились на канал где постоянно идет фильм Хатико")
        elif change == 5:
            print("Вы переключились на канал с аниме")
        else:
            print("Вы ввели неправильное значение")


tv1=TV()
choice= None
while choice != "0":
        print \
        ("""
        Мой телевизор
        0 - Выйти
        1 - Переключить канал
        2 - Прибавить громкость
        3 - Убавить громкость
        """)
        choice = input("Ваш выбор: ")
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            tv1.change()
        elif choice == "2":
            tv1.plus()
        elif choice == "3":
            tv1.minus()
        else:
            print("Извините, в меню игры нет такого пункта ", choice)
