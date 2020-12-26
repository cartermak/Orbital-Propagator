"""
Copyright (c) 2020 Carter Mak
"""

import numpy as np


class Body:
    def __init__(self, *args, **kwargs):
        """Class constructor defines properties of the body and its orbit"""

        # Break out optional arguments with default vaules
        self.name = kwargs.get('name', None)
        self.position = kwargs.get('position', np.array([0.0, 0.0, 0.0]))
        self.velocity = kwargs.get('velocity', np.array([0.0, 0.0, 0.0]))
        self.mass = kwargs.get('mass', 0)
        self.force = np.array([0.0, 0.0, 0.0])

        # Ensure position and velocity are typed as floats
        self.position = self.position.astype('float64')
        self.velocity = self.velocity.astype('float64')

        # Variable to store the number of fields in the state vector
        self.n_fields = 6

    def getStateVector(self) -> np.ndarray:
        """Get state vector as a list of numbers."""

        stateVector = np.concatenate((self.position, self.velocity), axis=0)

        return stateVector

    def getDerivativeStateVector(self) -> np.ndarray:
        """Get derivative of state vector elements."""

        # Divide force vector element-wise by mass to find acceleration.
        acceleration = self.force/self.mass

        # Concatenate velocity and acceleration
        derivativeStateVector = np.concatenate(
            (self.velocity, acceleration), axis=0)

        return derivativeStateVector

    def setStateVector(self, state: np.ndarray):
        """Pass in a state vector to update the state of the body."""

        self.position = state[0:3]
        self.velocity = state[3:6]
