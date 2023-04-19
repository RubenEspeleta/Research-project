from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from fluidsim.solvers.models0d.predaprey.solver import Simul

here = Path(__file__).absolute().parent

# path of the directory where the figure will be saved
path_dir_save = here / "../fig/"
path_dir_save.mkdir(exist_ok=True)
params = Simul.create_default_params()


xs = np.linspace(0.01, 5, 100)
ys = np.linspace(0.01, 5, 100)

Xs, Ys = np.meshgrid(xs, ys)

potential = (
    params.C * np.log(Xs) - params.D * Xs + params.A * np.log(Ys) - params.B * Ys
)

fig, ax = plt.subplots()

ax.contour(Xs, Ys, potential, 10)

ax.set_xlabel("$X$")
ax.set_ylabel("$y$")

ax.set_title("Isolines of potential for the prey-predator model")

tmp_dir = here.parent / "tmp"
tmp_dir.mkdir(exist_ok=True)
fig=plt.gcf()
fig.savefig(path_dir_save / "fig_isocountour_pot_preypreda")
fig.savefig(tmp_dir / "fig_isocontour.png")
plt.show()
