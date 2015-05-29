log = True
while log is True:
    file1 = input('Введите имя текстового файла с вопросами (без расширения): ') + '.txt'
    
    try:
        test1 = open(file1, 'r')
        log = False
    except FileNotFoundError:
        print('Файл ', file1, 'не найден!')

while log is False:
    try:
        n = input('Введите номер первого вопроса: ')
        nnn = int(n)
        log = True
    except ValueError:
        print('Ошибка ввода! Введите целое число!')

list_correct_answer = []

for line in test1:
    if line.startswith('%*Верный'):
        correct_answer = line[16:-4].strip()
        list_correct_answer.append(correct_answer)
test1.close
test1 = open('test1.txt', 'r')
i = 0
for line in test1:
    
    if line.startswith('%*--'):
        print('#L', nnn, 'W4')
        nnn += 1
        b = 0
        correct = list_correct_answer[i]
        i += 1

    start = line[0]
    if start.isalpha() or start.isdigit():
        question = line[0:-3].strip()
        print(question)        

    if line.startswith('%*Ответ'):
        b += 1
        answer = line[11:-3]
        if b == int(correct):
            print('$!', answer.strip())
        else:
            print('$?', answer.strip())
test1.close

input()
