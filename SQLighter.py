# -*- coding: utf-8 -*-
import sqlite3


class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def select_all(self):
        """ Получаем все строки """
        with self.connection:
            print('select_all Получаем все строки')
            print(self.cursor.execute('SELECT * FROM music').fetchall())

            return self.cursor.execute('SELECT * FROM music').fetchall()

    def select_single(self, rownum):
        """ Получаем одну строку с номером rownum """
        with self.connection:
            select_single = self.cursor.execute('SELECT * FROM music WHERE id = ?', (rownum,)).fetchall()[0]
            print('select_single Получаем одну строку с номером rownum')
            print(select_single)
            return select_single

    def count_rows(self):
        """ Считаем количество строк """
        with self.connection:
            result = self.cursor.execute('SELECT * FROM music').fetchall()
            print('count_rows Считаем количество строк')
            print(result)
            print(len(result))
            return len(result)

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()
