import random


class Map:
    def __init__(self, size=15):
        self.size = size
        self.matriz = [[0] * size for _ in range(size)]
        self.posicao_1 = None
        self.posicao_2 = None

    def posicoes_1_e_2(self):
        self.posicao_1 = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
        self.posicao_2 = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))

        while self.posicao_2 == self.posicao_1:
            self.posicao_2 = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))

        self.matriz[self.posicao_1[0]][self.posicao_1[1]] = 1
        self.matriz[self.posicao_2[0]][self.posicao_2[1]] = 2

    def Paredes(self):
        for i in range(self.size):
            if i != self.posicao_1[0] and i != self.posicao_2[0]:
                self.matriz[i][random.randint(0, self.size - 1)] = 3

        for j in range(self.size):
            if j != self.posicao_1[1] and j != self.posicao_2[1]:
                linha = random.randint(0, self.size - 1)
                while self.matriz[linha][j] == 3:
                    linha = random.randint(0, self.size - 1)
                self.matriz[linha][j] = 3

    def gerar_matriz(self):
        self.posicoes_1_e_2()
        self.Paredes()
        return self.matriz


# Exemplo de uso
gerador = Map()
matriz_gerada = gerador.gerar_matriz()

# Exibe a matriz gerada
for linha in matriz_gerada:
    print(linha)
