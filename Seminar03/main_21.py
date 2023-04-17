#21. Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

my_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
print(my_list,"\n")

my_list_new = []

for i in range(len(my_list)):
     for (k, v) in my_list[i].items():
          my_list_new.append(v) #add new value to list
          my_list_new[-1] = str(my_list_new[-1].replace(' ','')) #eliminate spaces - to ensure the same values

my_set = set(my_list_new) #set has unique elements only !!!

print(my_set)


