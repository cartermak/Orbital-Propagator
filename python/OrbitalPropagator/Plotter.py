"""
Copyright (c) 2020 Carter Mak
"""

from OrbitalPropagator.Body import Body
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import typing
import numpy as np

class Plotter():
    def __init__(self,bodies: typing.List = list()):
        self.bodies = bodies
        return
    
    def addBody(self,body: Body):
        self.bodies.append(body)
    
    def plotOrbits(self,fname = "orbit.png",**kwargs):

        # Declare figure and axes
        fig = plt.figure()
        ax_xy = fig.add_subplot(2,2,1)
        ax_xz = fig.add_subplot(2,2,2)
        ax_yz = fig.add_subplot(2,2,3)
        ax_3d = fig.add_subplot(2,2,4,projection='3d')

        for ax in [ax_xy,ax_xz,ax_yz,ax_3d]:
            ax.set_xticks([])
            ax.set_yticks([])
        
        ax_3d.set_zticks([])
        
        ax_xy.set_title("X-Y Plane")
        ax_xz.set_title("X-Z Plane")
        ax_yz.set_title("Y-Z Plane")
        ax_3d.set_title("3D Projection")

        # Loop over bodies and plot orbits
        for body in self.bodies:
            t,x,y,z = body.getVectorComponentSeries()
            ax_xy.plot(x,y)
            ax_xz.plot(x,z)
            ax_yz.plot(y,z)
            ax_3d.plot(x,y,z)

        # Save image
        plt.savefig(fname,dpi=kwargs.get('dpi',600))

