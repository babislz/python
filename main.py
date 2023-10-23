import random
import numpy as np

class Indiciduo:
    x: np.ndarray
    y: float 

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Populacao:
    p: np.array
    best: Indiciduo
    

    def __init__(self, func, dim, popsize, bounds = (0,1)):
        self.p = np.empty(popsize, dtype = Indiciduo)
        self.func = func

        for i in range(popsize):
            # x = (bounds[1] - bounds[0]) * (np.random.rand(dim) + bounds[0])
            x = np.random.rand(dim)
            self.p[i] = Indiciduo(x, func(x))
        
        self.best = self.p[0]
        self.best()

    def best(self):
        for i in range(self.popsize):
            self.p[i].y = self.func(self.p[i].x)
            if self.p[i].y < self.best.y:
                self.best = self.p[i]

def funcao(x1, x2, x3):
    return np.abs(x1 - 10) + np.abs(x2 - 20) + np.abs(x3 - 30)

tamanho = 10000

pop = Populacao(funcao, 3, tamanho, bounds=(0, 100))
best = pop.best()


print(best_x)
print(f"{best_y:.5e}")



# Mutacao
for _ in range(50):
    for i in range(tamanho):
        index_rand1 = random.randint(0, tamanho - 1)

        x1_rand1 = x1[index_rand1]
        x2_rand1 = x2[index_rand1]
        x3_rand1 = x3[index_rand1]
        
        index_rand2 = random.randint(0, tamanho - 1)

        x1_rand2 = x1[index_rand2]
        x2_rand2 = x2[index_rand2]
        x3_rand2 = x3[index_rand2]

        if random .uniform():
            x1[i] = best_x[0] + 0.1 * (x1_rand1 - x1_rand2)
            x2[i] = best_x[1] + 0.1 * (x2_rand1 - x2_rand2)
            x3[i] = best_x[2] + 0.1 * (x3_rand1 - x3_rand2)


    y = funcao(x1, x2, x3)

    for i in range(tamanho):
        if y[i] < best_y:
            best_y = y[i]
            best_x[0] = x1[i]
            best_x[1] = x2[i]
            best_x[2] = x3[i]

    print(best_x)
    print(f"{best_y:.5e}")

    if best_y <0.00001:
        break
