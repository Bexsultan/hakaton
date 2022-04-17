# # Задание 1
# AK-47:
# У солдата Райана есть АК-47
# Солдаты могут стрелять («тиги-тигитиш»).
# Пистолеты могут стрелять пулями.
# Пистолеты могут начинать патроны - увеличивайте количество патронов (перезаряжает)
# Создайте класс Act_of_Shooting, который унаследует от класса Soldier класс Guns.
# Где солдат будет стрелять из пушки и перезаряжаться, и стрелять еще раз.


# class Soldier():
#     def Load(self,G):
#         if G.bullets==0:
#             return G.fire()
    
#     def shoot(self,G):
#         while G.bullets>0:
#             print('Райан возьми {}, и стреляй'.format(G.guns))
#             G.bullets -= 10
#             print(' Патронов ：{}'.format(G.bullets))
#         else:
#             G.fire()

# class Guns():
#     def __init__(self,guns):
#         self.guns=guns
#         self.bullets=0
#     def fire(self):
#         print(' Патронов нет, перезарядись ！')
#         self.bullets += 100
#         print(' Перезаряжена ：{} патронами '.format(self.bullets))

# class Act_of_Shooting(Guns, Soldier):
#     def __init__(self):
#         super().__init__('ak-47')
    
# soldat = Act_of_Shooting()
# soldat.Load(soldat)
# soldat.shoot(soldat)
# soldat.shoot(soldat)


#Задание 5
# Deck of Cards:
# Создайте класс колоды карт. Внутри колода карт должна использовать другой класс - класс карт. Ваши требования:
# Класс Deck должен иметь метод раздачи для раздачи одной карты из колоды.
# После раздачи карты она удаляется из колоды.
# Должен быть метод «смешивания», который проверяет, что в колоде есть все 52 карты, а затем меняет их случайным образом.
# Класс должен иметь масть (червы, бубны, трефы, пики) и ценность карты (A, 2,3,4,5,6,7,8,9,10, J, Q, K)
# ПРИМЕЧАНИЕ: используйте случайное перемешивание
# Copy # from random import shuffle


# from random import shuffle, randint

# suits = ("Hearts", "Diamonds", "Spades", "Clubs")
# values = ("A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K")


# class Card:
#     def __init__(self, suit, value):
#         if suit in suits:
#             self.suit = suit
#         else:
#             raise Exception("Wrong suit given")

#         if value in values:
#             self.value = value
#         else:
#             raise Exception("Wrong value given")

#     def __str__(self):
#         return f"{self.value} of {self.suit}"

# class Deck:
#     cards = []

#     def __init__(self):
#         self.renew_cards()
#         self.shuffle_cards()

#     def renew_cards(self):
#         for suit in suits:
#             for value in values:
#                 self.cards.append(Card(suit, value))

#     def show_cards(self):
#         for card in self.cards:
#             print(card)

#     def shuffle_cards(self):
#         if len(self.cards) == 52:
#             shuffle(self.cards)
#         else:
#             print("Not 52 cards in Deck")

#     def give_card(self):
#         return self.cards.pop(randint(0, len(self.cards)))


# deck = Deck()

# deck.show_cards()