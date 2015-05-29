log = True
while log is True:
    file1 = input('Введите имя текстового файла с тестом (без расширения): ') + '.txt'
    
    try:
        test1 = open(file1, 'r')
        log = False
    except FileNotFoundError:
        print('\nФайл ', file1, 'не найден!\n')

list_correct_answer = []

for line in test1:
    if line.startswith('%*Верный'):
        correct_answer = line[16:-4].strip()
        list_correct_answer.append(correct_answer)

print('Правильные ответы на тест: ', list_correct_answer)
input()
