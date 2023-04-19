
import os
import sys

import numpy as np
import matplotlib.pyplot as plt

from fluiddyn.output.rcparams import set_rcparams

path_tmp = os.path.join(os.path.split(os.path.split(__file__)[0])[0], 'tmp')
if not os.path.exists(path_tmp):
    os.makedirs(path_tmp)

# # iexps_norot = [18] + range(21, 25) + range(32, 39) + range(64, 74)
# iexps_norot = list(np.r_[18, 21:25, 32:39, 64:74])

# # bad PIV ?
# # iexps_norot.remove(18)
# # iexps_norot.remove(21)
# # iexps_norot.remove(22)
# iexps_norot.remove(23)  # bad piv for some times
# iexps_norot.remove(37)
# iexps_norot.remove(67)
# # no pack
# iexps_norot.remove(36)
# iexps_norot.remove(38)


if 'save_for_tex' in sys.argv:
    set_rcparams(fontsize=18, for_article=False, for_beamer=False)

    def save(fig, name):
        fig.savefig(os.path.join(path_tmp, name))

    def show():
        'show function doing nothing'
else:
    set_rcparams(fontsize=14, for_article=False, for_beamer=False)

    show = plt.show

    try:
        __IPYTHON__
        plt.ion()
    except NameError:
        pass

    def save(fig, name):
        'save function doing nothing'
