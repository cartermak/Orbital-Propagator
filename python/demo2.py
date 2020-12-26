"""
Copyright (c) 2020 Carter Mak
"""

import OrbitalPropagator
import numpy as np


def main():

    # Instantiate an integrator for the propagation
    # integrator = OrbitalPropagator.EulerIntegrator()
    integrator = OrbitalPropagator.NaiveRKF45Integrator()

    # Instantiate a simple propagator
    propagator = OrbitalPropagator.SimplePropagator(integrator)
    propagator.integratorArgs["maxArgs"] = 1e5

    # Define a 90-minute time span (roughly 1 orbit for the ISS)
    propagator.timespan = (0, 60*60*24*10)

    # Define a stationary body
    propagator.addBody(
        name="Body1",
        mass=1e26
    )

    # Define a moving body
    propagator.addBody(
        name="Body2",
        position=np.array([5e7, 1e7, 1e7]),
        velocity=np.array([-1000, 0, 0]),
        mass=1e24
    )

    # Define a moving body
    propagator.addBody(
        name="Body3",
        position=np.array([-5e7, -1e7, -1e7]),
        velocity=np.array([1000, 0, 0]),
        mass=1e24
    )

    # Run the actual propagation
    propagator.propagate()

    # Plot results
    plotter = OrbitalPropagator.Plotter(propagator.bodies)
    plotter.plotOrbits("ThreeBody.png",dpi=1000)


if __name__ == "__main__":
    main()
