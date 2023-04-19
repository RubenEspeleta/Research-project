
from util import os, path_tmp
from milestone17 import Exp, Us, calcul_nt0

table = []

cells = [r'D_c', 'N', 'U_c', r'\mathcal{R}', 'F_h', 'T_c',
         r'\Delta \tilde E_P',
         r't_{\min}/T_c', r't_{\max}/T_c', 't_{tot}/T_c', 't_{tot}']

table.append(['$' + cell + '$' for cell in cells])

cells = ['cm', 'rad/s', 'cm/s', '', '', 's',
         '', '', '', '', 's']

table.append(cells)


def make_line(N, Dc, exps, i):
    Tc = exps.Tc[i]
    nt = calcul_nt0(exps.t_min[i], exps.t_max[i], Tc)
    return [
        int(100*Dc), N, int(U*100), exps.Rt[i], exps.Fht[i], Tc,
        exps.mixing_one_period[i],
        exps.t_min[i], exps.t_max[i],
        nt, int(round(nt*Tc))]


N = 0.55
Dc = 0.25
exps = Exp(Us[Dc], Dc=Dc, N=N)

for i, U in enumerate(exps.Uc):
    table.append(make_line(N, Dc, exps, i))

table.append([])

N = 0.8
Dc = 0.5
exps = Exp(Us[Dc], Dc=Dc, N=N)

for i, U in enumerate(exps.Uc):
    table.append(make_line(N, Dc, exps, i))


for il, line in enumerate(table):
    for ir, contain in enumerate(line):
        if isinstance(contain, str):
            continue
        fmt = '{}'
        if ir == 4:
            fmt = '{:.3f}'
        elif ir == 5:
            fmt = '{:.1f}'
        elif ir == 6:
            fmt = '{:.1e}'
        elif isinstance(contain, float):
            fmt = '{:.2f}'
        table[il][ir] = fmt.format(contain)


txt = r"""
\begin{table}
\centerline{\begin{tabular}{""" + 'c'*len(cells) + """}
"""

for il, line in enumerate(table):
    txt += ' & '.join(line) + ' \\\\\n'

txt += r"""\end{tabular}}
\caption{Parameters for the new experiments.}
\label{table_exps}
\end{table}
"""

print(txt)


with open(os.path.join(path_tmp, 'table_exps.tex'), 'w') as f:
    f.write(txt)
