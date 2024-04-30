# Завдання 1
# Створіть два окремих "мікросервіси" (дві окремі
# програми). Одна програма створює та експортує дані у
# форматі JSON, а інша програма завантажує та обробляє ці
# дані. Це може бути, наприклад, система, яка створює та
# обробляє замовлення.
# import json
#
# class OrderExport:
#     def __init__(self):
#         self.orders = []
#
#     def make_order(self, order_num, customer_name, ordering):
#         order = {
#             "order_num": order_num,
#             "customer_name": customer_name,
#             "ordering": ordering
#         }
#         self.orders.append(order)
#
#     def export_orders(self, file_name):
#         with open(file_name, 'w') as f:
#             json.dump(self.orders, f)
#
#
# def main():
#     exporter = OrderExport()
#     exporter.make_order(1, "Dana", "1 juice, 2 cheeseburgers")
#     exporter.make_order(2, "Dima", "2 coca-cola")
#     exporter.export_orders("orders.json")
#
#     with open("orders.json", 'r') as file:
#         orders = json.load(file)
#         for order in orders:
#             print(f"Order number: {order['order_num']}\nCustomer: {order['customer_name']},\nOrder: {order['ordering']}")
#
#
# if __name__ == "__main__":
#     main()


# Завдання 2
# Створіть програму для проведення опитування або
# анкетування. Зберігайте відповіді користувачів у форматі
# JSON файлу. Кожне опитування може бути окремим
# об'єктом у файлі JSON, а відповіді кожного користувача -
# списком значень.
# import json
#
# def conduct_survey():
#     survey = {}
#
#     questions = [
#         "How old are you ?",
#         "What is your name ?",
#         "Are you learning Python?"
#     ]
#
#     for question in questions:
#         answer = input(question + " ")
#         survey[question] = answer
#
#     return survey
#
# def save_survey(survey, file_name):
#     with open(file_name, 'w') as file:
#         json.dump(survey, file)
#
# def main():
#     survey = conduct_survey()
#     file_name = input('Введіть назву файлу:')
#     save_survey(survey, file_name)
#
# if __name__ == "__main__":
#     main()





# Завдання 3
# До вже реалізованого класу «Стадіон» додайте можливість
# стиснення та розпакування даних з використанням json та
# pickle.
import json
import pickle
class Stadium:
    def __init__(self, name="", date="", country="", city="", capacity=0):
        self.name = name
        self.date = date
        self.country = country
        self.city = city
        self.capacity = capacity

    def display(self):
        print("Назва стадіону:", self.name)
        print("Дата відкриття:", self.date)
        print("Країна:", self.country)
        print("Місто:", self.city)
        print("Місткість:", self.capacity)

    def info(self):
        self.name = input("Введіть назву стадіону:")
        self.date = input("Введіть дату відкриття стадіону:")
        self.country = input("Введіть назву країни:")
        self.city = input("Введіть місто:")
        self.capacity = int(input("Введіть місткість стадіону:"))

    def __str__(self):
        return f"Стадіон {self.name}, Дата відкриття: {self.date}, Знаходиться {self.country}, {self.city}, Місткість стадіону: {self.capacity}"

    def __eq__(self, other):
        return self.capacity == other.capacity

    def __lt__(self, other):
        return self.capacity < other.capacity

    def __le__(self, other):
        return self.capacity <= other.capacity

    def __gt__(self, other):
        return self.capacity > other.capacity

    def __ge__(self, other):
        return self.capacity >= other.capacity

    def __ne__(self, other):
        return self.capacity != other.capacity

    def to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump({
                "name": self.name,
                "date": self.date,
                "country": self.country,
                "city": self.city,
                "capacity": self.capacity
            }, file)

    def from_json(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.name = data['name']
            self.date = data['date']
            self.country = data['country']
            self.city = data['city']
            self.capacity = data['capacity']

    def to_pickle(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump({
                "name": self.name,
                "date": self.date,
                "country": self.country,
                "city": self.city,
                "capacity": self.capacity
            }, file)

    def from_pickle(self, filename):
        with open(filename, 'rb') as file:
            data = pickle.load(file)
            self.name = data['name']
            self.date = data['date']
            self.country = data['country']
            self.city = data['city']
            self.capacity = data['capacity']

stadium1 = Stadium()
stadium1.info()

stadium2 = Stadium()
stadium2.info()

print("\nІнформація про перший стадіон:")
stadium1.display()

print("\nІнформація про другий стадіон:")
stadium2.display()

if stadium1 >= stadium2:
    print("\nПерший стадіон має більшу місткість, ніж другий")
else:
    print("\nДругий стадіон має більшу місткість, ніж перший")

stadium1.to_json("stadium1.json")
stadium1.from_json("stadium1.json")

stadium2.to_pickle("stadium2.pkl")
stadium2.from_pickle("stadium2.pkl")