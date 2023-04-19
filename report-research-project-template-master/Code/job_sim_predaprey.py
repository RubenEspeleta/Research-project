"""
Start ipython with the command `ipython --matplotlib`

Then, run this script with:

```
run job_sim_predaprey.py
```
"""
import matplotlib.pyplot as plt

from fluidsim.solvers.models0d.predaprey.solver import Simul

params = Simul.create_default_params()

params.time_stepping.deltat0 = 0.1
params.time_stepping.t_end = 20

params.output.periods_print.print_stdout = 0.01

sim = Simul(params)

sim.state.state_phys.set_var("X", sim.Xs + 2.0)
sim.state.state_phys.set_var("Y", sim.Ys + 1.0)

# sim.output.phys_fields.plot()
sim.time_stepping.start()

sim.output.print_stdout.plot_XY()

# Note: if you want to modify the figure and/or save it, you can use
# ax = plt.gca()
# fig = ax.figure

sim.output.print_stdout.plot_XY_vs_time()

plt.show()
