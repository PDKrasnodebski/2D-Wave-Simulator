from SimulationAlgorithm import Simulation
from SimulationEnvironment import Environment
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from IPython.display import display, clear_output

class SineSimulation(Simulation):

    def __init__(self, environment: Environment = Environment()):
        super().__init__(environment)


    def wave_propagation(self, s):
        n1 = self.n1
        n11 = self.n11
        n2 = self.n2
        n22 = self.n22

        self.SimEnvironment.Hx[n1:n2 - 1, n11:n22 - 1] = np.multiply(
                self.SimEnvironment.A[n1: n2 - 1, n11: n22 - 1],
                self.SimEnvironment.Hx[n1: n2 - 1, n11: n22 - 1]) - np.multiply(
                self.SimEnvironment.B[n1: n2 - 1, n11: n22 - 1],
                (self.SimEnvironment.Ez[n1:n2 - 1, n11 + 1:n22] - self.SimEnvironment.Ez[n11: n2 - 1, n11: n22 - 1]))

        self.SimEnvironment.Hy[n1:n2 - 1, n11:n22 - 1] = np.multiply(
                self.SimEnvironment.A[n1: n2 - 1, n11: n22 - 1],
                self.SimEnvironment.Hy[n1: n2 - 1, n11: n22 - 1]) + np.multiply(
                self.SimEnvironment.B[n1: n2 - 1, n11: n22 - 1],
                (self.SimEnvironment.Ez[n1 + 1:n2, n11:n22 - 1] - self.SimEnvironment.Ez[n11: n2 - 1, n11: n22 - 1]))

        self.SimEnvironment.Ez[n1 + 1: n2 - 1, n11 + 1: n22 - 1] = np.multiply(
                self.SimEnvironment.C[n1 + 1: n2 - 1, n11 + 1: n22 - 1],
                self.SimEnvironment.Ez[n1 + 1: n2 - 1, n11 + 1: n22 - 1]) + np.multiply(
                (self.SimEnvironment.Hy[n1 + 1:n2 - 1, n11 + 1:n22 - 1] -
                 self.SimEnvironment.Hy[n1: n2 - 2, n11 + 1: n22 - 1] -
                 self.SimEnvironment.Hx[n1 + 1: n2 - 1, n11 + 1: n22 - 1] +
                 self.SimEnvironment.Hx[n1 + 1: n2 - 1, n11: n22 - 2]),
                self.SimEnvironment.D[n1 + 1: n2 - 1, n11 + 1: n22 - 1])

        self.SimEnvironment.Ez[self.SimEnvironment.xSource, self.SimEnvironment.ySource] = np.sin(((
                    2 * np.pi * (
                        3E8 / (1E-6 * self.SimEnvironment.n_lambda)) * s * self.SimEnvironment.temporal_grid_step)))
        
    def boundaries(self, s):

        #print(f"{s}, {self.SimEnvironment.X_DIMENSION-2-self.SimEnvironment.xSource}")
        #if s >= self.SimEnvironment.X_DIMENSION-2-self.SimEnvironment.xSource:
            #self.SimEnvironment.Ez[self.SimEnvironment.X_DIMENSION-2, 3:1:self.SimEnvironment.Y_DIMENSION - 3] = self.SimEnvironment.c0efffor * (self.SimEnvironment.Ez[self.SimEnvironment.X_DIMENSION - 3,3:1:self.SimEnvironment.Y_DIMENSION - 3] + self.SimEnvironment.prev_prev_x_for[1,3:1:self.SimEnvironment.Y_DIMENSION - 3]) - self.SimEnvironment.prev_prev_x_minus_1for[1,3:1:self.SimEnvironment.Y_DIMENSION-3]+self.SimEnvironment.c2efffor * (self.SimEnvironment.prev_xfor[1,3:1:self.SimEnvironment.Y_DIMENSION - 3] + self.SimEnvironment.prev_x_minus_1for[1,3:1:self.SimEnvironment.Y_DIMENSION - 3]) + self.SimEnvironment.c3efffor*(self.SimEnvironment.prev_x_minus_1for[1,2:1:self.SimEnvironment.y - 4] + self.SimEnvironment.prev_x_minus_1for[1,4:1:self.SimEnvironment.ydim - 2] + self.SimEnvironment.prev_x_for[1,2:1:self.SimEnvironment.Y_DIMENSION-4] + self.SimEnvironment.prev_x_for[1,4:1:self.SimEnvironment.Y_DIMENSION - 2])

        self.SimEnvironment.prev_prev_x_for = self.SimEnvironment.prev_x_for
        self.SimEnvironment.prev_prev_x_minus_1for = self.SimEnvironment.prev_x_minus_1for
        self.SimEnvironment.prev_x_for[0,1:1:self.SimEnvironment.Y_DIMENSION] = self.SimEnvironment.Ez[self.SimEnvironment.X_DIMENSION-2,1:1:self.SimEnvironment.Y_DIMENSION]
        self.SimEnvironment.prev_x_minus_1for[0,1:1:self.SimEnvironment.Y_DIMENSION] = self.SimEnvironment.Ez[self.SimEnvironment.X_DIMENSION-3,1:1:self.SimEnvironment.Y_DIMENSION]
        
        #self.SimEnvironment.Ez[2,2] = self.SimEnvironment.prev_prev_x_rev[3]
        #self.SimEnvironment.Ez[2,self.SimEnvironment.Y_DIMENSION-2] = self.SimEnvironment.prev_prev_x_rev[self.SimEnvironment.Y_DIMENSION-3]
        self.SimEnvironment.Ez[self.SimEnvironment.X_DIMENSION - 2,2]=self.SimEnvironment.prev_prev_x_minus_1for[0,2]
        #self.SimEnvironment.Ez[self.SimEnvironment.X_DIMENSION-2, self.SimEnvironment.Y_DIMENSION - 2] = self.SimEnvironment.prev_prev_x_minus_1for[self.SimEnvironment.Y_DIMENSION - 3]