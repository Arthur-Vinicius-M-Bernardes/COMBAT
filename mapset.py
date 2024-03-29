import random


class MapSet:
    def __init__(self):
        self.matrizes = {
            0: [[0, 0, 0, 0, 0, 3, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 3, 0, 0, 0, 0],
                [0, 0, 3, 0, 0, 0, 0, 3, 0, 0],
                [0, 0, 3, 0, 0, 0, 0, 3, 0, 0],
                [0, 0, 3, 0, 0, 0, 0, 3, 0, 0],
                [0, 0, 3, 0, 0, 0, 0, 3, 0, 0],
                [0, 0, 0, 0, 0, 3, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 3, 0, 0, 0, 0]],

            1: [[0, 3, 0, 0, 0, 0, 0, 0, 3, 0],
                [0, 3, 0, 0, 0, 3, 0, 0, 3, 0],
                [0, 0, 0, 0, 0, 3, 0, 0, 0, 0],
                [0, 0, 0, 0, 3, 3, 3, 0, 0, 0],
                [0, 0, 0, 0, 3, 3, 3, 0, 0, 0],
                [0, 0, 0, 0, 0, 3, 0, 0, 0, 0],
                [0, 3, 0, 0, 0, 3, 0, 0, 3, 0],
                [0, 3, 0, 0, 0, 0, 0, 0, 3, 0]],

            2: [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 3, 3, 0, 0, 0, 0, 3, 3, 0],
                [0, 3, 0, 0, 0, 0, 0, 0, 3, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 3, 3, 3, 3, 3, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 3, 0, 0, 0, 0, 0, 0, 3, 0],
                [0, 3, 3, 0, 0, 0, 0, 3, 3, 0]]
        }

    def switch_case(self, matriz_id):
        return self.matrizes.get(matriz_id, "Matriz não encontrada")

    def preencher_array(self):
        array = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                matriz_id = random.randint(0, 2)
                matriz = self.switch_case(matriz_id)
                array[i][j] = matriz[i][j]
        return array
