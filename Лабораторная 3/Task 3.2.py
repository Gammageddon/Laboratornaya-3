# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, symbol_=","):
    list1 = str1.split(symbol_)
    list2 = str2.split(symbol_)
    common_participants = []

    for i in list1:
        for j in list2:
            if i == j:
                common_participants.append(i)
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))