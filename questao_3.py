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


class Zero_Error(Exception):
    """
    Handle exceptions.
    """

    def __init__(self):
        super().__init__()


class Financial_Health():
    """
    This program takes an exam about your financial health.
    """

    def __init__(self):
        """
        Constructor
        """
        self.wage = float
        self.base_wage = self.wage
        self.housing = float
        self.education = float
        self.transportation = float
        self.data = {}
        self.report = ''
        self.expenditure = {self.wage: {self.housing: [0.3, 0, 0], self.education: [
            0.2, 0, 0], self.transportation: [0.15, 0, 0], }}

    def init_class(self):
        """
        This function receives and orders the input data from users.
        """
        self.validate_values(
            self.wage, 'wage', '  Digite sua renda total mensal: R$ ')
        self.validate_values(self.housing, 'housing',
                             '  Digite seus gastos totais com moradia: R$ ')
        self.validate_values(self.education, 'education',
                             '  Digite seus gastos totais com educação: R$ ')
        self.validate_values(self.transportation, 'transportation',
                             '  Digite seus gastos totais com transporte: R$ ')
        return self.data

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
                if expenditure == 'wage':
                    value = float(input(title))
                    self.error(value)
                    self.data[expenditure] = [value, 100, 'total', 'base']
                else:
                    value = float(input(title))
                    self.error(value)
                    self.data[expenditure] = [value, 0, 0, 'undefined']
                break
            except ValueError:
                print('Digite um número!')
            except Zero_Error:
                print('Digite um número maior que zero!')

    def process_data(self):
        """
        This function receives and process the input data from users.
        """
        processed_data = self.init_class()
        self.base_wage = processed_data.get('wage')[0]

        for k, v in processed_data.items():
            percentage = (v[0] / self.base_wage)

            if k == 'housing' and percentage <= 0.3:
                processed_data[k][1:4] = [percentage,
                                          self.base_wage * 0.3, 'healthy']
            elif k == 'housing' and percentage >= 0.3:
                processed_data[k][1:4] = [percentage,
                                          self.base_wage * 0.3, 'not healthy']

            if k == 'education' and percentage <= 0.2:
                processed_data[k][1:4] = [percentage,
                                          self.base_wage * 0.2, 'healthy']
            elif k == 'education' and percentage >= 0.2:
                processed_data[k][1:4] = [percentage,
                                          self.base_wage * 0.2, 'not healthy']

            if k == 'transportation' and percentage <= 0.15:
                processed_data[k][1:4] = [percentage,
                                          self.base_wage * 0.15, 'healthy']
            elif k == 'transportation' and percentage >= 0.15:
                processed_data[k][1:4] = [percentage,
                                          self.base_wage * 0.15, 'not healthy']

        return processed_data

    def print_result(self):
        """
        This is a printer! This prints.
        """
        not_healthy = []
        repo = []
        print('===' * 25, '{:^63}'.format('Questão 03'), '===' * 25, sep='\n')
        report = self.process_data()
        print('---' * 25)
        for k, v in report.items():
            if v[3] == 'not healthy' and k != 'wage':
                not_healthy.append(k)
                repo.append(
                    '   Seus gastos totais com {} comprometem {:.2%} de sua renda total. \nO máximo recomendado é de {:.2f}. Portanto, idealmente, o máximo de sua renda \ncomprometida com moradia deveria ser de R$ {}.'.format(k, v[1], v[0], v[2]))
            elif k == 'wage':
                pass
        print('  Diagnóstico:')
        if len(repo) == 0:
            print(
                '   Parabéns', '   Seus gastos estão dentro da margem recomendada.', sep='\n')
        else:
            for i in range(len(repo)):
                print(repo[i])

        print('---' * 25,
              '{:>63}'.format('Aluno: Francisco Camello'), sep="\n")


Financial_Health().print_result()
