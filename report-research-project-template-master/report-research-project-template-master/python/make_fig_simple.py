
import os
import sys

import numpy as np
import matplotlib.pyplot as plt

# path of the directory where is the script
here = os.path.abspath(os.path.dirname(__file__))
# path of the directory where the figure will be saved
path_dir_save = os.path.abspath(here + '/../tmp/')
if not os.path.exists(path_dir_save):
    os.mkdir(path_dir_save)

tmin = 0.  # s
tmax = 5.   # s
nb_points = 50

times = np.linspace(tmin, tmax, nb_points)

z0 = 100.  # m
v0 = 1.   # m/s
g = 9.8   # m/s**2

vs = v0 - g*times
zs = z0 + vs*times

fig, (ax0, ax1) = plt.subplots(2, figsize=(6, 4))

ax0.plot(times, vs)
ax0.set_xlabel('$t$')
ax0.set_ylabel('$v$')

ax1.plot(times, zs)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$z$')

fig.tight_layout()

fig.savefig(path_dir_save + '/fig_simple.png')

if '--no-show' not in sys.argv:
    plt.show()
