import bullet


class Tank:

    def __init__(self):
        self.posicao = None
        self.ultimo_mov = None

    def posicionar(self, pos):
        self.posicao = pos

    def acoes(self, mov):
        if mov.upper != 'F':
            self.ultimo_mov = mov
            print("AAAAAAAAAAAA")

        if mov.upper == "W":
            self.posicao[1] += 1
            print("sdasda")
        elif mov.upper == "S":
            self.posicao[1] = 50
        elif mov.upper == "D":
            self.posicao[0] += 1
        elif mov.upper == "A":
            self.posicao[0] -= 1
        elif mov.upper == "F":
            bala = bullet.Bullet()
            bala.inicio(self.posicao)
            return bala



    def voltar_pos(self):
        match self.ultimo_mov.upper:
            case 'W':
                self.posicao[1] -= 1
            case 'S':
                self.posicao[1] += 1
            case 'D':
                self.posicao[0] -= 1
            case 'A':
                self.posicao[0] += 1
