# coding: utf8

import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    def __init__(self, parent=None, se=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setWindowTitle(self.trUtf8('Конвертирование тестов в формат ЦДО'))
        self.resize(650, 245)
        self.center()  # Function places the window in the center of the screen
        self.statusBar()
        self.setMinimumSize(650, 245)
        self.setMaximumSize(650, 245)
#        self.setGeometry(100, 100, 1000, 205)
#        self.statusBar().showMessage('Pleshkov Andrey')

        self.exit_program = QtGui.QAction(QtGui.QIcon('open.png'), 'Закрыть программу', self)
        self.exit_program.setShortcut('Ctrl+Q')
        self.exit_program.setStatusTip('Выход из программы')
        self.connect(self.exit_program, QtCore.SIGNAL('triggered()'), exit)

        self.select_folder = QtGui.QAction(QtGui.QIcon('open.png'), 'Выбрать файлы с тестами', self)
        self.select_folder.setShortcut('Ctrl+O')
        self.select_folder.setStatusTip('Выбор файлов с тестами в исходном формате')
        self.connect(self.select_folder, QtCore.SIGNAL('triggered()'), self.select_files)

        self.convert = QtGui.QAction(QtGui.QIcon('open.png'), 'Отконвертировать тесты', self)
        self.convert.setShortcut('Ctrl+K')
        self.convert.setStatusTip('Запуск конвертирования тестов в формат ЦДО')
        self.connect(self.convert, QtCore.SIGNAL('triggered()'), self.conversion)

        self.menu = self.menuBar()  # Create menu
        self.button1 = self.menu.addMenu('&Файл')
        self.button1.addAction(self.exit_program)

        self.button2 = self.menu.addMenu('&Конвертирование')
        self.button2.addAction(self.select_folder)
        self.button2.addAction(self.convert)

        self.font2 = QtGui.QFont(self)
        self.font2.setBold(False)
        self.font2.setPixelSize(12)

        self.button3 = QtGui.QPushButton('Выбрать файлы с тестами', self)
        self.button3.setGeometry(10, 32, 170, 32)
        self.button3.setFont(self.font2)
        self.button3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button3.setStatusTip('Выбор файлов с тестами в исходном формате')
        self.connect(self.button3, QtCore.SIGNAL('clicked()'), self.select_files)

        self.button4 = QtGui.QPushButton('Отконвертировать тесты', self)
        self.button4.setFont(self.font2)
        self.button4.setGeometry(10, 71, 170, 32)
        self.button4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button4.setStatusTip('Запуск конвертирования тестов в формат ЦДО')
        self.connect(self.button4, QtCore.SIGNAL('clicked()'), self.conversion)

        """ First frame """

        self.frame1 = QtGui.QFrame(self)
        self.frame1.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtGui.QFrame.Raised)
        self.frame1.setGeometry(180, 15, 165, 100)
        self.gridlay1 = QtGui.QGridLayout(self.frame1)

        self.group1 = QtGui.QGroupBox('Конвертировать тесты:', self.frame1)  # Frame with an inscription
        self.lay1 = QtGui.QVBoxLayout(self.group1)  # Manager placement of elements in the frame

        # Two dependent RadioButton:
        self.radio1 = QtGui.QRadioButton('В один файл', self.group1)
        self.radio1.setStatusTip('Все тесты после конвертирования будут сохранены в один файл')
        self.radio2 = QtGui.QRadioButton('В отдельные файлы', self.group1)
        self.radio2.setStatusTip('Каждый тест после конвертирования будет сохранен в отдельный файл')
        self.radio2.setChecked(True)

        self.lay1.addWidget(self.radio1)
        self.lay1.addWidget(self.radio2)
        self.gridlay1.addWidget(self.group1, 0, 0, 0, 0)
        self.radio1.toggled.connect(self.selection_radio_button)

        """ Second frame """

        global number
        number = 1

        self.frame2 = QtGui.QFrame(self)
        self.frame2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame2.setGeometry(335, 15, 165, 100)
        self.gridlay2 = QtGui.QGridLayout(self.frame2)

        self.group2 = QtGui.QGroupBox('Номер первого вопроса:', self.frame2)
        self.lay2 = QtGui.QVBoxLayout(self.group2)

        self.flag = QtGui.QCheckBox('Сквозная нумерация', self.group2)
        self.flag.setStatusTip('Нумерация вопросов каждого теста не сбрасывается, а продолжается')
        self.flag.setCheckState(QtCore.Qt.Unchecked)

        self.lay2.addWidget(self.flag)
        self.flag.stateChanged.connect(self.state_changed)

        self.ln_edit = QtGui.QLineEdit('', self.group2)
        self.ln_edit.setReadOnly(True)  # Read-only
        self.ln_edit.setFrame(False)  # Frame
        self.ln_edit.setText('1 (для всех тестов)')
        self.ln_edit.setStatusTip('Нумерация вопросов каждого теста будет начинаться с единицы')

#        self.ln_edit.editingFinished.connect(self.input_number)
#        self.ln_edit.textChanged.connect(self.input_number)

        self.lay2.addWidget(self.ln_edit)
        self.gridlay2.addWidget(self.group2, 0, 0, 0, 0)

        """ Third frame """

        global name
        name = 'для проверки на длину'

        self.frame3 = QtGui.QFrame(self)
        self.frame3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame3.setGeometry(490, 15, 160, 100)
        self.gridlay3 = QtGui.QGridLayout(self.frame3)

        self.group3 = QtGui.QGroupBox('Имя выходного файла:', self.frame3)
        self.lay3 = QtGui.QVBoxLayout(self.group3)

        self.flag2 = QtGui.QCheckBox('Изменить', self.group3)
        self.flag2.setStatusTip('Изменить имя выходного файла (доступно только при конвертировании в один файл)')
        self.flag2.setCheckState(QtCore.Qt.Unchecked)
        self.lay3.addWidget(self.flag2)
        self.flag2.stateChanged.connect(self.state_changed2)

        self.ln_edit2 = QtGui.QLineEdit('', self.group3)
        self.ln_edit2.setStatusTip('Формат имен выходных файлов: test - имя исходного файла с тестом')
        self.ln_edit2.setReadOnly(True)  # Read-only
        self.ln_edit2.setFrame(False)  # Frame
        self.ln_edit2.setText('test (ЦДО)')

        self.lay3.addWidget(self.ln_edit2)
        self.gridlay3.addWidget(self.group3, 0, 0, 0, 0)

        """ Fourth frame """

        self.frame4 = QtGui.QFrame(self)
        self.frame4.setStatusTip('Путь к папке, в которой находятся выбранные файлы с тестами для конвертирования')
        self.frame4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame4.setGeometry(0, 100, 650, 70)
        self.gridlay4 = QtGui.QGridLayout(self.frame4)

        self.group4 = QtGui.QGroupBox('Папка с тестами:', self.frame4)
        self.lay4 = QtGui.QVBoxLayout(self.group4)

        self.label1 = QtGui.QLabel(self.group4)
        self.label1.setText('<font color = grey>Файлы не выбраны<\\font>')

        self.lay4.addWidget(self.label1)
        self.gridlay4.addWidget(self.group4, 0, 0, 0, 0)

        """ Fifth frame """

        self.frame5 = QtGui.QFrame(self)
        self.frame5.setStatusTip('Количество файлов, выбранных для конвертирования')
        self.frame5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame5.setGeometry(0, 155, 145, 75)
        self.gridlay5 = QtGui.QGridLayout(self.frame5)

        self.group5 = QtGui.QGroupBox('Количество файлов:', self.frame5)
        self.lay5 = QtGui.QVBoxLayout(self.group5)

        self.label2 = QtGui.QLabel(self.group5)
        self.label2.setText('<font color = grey>Файлы не выбраны<\\font>')

        self.lay5.addWidget(self.label2)
        self.gridlay5.addWidget(self.group5, 0, 0, 0, 0)

        """ Sixth frame """

        self.frame6 = QtGui.QFrame(self)
        self.frame6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame6.setGeometry(135, 155, 275, 75)
        self.gridlay6 = QtGui.QGridLayout(self.frame6)

        self.group6 = QtGui.QGroupBox('Результат конвертирования:', self.frame6)
        self.lay6 = QtGui.QVBoxLayout(self.group6)

        self.label3 = QtGui.QLabel(self.group6)
        self.label3.setText('<font color = grey>Конвертирование не запущено<\\font>')

        self.lay6.addWidget(self.label3)
        self.gridlay6.addWidget(self.group6, 0, 0, 0, 0)

        """ Seventh frame """

        self.frame7 = QtGui.QFrame(self)
        self.frame7.setStatusTip('Author: Andrey Pleshkov (ITMO University) © 2015')
        self.frame7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame7.setGeometry(400, 155, 250, 75)
        self.gridlay7 = QtGui.QGridLayout(self.frame7)

        self.group7 = QtGui.QGroupBox('Автор программы:', self.frame7)
        self.lay7 = QtGui.QVBoxLayout(self.group7)

        self.label4 = QtGui.QLabel(self.group7)
        self.label4.setText('<font color = grey>Андрей Плешков © 2015<\\font>')

        self.lay7.addWidget(self.label4)
        self.gridlay7.addWidget(self.group7, 0, 0, 0, 0)

    def state_changed(self):

        """

        The function starts when changing the status flag 'Сквозная нумерация'
        Depending on the status of the flag to set parameters for a LineEdit (enter the number).

        """

        global number

        if self.flag.isChecked():  # If the flag is set
            self.ln_edit.setReadOnly(False)  # Read-only
            self.ln_edit.setFrame(True)  # Frame
            self.ln_edit.setValidator(QtGui.QIntValidator(0, 999999999))  # Limit input
            self.ln_edit.setPlaceholderText('Например: 1')  # Help
            self.ln_edit.textChanged.connect(self.input_number)
            self.ln_edit.clear()
            self.ln_edit.setStatusTip('Номер, с которого начнется сквозная нумерация вопросов')

        else:
            self.ln_edit.setReadOnly(True)  # Read-only
            self.ln_edit.setFrame(False)  # Frame
            self.ln_edit.setText('1 (для всех тестов)')
            self.ln_edit.setStatusTip('Нумерация вопросов каждого теста будет начинаться с единицы')
            number = 1

        self.label3.setText('<font color = grey>Конвертирование не запущено<\\font>')

    def state_changed2(self):

        """

        The function starts when changing the status flag 'Изменить'
        Depending on the status of the flag to set parameters for a LineEdit (enter the name).

        """

        global error_id
        error_id = None

        if self.radio1.isChecked():

            if self.flag2.isChecked():  # If the flag is set
                self.ln_edit2.setReadOnly(False)  # Read-only
                self.ln_edit2.setFrame(True)  # Frame
                self.ln_edit2.setPlaceholderText('Например: ЦДО')  # Help
                self.ln_edit2.textChanged.connect(self.input_name)
                self.ln_edit2.clear()
                self.ln_edit2.setStatusTip('Введите имя выходного файла')
#                self.ln_edit2.setInputMask('Имя: NNNNNNNNNNN.t\\xt')

            else:
                self.ln_edit2.setReadOnly(True)  # Read-only
                self.ln_edit2.setFrame(False)  # Frame
                self.ln_edit2.setText('ЦДО')
                self.ln_edit2.setStatusTip('Имя выходного файла')

        elif self.radio2.isChecked():

            if self.flag2.isChecked():  # If the flag is set
                self.flag2.setCheckState(QtCore.Qt.Unchecked)
                error_id = 3

            else:
                self.ln_edit2.setReadOnly(True)  # Read-only
                self.ln_edit2.setFrame(False)  # Frame
                self.ln_edit2.setText('test (ЦДО)')
                self.ln_edit2.setStatusTip('Формат имен выходных файлов: test - имя исходного файла с тестом')

        if error_id is not None:  # If an error occurs, a message box opens
                self.error_window()

        self.label3.setText('<font color = grey>Конвертирование не запущено<\\font>')

    def center(self):

        """ We get the display resolution, get the size of the window, move window to the center of the screen. """

        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) // 2, (screen.height() - size.height()) // 2)

    def input_number(self):

        """ The function starts when changing the text in LineEdit. LineEdit value assigned to the variable number. """

        global number
        number = self.ln_edit.text()

    def input_name(self):

        """ The function starts when changing the text in LineEdit. LineEdit value assigned to the variable name. """

        global name
        name = self.ln_edit2.text()

        if name.endswith('.txt'):  # If the user specifies a file extension, it will be deleted
            name = name[0:-4]

    def selection_radio_button(self):

        """ Function is starts when the user toggles the RadioButton. It restores defaults. """

        self.flag2.setCheckState(QtCore.Qt.Unchecked)

        if self.radio1.isChecked():
            self.ln_edit2.setReadOnly(True)  # Read-only
            self.ln_edit2.setFrame(False)  # Frame
            self.ln_edit2.setText('ЦДО')
            self.ln_edit2.setStatusTip('Имя выходного файла')

        elif self.radio2.isChecked():
            self.ln_edit2.setReadOnly(True)  # Read-only
            self.ln_edit2.setFrame(False)  # Frame
            self.ln_edit2.setText('test (ЦДО)')
            self.ln_edit2.setStatusTip('Формат имен выходных файлов: test - имя исходного файла с тестом')

        self.label3.setText('<font color = grey>Конвертирование не запущено<\\font>')

    def select_files(self):

        """ File selection tests.

        Performs multi-select text files (.txt) with questions for the test.
        If you select at least one file:
            From the path to one of the selected files are retrieved path to a test that is displayed.
            Also displays the number of selected files.
        If not selected any file conversion results and selecting the files are cleared

        """

        global list_tests
        list_tests = QtGui.QFileDialog.getOpenFileNames(self, 'Выбрать файлы', '', '*.txt')

        if len(list_tests) > 0:

            d = list_tests[0]
            dd = d.rfind('\\')
            folder = d[0:dd]

            self.label2.setText('<font color = grey>' + str(len(list_tests)) + '<\\font>')
            self.label3.setText('<font color = grey>Конвертирование не запущено<\\font>')

            if len(str(folder)) > 106:
                label1_text = str(folder)[0:104] + '... '
                self.label1.setText('<font color = grey>' + label1_text + '<\\font>')
            else:
                self.label1.setText('<font color = grey>' + str(folder) + '<\\font>')

        else:
            self.label1.setText('<font color = grey>Файлы не выбраны<\\font>')
            self.label2.setText('<font color = grey>Файлы не выбраны<\\font>')
            self.label3.setText('<font color = grey>Конвертирование не запущено<\\font>')

    def closeEvent(self, event):  # Confirmation of exit

        """ Message Box opens to confirm the exit from the program. """

        reply = QtGui.QMessageBox.question(self, self.trUtf8('Закрытие программы'),
                                           self.trUtf8("Вы уверены что хотите выйти?"),
                                           QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        event.accept() if reply == QtGui.QMessageBox.Yes else event.ignore()

    def conversion(self):

        """ Conversion testing.

        Using the RadioButton to select options for saving of converted tests: a single file or separate.
        In the cycle:
            Open original tests, generated tuple correct answers, tests are closed.
            Open original tests, open for writing text files (using the context manager).
            Original tests are read line by line. Transformed questions are written to a file. Files closed.
            If error occurs, a window opens with an error message.
            If the conversion is completed, a window opens with an error message.

        Exceptions:
            ValueError - if you have entered is not an integer.
            NameError - if no number is entered first question or if not selected any test.
            UnicodeDecodeError - if the wrong encoding original file.
            OSError - if the input field name of the output file type invalid characters.

        Problems: the exception is invoked only if the original file in UTF-8 encoding. In any other encoding
        (except ANSI) during the conversion error will not occur, but the conversion will not work correctly.

        """

        global error_id, success_id, current_test
        error_id = None
        success_id = None

        try:
            n = int(number)
        except ValueError:
            error_id = 1
            self.label3.setText('<font color = red>Невозможно начать конвертирование<\\font>')

            if error_id is not None:  # If an error occurs, a message box opens
                self.error_window()
                return

        try:
            if len(list_tests) > 0 and len(name) > 0:
                i = 0
                for element in list_tests:

                    if self.flag.isChecked():
                        None
                    else:
                        n = 1

                    current_test = list_tests[i]

                    if current_test.endswith('(ЦДО).txt') or current_test.endswith('ЦДО.txt'):
                        i += 1
                        continue

                    test1 = open(current_test, 'r')

                    list_correct_answer = ()  # Tuple of correct answers

#                        for line in test1:
#                            if line.startswith('%*Верный'):  # If the string contains the number of the correct answer
#                                correct_answer = line[16:-4].strip()
#                                list_correct_answer.append(correct_answer)

                    list_correct_answer += tuple(line[16:-4].strip() for line in test1 if line.startswith('%*Верный'))

                    test1.close()

                    """ The full path to the output file: """

                    if self.radio1.isChecked():
                        ddd = current_test.rfind('\\') + 1

                        if self.flag2.isChecked():  # If the flag is set
                            f2 = current_test[0:ddd] + name + '.txt'
                        else:
                            f2 = current_test[0:ddd] + 'ЦДО.txt'

                    elif self.radio2.isChecked():
                        f2 = current_test.replace('.txt', ' (ЦДО).txt')

                    file2 = f2

                    test1 = open(current_test, 'r')

#                        test2 = open(file2, 'a')
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
#                        test2.close()
                    test1.close()

                    i += 1

                success_id = 0
                self.label3.setText('<font color = green>Конвертирование успешно завершено!<\\font>')

            elif len(list_tests) == 0 and len(name) > 0:
                error_id = 0
            elif len(list_tests) > 0 and len(name) == 0:
                error_id = 4
            elif len(list_tests) == 0 and len(name) == 0:
                error_id = 5

        except NameError:
            error_id = 0
            self.label3.setText('<font color = red>Невозможно начать конвертирование<\\font>')
        except UnicodeDecodeError:
            error_id = 2
            self.label3.setText('<font color = red>Невозможно начать конвертирование<\\font>')
        except OSError:
            error_id = 6
            self.label3.setText('<font color = red>Невозможно начать конвертирование<\\font>')
            self.ln_edit2.selectAll()

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

        """ It describes the parameters of the window with the success message and set success codes. """

        QtGui.QMessageBox.__init__(self)
        self.setWindowTitle('Успех')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setIcon(QtGui.QMessageBox.Information)
        self.addButton('ОК', QtGui.QMessageBox.AcceptRole)

        if success_id == 0:
            self.setText('Конвертирование успешно завершено!')

class ErrorMessage(QtGui.QMessageBox):
    def __init__(self, error_id):

        """ It describes the parameters of the window with the error message and set error codes. """

        QtGui.QMessageBox.__init__(self)
        self.setWindowTitle('Ошибка')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setIcon(QtGui.QMessageBox.Warning)
        self.addButton('ОК', QtGui.QMessageBox.AcceptRole)

        if error_id == 0:
            self.setText('Сначала выберите файлы с тестами для конвертирования.')
        elif error_id == 1:
            self.setText('Сначала введите номер первого вопроса.')
        elif error_id == 2:
            self.setText('Исходный файл с тестом должен быть в кодировке ANSI.')
        elif error_id == 3:
            self.setText('При выборе конвертирования в отдельные файлы нельзя изменить имена выходных файлов. '
                         'Им будут присвоены имена вида "test (ЦДО).txt", где test - имя исходного файла.')
        elif error_id == 4:
            self.setText('Сначала введите имя выходного файла.')
        elif error_id == 5:
            self.setText('Сначала выбере файлы с тестами для конвертирования и введите имя выходного файла.')
        elif error_id == 6:
            self.setText('Имя выходного файла не может содержать символы \ / : " ? * | < >')

app = QtGui.QApplication(sys.argv)
qb = Window()
qb.show()
sys.exit(app.exec_())
