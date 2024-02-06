import tank
import map
import bullet
import random

# Creating objects
tank1 = tank.Tank()
tank2 = tank.Tank()
mapa = map.Map()

# Posicioning the walls and tanks
tank1.posicionar([random.randint(0, mapa.size - 1), random.randint(0, mapa.size - 1)])
tank2.posicionar([random.randint(0, mapa.size - 1), random.randint(0, mapa.size - 1)])
while tank2.posicao == tank1.posicao:
    tank2.posicionar((random.randint(0, mapa.size - 1), random.randint(0, mapa.size - 1)))
mapa.paredes(tank1.posicao, tank2.posicao)

run = True
while run:
    print("Comandos:")
    print("W - Cima")
    print("S - Baixo")
    print("D - Direita")
    print("A - Esquerda")
    print("F - Atirar")
    comando = input()
    bala = tank1.acoes(comando)
    if mapa.matriz[tank1.posicao[0]][tank1.posicao[1]] == 3:
        tank1.voltar_pos()
    while bala is not None:
        flag = bala.movimento(tank2.posicao)
        if mapa.matriz[bala.pos[0]][bala.pos[1]] == 3:
            bala = None
            print("Tiro acertou na parede")
        if flag:
            print("Tiro acertado")
            print(("Você ganhou"))
            run = False
            bala = None

    comandos = ["W", "S", "D", "A", "F"]
    bala = tank2.acoes(random.choice(comandos))

    if mapa.matriz[tank2.posicao[0]][tank1.posicao[1]] == 3:
        tank2.voltar_pos()
    while bala is not None:
        flag = bala.movimento(tank1.posicao)
        if mapa.matriz[bala.pos[0]][bala.pos[1]] == 3:
            bala = None
            print("Inimigo acertou na parede")
        if flag:
            print("Inimigo acertou você")
            print("Você perdeu")
            run = False
            bala = None
