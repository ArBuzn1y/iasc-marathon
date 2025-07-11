# task 1
contacts = {
    "Anna": "093-123-45-67",
    "Ivan": "050-888-99-00",
    "Olha": "097-777-33-22"
}
contacts["Taras"] = "063-000-11-22"
contacts.pop("Ivan", None)
print(list(contacts.keys()))
print(list(contacts.values()))
print("Katya" in contacts)

# task 2
grades = {
    "math": 88,
    "physics": 75,
    "english": 93,
    "history": 59
}
kamay_velika = max(grades, key=grades.get)
print(kamay_velika)
seredniy_ball = sum(grades.values()) / len(grades)
print(seredniy_ball)
mayMalo_80 = [subject for subject, grade in grades.items() if grade > 80]
print(mayMalo_80)

# task 3
transactions = [
    ("Anna", 200),
    ("Ivan", -50),
    ("Anna", 100),
    ("Olha", 500),
    ("Ivan", 150),
    ("Olha", -100),
]
balances = {}
for name, amount in transactions:
    balances[name] = balances.get(name, 0) + amount
print(balances)
MayVelikiyBalanc = max(balances, key=balances.get)
print(MayVelikiyBalanc)
MaliyBalanc = [name for name, balance in balances.items() if balance < 0]
print(MaliyBalanc)

# task 4
text = "hello world hello again hello world test world"
words = text.split()
KilkoSliv = {}
for word in words:
    KilkoSliv[word] = KilkoSliv.get(word, 0) + 1
print(KilkoSliv)
import json

# task 5
student = {
    "name": "Anna",
    "age": 20,
    "courses": ["math", "physics", "english"]
}
json_string = json.dumps(student)
print(json_string)
SlovnikStudenta = json.loads(json_string)
SlovnikStudenta["courses"].append("history")
print(SlovnikStudenta)