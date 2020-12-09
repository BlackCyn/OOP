import random
suits = ('Черви','Бубны','Пики','Трефы')
ranks = ('Двойка','Тройка','Четверка','Пятерка','Шестерка','Семерка','Восьмерка','Девятка','Десятка','Валет','Дама','Король','Туз')
values = {'Двойка': 2, "Тройка":3,"Четверка":4,"Пятерка":5,"Шестерка":6,"Семерка":7,"Восьмерка":8,"Девятка":9,"Десятка":10,"Валет":10,"Дама":10,"Король":10, 'Туз':11}

playing = True

class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank +" "+ self.suit

class Deck:

    def __init__(self):
        self.deck = [] 
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__ (self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "Колода состоит из :" +deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

test_deck = Deck()
test_deck.shuffle()
print(test_deck)


class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0 
        self.aces = 0 

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Туз':
            self.aces += 1

    def adjust_for_ace(self):

        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -=1



class Chips:

    def __init__(self,total=100):
        self.total = total 
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):

    while True:

        try:
            chips.bet = int(input("Какую ставку вы хотите сделать?(всего у вас 100 фишек) "))
        except:
            print("Напишите число")
        else:
            if chips.bet > chips.total:
                print('Извините, но у вас столько нету. Ваше количество фишек равно: {}'.format(chips.total))
            else:
                break

def hit(deck,hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing 

    while True:
        x = input('Хит(берете карту) или Стенд(не берете карту)? Напишите х или с: ')

        if x[0].lower() == 'х':
            hit(deck,hand)

        elif x[0].lower() == 'с':
            print("Игрок не берет карту. Ход дилера")
            playing = False

        else:
            print("Вы неправильно ответили на вопрос! Попробуйте еще раз")
            continue

        break

def show_some(player,dealer):
    print("\nРука дилера:")
    print(" <скрытая карта>")
    print('',dealer.cards[1])  
    print("\nРука игрока:", *player.cards, sep='\n ')    

def show_all(player,dealer):
    print("\nРука дилера:", *dealer.cards, sep='\n ')
    print("Рука дилера =",dealer.value)
    print("\nРука игрока:", *player.cards, sep='\n ')
    print("Рука игрока =",player.value)
 

def player_busts(player,dealer,chips):
    print("Игрок перебрал!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('Игрок победил!')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Игрок победил! Дилер перебрал!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Дилер победил!")
    chips.lose_bet()

def push(player,dealer):
    print('Ничья!')

a=input("Если хотите узнать правила игры BlackJack напишите правила\nЕсли нет, просто нажмите Enter: ")
if a=="правила":
    print("""
1)Дилер перемешивает все колоды карт.
2)Игроки делают ставки.
3)Дилер всем игрокам раздает по 2 карты, в том числе и себе и при этом открывает свою одну карту. Есть вариант также, что всем раздают по две карты, а дилер себе оставляет только одну открытую. После чего себе набирает карты.
4)Игроки оценивают свои карты и открытую карту дилера.
5)После оценки ситуации игроки могут взять любое количество карт или остаться на той сумме очков что есть. Главное сумма очков не должно превышать “21” очко.
6)Набор карт игроками проходит строго по очереди.
7)После того как все набрали карты или не взяли в зависимости от ситуации – дилер открывает вторую карту.
8)После открытия второй карты дилер обязан по правилам брать карты если у него 16 и меньше очков и остановиться когда у него будет 17 и больше очков.
9)Игроки свои карты не имеют право трогать – открывает их только дилер.

""")

while True:

    print("\nДобро пожаловать в игру BLACKJACK")
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()
    take_bet(player_chips)
    show_some(player_hand,dealer_hand)

    while playing: 
        
        hit_or_stand(deck,player_hand)

        show_some(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)

            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
        show_all(player_hand,dealer_hand)
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)

    print('\n Общее количество фишек игрока составляет: {}'.format(player_chips.total))

    new_game = input("Хотели бы вы сыграть еще в одну игру? (да/нет): ")

    if new_game[0].lower() == 'да':
        playing = True
        continue
    elif new_game[0].lower() == 'нет':
        print('Спасибо за игру! До свидания!')
        break
    else:
        print("\nВы ввели неправильные данные\nВыхожу из игры\nДля запуска новой нужно перезапустить программу ")
        break

