    # Пример 1. [1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
list = [1, 2, 3, 4, 5, 6]
list1 = list[:3]
list2 = list[3:]
list3 = [list1, list2]
print(list3)

    # Пример 2. [1, 2, 3] => [[1, 2], [3]]
list = [1, 2, 3]
list1 = list[:2]
list2 = list[2:]
list3 = [list1, list2]
print(list3)
    # Пример 3. [1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
list = [1, 2, 3, 4, 5]
list1 = list[:3]
list2 = list[3:]
list3 = [list1, list2]
print(list3)
    # Пример 4. [1] => [[1], []]
list = [1]
list1 = list[:1]
list2 = list[1:]
list3 = [list1, list2]
print(list3)
    # Пример 5. [] => [[], []]
list = []
list1 = list[:1]
list2 = list[1:]
list3 = [list1, list2]
print(list3)