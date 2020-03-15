#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Main file of this project.
Version: 1.1.0
Python 3.7
Date created: 08.08.2019
"""

import sys
import pyperclip
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QMainWindow, QWidget, QAction, QApplication,
        QMessageBox, QLabel, QLineEdit, QGridLayout, QPushButton, qApp)
# import create_password
from src import create_password


def show_about_dialog():
    text = "<center>" \
           "<h1>Password Creator</h1>" \
           "&#8291;" \
           "<img src=img/icon.svg>" \
           "</center>" \
           "<p>Version 1.1.0<br/>" \
           "Created by niftycode<br/>" \
           "MIT License</p>"
    QMessageBox.about(window, "About Password Creator", text)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        # Add grid layout
        master_password_label = QLabel('Enter your masterpassword:')
        self.master_password_input = QLineEdit()

        domain_label = QLabel('Enter the URL:')
        self.domain_input = QLineEdit()

        button = QPushButton('Show Password', self)
        button.clicked.connect(self.button_clicked)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(master_password_label, 1, 0)
        grid.addWidget(self.master_password_input, 1, 1)

        grid.addWidget(domain_label, 2, 0)
        grid.addWidget(self.domain_input, 2, 1)

        grid.addWidget(button, 3, 0)

        widget.setLayout(grid)

        self.title = 'Password Creator'
        self.window_icon = 'img/pw_creator_icon.png'
        self.left = 300
        self.top = 300
        self.width = 500
        self.height = 200

        self.create_actions()
        self.init_ui()

    def button_clicked(self):

        password = self.master_password_input.text()
        domain = self.domain_input.text()

        if password == "" or domain == "":
            message = QMessageBox()
            message.setIcon(QMessageBox.Warning)
            message.setText('Missing values!')
            message.setInformativeText('You have to enter a master password and a domain.')
            message.exec_()
        else:
            password = create_password.Password(self.master_password_input.text(), self.domain_input.text())
            created_password = password.create_hash()
            pyperclip.copy(created_password)

            message = QMessageBox()
            message.setIcon(QMessageBox.Information)
            message.setText('Your password:')
            message.setInformativeText('{0}.'.format(created_password))
            message.exec_()

    def create_actions(self):
        # Add quit and about action
        self.quit_action = QAction('&Quit', self)
        self.about_action = QAction('&About', self)

        # Quit Action
        self.quit_action.setShortcut('Ctrl+Q')
        self.quit_action.setStatusTip('Exit this application.')
        self.quit_action.triggered.connect(qApp.quit)

        # About Action
        self.about_action.setShortcut('Ctrl+A')
        self.about_action.setStatusTip('About this application.')
        self.about_action.triggered.connect(show_about_dialog)

    def create_menubar(self):
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        self.help_menu.addAction(self.about_action)
        self.file_menu.addAction(self.quit_action)

    def init_ui(self):

        # Create menus
        self.file_menu = self.menuBar().addMenu("&File")
        self.help_menu = self.menuBar().addMenu("&Help")
        self.create_menubar()

        # Set basic window layout
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(self.window_icon))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyle('Windows')  # Fusion, Macintosh
    window = MainWindow()
    sys.exit(app.exec_())
