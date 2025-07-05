# Task 1
my_list=["butter","coffe","tea","salt"]
print(my_list)
my_list.append("bread")
print(my_list)


# Task 2
numbers = [10, 7, 1, 12, 11]
Average = sum(numbers) / len(numbers)
print(Average)


# Task 3
name = ["Oleg", "Alexandra", "Ivan", "Kolya", "Bogdan", "Elena"]
name.sort()
print(name)


# Task 4 
my_list = ["Odesa", "Ivano-Frankivsk", "Kyiv", "Lviv"]
my_list[1] = ['Poltava']
print(my_list[0])
print(my_list[-1])


# Task 5
songs_list = ["Roberto Kan - Dreamres",
              "I never Felt So Right",
              "Darkness",
              "Deep Mind - Open Your Eyes",
              "More - Slider & Magnit"]
print(len(songs_list))
songs_list.remove("Darkness")
songs_list.sort()
print(songs_list)
songs_list.reverse()
print(songs_list)