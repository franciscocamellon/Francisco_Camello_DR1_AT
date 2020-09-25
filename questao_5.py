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

class World_PIB_Projection():
    """
    """
    def __init__(self):
        """
        Constructor
        """
        self.data = {
            'x_label':[]

        }

    def open_file(self):
        """
        """




    def init_class(self ):
        """
        This function receives and orders the input data from users.
        PIB Brasil em 2020: US$2.35 trilhões.
        """
        # country = input('Informe um país: ')
        # year = int(input('Informe um ano entre 2013 e 2020: '))

        with open('Assessment_PIBs.csv', 'r', encoding='utf8') as csv_file:
            csv_reader = csv.DictReader(csv_file , delimiter=',')

            for rows in csv_reader:
                print(rows[ '2020'])
                # print('PIB {} em {}: US$  trilhões.'.format(rows[country], rows[year]))



    # def process_data(self):



World_PIB_Projection().init_class()