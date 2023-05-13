"""Программа может зашифровать ваш файл по заданному или генерированному ключу
Так же программа может расшифровать ваш файл лишь по тому ключу, по которому она зашифрована.
Генерированный ключ к расшифровке файла не подлежит. Всю инструкцию о программе вы можете прочитать
нажав "ПОМОЩЬ", все мои основные контакты можете узнать нажав "Обо мне". Приятного пользования!"""

# import os - Библиотека предоставляет переносимый способ использования функций, зависящих от операционной системы.
# import webbrowser - Библиотека, которая делает запрос в браузер и даёт результат.
# import random - Библиотека, которая реализует генератор псевдослучайных чисел.
# import string - Библиотека, которая делает общие операции со строками.
# import sys - Библиотека, которая предоставляет доступ к некоторым переменным, используемым или поддерживаемым
# import sqlite3 - Библиотека присваевания БД
# from itertools import cycle - Модуль itertools стандартизирует основной набор быстрых эффективных инструментов. \
# Итератор cycle примером является данный способ cycle('ABCD') --> A B C D A B C D ...
# from PyQt6.QtCore import Qt - Библиотека для создания приложений с графическим интерфейсом с помощью инструментария Qt


import os
import webbrowser
import random
import string
import sqlite3
from itertools import cycle
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon, QPixmap, QFont
from PyQt6.QtWidgets import QHBoxLayout, QFrame, QTabWidget, QPushButton, QLineEdit, \
    QFileDialog, QMessageBox, QWidget
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QDialog
from PyQt6.QtWidgets import QLabel

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
        self.setWindowIcon(QIcon(r"DesignProgramm/icon.ico"))
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
    # Открывает файл, читает его, зашифровывает по ключу, сохраняет новым файлом.
    def cryptography(self, fileName, newName, key: bytes):
        with open(fileName, 'rb') as file:
            data = file.read()

        cryptographed = self.alghorythm(data, key)

        with open(newName, 'wb') as file:
            file.write(cryptographed)

    # Используется для создания метода, который ничего не знает о классе или экземпляре, через который он был вызван.
    @staticmethod
    # Функция по генерации ключа и добавление его в БД, добавление в txt и вывод в консоль
    def generate_key(key_name):
        strings = string.ascii_letters + string.digits + string.hexdigits + string.ascii_uppercase
        key = ''.join(random.sample(strings, 50)).encode()
        with open(key_name, 'wb') as keyFile:
            keyFile.write(key)
        with open('keysss.txt', 'a') as keyss:
            keyss.write(str(key) + '\n')
        con = sqlite3.connect('key.db')
        cur = con.cursor()
        reg = f'INSERT INTO keys (key) VALUES' \
              f'("{key}")'
        con.execute(reg).fetchall()
        cur.execute("SELECT * FROM keys")
        for row in cur.fetchall():
            print(row)
        con.commit()
        con.close()

    # Идёт загрузка существующего ключа
    @staticmethod
    def load_key(key_name):
        with open(key_name, 'rb') as keyFile:
            key = keyFile.read()
        return key

    # Алгоритм закодированния файла (по принципу известного хакера (Рафаэля Херцога)
    @staticmethod
    def alghorythm(data, key):
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
        window_icon = QIcon(QPixmap(r"DesignProgramm\icon.ico"))

        super(Widget, self).__init__()

        self.setGeometry(430, 270, 580, 190)
        self.setFixedSize(580, 190)
        self.setWindowIcon(window_icon)
        self.setWindowTitle("Файл Криптографии")

        key_frame = QFrame(self)
        key_frame.setGeometry(440, 41, 121, 120)

        load_key_btn_key_frame = QPushButton(key_frame)
        load_key_btn_key_frame.setGeometry(13, 30, 80, 40)
        load_key_btn_key_frame.setText("Загрузить\nключ")
        load_key_btn_key_frame.clicked.connect(self.load_key)

        generate_key_btn_key_frame = QPushButton(key_frame)
        generate_key_btn_key_frame.setGeometry(13, 75, 107, 42)
        generate_key_btn_key_frame.setText("Сгенерировать\nключ")
        generate_key_btn_key_frame.clicked.connect(self.generate_key)

        self.selected_key_lbl_key_frame = QLabel(key_frame)
        self.selected_key_lbl_key_frame.setGeometry(13, 0, 100, 20)
        self.selected_key_lbl_key_frame.setText("КЛЮЧ: ")

        lineEdit_font = QFont()
        lineEdit_font.setPointSize(10)
        lineEdit_font.setWeight(50)
        lineEdit_font.setKerning(True)

        tabWidget = QTabWidget(self)
        tabWidget.setGeometry(20, 35, 400, 130)
        tabWidget.setMovable(True)

        encoderTab_icon = QIcon(QPixmap(r"DesignProgramm\encrypt.ico"))
        encoderTab = QWidget()

        open_file_btn_encoderTab = QPushButton(encoderTab)
        open_file_btn_encoderTab.setGeometry(290, 20, 100, 31)
        open_file_btn_encoderTab.setText("Открыть файл")
        open_file_btn_encoderTab.clicked.connect(self.open_encode_file)

        encode_btn_encoderTab = QPushButton(encoderTab)
        encode_btn_encoderTab.setGeometry(290, 60, 100, 31)
        encode_btn_encoderTab.setText("Зашифровать")
        encode_btn_encoderTab.clicked.connect(self.encrypt)

        self.file_path_line_encoder_tab = QLineEdit(encoderTab)
        self.file_path_line_encoder_tab.setGeometry(10, 20, 261, 31)
        self.file_path_line_encoder_tab.setFont(lineEdit_font)
        self.file_path_line_encoder_tab.setFocusPolicy(
            Qt.FocusPolicy.ClickFocus)
        self.file_path_line_encoder_tab.setReadOnly(True)
        self.file_path_line_encoder_tab.setPlaceholderText("Путь к файлу")

        decoderTab_icon = QIcon(QPixmap(r"DesignProgramm\decrypt.ico"))
        decoderTab = QWidget()

        open_file_btn_decoderTab = QPushButton(decoderTab)
        open_file_btn_decoderTab.setGeometry(290, 20, 100, 31)
        open_file_btn_decoderTab.setText("Открыть файл")
        open_file_btn_decoderTab.clicked.connect(self.open_decode_file)

        decode_btn_decoderTab = QPushButton(decoderTab)
        decode_btn_decoderTab.setGeometry(290, 60, 100, 31)
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

    # Кнопка зашифровки файла
    def encrypt(self):
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

    # Кнопка расшифровки файла
    def decrypt(self):
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

    # Кнопка загрузка ключа по которому будет происходит зашифрование | расшифрование
    def load_key(self):
        key_path, _ = QFileDialog.getOpenFileName(
            self, 'Открыть ключ файл', '', "Ключ файлы (*.key)")

        if key_path:
            key_name = os.path.basename(key_path)
            self.selected_key_lbl_key_frame.setText(f'КЛЮЧ:  {key_name}')
            self.key = self.cryptographer.load_key(key_path)

    # Кнопка генерации особого ключа по которому будет происходит  зашифрование | расшифрование
    def generate_key(self):
        key_path, _ = QFileDialog.getSaveFileName(
            self, 'Сохранить ключ файл', '', "Ключ файлы (*.key)")

        if key_path:
            self.cryptographer.generate_key(key_path)

    # Открытие файла для расшифровки
    def open_encode_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Открыть файл')
        if file_path:
            self.file_path_line_encoder_tab.setText(file_path)

    # Открытие файла для зашифровки
    def open_decode_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, 'Открыть файл', '', "Шифрование файлов (*.encrypt)")
        if file_path:
            self.file_path_line_decoder_tab.setText(file_path)

    # Дополнительные кнопки о ПОМОЩИ и ОБО МНЕ
    def init_menu(self):
        helpAction = QAction("Помощь", self)
        helpAction.triggered.connect(
            lambda: QMessageBox.information(self, 'Помощь', HELP_MESSAGE))

        aboutAction = QAction("Обо мне", self)
        aboutAction.triggered.connect(lambda: self.aboutDialog.exec())

        menu = self.menuBar()
        menu.addAction(helpAction)
        menu.addAction(aboutAction)


# Текст, который выводится в диалоговом окне "Помощь"
HELP_MESSAGE = ''' 
1) Загрузите ключ. (Если у вас отсутствует ключ, пожалуйста, сгенерируйте его, а затем выполните его загрузку.)
2) Откройте файл для шифрования или дешифрования.
3) Нажмите кнопку зашифровать/расшифровать и выберите путь сохранения.
4) Теперь ваш файл готов!
5) Вы прекрасны!


(Алгоритм был придуман Рафаэлем Херцогом - известным хакером который смог взломать базу данных Интерпола с помощью лазейки Брауманга по API запросу и мощного ядра С++)
'''

if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
