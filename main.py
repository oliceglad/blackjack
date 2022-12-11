
import random
class Card:
    #  Карта, у которой есть значения
    #   - масть
    #   - ранг/принадлежность 2, 3, 4, 5, 6, 7 и так далее

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


class Deck:
    #  Колода создаёт у себя объекты карт
    def __init__(self, cards):
        self.cards = cards
    def add_card(self, suit, rank):
        self.cards.append(Card(suit, rank))


class Player:
    #  Игрок, у которого есть имя и какие-то карты на руках
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck

    def print_info(self):
        print(f"{self.name}:", end=' ')
        for i_elem in range(len(self.deck.cards)):
            if isinstance(self.deck.cards[i_elem].suit, str):
                print(self.deck.cards[i_elem].suit, end=' ' )
            else:
                print(self.deck.cards[i_elem].rank, end=' ')
        print()
        points = 0
        for i_elem in range(len(self.deck.cards)):
            points += self.deck.cards[i_elem].rank
        print(f'Кол-во очков: {points}')

    def set_points(self):
        points = 0
        for i_elem in range(len(self.deck.cards)):
           points += self.deck.cards[i_elem].rank
        return points

# Инициализация игроков
human = Player('Вася', Deck([]))
computer = Player('Компьютер', Deck([]))

# Добавить карту в колоду игрока
def give_card(player):
    number = random.randint(2, 14)
    if 2 <= number <= 10:
        player.deck.add_card(number, number)
    elif number == 11:
        player.deck.add_card('Валет', 10)
    elif number == 12:
        player.deck.add_card('Дама', 10)
    elif number == 13:
        player.deck.add_card('Король', 10)
    elif number == 14:
        player.deck.add_card('Туз', 11)

#Изначальная колода
for card in range(2):
    give_card(human)
    give_card(computer)

#Сама игра
while True:
    human.print_info()
    action = input('Введите действие: 1 - Взять карту 2 - Остановить игру ')
    if action == '2':
        if human.set_points() > computer.set_points() and human.set_points() <= 21:
            print('Вы победили! Ура!')
        elif human.set_points() < computer.set_points():
            print('Победил компьютер! ')
        elif human.set_points() == computer.set_points():
            print('Ничья!')
        else:
            print('Больше 21-го( Проигрыш!')
        break
    elif action == '1':
        give_card(human)
    else:
        print('Неверная команда, введите еще раз!')
