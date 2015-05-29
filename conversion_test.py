log = True
while log is True:
    name1 = input('Введите имя текстового файла с тестом (без расширения): ')   #Ввод имени файла
    file1 = name1 + '.txt'  #Присвоение расширения файлу
    try:
        test1 = open(file1, 'r')    #Открытие файла с тестом для конвертирования
        log = False
    except FileNotFoundError:   #Если файл не найден
        print('\nФайл ', file1, 'не найден!\n')

name2 = name1 + ' (ЦДО)'    #Имя файла с отконвертированным тестом
file2 = name2 + '.txt'      #Присвоение расширения файлу

#ВВОД ИМЕНИ ФАЙЛА С ОТКОНВЕРТИРОВАННЫМ ТЕСТОМ
#log = True
#while log is True:        
#    file2 = input('Файл с отконвертированным тестом будет сохранен в той же папке.\nВведите имя этого файла (без расширения): ') + '.txt'
#    try:
#        test2 = open(file2, 'w')
#        log = False        
#    except OSError:
#        print('\nИмя файла не должно содержать символы \ / : " ? * | < >\n')

log = True    
while log is True:
    try:
        n = input('Введите номер первого вопроса: ') #Нумерация вопросов начнется с этого числа
        nnn = int(n)
        log = False
    except ValueError:  #Если введено не целое число
        print('\nОшибка ввода! Должно быть введено целое число!\n')

list_correct_answer = []    #Список правильных ответов

for line in test1:
    if line.startswith('%*Верный'): #Если строка с номером правильного ответа
        correct_answer = line[16:-4].strip() #Номер правильного ответа
        list_correct_answer.append(correct_answer) #Добавления элемента в список правильных ответов

test1.close()

test1 = open(file1, 'r')    #Открытие файла с тестом для конвертирования
test2 = open(file2, 'w')    #Открытие файла для записи отконвертированного теста    

i = 0
for line in test1:
    
    if line.startswith('%*--'): #Если строка с номером вопроса
        test2.write('\n' + '#L' + str(nnn) + ' W4' + '\n')
        correct = list_correct_answer[i] #Номер правильного ответа на этот вопрос
        b = 0       #Сброс кол-ва вариантов ответов
        nnn += 1    #Номер следующего вопроса
        i += 1      #Номер элемента списка - правильный ответ на след. вопрос

    start = line[0]
    if start.isalpha() or start.isdigit():  #Если строка начинается с буквы или цифры
        question = line[0:-3].strip()
        test2.write(question + '\n')
 
    if line.startswith('%*Ответ'):  #Если вариант ответа
        b += 1      #Увеличиваем кол-во вариантов ответа
        answer = line[11:-3].strip()
        if b == int(correct):   #Если ответ правильный
            test2.write('$!' + answer + '\n')
        else:
            test2.write('$?' + answer + '\n')
test2.close()
test1.close()

print('\nКонвертирование завершено!\nВопросы в формате ЦДО сохранены в файле "' + file2 + '"')

input()
