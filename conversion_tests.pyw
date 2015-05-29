import sys, os
from PyQt4 import QtGui
from PyQt4 import QtCore

class Window(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setGeometry(300, 300, 800, 175)
        self.setWindowTitle(self.trUtf8('Конвертирование тестов в формат ЦДО'))
        #self.textEdit = QtGui.QTextEdit()
        #self.setCentralWidget(self.textEdit)
        self.statusBar()
        self.setFocus()

        exit_prog = QtGui.QAction(QtGui.QIcon('open.png'), 'Закрыть программу', self)
        exit_prog.setShortcut('Ctrl+Q')
        exit_prog.setStatusTip('Выход из программы')
        self.connect(exit_prog, QtCore.SIGNAL('triggered()'), exit)


        select_folder = QtGui.QAction(QtGui.QIcon('open.png'), 'Выбрать папку с тестами', self)
        select_folder.setShortcut('Ctrl+O')
        select_folder.setStatusTip('Выбор папки, содержащей тесты в исходном формате')
        self.connect(select_folder, QtCore.SIGNAL('triggered()'), self.showDialog)

        input_number = QtGui.QAction(QtGui.QIcon('open.png'), 'Ввести номер первого вопроса', self)
        input_number.setShortcut('Ctrl+N')
        input_number.setStatusTip('Ввод номера, который будет присвоен первому вопросу отконвертированного теста')
        self.connect(input_number, QtCore.SIGNAL('triggered()'), self.showDialog2)

        convert = QtGui.QAction(QtGui.QIcon('open.png'), 'Отконвертировать', self)
        convert.setShortcut('Ctrl+K')
        convert.setStatusTip('Запуск конвертирования тестов в формат ЦДО')
        self.connect(convert, QtCore.SIGNAL('triggered()'), self.conversion)

        menubar = self.menuBar()
        button1 = menubar.addMenu('&Файл')
        button1.addAction(exit_prog)

        button2 = menubar.addMenu('&Конвертирование')
        button2.addAction(select_folder)
        button2.addAction(input_number)
        button2.addAction(convert) 

        fntMyFont1 = QtGui.QFont(self)
        fntMyFont1.setBold(True)
        fntMyFont1.setPixelSize(12)

        fntMyFont2 = QtGui.QFont(self)
        fntMyFont2.setBold(False)
        fntMyFont2.setPixelSize(12)

        fntMyFont3 = QtGui.QFont(self)
        fntMyFont3.setBold(True)        
        fntMyFont3.setPixelSize(14)        

        self.button1 = QtGui.QPushButton('Выбрать папку с тестами', self)
        self.button1.setGeometry(20, 35, 160, 30)
        self.button1.setFont(fntMyFont2)        
        self.button1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button1.setStatusTip('Выбор папки, содержащей тесты в исходном формате')
        self.connect(self.button1, QtCore.SIGNAL('clicked()'), self.showDialog)
        #self.setFocus()

        self.button2 = QtGui.QPushButton('Ввести номер первого вопроса', self)
        self.button2.setFont(fntMyFont2)
        self.button2.setGeometry(190, 35, 200, 30)
        self.button2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button2.setShortcut('Ctrl+N')
        self.button2.setStatusTip('Ввод номера, который будет присвоен первому вопросу отконвертированного теста')
        self.connect(self.button2, QtCore.SIGNAL('clicked()'), self.showDialog2)
        #self.setFocus()
        
        self.button3 = QtGui.QPushButton('Отконвертировать тесты', self)
        self.button3.setFont(fntMyFont2)
        self.button3.setGeometry(400, 35, 200, 30)
        self.button3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.connect(self.button3, QtCore.SIGNAL('clicked()'), self.conversion)
        #self.setFocus()

        self.label1 = QtGui.QLabel(self)
        self.label1.setGeometry(20, 65, 105, 30)
        self.label1.setFont(fntMyFont1)        
        self.label1.setText('Папка с тестами:')

        self.label2 = QtGui.QLabel(self)
        self.label2.setGeometry(135, 65, 1000, 30)
        self.label2.setFont(fntMyFont2)
        #self.label2.move(135, 65)
        #self.label2.adjustSize()
        #self.label2.setScaledContents(True)

        
        self.label2.setText('не задана')

        self.label3 = QtGui.QLabel(self)
        self.label3.setGeometry(20, 80, 130, 30)
        self.label3.setFont(fntMyFont1)
        self.label3.setText('№ первого вопроса:')

        self.label4 = QtGui.QLabel(self)
        self.label4.setGeometry(160, 80, 300, 30)
        self.label4.setFont(fntMyFont2)        
        self.label4.setText('не задан')        

        self.label5 = QtGui.QLabel(self)
        self.label5.setGeometry(20, 95, 130, 30)
        self.label5.setFont(fntMyFont1)

        self.label6 = QtGui.QLabel(self)
        self.label6.setGeometry(160, 95, 700, 30)
        self.label6.setFont(fntMyFont2)

        self.label7 = QtGui.QLabel(self)
        self.label7.setGeometry(20, 110, 700, 30)
        self.label7.setFont(fntMyFont3)

        self.label8 = QtGui.QLabel(self)
        self.label8.setGeometry(20, 125, 700, 30)
        self.label8.setFont(fntMyFont2)
        



    def showDialog(self):

        #files = QtGui.QFileDialog.getOpenFileNames(self, 'Выбрать файлы')
        #print(files)
        #list_tests = str(files)
        global folder
        folder = QtGui.QFileDialog.getExistingDirectory(self, 'Выбор папки с тестами')
        if len(folder) > 0:
            self.label2.setText(folder)
            global list_tests
            list_tests = os.listdir(path=folder)
            self.label5.setText('Количество файлов:')
            self.label6.setText(str(len(list_tests)))
            self.label7.setText('')      
            self.label8.setText('')            

    def showDialog2(self):
        global number
        number, ok = QtGui.QInputDialog.getText(self, 'Номер первого вопроса', 'Введите номер, который будет присвоен первому вопросу теста:')
        
        try:
            global nnn
            nnn = int(number)
            if ok:
                self.label4.setText(number)
                self.label7.setText('')      
                self.label8.setText('')                
        except ValueError:  #Если введено не целое число
            if ok:
                self.label4.setText('<font color = red>Ошибка ввода! Должно быть введено целое число!<\\font>')
                self.label7.setText('')      
                self.label8.setText('')

    def closeEvent(self, event):    #Подтверждение выхода
        reply = QtGui.QMessageBox.question(self, self.trUtf8('Закрытие программы'),
            self.trUtf8("Вы уверены что хотите выйти?"),
                QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        
    def conversion(self):   

        try:
            nnn = int(number)
            file2 = folder + '\\' + 'ЦДО.txt'

            i = 0
            for element in list_tests:
                g = list_tests[i]
                if g.endswith('.txt'):
                
                    if list_tests[i] == 'ЦДО.txt':
                        i += 1
                        continue
          
                    test1 = open(folder + '\\' + list_tests[i], 'r')

                    list_correct_answer = []    #Список правильных ответов
                    
                    for line in test1:
                        if line.startswith('%*Верный'): #Если строка с номером правильного ответа
                            correct_answer = line[16:-4].strip() #Номер правильного ответа
                            list_correct_answer.append(correct_answer) #Добавления элемента в список правильных ответов

                    test1.close()

                    test1 = open(folder + '\\' + list_tests[i], 'r')
                    test2 = open(file2, 'a')

                    x = 0
                    for line in test1:
                        
                        if line.startswith('%*--'): #Если строка с номером вопроса
                            test2.write('\n' + '#L' + str(nnn) + ' W4' + '\n')
                            correct = list_correct_answer[x] #Номер правильного ответа на этот вопрос
                            b = 0       #Сброс кол-ва вариантов ответов
                            nnn += 1    #Номер следующего вопроса
                            x += 1      #Номер элемента списка - правильный ответ на след. вопрос

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
                    
                    i += 1
                else:
                    i += 1
            
            self.label7.setText("<font color = green>Конвертирование завершено!<\\font>")      
            self.label8.setText('Файл "ЦДО.txt" с тестом в формате ЦДО сохранен в папке с исходными тестами!')   
        except ValueError:  #Если введено не целое число
            self.label7.setText('<font color = red>Невозможно начать конвертирование. Неверно задан номер вопроса!<\\font>')
        except NameError:
            self.label7.setText('<font color = red>Невозможно начать конвертирование. Не выбрана папка с тестами или выбрана пустая папка!<\\font>')
            
 
app = QtGui.QApplication(sys.argv)
qb = Window()
qb.show()
sys.exit(app.exec_())
