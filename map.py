import random
import tank


class Map:

    def __init__(self, size=15):
        self.size = size
        self.matriz = [[0] * size for _ in range(size)]
        self.tank1 = tank.Tank()
        self.tank2 = tank.Tank()

    def gerar_tanks(self):

        self.tank1.posicionar((random.randint(0, self.size - 1), random.randint(0, self.size - 1)))
        self.tank2.posicionar((random.randint(0, self.size - 1), random.randint(0, self.size - 1)))

        while self.tank2.posicao == self.tank1.posicao:
            self.tank2.posicionar((random.randint(0, self.size - 1), random.randint(0, self.size - 1)))

    def Paredes(self):
        for i in range(self.size):
            if i != self.tank1.posicao[0] and i != self.tank2.posicao[0]:
                self.matriz[i][random.randint(0, self.size - 1)] = 3

        for j in range(self.size):
            if j != self.tank1.posicao[1] and j != self.tank2.posicao[1]:
                linha = random.randint(0, self.size - 1)
                while self.matriz[linha][j] == 3:
                    linha = random.randint(0, self.size - 1)
                self.matriz[linha][j] = 3

    def gerar_matriz(self):
        self.gerar_tanks()
        self.Paredes()
        return self.matriz


# Exemplo de uso
gerador = Map()
matriz_gerada = gerador.gerar_matriz()

# Exibe a matriz gerada
for linha in matriz_gerada:
    print(linha)

run = True
while run:
    print("Comandos:")
    print("W - Cima")
    print("S - Baixo")
    print("D - Direita")
    print("A - Esquerda")
    print("F - Atirar")
    comando = input()
    bala = gerador.tank1.acoes(comando)
    if gerador.matriz[gerador.tank1.posicao[0]][gerador.tank1.posicao[1]] == 3:
        gerador.tank1.voltar_pos()
    while bala is not None:
        flag = bala.movimento(gerador.tank2.posicao)
        if gerador.matriz[bala.pos] == 3:
            bala = None
            print("Tiro acertou na parede")
        if flag:
            print("Tiro acertado")
            run = False

    comandos = ["W", "S", "D", "A", "F"]
    bala = gerador.tank2.acoes(random.choice(comandos))

    if gerador.matriz[gerador.tank2.posicao[0]][gerador.tank1.posicao[1]] == 3:
        gerador.tank2.voltar_pos()
    while bala is not None:
        flag = bala.movimento(gerador.tank1.posicao)
        if gerador.matriz[bala.pos] == 3:
            bala = None
            print("Tiro acertou na parede")
        if flag:
            print("Tiro acertado")
            run = False
