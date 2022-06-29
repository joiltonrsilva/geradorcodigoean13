__author__="Joilton Ribeiro da Silva"
#Criando a Classe GeradorCodBarras:
class GeradorCodBarras():
    # Definimos o Construtor da Classe:
    def __init__(self):
        self._entry_cod = '0'

    # Aplicando decorator property para determinar o método entry_codproduto como getter:
    @property
    def entry_codproduto(self):
        return self._entry_cod

    # Definindo o método entry_codproduto como setter usando decorator property:
    @entry_codproduto.setter
    def entry_codproduto(self, cod):
        self._entry_cod = cod
        self._cod_init_var = '200'
        # contador de caracteres p/ determinar a quantidade de 0 a serem inseridos no código de barras:
        self._x = 9 - len(self._entry_cod)
        self._vet_0 = []
        self._i = 0
        while self._i < self._x:
            self._vet_0.append(0)
            self._i = self._i + 1

        # conversor de vetor p/ string + eliminação de espaços:
        self._vet_0 = ''.join(map(str, self._vet_0))

        # concatenação de valores:
        self._codigo_inicial = self._cod_init_var + self._vet_0 + self.entry_codproduto

        # deteminação de laço com objetivo de realizar a multiplicação de valores impares no vetor:
        self._multip_vetor = []
        self._i = 0
        while (self._i < 12):
            if (self._i % 2 == 0):
                self._multip_vetor.append(int(self._codigo_inicial[self._i]))
            else:
                self._multip_vetor.append(int(self._codigo_inicial[self._i]) * 3)
            self._i = self._i + 1

        # soma dos valores p/ determinar o digito verificador:
        self._soma = sum(self._multip_vetor)
        self._d_verificador = (((self._soma // 10 ) + 1) * 10) - self._soma

        # concatenação de valores com os valores inciais + digito verificador:
        self._res_valid = int(self._codigo_inicial + str(self._d_verificador))
        
        # saída dos valores finais:
        self._entry_cod = self._res_valid
        
