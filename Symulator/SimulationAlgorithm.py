from SimulationEnvironment import Environment
import threading
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Simulation():

    def __init__(self, environment: Environment = Environment()):
        self.SimEnvironment = environment
        self.matrice = None
        self.n1 = 1
        self.n11 = 1
        self.n2 = self.SimEnvironment.X_DIMENSION - 1
        self.n22 = self.SimEnvironment.Y_DIMENSION - 1
        self.s=0

    def wave_propagation(self, s: int):
        return self.SimEnvironment.Ez
    
    def boundaries(self, s: int):
        return self.SimEnvironment.Ez
    
    
    def simulate(self):

        fig, ax = plt.subplots()
        self.matrice = ax.matshow(self.SimEnvironment.Ez, cmap='RdYlGn', vmin=-0.5, vmax=0.5)
        plt.colorbar(self.matrice)
        ani = FuncAnimation(fig, self.update, frames=100, interval=20)
        plt.show()

    def update(self, i):

            self.s+=1

            self.wave_propagation(self.s)
            self.boundaries(self.s)

            self.matrice.set_array(self.SimEnvironment.Ez)


            
