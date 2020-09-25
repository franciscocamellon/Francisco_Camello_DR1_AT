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
import matplotlib.pyplot as plotter


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
        self.eixoXAno = []
        self.eixoYPib = []
        self.input = {'country': ['  Informe um país:  ', ''],
                     'year': ['  Informe um ano entre 2013 e 2020: ', '']}
        self.file = []
        self.file_reader = {}
        

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

    def init_class(self):

        with open('Assessment_PIBs.csv', newline="", encoding="utf-8") as csvfile:
            self.file = csv.DictReader(csvfile)

            for k, v in self.input.items():
                self.validate_values(v[1], k, v[0])
            
            for coluna in self.file_reader:
                if coluna.get("País").lower() == self.input.get('country')[1].lower():
                    paisSelecionado = coluna.get("País")
                    ano = self.input.get('year')[1]
                    pibPais = coluna.get(ano)
                    print("\n  PIB {} em {}: US${} trilhões.".format(
                        paisSelecionado, ano, pibPais))
                    break

    

    def process_data(self):
        with open('Assessment_PIBs.csv', newline="", encoding="utf-8") as csvfile:
            self.file_reader = csv.DictReader(csvfile)

            for coluna in self.file_reader:
                primeiroAno = float(coluna.get("2013").replace(",", "."))
                ultimoAno = float(coluna.get("2020").replace(",", "."))
                variacao = (ultimoAno * 100 / primeiroAno) - 100
                paisAtual = coluna.get("País")
                print("  {}: Variação de {:.2f}% entre 2013 e 2020.".format(paisAtual, variacao))

    def plot_data(self):
        eixoXAno, eixoYPib = [], []
        with open('Assessment_PIBs.csv', newline="", encoding="utf-8") as csvfile:
            self.file_reader = csv.DictReader(csvfile)

            for coluna in self.file_reader:
                if coluna.get("País").lower() == self.input.get('country')[1].lower():
                    print(coluna)

                    for index in range(1, len(coluna.values())): # percorrendo a lista gerada por cada coluna a partir dos anos
                        valorAtualPib = list(coluna.values())
                        dataAtual = list(coluna.keys())
                        eixoYPib.append(float(valorAtualPib[index]))
                        eixoXAno.append(int(dataAtual[index]))
                    break
        
        plotter.plot(eixoXAno, eixoYPib)
        plotter.show()

    def print_result(self):
        """
        """
        print('===' * 25, '{:^63}'.format('Questão 04'), '===' * 25, sep='\n')
        
        self.init_class()
        print('---' * 25, ' Estimativa de variação do PIB, entre 2013 e 2020', sep='\n')
        self.process_data()
        print('---' * 25,
              '{:>63}'.format('Aluno: Francisco Camello'), sep="\n")
        self.plot_data()


World_PIB_Projection().print_result()
