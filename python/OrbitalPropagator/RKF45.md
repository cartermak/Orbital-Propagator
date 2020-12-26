# Runge-Kutta Fehlberg Combined 4th and 5th Order Numerical Integrator

Lots of people have implemented this before, but it's always fun to see how naive I can be.

I'm mostly following the Wikipedia page, which appears to be based on a few NASA publications by Fehlberg. I'll be hardcoding the coefficients based on Fehlberg's "Formula 1" in those publications. 

After implementing RKF45, I'd like to implement the Dormand-Prince method. This is the method used in the beloved MATLAB routine `ode45`. I also intend to include an integrator subclass which uses a more robust RKF45 implementation --- I believe it's implemented as one available method in the [SciPy `solve_ivp` method](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html).

Sources:

- [Wikipedia: Runge-Kutta Fehlberg Method](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta%E2%80%93Fehlberg_method)
- [FSU: RK45 Python Library](https://people.sc.fsu.edu/~jburkardt/py_src/rkf45/rkf45.html)
- [Shampine & Watts: The Art of Writing Runge-Kutta Code](https://www.sciencedirect.com/science/article/pii/0096300379900018)