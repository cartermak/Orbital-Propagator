"""
Copyright (c) 2020 Carter Mak
"""

import OrbitalPropagator
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def main():

    # Instantiate an integrator for the propagation
    # integrator = OrbitalPropagator.EulerIntegrator()
    integrator = OrbitalPropagator.NaiveRKF45Integrator()

    # Instantiate a simple propagator
    propagator = OrbitalPropagator.SimplePropagator(integrator)

    # Define a 90-minute time span (roughly 1 orbit for the ISS)
    propagator.timespan = (0, 5*60*90)

    # Define the Earth. Use default position and velocity (origin and zero)
    propagator.addBody(
        name="Earth",
        mass=6E24
    )

    # Define the ISS. Start at +X axis heading in +Y direction
    propagator.addBody(
        name="ISS",
        position=np.array([6800000, 0, 0]),
        velocity=np.array([0, 7650, 0]),
        mass=500000
    )

    # Run the actual propagation
    propagator.propagate()

    # Plot the results
    t,x,y,z = propagator.bodies[1].getVectorComponentSeries()
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1,projection='3d')
    ax.plot(x,y,z)
    plt.savefig('ISS_orbit.png',dpi=600)


if __name__ == "__main__":
    main()
