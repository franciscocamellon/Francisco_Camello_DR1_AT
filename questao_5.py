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
        _file = open('Assessment_PIBs.csv', 'r' , encoding='utf-8')
        # Lê todos os dados do arquivo
        country_pib=[]
        data = _file.read()
        x_label = data.splitlines()[0].split(",")
        self.data['x_label'] = x_label

        country_data = data.splitlines()[1:]

        for line in country_data:
            country = line.split(',')
            # print(country)
            # print(len(country_data)-1)
            for data in country:
            for i in range(len(country)-1):

                country_pib.append(float(country[i+1]))

        self.data[country[0]] = country_pib
        print(self.data)
        # x = self.data.get('EUA')[1:8]
        # y = self.data.get('x_label')[1:8]
        # print(x)
        # print(y)
        # plot.plot(x,y)
        # plot.show()
        # Com splitlines(), quebramos os dados crus do arquivo em linhas,
        # armazenando-os em uma lista
        # linhas = dados_crus.splitlines()
        # Separamos apenas a primeira linha dos dados,
        # que é a linha que contém os rótulos das colunas
        # dados_crus_rotulos = linhas[0]
        # E a quebramos em uma lista,
        # utilizando o ponto e vírgula como separador
        # lista_rotulos = dados_crus_rotulos.split(",")
        # Já os candidatos serão a fatia restante dos dados, da linha 1 em diante.
        # Para isso, podemos utilizar linhas[1:], que tomará a linha 1 em diante de linhas.
        # Primeiro, armazenaremos os dados crus dos candidatos,
        # onde cada candidato é uma string com todos os dados separados por ponto e vírgula:
        # dados_crus_candidatos = linhas[1:]


    # def init_class(self):
    #     """
    #     This function receives and orders the input data from users.
    #     """
    #     for k, v in self.data.items():
    #         self.validate_values(v[1], k, v[0])
    #     self.pv = self.data.get('present value')[1]
    #     self.i = self.data.get('interest')[1]
    #     self.pmt = self.data.get('periodic payment amount')[1]
    #     self.n = int(self.data.get('number of periods')[1])
    #     return self.data

    # def process_data(self):



World_PIB_Projection().open_file()