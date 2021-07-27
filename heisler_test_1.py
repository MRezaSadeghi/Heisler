from Heisler import Heisler as hs

problem = hs("W", "lE", verbose = 0)

alpha = 8.4*10**-5
L = 7/1000
h = 200
k = 215
t = 120

problem.calculator(alpha, L, h, k, t, verbose = 1)
problem.show_plot()
