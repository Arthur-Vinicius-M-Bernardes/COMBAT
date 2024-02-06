class Bullet:

    def __init__(self):
        self.pos = None

    def inicio(self, pos):
        self.pos = pos

    def movimento(self, alvo):
        if self.pos[0] > alvo[0]:
            self.pos[0] -= 1
        elif self.pos[0] < alvo[0]:
            self.pos[0] += 1

        if self.pos[1] > alvo[1]:
            self.pos[1] -= 1
        elif self.pos[1] < alvo[1]:
            self.pos[1] += 1

        if self.pos == alvo:
            return True
