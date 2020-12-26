"""
Copyright (c) 2020 Carter Mak
"""

import numpy as np
import typing

class NumericalIntegrator:
    def __init__(self):
        return

    def integrate(self, odefun, y0: np.ndarray, timespan: typing.Tuple):
        """Numerically integrate the given ODE function.

        Arguments:
        odefun -- lambda function which takes in the time and 
        """
        return


"""Euler Integration Class"""
class EulerIntegrator(NumericalIntegrator):
    def __init__(self):

        # Pre-define the number of steps to use
        self.n_steps = 10000

        # Superclass constructor call
        super().__init__()

    def integrate(
        self,
        odeFun,
        y0: np.ndarray,
        timespan: typing.Tuple
    ) -> np.ndarray:

        # Calculate time step based on span and number of steps
        startTime, endTime = timespan
        duration = endTime-startTime
        timestep = duration/self.n_steps

        # Store state vector
        y = y0
        yArr = [y0]

        # Initialize time value
        t = startTime
        tArr = [t]

        while t < endTime:

            # Calculate derivative of state vector
            y_dot = odeFun(t, y)

            # Iterate time value
            t  = t + timestep

            # Next time step
            y = y + timestep*y_dot

            # Store updated state vector to list
            yArr.append(y)

            # Store time stamp to list
            tArr.append(t)
        
        return (tArr,yArr)

class RKF45Integrator(NumericalIntegrator):
    def __init__(self):

        # Superclass constructor call
        super().__init__()
