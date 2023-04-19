"""Make the figure fig_R_vs_Fh_other_studies.png

"""
from __future__ import print_function

from util import np, plt, show, save

from other_studies import almakie2012, gargett1981, augier2013, kimura2012,\
    brethouwer2007, milestone, praud2005, riley2003

import milestone17
from milestone17 import Exp, Us

studies = [gargett1981, praud2005, milestone, riley2003, brethouwer2007,
           almakie2012, kimura2012, augier2013,
           milestone17]


fig = plt.figure(figsize=(9, 5))

rect = [0.1, 0.14, 0.55, 0.8]
ax = fig.add_axes(rect)

ylim = [1, 300]
xlim = [3e-4, 3e-1]

Flim = 3e-2
Rlim = 10
color = [0.9]*3
linewidth = 20
ax.plot([Flim]*2, [Rlim, ylim[1]], '-',
        color=color, linewidth=linewidth)
ax.plot(xlim, [Rlim]*2, '-', color=color, linewidth=linewidth)


Dc = 0.5
exps = Exp(Us[Dc], Dc=Dc)


for studie in studies:
    print(studie.label)
    ax.plot(studie.Fht, studie.Rt, studie.symbol, label=studie.label)

ax.set_xlabel(r'$F_h$')
ax.set_ylabel(r'$\mathcal{R}$')

ax.set_xscale('log')
ax.set_yscale('log')

ax.set_xlim(xlim)
ax.set_ylim(ylim)

ax.text(7e-4, 40, 'Strongly strat. turb.')
ax.text(0.2, 2e2, 'Weakly strat. turb.', rotation=90)
ax.text(7e-4, 2, 'Viscous regime')

# Fht = np.linspace(1, 8, 20) * 3e-3
# ax.plot(Fht, 1e7 * Fht**3, '--k')

plt.legend(loc=(1.02, 0.04), fontsize=10, numpoints=1)
save(fig, 'fig_R_vs_Fh_other_studies.png')
show()
