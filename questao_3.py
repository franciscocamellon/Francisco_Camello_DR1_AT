# -*- coding: utf-8 -*-
"""
/***************************************************************************
*    Questao 01                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : TP 03 - Lógica, Computação e Algoritmos         *
*        Professor       : Carlos Pivotto                                  *
*        Nome do arquivo : questao_01.py                                   *
***************************************************************************/
"""

import time


class Zero_Error(Exception):

    def __init__(self):
        super().__init__()


class Financial_Health():

    """
    """

    def __init__(self):
        """
        Constructor
        """
        self.wage = float
        self.housing = float
        self.education = float
        self.trasnport = float
        self.data = {}
        self.report = ''

    def init_class(self):
        """
        This function receives and orders the input data from users.
        """
        self.validate_values(
            self.wage, 'wage', 'Digite sua renda total mensal: ')
        self.validate_values(self.housing, 'housing',
                             'Digite seus gastos totais com moradia: ')
        self.validate_values(self.education, 'education',
                             'Digite seus gastos totais com educação: ')
        self.validate_values(self.trasnport, 'trasnport',
                             'Digite seus gastos totais com transporte: ')
        return print(self.data)

    def error(self, value):
        """
        Raises a customized exception.
        """
        if value <= 0:
            raise Zero_Error()
        else:
            return value

    def validate_values(self, value, expenditure, title):
        """
        Validates the input value from wage given by the user.
        """
        while True:
            try:
                value = float(input(title))
                self.error(value)
                self.data[expenditure] = [value]
                break
            except ValueError:
                print('Digite um número!')
            except Zero_Error:
                print('Digite um número maior que zero!')

        return self.data

    def process_data(self, data):
        """
        This function receives and process the input data from users.
        """
        for k, v in self.data.items():
            if k == 'wage':
                self.data[k] = [v, 100]
            else:
                percentage = (v / self.data[0][0]) * 100
                print(percentage)
                self.data[k] = [v, percentage]

        return print(self.data)

    def print_result(self):
        """
        """
        print('===' * 21)
        print('{:^63}'.format('Questão 01'))
        print('===' * 21)


Financial_Health().process_data(Financial_Health().init_class())
