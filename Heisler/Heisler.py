#!/usr/bin/python
# coding: UTF-8
#
# Author:   Dawid Laszuk
# Contact:  ** Github link
#
# Feel free to contact for any information.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from numpy import *
import pkg_resources

class Heisler():
    """
    Heisler Class Guide:

    At first use have to defone configuration of the problem.
    There are there kind of shapes:
        1- Plane (W)
        2- Cylinder (C)
        3- Sphere (S)
    Also three types of charts:
        1- Center Temperature (CT)
        2- Internal Energy Chnage (IE)
        3- Temperature Distribution (TD)

    ---------
    Heisler(object_shape, chart_type, verbose = False)

    Parameters: object_shape : {"Sphere", "Cylinder", "Wall"}
                                Although there are some alternatives for above
                                items, these type notation is recommended.

                chart_type :    {"center_temp", "internal_energy", "temp_dist"}
                                Although there are some alternatives for above
                                items, these type notation is recommended.
                verbose :       bool, default = 0
                                verbose= 1: Prints variables and returns Bi & Fo.
                                verbose= 0: Returns Bi & Fo without printing anything.

    ---------
    Example: get Internal Energy chart for a shpere shape


    problem =

    """
    def __init__(self, object_shape, target_chart, verbose = 0):

        # Turn all inputs into lower case format
        sh, ch = object_shape.lower(), target_chart.lower()

        # Figure out the shape
        if sh in ["wall", "w", "plane", "p"]:
            self.sh = "Wall"
        elif sh in ["cylinder", "cylender", "c", "pipe", "tube"]:
            self.sh = "Cylinder"
        elif sh in ["sphere", "s", "globe"]:
            self.sh = "Sphere"
        else:
            raise ValueError("The input shape is not valid.\n\
            Choose from \'sphere', \'cylinder' or \'wall'.\n\
            You can even use \'S', \'C' or \'W' instead.")

        # Figure out the chart type
        if ch in ["center_temp", "ct", "center temp",
                  "center_temperature", "center temperature"]:
            self.ch = "Center_Temp"
        elif ch in ["internal_energy", "ie", "le", "internal energy"]:
            self.ch = "Internal_Energy"
        elif ch in ["temp_dist", "td", "temp dist",
        "temperature distribution", "temperature_distribution"]:
            self.ch = "Temp_Dist"
        else:
            raise ValueError("The input shape is not valid.\n\
            Choose from \'center_temp', \'internal_energy' or \'temp_dist'.\n\
            You can even use \'CT', \'IE' or \'TD' instead.")

        # Test Indicator
        if verbose:
            print(f"Model has been set.\nShape: {self.sh} & Chart: {self.ch}")
        else:
            pass

    def show_plot(self):
        """
        -
        Show Plot Funtion Guide:
        Using this function based on made object, the plot related to the
        desired shape will be depicted. This function does not require and
        mandatory arguments. After running this function, the shown chart
        allows users to click on it and draw a vertical and a horizontal line
        to determine the accurate position of the selected point. You can check
        an unlimited number of points, and just by pressing X button on the top
        left corner, the chart will be closed.

        Unfortunately, in this version (1.0), the numeric analysis of the chart
        is not available, so users ought to select points and read its position
        manually. We are planning to make it easier to work with this package.

        Would you please send us your suggestion and feedback?
        Undoubtably we will embrace them.
        """

        # Generate the path
        path = pkg_resources.resource_stream(__name__, f'data/{self.ch}_{self.sh}.png')
        # print(path)

        # In order to facilitate the ginput process
        def ginpret(point):
            x =  [p[0] for p in point]
            y =  [p[1] for p in point]
            return x[0], y[0]

        image = mpimg.imread(path)
        fig = plt.figure(frameon = None, edgecolor = 'w',
                         dpi = 160, figsize = (8, 4))
        ax = fig.add_subplot(1, 1, 1)
        ax.imshow(image)

        Xt, Yt = shape(image)[0], shape(image)[1]

        ax.set_xlim([0, Yt])
        ax.set_ylim([Xt, 0])
        ax.set_xticks([])
        ax.set_yticks([])
        ax.axis('off')
        plt.subplots_adjust(left=0.00, bottom=0.00, right=1.00,
                            top=1.00, wspace=0.30, hspace=0.31)
        colors = "bgrcmk"
        ci = 0
        try:
            while 1:
                yo, xo = ginpret(plt.ginput(1, timeout=0))
                c = colors[ci]
                ci = (1+ci) % 6
                ax.plot([yo, yo], [xo, Xt], lw=1.3, ls='--', color=c)
                ax.plot([0, yo], [xo, xo], lw=1.3, ls='--', color=c)
        except: pass
        plt.show()
        return f"{self.ch}_{self.sh}"

    def calculator(self, alpha, L, h, k, t, verbose = 1):
        """
        -
        Calculator Function Guide:

        Input parameters:
        name            unit            description
        =================================================
        alpha           m2/s            Thermal diffusivity
        L               length [m]      Characteristic length (L = Volume/Area)
        h               [W/m2.K]        Heat transfer coefficient
        k               [W/mK.]         Thermal conductivity
        t               time [s]        Elapsed time

        Output parameters:
        name            unit            description
        =================================================
        Bi              nan             Biot number (h*L/k)
        Fo              nan             Fourier number (alpha*t/L^2)

        * L in shperical and cylinderical shape is radius of them.
        * It is generally accepted that the lumped system analysis is
          applicable if Bi <= 0.1

        * verbose = 1: Prints variables and returns Bi & Fo.
          verbose = 0: Returns Bi & Fo without printing anything.

        Would you please send us your suggestion and feedback?
        Undoubtably we will embrace them.
        """
        Bi = h*L/k
        Fo = alpha * (t/L**2)
        if verbose:
            print(f"\
            Bi = {Bi: 2.4f}\n\
            Fo = {Fo: 2.4f}\n\
            1/Bi = {1/Bi: 2.4f}\n\
            Bi2Fo = {Bi**2*Fo: 2.4f}\n\
            rho*c = {k/alpha/1000: 2.4f} (x1000)")
        else:
            pass
        return Bi, Fo


if __name__ == "__main__":
    print("Now the main file is runing!")
