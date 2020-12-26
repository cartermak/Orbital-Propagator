"""
Copyright (c) 2020 Carter Mak
"""

import numpy as np
import typing

class _NumericalIntegrator:
    def __init__(self):
        return

    def integrate(self, odefun, y0: np.ndarray, timespan: typing.Tuple):
        """Numerically integrate the given ODE function.

        Arguments:
        odefun -- lambda function which takes in the time and 
        """
        return


"""Euler Integration Class"""
class EulerIntegrator(_NumericalIntegrator):
    def __init__(
        self,
        odeFun,
        y0: np.ndarray,
        timespan: typing.Tuple
    ):

        # Pre-define the number of steps to use
        self.n_steps = 100

        # Store member variables
        self.odeFun = odeFun
        self.y0 = y0
        self.timespan = timespan

        # Superclass constructor call
        super().__init__()

    def integrate(self) -> np.ndarray:

        # Calculate time step based on span and number of steps
        startTime, endTime = self.timespan
        duration = endTime-startTime
        timestep = duration/self.n_steps

        # Store state vector
        y = self.y0
        self.y_arr = [self.y0]

        # Initialize time value
        t = startTime
        self.t_arr = [t]

        for i in range(self.n_steps+2):

            # Calculate derivative of state vector
            y_dot = self.odeFun(t, y)

            # Iterate time value
            t += timestep

            # Next time step
            y += timestep*y_dot

            # Store updated state vector to list
            self.y_arr.append(y)

            # Store time stamp to list
            self.t_arr.append(t)
        
        return (self.t_arr,self.y_arr)

class RKF45(_NumericalIntegrator):
    def __init__(self):

        # Superclass constructor call
        super().__init__()
