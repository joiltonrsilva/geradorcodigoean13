__author__ = "Joilton R. Silva"

from fncs.gerador import GeradorCodBarras

if __name__ == '__main__':
    print("---- PROGRAMA DE GERADOR DE CÓDIGO DE BARRAS EAN-13 P/ PRODUTOS PESO ----")
    obj = GeradorCodBarras()
    digit_value = input("DIGITE O CÓDIGO DO PRODUTO NO SISTEMA:")
    obj.entry_codproduto = digit_value
    print("O CÓDIGO DE BARRAS GERADO É:", obj.entry_codproduto)
