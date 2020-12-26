"""
Copyright (c) 2020 Carter Mak
"""

from OrbitalPropagator.Body import Body
from OrbitalPropagator.NumericalIntegrator import EulerIntegrator

import math
import numpy as np


class _Propagator:
    def __init__(self, *args, **kwargs):
        """Class constructor

        Arguments (optional):
        bodies -- list of Body-typed objects to include in the model
        timespan -- tuple of start and end times
        """

        # Break out optional arguments
        self.bodies = kwargs.get('bodies', list())
        self.timespan = kwargs.get('timespan', (0, 3600))

        # Define necessary constant(s)
        self._G = 6.67430E-11

        return

    def addBody(self, body=None, *args, **kwargs):
        """Add body to orbit model.

        Args:
            body (Body, optional): Predefined body. Defaults to None.

        Keyword Args:
            name (string, optional): Name of body to add
            position (np.ndarray(3),optional): initial position
            velocity (np.ndarray(3),optional): initial velocity
            mass (float, optional): mass of the body
        """
        if body is None:
            body = Body(*args, **kwargs)

        self.bodies.append(body)

    def propagate(self):

        self.N = len(self.bodies)

        if self.N == 0:
            raise Exception("No bodies present in model.")

        # TODO Method to actually perform the propagation
        # Step 1: Define ODE function
        # Step 2: Pass to propagator

        def odeFun(t, y): return self._odeFun(t, y)

        integrator = EulerIntegrator(
            odeFun,
            self._getInitialValue(),
            self.timespan
        )

        t_arr, y_arr = integrator.integrate()

        return (t_arr, y_arr)

    def _odeFun(self, _, y):

        # Update member properties
        for i in range(self.N):
            self.bodies[i].setStateVector(y[
                self.bodies[i].n_fields*(i):self.bodies[i].n_fields*(i+1)
            ])

        zero_array = np.array([0.0, 0.0, 0.0])
        for i in range(self.N):
            self.bodies[i].force = zero_array

        for i in range(self.N):
            for j in range(i+1, self.N):

                # Break out values from objects
                pos_i = self.bodies[i].position
                pos_j = self.bodies[j].position
                mass_i = self.bodies[i].mass
                mass_j = self.bodies[j].mass

                # Calculate radius vector and distance
                R = pos_j - pos_i  # Position vector from i to j
                r = np.sqrt(np.dot(R, R))  # Distance between i and j

                # Calculate force vector
                F_ij = (self._G*mass_i*mass_j/(r**3)) * \
                    R  # Force exerted on i by j
                F_ji = - F_ij  # Force exerted on j by i

                # Accumulate net force vector acting on each s/c
                self.bodies[i].force = self.bodies[i].force + F_ij
                self.bodies[j].force = self.bodies[j].force + F_ji

        # Concatenate final system derivative state vector
        # Note: `getDerivativeStateVector` returns a numpy array,
        # so we can use the nummpy `concatenate` method to create a
        # single mega-array state vector.
        systemDerivativeStateVector = np.concatenate([
            b.getDerivativeStateVector() for b in self.bodies
        ], axis=0)

        return systemDerivativeStateVector

    def _getInitialValue(self):
        """Return system state vector of initial values"""

        systemStateVector = np.concatenate([
            b.getStateVector() for b in self.bodies
        ], axis=0)

        return systemStateVector


class SimplePropagator(_Propagator):
    pass
