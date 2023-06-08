# coding: utf-8
#from matplotlib import pyplot  as plt
#import numpy as np
#plt.rcParams["figure.figsize"] = [7.00, 3.50]
#plt.rcParams["figure.autolayout"] = True
#x = np.array([10, 5, 2, 1, 0.5, 0.25])
#y_error=x/2
#y = np.array([650,600,580, 570, 560, 558])
#x= -x
#plt.grid()
#plt.errorbar(x,y, yerr=y_error, linestyle="None", fmt="ob", capsize=1, ecolor="k")
#plt.xticks(x, -x)
#plt.show()


##New script###
import numpy as np
import matplotlib.pyplot as plt
x = np.array([10, 5, 1])
y = np.array([399530, 419060, 427010])
y_error = x*1000/2
plt.errorbar(x*1000, y, yerr=y_error, linestyle="None", fmt="ob", capsize=1, ecolor="k")
plt.xticks(x*1000, -x)
plt.show

