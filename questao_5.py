# -*- coding: utf-8 -*-
"""
/***************************************************************************
*    Questao 05                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : AT - Lógica, Computação e Algoritmos            *
*        Professor       : Carlos Pivotto                                  *
*        Nome do arquivo : questao_05.py                                   *
***************************************************************************/
"""
import csv
import matplotlib.pyplot as plot

class Zero_Error(Exception):

    def __init__(self):
        super().__init__()

class World_PIB_Projection():
    """
    """
    def __init__(self):
        """
        Constructor
        """
        self.label = []
        self.input = {'country': ['  Informe um país:  ', ''],
                     'year': ['  Informe um ano entre 2013 e 2020: ', '']}
        self.data = {}

    def open_file(self):
        """
        """
        _file = open('Assessment_PIBs.csv', newline='', encoding='utf8')
        data = _file.read()
        self.label = data.splitlines()[0].split(',')
        self.data[self.label[0]] = self.label[1:]

        for line in data.splitlines()[1:]:
            country = line.split(',')
            self.data[country[0]] = country[1:]
        for k in self.data.keys():
            countries = []
            countries.append(k)
       
        _file.close()
        return self.data, countries

    def error(self, value):
        """
        Raises a customized exception.
        """
        if isinstance(value, str):
            return value
        else:
            raise Zero_Error()
            

    def validate_values(self, value, string, title):
        """
        Validates the input value from wage given by the user.
        """
        while True:
            try:
                value = str(input(title))
                self.error(value)
                self.input[string][1] = value
                break
            except TypeError:
                print('Digite um número!')
            except Zero_Error:
                print('Digite o nome de um país!')


    def init_class(self ):
        """
        This function receives and orders the input data from users.
        PIB Brasil em 2020: US$2.35 trilhões.
        OrderedDict([('País', 'EUA'), ('2013', '16.76'), ('2014', '17.41'), ('2015', '18.12'), ('2016', '18.95'), ('2017', '19.86'), ('2018', '20.76'), ('2019', '21.61'), ('2020', '22.48')])
        {
            'EUA': ['16.76', '17.41', '18.12', '18.95', '19.86', '20.76', '21.61', '22.48']
        }
        {
            'country': ['  Informe um país:  ', ''],
            'year': ['  Informe um ano entre 2013 e 2020: ', '']
        }
        """
        a = self.open_file()[0]
        for k, v in self.input.items():
            self.validate_values(v[1], k, v[0])
            ano = self.input.get('year')[1]
            country = self.input.get('country')[1]
            if ano in self.label:
                index = self.label.index(ano)
                pib = self.data.get(country)[index - 1]
                print('O PIB do {} em {} é de: US$ {} trilhões.'.format(country, self.label[index], pib ))


    def process_data(self):
             # print(country)
            # print(len(country_data)-1)
            for data in country:
                for i in range(len(country)-1):

                country_pib.append(float(country[i+1]))

        self.data[country[0]] = country_pib



World_PIB_Projection().init_class()