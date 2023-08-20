from SineSimulation import SineSimulation
from SimulationEnvironment import Environment
import matplotlib.animation as animation
import matplotlib.pyplot as plt

if __name__ == '__main__':

    E = Environment(x_source = 200, y_source = 200)
    S = SineSimulation(environment = E)
    S.simulate()
