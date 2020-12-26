"""
Copyright (c) 2020 Carter Mak
"""

import numpy as np
import typing


class NumericalIntegrator:
    def __init__(self):
        return

    def integrate(self):
        """Numerically integrate the given ODE function.

        TEMPLATE ONLY
        """

        raise Warning("NumericalIntegrator is only a template.")

        exit(0)


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
            t = t + timestep

            # Next time step
            y = y + timestep*y_dot

            # Store updated state vector to list
            yArr.append(y)

            # Store time stamp to list
            tArr.append(t)

        return (tArr, yArr)


"""RKF45 Numerical Integrator

Adaptive step size numerical integrator using the RKF45 algorithm.
Called "naive" because I'm sure it's filled with ignorant mistakes and 
inefficiencies.
"""


class NaiveRKF45Integrator(NumericalIntegrator):
    def __init__(self):

        # Superclass constructor call
        super().__init__()

        # Define variables for $\alpha_2$=1/3
        self.A = np.array([0, 2/9, 1/3, 3/4, 1, 5/6], dtype=float)
        self.B = [
            [],
            [2/9],
            [1/12, 1/4],
            [69/128, -243/128, 135/64],
            [-17/12, 27/4, -27/5, 16/15],
            [65/432, -5/16, 13/16, 4/27, 5/144]
        ]
        self.CH = np.array(
            [47/450, 0, 12/25, 32/225, 1/30, 6/25], dtype=float
        )
        self.CT = np.array(
            [-1/150, 0, 3/100, -16/75, -1/20, 6/25], dtype=float
        )

    def integrate(
        self,
        odeFun,
        y0: np.ndarray,
        timespan: typing.Tuple,
        *args, **kwargs
    ) -> np.ndarray:

        # Additional integration parameters
        maxSteps = kwargs.get('maxSteps', 1e4)
        relTol = kwargs.get('relTol', 0.1)

        # Break out elements in timespan tuple
        startTime, endTime = timespan

        # Use 1% of duration as starting h value
        h = (endTime-startTime)/100

        # Initialize times
        t = startTime
        tArr = [t]

        # Initialize state vectors
        y = y0
        yArr = [y]

        # Declare array of k values for RK
        k = [[0.0]*6]*6

        # Initialize a counter to automatically exit if too many steps
        # are taken
        counter = 0

        while t < endTime:

            # If we're going to overshoot the end, cut off the step size
            if endTime - t < h:
                h = endTime - t

            # Calculate k coefficients for RK
            k[0] = h*odeFun(t + self.A[0]*h, y)
            for i in range(1, 6):
                k[i] = h*odeFun(
                    t + self.A*h,
                    y + np.sum([self.B[i][j]*k[j] for j in range(i)], axis=0)
                )

            # Calculate truncation error
            TE = np.max(
                np.abs(
                    np.sum([self.CT[i]*k[i] for i in range(6)], axis=0)
                )
            )

            # Decide whether or not to iterate
            if TE <= relTol:
                # Iterate!

                # Calculate new y value
                y = y + np.sum([self.CH[i]*k[i] for i in range(6)], axis=0)

                # Calculate new t value
                t = t + h

                # Store values
                tArr.append(t)
                yArr.append(y)

            # Update step size
            h = 0.9*h*((relTol/TE)**(0.2))

            counter = counter + 1
            if counter > maxSteps:
                raise ResourceWarning(
                    "Stopping integration. Max steps surpassed.")

        return (tArr, yArr)
