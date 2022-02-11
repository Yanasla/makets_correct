from itertools import islice

# вставить в текстовый файл отсутствующие нули
fin = open("makets_12-21/Gelicon_SES_20211231.txt")
fout = open("makets_12-21/Gelicon_SES_20211231_cor.txt", "wt")
for line in fin:
    fout.write(line.replace(':,', ':0,'))
fin.close()
fout.close()

fin = open("makets_12-21/Gelicon_SES_20211231_cor.txt")
fout = open("makets_12-21/Gelicon_SES_20211231_cor1.txt", "wt")
for line in fin:
    fout.write(line.replace('::', ':0:'))
fin.close()
fout.close()

# замена запятых на точки
fin = open("makets_12-21/Gelicon_SES_20211231_cor1.txt")
fout = open("makets_12-21/Gelicon_SES_20211231_cor2.txt", "wt")
for line in fin:
    fout.write(line.replace(',', '.'))
fin.close()
fout.close()

# считываем все строки
with open('makets_12-21/Gelicon_SES_20211231_cor2.txt') as f:
    line13 = next(islice(f, 13, None))
print(line13)

with open('makets_12-21/Gelicon_SES_20211231_cor2.txt') as f:
    line16 = next(islice(f, 15, None))
print(line16)

with open('makets_12-21/Gelicon_SES_20211231_cor2.txt') as f:
    line17 = next(islice(f, 16, None))
print(line17)

with open('makets_12-21/Gelicon_SES_20211231_cor2.txt') as f:
    line18 = next(islice(f, 17, None))
print(line18)

with open('makets_12-21/Gelicon_SES_20211231_cor2.txt') as f:
    line3 = next(islice(f, 2, None))
print(line3)

line13_list = line13.split(':')
line16_list = line16.split(':')
line17_list = line17.split(':')
line18_list = line18.split(':')
line3_list = line3.split(':')

list1 = list(line18_list[0])
list2 = list(line13_list[1:])

line18_new = list1 + list2

print(line13_list)
print(line16_list)
print(line17_list)
print(line18_list)

# замена запятых на точки
#for i in range(len(line_list[1:])):
    #line_list[i] = line_list[i].replace(',', '.')
#print(line_list)

# Перевод списка строк в список чисел
for i in range(1, len(line13_list)-1):
    old_13 = line13_list[i]
    new_13 = float(old_13)
    line13_list[i] = new_13
print(line13_list)
l13 = len(line13_list) - 1


for i in range(1, len(line16_list)-1):
    old_16 = line16_list[i]
    new_16 = float(old_16)
    line16_list[i] = new_16
print(line16_list)
l16 = len(line16_list) - 1

for i in range(1, len(line17_list)-1):
    old_17 = line17_list[i]
    new_17 = float(old_17)
    line17_list[i] = new_17
print(line17_list)
l17 = len(line17_list) - 1

for i in range(1, len(line18_list)-1):
    old_18 = line18_list[i]
    new_18 = float(old_18)
    line18_list[i] = new_18
print(line18_list)
l18 = len(line18_list) - 1

for i in range(1, len(line3_list)-1):
    old_3 = line18_list[i]
    new_3 = float(old_3)
    line3_list[i] = new_3
print(line3_list)
l3 = len(line3_list) - 1

#обновление списка +11.26
for i in range(2, l13):
    old_13 = line13_list[i]
    new_13 = old_13 + 11.26
    line13_list[i] = round(new_13, 2)
    line13_list[1] = round(sum(line13_list[2:l13]),2)
print(line13_list)

#обновление списка +0.17
for i in range(2, l16):
    old_16 = line16_list[i]
    new_16 = old_16 + 0.17
    line16_list[i] = round(new_16, 2)
    line16_list[1] = round(sum(line16_list[2:l16]),2)
print(line16_list)

#обновление списка +1.22
for i in range(2, l17):
    old_17 = line17_list[i]
    new_17 = old_17 + 1.22
    line17_list[i] = round(new_17, 2)
    line17_list[1] = round(sum(line17_list[2:l17]),2)
print(line17_list)

#обновление списка ФОРМУЛА
for i in range(2, l18):
    a = line13_list[i]/0.5
    b = 0.8*line13_list[i]/0.5
    c = ((a**2)+(b**2))**0.5
    g = c/40
    renew_18 = 0.19*0.5+(g**2)*0.88*0.5+0.9933
    line18_list[i] = round(renew_18, 4)
    line18_list[1] = round(sum(line18_list[2:l18]), 4)
print(line18_list)


print(line3_list)


# преобразовать список в строку
makestring13 = ':'.join(map(str, line13_list))
print(makestring13)
makestring16 = ':'.join(map(str, line16_list))
print(makestring16)
makestring17 = ':'.join(map(str, line17_list))
print(makestring17)

makestring18 = ':'.join(map(str, line18_list))
print(makestring18)

#вписываем файл все строки
# Открываем файл только для чтения
f = open('makets_12-21/Gelicon_SES_20211231_cor2.txt', 'r')
lines = f.readlines()
lines[13] = makestring13
lines[15] = makestring16
lines[16] = makestring17
lines[17] = makestring18

# Закрываем файл
f.close()
# Открываем файл для записи
save_changes = open('makets_12-21/Gelicon_SES_20211231_cor2.txt', 'w')
# Сохраняем список строк
save_changes.writelines(lines)
# Закрываем файл
save_changes.close()

# замена точек на запятые
fin = open("makets_12-21/Gelicon_SES_20211231_cor2.txt")
fout = open("Gelicon_SES_20211231_cor3.txt", "wt")
for line in fin:
    fout.write(line.replace('.', ','))
fin.close()
fout.close()