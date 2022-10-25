"""Программа может зашифровать ваш файл по заданному или генерированному ключу
Так же программа может расшифровать ваш файл лишь по тому ключу, по которому она зашифрована.
Генерированный ключ к расшифровке файла не подлежит. Всю инструкцию о программе вы можете прочитать
нажав "ПОМОЩЬ", все мои основные контакты можете узнать нажав "Обо мне". Приятного пользования!"""

# import os - Библиотека предоставляет переносимый способ использования функций, зависящих от операционной системы.
# import webbrowser - Библиотека, которая делает запрос в браузер и даёт результат.
# import random - Библиотека, которая реализует генератор псевдослучайных чисел.
# import string - Библиотека, которая делает общие операции со строками.
# import sys - Библиотека, которая предоставляет доступ к некоторым переменным, используемым или поддерживаемым
# from itertools import cycle - Модуль itertools стандартизирует основной набор быстрых эффективных инструментов. \
# Итератор cycle примером является данный способ cycle('ABCD') --> A B C D A B C D ...
# from PyQt6.QtCore import Qt - Библиотека для создания приложений с графическим интерфейсом с помощью инструментария Qt

import os
import webbrowser
import random
import string
import sys
from itertools import cycle
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon, QPixmap, QFont
from PyQt6.QtWidgets import QApplication, QDialog, QHBoxLayout, QFrame, QTabWidget, QLabel, QPushButton, QLineEdit, \
    QFileDialog, QMainWindow, QMessageBox, QWidget

# import Qt - разрешает доступ к любому классу или элементу любого подмодуля. (всё что ниже, его подмодули)
# import QAction - даёт различие панели инструментов и меню.
# import QIcon - может ставить иконки рядом | около | в указанном месте.
# import QPixmap - можно использовать в качестве устройства рисования.
# import QFont - задает запрос для шрифта, используемого для рисования текста.
# import QApplication, QWidget - обработчик приложения и базовый пустой виджет графического интерфейса.
# import QDialog - происходит вся обработка диалогового окна.
# import QHBoxLayout - создаётся виджет горизонтального линейного макета.
# import QFrame - является базовым классом виджетов, которые могут иметь фрейм (структуру чего-либо).
# import QTabWidget - предоставляет стек виджетов с вкладками.
# import QLabel - виджет обеспечивает отображение текста или изображения.
# import QPushButton - виджет предоставляет командную кнопку.
# import QLineEdit - виджет представляет собой однострочный текстовый редактор.
# import QFileDialog - предоставляет диалоговое окно, позволяющее выбирать файлы или каталоги.
# import QMainWindow - предоставляет главное окно приложения.
# import QMessageBox - класс, который задаёт пользователю вопрос и получает от него ответ.


"""Класс который вызывает Диалоговое окно ОБО МНЕ, там написаны мои действующие контакты
как со мной можно связаться и так же мой ГитХаб где будут выложены проекты."""


class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowIcon(QIcon(r"Files/icon.ico"))
        self.setFixedSize(300, 100)
        self.setWindowTitle("Обо мне")

        discription = QLabel(self)
        discription.setGeometry(75, 10, 150, 30)
        discription.setAlignment(Qt.AlignmentFlag.AlignCenter)
        discription.setText("$ H V E P S")

        horizontalLayoutWidget = QWidget(self)
        horizontalLayoutWidget.setGeometry(15, 50, 270, 40)
        horizontalLayout = QHBoxLayout(horizontalLayoutWidget)
        horizontalLayout.setContentsMargins(0, 0, 0, 0)
        horizontalLayout.setSpacing(12)

        btn_github = QPushButton(horizontalLayoutWidget)
        btn_github.setText("ГитХаб")
        btn_github.clicked.connect(lambda: webbrowser.open(
            'https://github.com/coder-medved'))

        btn_instagram = QPushButton(horizontalLayoutWidget)
        btn_instagram.setText("VK")
        btn_instagram.clicked.connect(lambda: webbrowser.open(
            'https://vk.com/shveps78'))

        btn_telegram = QPushButton(horizontalLayoutWidget)
        btn_telegram.setText("Telegram")
        btn_telegram.clicked.connect(
            lambda: webbrowser.open('https://t.me/ShVePs86'))

        horizontalLayout.addWidget(btn_github)
        horizontalLayout.addWidget(btn_instagram)
        horizontalLayout.addWidget(btn_telegram)


"""Класс Cryptographer именно так написаны действия Генерации ключа, Загруженность Ключа, 
Зашифровки и Расшифровки файла"""


class Cryptographer:
    # Функция cryptography принимает fileName (Файл который нужно обработать, newName (Файл который будет обработан)
    # и ключ, который будет символы кодировать в байты например \xb9\xd1\x82\
    def cryptography(self, fileName, newName, key: bytes):
        # Открываем файл и читаем его, сохраняя прочитанное в переменную data
        with open(fileName, 'rb') as file:
            data = file.read()

        # Переменная cryptographed содержит алгоритм зашифровки полученного с файла, который состоит из файла и ключа
        cryptographed = self.xor(data, key)

        # Открываем файл, где зашифровка и меняем файл по алгоритму переменной cryptographed
        with open(newName, 'wb') as file:
            file.write(cryptographed)

    # Используется для создания метода, который ничего не знает о классе или экземпляре, через который он был вызван.
    @staticmethod
    def generate_key(key_name):  # Происходит момент генерации ключа по заданным функциям библиотеки string
        strings = string.ascii_letters + string.digits + \
                  string.hexdigits + string.ascii_uppercase + string.punctuation
        key = ''.join(random.sample(strings, 50)).encode()

        # Открывается файл с ключом и туда идёт запись ключа
        with open(key_name, 'wb') as keyFile:
            keyFile.write(key)

    @staticmethod
    def load_key(key_name):  # Идёт загрузка существующего ключа
        with open(key_name, 'rb') as keyFile:
            key = keyFile.read()
        return key

    @staticmethod
    def xor(data, key):  # Алгоритм закодированния файла (по принципу известного хакера (Рафаэля Херцога)
        return bytes(a ^ b for a, b in zip(data, cycle(key)))


# Класс призыва главного окна
class Widget(QMainWindow):
    def __init__(self):
        super(Widget, self).__init__()
        self.cryptographer = Cryptographer()
        self.aboutDialog = AboutDialog()
        self.key = None
        self.setupUi()

    def setupUi(self):  # Идёт запуск дизайна и присваивание кнопок
        window_icon = QIcon(QPixmap(r"Files\icon.ico"))

        self.setGeometry(430, 270, 580, 190)
        self.setFixedSize(580, 190)
        self.setWindowIcon(window_icon)
        self.setWindowTitle("Файл Криптографии")

        key_frame = QFrame(self)
        key_frame.setGeometry(440, 41, 121, 120)

        load_key_btn_key_frame = QPushButton(key_frame)
        load_key_btn_key_frame.setGeometry(25, 40, 80, 30)
        load_key_btn_key_frame.setText("Load КЛЮЧ")
        load_key_btn_key_frame.clicked.connect(self.load_key)

        generate_key_btn_key_frame = QPushButton(key_frame)
        generate_key_btn_key_frame.setGeometry(25, 80, 95, 30)
        generate_key_btn_key_frame.setText("Generate КЛЮЧ")
        generate_key_btn_key_frame.clicked.connect(self.generate_key)

        self.selected_key_lbl_key_frame = QLabel(key_frame)
        self.selected_key_lbl_key_frame.setGeometry(25, 10, 100, 20)
        self.selected_key_lbl_key_frame.setText("КЛЮЧ: ")

        lineEdit_font = QFont()
        lineEdit_font.setPointSize(10)
        lineEdit_font.setWeight(50)
        lineEdit_font.setKerning(True)

        tabWidget = QTabWidget(self)
        tabWidget.setGeometry(20, 35, 400, 130)
        tabWidget.setMovable(True)

        encoderTab_icon = QIcon(QPixmap(r"Files\encrypt.ico"))
        encoderTab = QWidget()

        open_file_btn_encoderTab = QPushButton(encoderTab)
        open_file_btn_encoderTab.setGeometry(290, 20, 90, 31)
        open_file_btn_encoderTab.setText("Открыть файл")
        open_file_btn_encoderTab.clicked.connect(self.open_encode_file)

        encode_btn_encoderTab = QPushButton(encoderTab)
        encode_btn_encoderTab.setGeometry(290, 60, 90, 31)
        encode_btn_encoderTab.setText("Зашифровать")
        encode_btn_encoderTab.clicked.connect(self.encrypt)

        self.file_path_line_encoder_tab = QLineEdit(encoderTab)
        self.file_path_line_encoder_tab.setGeometry(10, 20, 261, 31)
        self.file_path_line_encoder_tab.setFont(lineEdit_font)
        self.file_path_line_encoder_tab.setFocusPolicy(
            Qt.FocusPolicy.ClickFocus)
        self.file_path_line_encoder_tab.setReadOnly(True)
        self.file_path_line_encoder_tab.setPlaceholderText("Путь к файлу")

        decoderTab_icon = QIcon(QPixmap(r"Files\decrypt.ico"))
        decoderTab = QWidget()

        open_file_btn_decoderTab = QPushButton(decoderTab)
        open_file_btn_decoderTab.setGeometry(290, 20, 90, 31)
        open_file_btn_decoderTab.setText("Открыть файл")
        open_file_btn_decoderTab.clicked.connect(self.open_decode_file)

        decode_btn_decoderTab = QPushButton(decoderTab)
        decode_btn_decoderTab.setGeometry(290, 60, 90, 31)
        decode_btn_decoderTab.setText("Расшифровать")
        decode_btn_decoderTab.clicked.connect(self.decrypt)

        self.file_path_line_decoder_tab = QLineEdit(decoderTab)
        self.file_path_line_decoder_tab.setGeometry(10, 20, 261, 31)
        self.file_path_line_decoder_tab.setFont(lineEdit_font)
        self.file_path_line_decoder_tab.setFocusPolicy(
            Qt.FocusPolicy.ClickFocus)
        self.file_path_line_decoder_tab.setReadOnly(True)
        self.file_path_line_decoder_tab.setPlaceholderText("Путь к файлу")

        tabWidget.addTab(encoderTab, encoderTab_icon, '')
        tabWidget.setTabText(tabWidget.indexOf(encoderTab), "Зашифровать  ")
        tabWidget.setTabToolTip(tabWidget.indexOf(
            encoderTab), "Вы можете зашифровать\nваши файлы здесь")

        tabWidget.addTab(decoderTab, decoderTab_icon, '')
        tabWidget.setTabText(tabWidget.indexOf(decoderTab), "Расшифровать   ")
        tabWidget.setTabToolTip(tabWidget.indexOf(
            decoderTab), "Вы можете расшифровать\nваши файлы здесь")

        self.init_menu()

    def encrypt(self):  # Кнопка зашифровки файла
        if self.key:
            file_path = self.file_path_line_encoder_tab.text()

            if file_path:
                save_path, _ = QFileDialog.getSaveFileName(
                    self, 'Сохранить зашифрованный файл', '', "Шифрование файлов (*.encrypt)")

                if save_path:
                    self.cryptographer.cryptography(
                        file_path, save_path, self.key)

            else:
                QMessageBox.critical(
                    self, 'ОШИБКА', '\nПожалуйста, откройте файл для шифрования!\t\n')

        else:
            QMessageBox.critical(
                self, 'ОШИБКА', '\nПожалуйста, сначала загрузите КЛЮЧ!\t\n')

    def decrypt(self):  # Кнопка расшифровки файла
        if self.key:
            file_path = self.file_path_line_decoder_tab.text()

            if file_path:
                save_path, _ = QFileDialog.getSaveFileName()

                if save_path:
                    self.cryptographer.cryptography(
                        file_path, save_path, self.key)

            else:
                QMessageBox.critical(
                    self, 'ОШИБКА', '\nПожалуйста, откройте файл для расшифровки!\t\n')

        else:
            QMessageBox.critical(
                self, 'ОШИБКА', '\nПожалуйста, сначала загрузите КЛЮЧ!\t\n')

    def load_key(self):  # Кнопка загрузка ключа по которому будет происходит зашифрование | расшифрование
        key_path, _ = QFileDialog.getOpenFileName(
            self, 'Открыть ключ файл', '', "Ключ файлы (*.key)")

        if key_path:
            key_name = os.path.basename(key_path)
            self.selected_key_lbl_key_frame.setText(f'КЛЮЧ:  {key_name}')
            self.key = self.cryptographer.load_key(key_path)

    def generate_key(self):  # Кнопка генерации особого ключа по которому будет происходит  зашифрование | расшифрование
        key_path, _ = QFileDialog.getSaveFileName(
            self, 'Сохранить ключ файл', '', "Ключ файлы (*.key)")

        if key_path:
            self.cryptographer.generate_key(key_path)

    def open_encode_file(self):  # Открытие файла для расшифровки
        file_path, _ = QFileDialog.getOpenFileName(self, 'Открыть файл')
        if file_path:
            self.file_path_line_encoder_tab.setText(file_path)

    def open_decode_file(self):  # Открытие файла для зашифровки
        file_path, _ = QFileDialog.getOpenFileName(
            self, 'Открыть файл', '', "Шифрование файлов (*.encrypt)")
        if file_path:
            self.file_path_line_decoder_tab.setText(file_path)

    def init_menu(self):  # Дополнительные кнопки о ПОМОЩИ и ОБО МНЕ
        helpAction = QAction("Помощь", self)
        helpAction.triggered.connect(
            lambda: QMessageBox.information(self, 'Помощь', HELP_MESSAGE))

        aboutAction = QAction("Обо мне", self)
        aboutAction.triggered.connect(lambda: self.aboutDialog.exec())

        menu = self.menuBar()
        menu.addAction(helpAction)
        menu.addAction(aboutAction)


HELP_MESSAGE = '''
1) Загрузите ключ (если у вас нет никакого ключа, сгенерируйте ключ, а затем загрузите его).
2) Откройте файл для шифрования или дешифрования.
3) Нажмите кнопку зашифровать/расшифровать и выберите путь сохранения.
4) Теперь ваш файл готов!


(Алгоритм был придуман Рафаэлем Херцогом - известным от ныне хакера который смог взломать базу данных крупного банка с помощью лазейки Брауманга по API запросу с помощью мощного ядра С++. )
'''

if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
