#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A password creator inspired by the ctSESAM project.

Version: 1.1
Python 3.6
Date created: 29/03/2018
"""

from hashlib import pbkdf2_hmac

lower_case_letters = list('abcdefghijklmnopqrstuvwxyz')
upper_case_letters = list('ABCDEFGHJKLMNPQRSTUVWXYZ')
numbers = list('0123456789')
special_characters = list('#!"§$%&/()[]{}=-_+*<;:.')
password_characters = lower_case_letters + upper_case_letters \
    + numbers + special_characters
salt = 'pepper'


class Password:
    def __init__(self, master_password, domain):
        self.master_password = master_password
        self.domain = domain

    @property
    def master_password(self):
        return self.__master_password

    @master_password.setter
    def master_password(self, master_password):
        self.__master_password = master_password

    @property
    def domain(self):
        return self.__domain

    @domain.setter
    def domain(self, domain):
        self.__domain = domain

    def convert_bytes_to_password(self, hb, length):
        password = ''
        number = int.from_bytes(hb, byteorder='big')
        while number > 0 and len(password) < length:
            password = password + password_characters[number % len(password_characters)]
            number = number // len(password_characters)
        return password

    def create_hash(self):

        hash_string = self.domain + self.master_password
        hashed_bytes = pbkdf2_hmac('sha512', hash_string.encode('utf-8'), salt.encode('utf-8'), 4096)
        return self.convert_bytes_to_password(hashed_bytes, 12)
        # print('Passwort: ' + self.convert_bytes_to_password(hashed_bytes, 10))
