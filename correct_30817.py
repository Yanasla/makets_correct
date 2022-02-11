#ИЗМЕНЕНИЕ 30817 МАКЕТА

from itertools import islice

# вставить в текстовый файл отсутствующие нули
fin = open("makets_12-21/Gelicon_SES_2022029.30817")
fout = open("makets_12-21/Gelicon_SES_2022029_cor.txt", "wt")
for line in fin:
    fout.write(line.replace(':,', ':0,'))
fin.close()
fout.close()
# замена :: на :0:
fin = open("makets_12-21/Gelicon_SES_2022029_cor.txt")
fout = open("makets_12-21/Gelicon_SES_2022029_cor1.txt", "wt")
for line in fin:
    fout.write(line.replace('::', ':0:'))
fin.close()
fout.close()

# замена запятых на точки
fin = open("makets_12-21/Gelicon_SES_2022029_cor1.txt")
fout = open("makets_12-21/Gelicon_SES_2022029_cor2.txt", "wt")
for line in fin:
    fout.write(line.replace(',', '.'))
fin.close()
fout.close()

# считываем строки
with open('makets_12-21/Gelicon_SES_2022029_cor2.txt') as f:
    line2 = next(islice(f, 2, None))
print(line2)

with open('makets_12-21/Gelicon_SES_2022029_cor2.txt') as f:
    line6 = next(islice(f, 6, None))
print(line6)

with open('makets_12-21/Gelicon_SES_2022029_cor2.txt') as f:
    line17 = next(islice(f, 17, None))
print(line17)

line2_list = line2.split(':')
line6_list = line6.split(':')
line17_list = ''

print(line2_list)
print(line6_list)
print(line17_list)

# замена запятых на точки
#for i in range(len(line_list[1:])):
    #line_list[i] = line_list[i].replace(',', '.')
#print(line_list)

# Перевод списка строк в список чисел
for i in range(1, len(line2_list)-1):
    old_1 = line2_list[i]
    new_1 = float(old_1)
    line2_list[i] = new_1
print(line2_list)
l2 = len(line2_list) - 1

for i in range(1, len(line6_list)-1):
    old_6 = line6_list[i]
    new_6 = float(old_6)
    line6_list[i] = new_6
print(line6_list)
l6 = len(line6_list) - 1


#обновление списка: удаление ночной генерации
for i in range(2, l2):
    if (((1 < i <= 8) or (34 <= i <= 25)) and (line2_list[i] != 0)):
        line2_list[11] = line2_list[11] + line2_list[i]
        line2_list[i] = 0
print(line2_list)

for j in range(2, l6):
    if (((0 < j <= 8) or (19 <= j <= 25)) and (line6_list[j] != 0)):
        line6_list[11] = line6_list[11] + line6_list[j]
        line6_list[j] = 0
print(line6_list)

# преобразовать список в строку
makestring2 = ':'.join(map(str, line2_list))
print(makestring2)

makestring6 = ':'.join(map(str, line2_list))
print(makestring2)

#вписываем файл все строки
# Открываем файл только для чтения
f = open('makets_12-21/Gelicon_SES_2022029_cor2.txt', 'r')
lines = f.readlines()
lines = lines[:-1]
lines[2] = makestring2
lines[6] = makestring6

# Закрываем файл
f.close()
# Открываем файл для записи
save_changes = open('makets_12-21/Gelicon_SES_2022029_cor2.txt', 'w')
# Сохраняем список строк
save_changes.writelines(lines)
# Закрываем файл
save_changes.close()

# замена точек на запятые
fin = open("makets_12-21/Gelicon_SES_2022029_cor2.txt")
fout = open("Gelicon_SES_2022029_cor3.30817", "wt")
for line in fin:
    fout.write(line.replace('.', ','))
fin.close()
fout.close()