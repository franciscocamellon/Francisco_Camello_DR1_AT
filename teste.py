# -*- coding: utf-8 -*-

import csv
import matplotlib.pyplot as plt

def evolucaoPibGraph(pais):
    """
        Função que plota um gráfico, usando matplotlib, para mostrar a evolução do
        pib do país selecionado.
        http://www.funag.gov.br/ipri/images/analise-pesquisa/tabelas/top15pib.pdf
        do FMI. Solicita um arquivo .csv como parâmetro e o nome do país.
    """
    eixoXAno = []
    eixoYPib = []

    with open('Assessment_PIBs.csv', newline="", encoding="utf-8") as csvfile:
        arquivoPibs = csv.DictReader(csvfile)
        

        for coluna in arquivoPibs:
            print(coluna)
            if coluna.get("País").lower() == pais.lower():

                for index in range(1, len(coluna.values())): # percorrendo a lista gerada por cada coluna a partir dos anos
                    valorAtualPib = list(coluna.values())
                    dataAtual = list(coluna.keys())
                    eixoYPib.append(float(valorAtualPib[index]))
                    eixoXAno.append(int(dataAtual[index]))
                break

    plt.plot(eixoXAno, eixoYPib)
    plt.show()

evolucaoPibGraph('Indonésia')