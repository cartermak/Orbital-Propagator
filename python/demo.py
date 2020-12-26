"""
Copyright (c) 2020 Carter Mak
"""

import OrbitalPropagator
import numpy as np


def main():
    propagator = OrbitalPropagator.SimplePropagator()
    propagator.timespan = (0, 60*90)  # One month ish

    propagator.addBody(
        name="Earth",
        mass=6E24
    )

    propagator.addBody(
        name="ISS",
        position=np.array([6800000, 0, 0]),
        velocity=np.array([0, 7650000, 0]),
        mass=500000
    )

    t_arr, y_arr = propagator.propagate()

    


if __name__ == "__main__":
    main()
