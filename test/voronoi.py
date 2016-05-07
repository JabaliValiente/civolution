import numpy as np
import matplotlib.pyplot as plt

nber_seed = 100
world_size = 1024
earth = 0.3


class seed_point:
    def __init__(self, x, y, v):
        self.x = round(x*world_size)
        self.y = round(y*world_size)
        if v < earth:
            self.v = 0
        else:
            self.v = 1

    def dist2(self, x, y):
        return (x-self.x)**2 + (y-self.y)**2


if __name__ == "__main__":
    seeds = []
    rand = np.random.rand(nber_seed, 3)
    for i in range(nber_seed):
        seeds.append(seed_point(rand[i, 0], rand[i, 1], rand[i, 2]))

    world = np.zeros((world_size, world_size))
    for i in range(world_size):
        for j in range(world_size):
            nearest = world_size**2
            for point in seeds:
                if point.dist2(i, j) < nearest:
                    nearest = point.dist2(i, j)
                    world[i, j] = point.v

    plt.figure()
    plt.imshow(world)
    plt.show()
