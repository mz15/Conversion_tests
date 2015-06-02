import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setWindowTitle(self.trUtf8('Конвертирование тестов в формат ЦДО'))
        self.resize(1000, 175)
        self.center()
        self.statusBar()
        self.setMinimumSize(1000, 175)
#        self.setMaximumSize(1000, 175)
#        self.setGeometry(100, 100, 1000, 175)
#        self.statusBar().showMessage('Ready')
#        self.setFocus()
#        self.textEdit = QtGui.QTextEdit()
#        self.setCentralWidget(self.textEdit)

        exit_program = QtGui.QAction(QtGui.QIcon('open.png'), 'Закрыть программу', self)
        exit_program.setShortcut('Ctrl+Q')
        exit_program.setStatusTip('Выход из программы')
        self.connect(exit_program, QtCore.SIGNAL('triggered()'), exit)

        select_folder = QtGui.QAction(QtGui.QIcon('open.png'), 'Выбрать файлы с тестами', self)
        select_folder.setShortcut('Ctrl+O')
        select_folder.setStatusTip('Выбор файлов с тестами в исходном формате')
        self.connect(select_folder, QtCore.SIGNAL('triggered()'), self.select_files)

        input_number = QtGui.QAction(QtGui.QIcon('open.png'), 'Ввести номер первого вопроса', self)
        input_number.setShortcut('Ctrl+N')
        input_number.setStatusTip('Ввод номера, который будет присвоен первому вопросу отконвертированного теста')
        self.connect(input_number, QtCore.SIGNAL('triggered()'), self.input_number)

        convert = QtGui.QAction(QtGui.QIcon('open.png'), 'Отконвертировать тесты', self)
        convert.setShortcut('Ctrl+K')
        convert.setStatusTip('Запуск конвертирования тестов в формат ЦДО')
        self.connect(convert, QtCore.SIGNAL('triggered()'), self.conversion)

        menu = self.menuBar()
        button1 = menu.addMenu('&Файл')
        button1.addAction(exit_program)

        button2 = menu.addMenu('&Конвертирование')
        button2.addAction(select_folder)
        button2.addAction(input_number)
        button2.addAction(convert) 

        font1 = QtGui.QFont(self)
        font1.setBold(True)
        font1.setPixelSize(12)

        font2 = QtGui.QFont(self)
        font2.setBold(False)
        font2.setPixelSize(12)

        font3 = QtGui.QFont(self)
        font3.setBold(True)
        font3.setPixelSize(14)

        self.button1 = QtGui.QPushButton('Выбрать файлы с тестами', self)
        self.button1.setGeometry(20, 35, 170, 30)
        self.button1.setFont(font2)
        self.button1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button1.setStatusTip('Выбор файлов с тестами в исходном формате')
        self.connect(self.button1, QtCore.SIGNAL('clicked()'), self.select_files)

        self.button2 = QtGui.QPushButton('Ввести номер первого вопроса', self)
        self.button2.setFont(font2)
        self.button2.setGeometry(200, 35, 200, 30)
        self.button2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button2.setStatusTip('Ввод номера, который будет присвоен первому вопросу отконвертированного теста')
        self.connect(self.button2, QtCore.SIGNAL('clicked()'), self.input_number)

        self.button3 = QtGui.QPushButton('Отконвертировать тесты', self)
        self.button3.setFont(font2)
        self.button3.setGeometry(410, 35, 200, 30)
        self.button3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button3.setStatusTip('Запуск конвертирования тестов в формат ЦДО')
        self.connect(self.button3, QtCore.SIGNAL('clicked()'), self.conversion)

        self.label1 = QtGui.QLabel(self)
        self.label1.setGeometry(20, 65, 105, 30)
        self.label1.setFont(font1)
        self.label1.setText('Папка с тестами:')

        self.label2 = QtGui.QLabel(self)
        self.label2.setGeometry(135, 65, 1300, 30)
#        self.label2.move(135, 65)
        self.label2.setFont(font2)
        self.label2.setText('не задана')
#        self.label2.adjustSize()
#        self.label2.resize(self.label2.sizeHint())
#        self.label2.setScaledContents(True)

        self.label3 = QtGui.QLabel(self)
        self.label3.setGeometry(20, 80, 130, 30)
        self.label3.setFont(font1)
        self.label3.setText('№ первого вопроса:')

        self.label4 = QtGui.QLabel(self)
        self.label4.setGeometry(160, 80, 500, 30)
        self.label4.setFont(font2)
        self.label4.setText('не задан')        

        self.label5 = QtGui.QLabel(self)
        self.label5.setGeometry(20, 95, 130, 30)
        self.label5.setFont(font1)

        self.label6 = QtGui.QLabel(self)
        self.label6.setGeometry(160, 95, 700, 30)
        self.label6.setFont(font2)

        self.label7 = QtGui.QLabel(self)
        self.label7.setGeometry(20, 110, 700, 30)
        self.label7.setFont(font3)

        self.label8 = QtGui.QLabel(self)
        self.label8.setGeometry(20, 125, 700, 30)
        self.label8.setFont(font2)

    def center(self):

        """ We get the display resolution, get the size of the window, move window to the center of the screen. """

        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())//2, (screen.height()-size.height())//2)

    def select_files(self):

        """ File selection tests.

        Performs multi-select text files (.txt) with questions for the test.
        If you select at least one file:
            From the path to one of the selected files are retrieved path to a test that is displayed.
            Also displays the number of selected files.

        """

        global list_tests
        list_tests = QtGui.QFileDialog.getOpenFileNames(self, 'Выбрать файлы', '', '*.txt')

        if len(list_tests) > 0:
            d = list_tests[0]
            dd = d.rfind('\\')
            folder = d[0:dd]

            self.label2.setText(str(folder))
            self.label5.setText('Количество файлов:')
            self.label6.setText(str(len(list_tests)))
            self.label7.setText('')
            self.label8.setText('')

    def input_number(self):

        """ Enter the number of the first question.

        InputDialog opens to enter the number (positive integer) from which to start numbering of converted questions.
        Displays the number entered or an error message. If error occurs, a window opens with an error message.

        Exceptions:
            ValueError - if you have entered is not an integer.
            NegativeError - if you enter a negative integer.
            ZeroError - if you enter zero.

        """

        global number, n, error_id
        error_id = None

        number, ok = QtGui.QInputDialog.getText(self, 'Номер первого вопроса',
                                                'Введите номер, который будет присвоен первому вопросу теста:')

        try:
            if ok:
                n = int(number)
                if n < 0:
                    raise NegativeError('Ошибка. Нумерация вопросов не может начинаться с отрицательного числа.')
                if n == 0:
                    raise ZeroError('Ошибка. Нумерация вопросов не может начинаться с нуля.')
                self.label4.setText(number)
                self.label7.setText('')
                self.label8.setText('')
        except ValueError:
            if ok:
                error_id = 1
                self.label4.setText('<font color = red>Ошибка. '
                                    'Номером вопроса может быть только целое положительное число.<\\font>')
                self.label7.setText('')      
                self.label8.setText('')
        except NegativeError:
            if ok:
                error_id = 1
                self.label4.setText('<font color = red>' + NegativeError.text + '<\\font>')
                self.label7.setText('')
                self.label8.setText('')
        except ZeroError:
            if ok:
                error_id = 1
                self.label4.setText('<font color = red>' + ZeroError.text + '<\\font>')
                self.label7.setText('')
                self.label8.setText('')

        if error_id is not None:  # If an error occurs, a message box opens
            self.error_window()

    def closeEvent(self, event):  # Confirmation of exit

        """ Message Box opens to confirm the exit from the program. """

        reply = QtGui.QMessageBox.question(self, self.trUtf8('Закрытие программы'),
                                           self.trUtf8("Вы уверены что хотите выйти?"),
                                           QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        event.accept() if reply == QtGui.QMessageBox.Yes else event.ignore()

    def conversion(self):

        """ Conversion testing.

        Opens the MessageBox to select options for saving of converted tests: a single file or separate.
        In the cycle:
            Open original tests, generated tuple correct answers, tests are closed.
            Open original tests, open for writing text files (using the context manager).
            Original tests are read line by line. Transformed questions are written to a file. Files closed.
            If error occurs, a window opens with an error message.
            If the conversion is completed, a window opens with an error message.

        Exceptions:
            ValueError - if you have entered is not an integer.
            NegativeError - if you enter a negative integer.
            ZeroError - if you enter zero.
            NameError - if no number is entered first question or if not selected any test.
            UnicodeDecodeError - if the wrong encoding original file.

        Problems: the exception is invoked only if the original file in UTF-8 encoding. In any other encoding
        (except ANSI) during the conversion error will not occur, but the conversion will not work correctly.

        """

        global error_id, success_id, n
        error_id = None
        success_id = None

        try:
            n = int(number)

            if n < 0:
                raise NegativeError('Невозможно начать конвертирование. Неверно задан номер вопроса.')
            if n == 0:
                raise ZeroError('Невозможно начать конвертирование. Неверно задан номер вопроса.')

        except ValueError:  # If you have entered is not an integer
            error_id = 1
            self.label7.setText('<font color = red>Невозможно начать конвертирование. '
                                'Неверно задан номер вопроса.<\\font>')

            if error_id is not None:  # If an error occurs, a message box opens
                self.error_window()

            return None

        except NegativeError:
            error_id = 1
            self.label7.setText('<font color = red>' + NegativeError.text + '<\\font>')

            if error_id is not None:  # If an error occurs, a message box opens
                self.error_window()

            return None

        except ZeroError:
            error_id = 1
            self.label7.setText('<font color = red>' + ZeroError.text + '<\\font>')

            if error_id is not None:  # If an error occurs, a message box opens
                self.error_window()

            return None

        except NameError:
            error_id = 1
            self.label7.setText('<font color = red>Невозможно начать конвертирование. '
                                'Не задан номер первого вопроса.<\\font>')
            if error_id is not None:  # If an error occurs, a message box opens
                self.error_window()

            return None

        try:
            if len(list_tests) > 0:
                reply = QtGui.QMessageBox.question(self, 'Конвертирование', 'Для конвертирования тестов в один файл '
                                                                            'нажмите "Yes", в отдельные - "No"',
                                                   QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)
            
            i = 0
            for element in list_tests:

                current_test = list_tests[i]

                if current_test.endswith('(ЦДО).txt'):
                    i += 1
                    continue
      
                test1 = open(current_test, 'r')

                list_correct_answer = ()  # Tuple of correct answers

#                for line in test1:
#                    if line.startswith('%*Верный'):  # If the string contains the number of the correct answer
#                        correct_answer = line[16:-4].strip()
#                        list_correct_answer.append(correct_answer)

                list_correct_answer += tuple(line[16:-4].strip() for line in test1 if line.startswith('%*Верный'))

                test1.close()

                test1 = open(current_test, 'r')

                if reply == QtGui.QMessageBox.Yes:
                    ddd = current_test.rfind('\\') + 1
                    f2 = current_test[0:ddd] + 'ЦДО.txt'
                if reply == QtGui.QMessageBox.No:
                    f2 = current_test.replace('.txt', ' (ЦДО).txt')

                file2 = f2
#                test2 = open(file2, 'a')
                with open(file2, 'a') as test2:

                    x = 0
                    for line in test1:
                        
                        if line.startswith('%*--'):  # If the string contains the question number
                            test2.write('\n' + '#L' + str(n) + ' W4' + '\n')
                            correct = list_correct_answer[x]  # Number of correct answers to the current question
                            b = 0  # Reset the number of options
                            n += 1  # Number next question
                            x += 1  # Element number tuple - correct answer to the following question

                        start = line[0]
                        if start.isalpha() or start.isdigit():  # If the string contains a question
                            question = line[0:-3].strip()
                            test2.write(question + '\n')
                     
                        if line.startswith('%*Ответ'):  # If the string contains answer
                            b += 1  # Increases the number of options
                            answer = line[11:-3].strip()
                            right_answer = '$!' + answer + '\n'
                            wrong_answer = '$?' + answer + '\n'
                            test2.write(right_answer) if b == int(correct) else test2.write(wrong_answer)
#                test2.close()
                test1.close()
                
                i += 1

            success_id = 0
            self.label7.setText("<font color = green>Конвертирование завершено!<\\font>")

            if reply == QtGui.QMessageBox.Yes:
                self.label8.setText('Файл "ЦДО.txt" с тестом в формате ЦДО сохранен в папке с исходными тестами.')
            if reply == QtGui.QMessageBox.No:
                self.label8.setText('Файлы с тестами в формате ЦДО сохранены в папке с исходными тестами.')

        except NameError:
            error_id = 0
            self.label7.setText('<font color = red>Невозможно начать конвертирование. '
                                'Не выбрано ни одного файла с тестом.<\\font>')
        except UnicodeDecodeError:
            error_id = 2
            self.label7.setText('<font color = red>Невозможно начать конвертирование. '
                                'Исходные тесты должны быть в кодировке ANSI<\\font>')

        if error_id is not None:  # If an error occurs, a message box opens
            self.error_window()
        if success_id is not None:  # If the operation is successful, a message box opens
            self.success_window()

    def error_window(self):

        """ It displays a message box with an error message. """

        em = ErrorMessage(error_id)
        em.show()
        em.exec_()

    def success_window(self):

        """ It displays a message box on the completion of the conversion. """

        sm = SuccessMessage(success_id)
        sm.show()
        sm.exec_()

class SuccessMessage(QtGui.QMessageBox):
    def __init__(self, success_id):
        QtGui.QMessageBox.__init__(self)
        self.setWindowTitle('Успех')
        self.setIcon(QtGui.QMessageBox.Information)
        self.addButton('ОК', QtGui.QMessageBox.AcceptRole)

        if success_id == 0:
            self.setText(u"Конвертирование завершено")

class ErrorMessage(QtGui.QMessageBox):
    def __init__(self, error_id):
        QtGui.QMessageBox.__init__(self)
        self.setWindowTitle('Ошибка')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setIcon(QtGui.QMessageBox.Warning)
        self.addButton('ОК', QtGui.QMessageBox.AcceptRole)

        if error_id == 0:
            self.setText(u"Не выбраны тесты")
        elif error_id == 1:
            self.setText(u"Неверно введен номер первого вопроса")
        elif error_id == 2:
            self.setText(u"Неверная кодировка исходного теста")

class NegativeError(Exception):
    def __init__(self, text):
        NegativeError.text = text

class ZeroError(Exception):
    def __init__(self, text):
        ZeroError.text = text

app = QtGui.QApplication(sys.argv)
qb = Window()
qb.show()
sys.exit(app.exec_())
