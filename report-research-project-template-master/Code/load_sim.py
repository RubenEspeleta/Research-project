"""To be used with `ipython --matplotlib` (aliased as `ipythonmatplotlib`)

```bash
cd directory of the simulation...

ipythonmatplotlib
```

Once ipython is launched:

```ipython
run ~/Output/Teach/coursem1_pa_instabilities_turbulence/Pysimul/load_sim.py
```

Then, an object simulation linked to the name `sim` has been
created. We can get all information on the simulation and plot
results:

```ipython
sim.output.print_stdout.plot_XY()
sim.output.print_stdout.plot_XY_vs_time()

# and for the lorenz model:
sim.output.print_stdout.plot_XYZ()
sim.output.print_stdout.plot_XZ()
```

"""
from fluidsim import load_sim_for_plot

sim = load_sim_for_plot()
