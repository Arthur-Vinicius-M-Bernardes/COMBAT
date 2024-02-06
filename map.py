import random
import tank


class Map:

    def __init__(self, size=15):
        self.size = size
        self.matriz = [[0] * size for _ in range(size)]

    def gerar_tanks(self):

        self.tank1.posicionar((random.randint(0, self.size - 1), random.randint(0, self.size - 1)))
        self.tank2.posicionar((random.randint(0, self.size - 1), random.randint(0, self.size - 1)))

        while self.tank2.posicao == self.tank1.posicao:
            self.tank2.posicionar((random.randint(0, self.size - 1), random.randint(0, self.size - 1)))

    def paredes(self, pos1, pos2):
        for i in range(self.size):
            if i != pos1[0] and i != pos2[0]:
                self.matriz[i][random.randint(0, self.size - 1)] = 3

        for j in range(self.size):
            if j != pos1[1] and j != pos2[1]:
                linha = random.randint(0, self.size - 1)
                while self.matriz[linha][j] == 3:
                    linha = random.randint(0, self.size - 1)
                self.matriz[linha][j] = 3




