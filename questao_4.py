# -*- coding: utf-8 -*-
"""
/***************************************************************************
*    Questao 04                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : AT - Lógica, Computação e Algoritmos            *
*        Professor       : Carlos Pivotto                                  *
*        Nome do arquivo : questao_04.py                                   *
***************************************************************************/
"""

import matplotlib.pyplot


class Zero_Error(Exception):

    def __init__(self):
        super().__init__()


class Yield():

    """
    """

    def __init__(self):
        """
        Constructor
        montante financeiro inicial, um percentual de rendimento por período, um valor de aporte para cada período e uma quantidade de períodos.

        Valor inicial: R$ 10000
        Rendimento por período (%): 0.54
        Aporte a cada período: R$ 1000
        Total de períodos: 120

        Após 1 períodos(s), o montante será de R$11054.00.
        Após 2 períodos(s), o montante será de R$12113.69.
        Após 3 períodos(s), o montante será de R$13179.11.
        Após 4 períodos(s), o montante será de R$14250.27.
        Após 5 períodos(s), o montante será de R$15327.22.
        (...)
        Após 115 períodos(s), o montante será de R$177406.76.
        Após 116 períodos(s), o montante será de R$179364.76.
        Após 117 períodos(s), o montante será de R$181333.33.
        Após 118 períodos(s), o montante será de R$183312.53.
        Após 119 períodos(s), o montante será de R$185302.42.
        Após 120 períodos(s), o montante será de R$187303.05.
        """
        self.pv = float
        self.i = float
        self.pmt = float
        self.n = int
        self.data = {'present value': ['  Valor inicial: R$ ', 0],
                     'interest': ['  Rendimento por período (%): ', 0],
                     'periodic payment amount': ['  Aporte a cada período: R$ ', 0],
                     'number of periods': ['  Total de períodos: ', 0]}

    def init_class(self):
        """
        This function receives and orders the input data from users.
        """
        for k, v in self.data.items():
            self.validate_values(v[1], k, v[0])
        self.pv = self.data.get('present value')[1]
        self.i = self.data.get('interest')[1]
        self.pmt = self.data.get('periodic payment amount')[1]
        self.n = int(self.data.get('number of periods')[1])
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
                value = float(input(title))
                self.error(value)
                self.data[expenditure][1] = value
                break
            except ValueError:
                print('Digite um número!')
            except Zero_Error:
                print('Digite um número maior que zero!')

    def process_data(self):
        """
        This function receives and process the input data from users.
        Como economista formado não posso deixar de citar que a fala de Einstein
        trata de juros compostos e o exercício pede que seja calculado juros
        simples.
        O código para calcular juros compostos seria:
            _yield = (self.pv * interest_factor**i+1) + self.pmt
        ao invés de:
            _yield = (self.pv * interest_factor) + self.pmt
        """
        _data = self.init_class()
        interest_factor = 1 + (self.i/100)
        processed_data = []
        for i in range(self.n):
            if i == 0:
                _yield = (self.pv * interest_factor) + self.pmt
                processed_data.append(_yield)
            else:
                _yield = (processed_data[i - 1] * interest_factor) + self.pmt
                processed_data.append(_yield)
        return processed_data

    def print_result(self):
        """
        """
        print('===' * 25, '{:^63}'.format('Questão 04'), '===' * 25, sep='\n')
        data = self.process_data()
        periods, values = [], []
        print('---' * 25)
        for period in range(len(data)):
            periods.append(period)
            values.append(data[period])
            print('  Após {} {}, o montante será de R$ {}.'.format(
                period + 1, 'períodos' if (period + 1) > 1 else 'período', str(round(data[period], 2)).replace('.',',')))

        print('---' * 25,
              '{:>63}'.format('Aluno: Francisco Camello'), sep="\n")

        matplotlib.pyplot.plot(periods, values)
        matplotlib.pyplot.show()


Yield().print_result()
