"""
Start ipython with the command `ipython --matplotlib`

Then, run this script with:

```
run job_sim_lorenz.py
```
"""

import matplotlib.pyplot as plt
from pathlib import Path
from fluidsim.solvers.models0d.lorenz.solver import Simul

# path of the directory where is this file
here = Path(__file__).absolute().parent
# path of the directory where the figure will be saved
path_dir_save = here / "../fig/"
path_dir_save.mkdir(exist_ok=True)

params = Simul.create_default_params()

params.time_stepping.deltat0 = 0.02
params.time_stepping.t_end = 20

params.output.periods_print.print_stdout = 0.01

sim = Simul(params)

sim.state.state_phys.set_var("X", sim.Xs0 + 2.0)
sim.state.state_phys.set_var("Y", sim.Ys0 - 1.0)
sim.state.state_phys.set_var("Z", sim.Zs0 - 10.0)

# sim.output.phys_fields.plot()
sim.time_stepping.start()

sim.output.print_stdout.plot_XY()
# see also the other plot_* methods of sim.output.print_stdout
fig=plt.gcf()
fig.savefig(path_dir_save / "fig_job_sim_lorenz_2")
plt.show()
