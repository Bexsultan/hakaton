# # 2
# Furniture:
# Тип дома, общая площадь и перечень наименований мебели В новом доме совсем нет мебели.
# Мебель имеет название и площадь, из которых Спальня: 4 квадратных метра Гардероб: 2 квадратных метра Стол: 1,5 квадратных метра.
# Добавьте в дом три вышеупомянутых предмета мебели.
# При печати дома требуются следующие данные: тип дома, общая площадь, оставшаяся площадь, список названий мебели.

# class Furniture:
#     def __init__(self, name, area):
#         self.name = name
#         self.area = area
#
#     def __str__(self):
#                  return'Мебель:% s - Занятая площадь:% .2f '% (self.name, self.area)
#
# class House:
#     def __init__(self, house_type, area):
#         self.house_type = house_type
#         self.area = area
#         self.free_area = area
#         self.furniture_list = []
#
#     def __str__(self):
#                  return'Тип дома: % s, площадь:% .2f. Остаточная площадь:% .2f. Список мебели% s '\
#                %(self.house_type,self.area,self.free_area,self.furniture_list)
#
#     def add_furniture(self,furniture):
#
#         print('Добавить мебель:  % s, площадь:% .2f '% (furniture.name, furniture.area))
#         if self.free_area < furniture.area:
#             print('Площадь мебели% s превышает оставшуюся площадь '% furniture.name)
#             return
#         self.furniture_list.append(furniture.name)
#         self.free_area -= furniture.area
#
# #
#
# bed = Furniture('Спальня', 4)
# table = Furniture('Стол', 1.5)
# wardrobe= Furniture('Гардероб', 2)
#
# my_house =House('Бунгало', 200)
# print(my_house)
#
#
# print(bed)
# print(table)
# print(wardrobe)
#
#
#
# my_house.add_furniture(bed)
# my_house.add_furniture(table)
# my_house.add_furniture(wardrobe)
#
# print(my_house)


# # 3
# Students room:
# Реализуйте студенческую комнату с помощью ООП:

# Copy:
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve)
# <name: Steven Schultz, age: 23, major: English>
# print(Johnny)
# <name: Jonathan Rosenberg, age: 24, major: Biology>

#
# class StudentsRoom:
#
#
#     def __init__(self, name, age, major):
#         self.name = name
#         self.age = age
#         self.major = major
#
#     def display_students(self):
#         print('name: {}, age: {}, major: {}'.format(self.name, self.age, self.major))
#
#
#
# steve = StudentsRoom("Steven Schultz", 23, "English")
# johnny = StudentsRoom("Jonathan Rosenberg", 24, "Biology")
# penny = StudentsRoom("Penelope Meramveliotakis", 21, "Physics")
#
# steve.display_students()
# johnny.display_students()
# penny.display_students()


# # 4
# Dollar
# Создайте функцию dollarize (), которая принимает Float и возвращает долларовый формат:

# Copy
# dollarize(123456.78901) -> "$123,456.80"
# dollarize(-123456.7801) -> "-$123,456.78"
# dollarize(1000000) -> "$1,000,000"

# Преобразуйте эту функцию в полезный класс MoneyFmt. MoneyFmt содержит одно значение данных (количество) и 4 метода.
# Copy
#     "init" //конструктор инициализирует значение данных
#     "update" //метод заменяет значение данных новым
#     "repr" //методы возвращают значение с плавающей запятой
#     "str" //метод, реализующий логику метода dollarize ()

# Copy
# //Результат будет выглядеть так:
# import moneyfmt
# cash = moneyfmt.MoneyFmt(12345678.021)
# print(cash) -- returns "$12,345,678.02"
# cash.update(100000.4567)
# print(cash) -- returns "$100,000.46"
# cash.update(-0.3)
# print(cash) -- returns "-$0.30"
# repr(cash) -- returns -0.3


# def dollarize(amount):
#     if amount >= 0:
#         return '${:,.2f}'.format(amount)
#     else:
#         return '-${:,.2f}'.format(-amount)
# print(dollarize(123456.78901))
# print(dollarize(-123456.7801))
# print(dollarize(1000000))
#
#
# import moneyfmt
# cash = moneyfmt.MoneyFmt(12345678.021)
# print(cash)
# cash.update(100000.4567)
# print(cash)
# cash.update(-0.3)
# print(cash)
# repr(cash)