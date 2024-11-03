# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, a=","):

 group1_members = group1.split(a)
 group2_members = group2.split(a)
 common_members = sorted(set(group1_members).intersection(set(group2_members)))
 return common_members

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
common_participants = find_common_participants(participants_first_group, participants_second_group, a="|")
print("Общие участники:", common_participants)
# TODO Провеьте работу функции с разделителем отличным от запятой
