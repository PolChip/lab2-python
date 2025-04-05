# Читаем числа из файла data.txt построчно
f = open('data.txt')
b = [int(f.readline().strip()) for i in range(10)]
# Создаем новый файл и запишем туда результы
result = open('result.txt', 'w')
# Построчно записываем результы
result.writelines('Сумма: ' + str(sum(b)) + '\n')
result.writelines('Среднее: ' + str(sum(b)//len(b)) + '\n')
result.writelines('Максимум: ' + str(max(b)) + '\n')
result.writelines('Минимум: ' + str(min(b)) + '\n')
