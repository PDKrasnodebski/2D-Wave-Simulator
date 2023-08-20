import numpy as np


class Environment:

    def __init__(self, x_source: int = 200, y_source: int = 200):

        self.xSource = x_source
        self.ySource = y_source

        self.X_DIMENSION = 400
        self.Y_DIMENSION = 400

        frequency = 1.5e+13

        speed_of_light = 3E8

        sigma = np.full((self.X_DIMENSION, self.Y_DIMENSION), 4E-4)
        sigma_star = np.full((self.X_DIMENSION, self.Y_DIMENSION), 4E-4)

        permittivity = (1.0 / (36.0 * np.pi)) * 1E-9
        permeability = 4 * np.pi * 1E-7

        epsilon = permittivity * np.ones((self.X_DIMENSION, self.Y_DIMENSION))
        mu = permeability * np.ones((self.X_DIMENSION, self.Y_DIMENSION))

        stability_factor = 1.0 / (2 ** 0.5)

        spatial_grid_step = 1E-6  # delta
        self.temporal_grid_step = stability_factor * spatial_grid_step / speed_of_light  # deltat

        p0 = 1
        p2 = - 0.5

        t_c = [(speed_of_light / (2 * stability_factor) * (1 - (p0 / stability_factor))),
               - (speed_of_light / (2 * stability_factor) * (1 + (p0 / stability_factor))),
               (speed_of_light / (stability_factor ** 2) * (p0 + (p2 * stability_factor * stability_factor))),
               - (p2 * speed_of_light) / 2,
               (speed_of_light / (2 * stability_factor) * (1 + (p0 / stability_factor))),
               - (speed_of_light / (2 * stability_factor) * (1 - (p0 / stability_factor)))]

        self.n_lambda = speed_of_light / (frequency * spatial_grid_step)

        self.Ez = np.zeros((self.X_DIMENSION, self.Y_DIMENSION))
        self.Hy = np.zeros((self.X_DIMENSION, self.Y_DIMENSION))
        self.Hx = np.zeros((self.X_DIMENSION, self.Y_DIMENSION))

        self.A = np.divide(mu - 0.5 * self.temporal_grid_step * sigma_star,
                           mu + 0.5 * self.temporal_grid_step * sigma_star)
        self.B = np.divide(self.temporal_grid_step / 1E-6, mu + 0.5 * self.temporal_grid_step * sigma_star)

        self.C = np.divide(epsilon - 0.5 * self.temporal_grid_step * sigma,
                           epsilon + 0.5 * self.temporal_grid_step * sigma)
        self.D = np.divide(self.temporal_grid_step / 1E-6, epsilon + 0.5 * self.temporal_grid_step * sigma)

        self.c0efffor = - (t_c[0] / t_c[1])
        self.c1efffor = - (t_c[2] / t_c[1])
        self.c2efffor = - (t_c[3] / t_c[1])

        self.c0effrev = - (t_c[5] / t_c[4])
        self.c1effrev = - (t_c[2] / t_c[4])
        self.c2effrev = - (t_c[3] / t_c[4])

        self.prev_x_for = np.zeros((1, self.Y_DIMENSION))
        self.prev_x_minus_1for = np.zeros((1, self.Y_DIMENSION))
        self.prev_y_for = np.zeros((self.X_DIMENSION, 1))
        self.prev_y_minus_1for = np.zeros((self.X_DIMENSION, 1))
        self.prev_x_rev = np.zeros((1, self.Y_DIMENSION))
        self.prev_x_minus_1rev = np.zeros((1, self.Y_DIMENSION))
        self.prev_y_rev = np.zeros((self.X_DIMENSION, 1))
        self.prev_y_minus_1rev = np.zeros((self.X_DIMENSION, 1))
