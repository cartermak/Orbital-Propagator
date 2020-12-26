# Orbital Propagator

*Copyright (c) 2020 Carter Mak. All rights reserved.*

---

## Requirements

- Support an arbitrary number of bodies
- Allow all bodies to act on all other bodies
- Assume point masses, i.e., no gravity-gradient-driven torque on bodies, no oblateness, etc.
- Store calculated path and velocity for plotting
- Use a simple numerical integrator, e.g., RK4
- Allow visualization of paths
- Reach goal: animation of the orbits propagating
- Reach goal: adaptive step sizing for numerical integration (RKF45?)
- Reach goal: be able to define static bodies, i.e., bodies which are assumed to be relatively much more massive than all others

Flexibility is enabled in the form of:
- Changing the integrator. Could even go from simple Euler integration to fixed step RK4 to RKF45?
- Changing the fidelity of the model. This would mean going from a basic point mass, Neutonian mechanics sort of deal up to models like J2 that consider spheroid oblateness and effects of finite size, for example. This requires changing/extending the state vector elements, the "influencers" (i.e., simply a force vector in our simple model), and the interplay between the two.

## Necessary Classes/Structs/Interfaces

- Body
- Propagator (Begin with a simple based on point masses and stuff, but design a base class to enable extension in the future)
- State (Begin with the basic necessary state elements of position and velocity vectors, but design a base class to enable extension in the future)
- Integrator (Reads in a state object and influence object)

### Body

#### Properties

- State (tree or array of values, depending on how I feel like addressing time stamps)
- Mass (*should* be constant)

#### Methods

- `ode_f(t)`: pass in a templated state vector;

### Propagator

#### Properties (public)

- time span
- List of bodies

#### Methods (public)

- `addBody(mass,initial_position,intial_velocity)`
- `setTimeSpan(start_time,end_time)`
- `run()`
- Various getter routines which facilitate plotting, etc...

#### Methods (private)

- 

### State

#### Properties

Base class can contain position and velocity; inherited classes can track higher-fidelity model properties (e.g., orientation, angular rate)

#### Methods

- `getDerivativeStateVector()`: returns the derivative of the state vector as an array/similar type
- `setStateVector()`: Assign the integrated state vector back to elements in the state class

## Procedure

1) Define initial system state (number of bodies, initial position and velocity)
2) Calculate forces applied to each body by all other bodies
3) Sum forces acting on each body
4) Apply Newtonian mechanics to solve for resultant acceleration
5) Numerically integrate state vector consisting of the resultant acceleration and known velocity over a finite time step to find the position and velocity of each body at some time t+h.
6) Repeat.

---

## Pseudocode

Defining the gravitaitonal force between each pair of bodies:
```
G = ...; // Define gravitational constant

// Zero out forces acting on each body
for i in 1 through <number of bodies>
    bodies(i).force = [0,0,0];
endfor

for i in 1 through <number of bodies>
    for j in i+1 through <number of bodies>

        // Break out values from objects
        pos_i = bodies(i).position; // Vector quantity
        pos_j = bodies(j).position; // Vector quantity
        mass_i = bodies(i).mass; // Scalar quantity
        mass_j = bodies(j).mass; // Scalar quantity

        // Calculate radius vector and distance
        R = pos_j - pos_i; // Position vector from i to j
        r = abs(r); // Distance between i and j

        // Calculate force vector
        F_ij = (G*mass_i*mass_j/r^3)*R; // Force exerted on i by j
        F_ji = - F_ij; // Force exerted on j by i

        // Add force vector component to net force acting on both bodies
        bodies(i).force = bodies(i).force + F_ij;
        bodies(j).force = bodies(j).force + F_ji;
    endfor
endfor
```