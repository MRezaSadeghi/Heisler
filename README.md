# Heisler Chart Guide

This is a Python library distributed on [Pypi](https://pypi.org/project/Heisler/) to increase the speed and accuracy of using the Heilser Chart. This package also provides users a simple additional calculator which allows users to calculate initial useful parameters for Heisler Chart [1]. For more information visit [Wikipedia page](https://en.wikipedia.org/wiki/Heisler_chart).

Using ```show_plot``` based on made object, the plot related to thedesired shape will be depicted. This function does not require any mandatory arguments. After running this function, the shown chart allows users to click on it and draw a vertical and a horizontal line to determine the accurate position of the selected point. You can check an unlimited number of points, and just by pressing X button on the top left corner, the chart will be closed.

Unfortunately, in this version (0.1.0), the numeric analysis of the chart is not available, so users ought to select points and read its position manually. We are planning to make it easier to work with this package.

## Installation
use the package manager [pip](https://pip.pypa.io/en/stable/) to install Heisler Chart Guide in Python.
```python
pip install HeislerChartsGuide
```

## An Example (Chart)

Heisler Class Guide:

At first use have to defone configuration of the problem.
There are there kind of shapes:\
  1- Plane (W)\
  2- Cylinder (C)\
  3- Sphere (S)

Also three types of charts:\
  1- Center Temperature (CT)\
  2- Internal Energy Chnage (IE)\
  3- Temperature Distribution (TD)

Consider you want to use the Internal Energy chart for a plane wall.
```python
from HeislerChartsGuide import Heisler as hc
problem = hs("W", "IE", verbose = 0)
problem.show_plot()
```

## An Example (Calculator)
And if you want to use the calculator, you can add the below code to the previous one. Then you
```python
alpha = 8.4*10**-5 		#m2/s            Thermal diffusivity
L = 7/1000			#length [m]      Characteristic length (L = Volume/Area)
h = 200				#[W/m2.K]        Heat transfer coefficient
k = 215				#[W/mK.]         Thermal conductivity
t = 120				#time [s]        Elapsed time
Bi, Fo = problem.calculator(alpha, L, h, k, t, verbose = 1)
```
## Reference
[1] Frank P. Incropera (2006). Fundamentals of Heat and Mass Transfer (6th ed.).\
John Wiley. ISBN-13: 978-0471457282

## License

Copyright 2021 Reza Sadeghi

Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the "Software"), to deal in 
the Software without restriction, including without limitation the rights to use, 
copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the 
Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL 
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.