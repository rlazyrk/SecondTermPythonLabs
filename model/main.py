from garden import Garden
garden1 = Garden(12, True, True, 135)
garden2 = Garden(214124, False, True, 1245)
gardens = [Garden.get_instance(), Garden.get_instance(), garden1, garden2]
for i in gardens:
    print(i)