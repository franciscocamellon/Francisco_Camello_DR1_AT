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
    """
    Handle exceptions.
    """

    def __init__(self):
        super().__init__()


class World_PIB_Projection():
    """
    This program handles with information from a .csv file.
    """

    def __init__(self):
        """
        Constructor
        """
        self.report = []
        self.countries = []
        self.x_axis = []
        self.y_axis = []
        self.input = {'country': ['  Informe um país: ', ''],
                      'year': ['  Informe um ano entre 2013 e 2020: ', '']}
        self.data = {'País': [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]}

    def open_file(self):
        """
        This function reads the CSV file and fills the self.data
        variable with its contents.
        """

        with open('Assessment_PIBs.csv', newline='', encoding='utf-8') as csvfile:
            file_reader = csv.DictReader(csvfile)

            for column in file_reader:
                self.countries.append(column.get('País'))
                self.data[column.get('País')] = [
                    float(column.get('2013')), float(column.get('2014')),
                    float(column.get('2015')), float(column.get('2016')),
                    float(column.get('2017')), float(column.get('2018')),
                    float(column.get('2019')), float(column.get('2020')),
                ]
        return self.data

    def error(self, value):
        """
        Raises a customized exception.
        """
        if isinstance(value, str) and value in self.countries:
            return value
        elif isinstance(value, str) and int(value) in self.data.get('País')[:]:
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
            except ValueError:
                print('  Digite uma string!')
            except Zero_Error:
                if int(value) not in [2013, 2020]:
                    print('  Ano não encontrado, digite novamente!')
                else:
                    print('  País não encontrado, digite novamente!')

    def init_class(self):
        """
        This function receives the iputs from users and links other methods
        from this class.
        """

        self.open_file()

        for k, v in self.input.items():
            self.validate_values(v[1], k, v[0])

        for k, v in self.data.items():
            year = int(self.input.get('year')[1])
            country = self.input.get('country')[1].lower()
            if k == 'País' and year in v:
                idx = v.index(year)
                self.report.insert(1, year)
            elif k.lower() == country:
                self.report.insert(0, k)
                self.report.insert(2, v[idx])
            else:
                break
        print(
            '\n  O PIB do(a) {} em {}: US$ {} trilhões.'.format(
                self.report[0], self.report[1], self.report[2]))

        return self.report

    def growth_data(self):
        """
        This function process the data concerning with users input.
        """

        for k, v in self.data.items():
            if k != 'País':
                growth = (v[7]*100 / v[0])-100
                print(
                    '  {}: obteve variação de {:.2f}% no PIB entre 2013 e 2020.'
                    .format(k, growth))

        self.y_axis = (self.data.get(self.report[0])[0:])
        self.x_axis = (self.data.get('País')[0:])
        plotter.plot(self.x_axis, self.y_axis)
        plotter.show()

    def print_result(self):
        """
        This is a printer! This prints.
        """
        print('===' * 25, '{:^63}'.format('Questão 04'), '===' * 25, sep='\n')
        self.init_class()
        print('---' * 25, ' Estimativa de variação do PIB, entre 2013 e 2020\n', sep='\n')
        self.growth_data()
        print('---' * 25,
              '{:>63}'.format('Aluno: Francisco Camello'), sep='\n')


World_PIB_Projection().print_result()
