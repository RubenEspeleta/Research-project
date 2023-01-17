import numpy as np # Imports a library called numpy. The name in the program is going to be np.
import matplotlib # if you don't include an "as" then the local-name is going to be matplotlib.
# from matplotlib import * ### In this case you import all contained libraries in matplotlib and you call them only by their name.
##########################FUNCTIONS DEFINITION ###############################################################
def cone(x,y,R,Bc,Bl) :
    rc=0
    ###############################################################
    ## Transformation of Coordinates from cartesian to cylindric ##
    r=np.sqrt(x*x+y*y)
    theta=np.arctan2(y,x)
    ###############################################################
    B=Bc-(Bc-Bl)*(r-rc)**2/(R-rc)**2
    return(B)

def b(x,y,R,Bc,Bl) :
    ###############################################################
    ## Transformation of Coordinates from cartesian to cylindric ##
    r=np.sqrt(x*x+y*y)
    theta=np.arctan2(y,x)
    ###############################################################
    l=R-np.cos(2*theta)*R/2
    #a=Bc-(Bc-Bl)*(r-rc)**2/(R-rc)**2
    a=cone(x,y,R,Bc,Bl)
    B=Ba*np.cos(3*np.pi*r/l)+a
    return (B)
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 22})

N=21
def segmentcolormap(N) : 
    return(matplotlib.colors.ListedColormap(plt.get_cmap('jet')(np.linspace(0,1,N))))
segmented_cmaps = segmentcolormap(N)

###################################### END OF FUNCTIONS ######################################################
## PARAMETERS #####################
R=800e3 # 80km
Bc=0.9e3 # 0.9km
Bl=-2e3 # -2km
Ba=1.1e3
rc=0
##########- END OF PARAMETERS #########

## FIGURA 1. - 2D: Cone
#R=800e3
x,y = np.mgrid[-1600e3:1600e3:100j, -1600e3:1600e3:100j]
plt.rcParams.update({'font.size': 22})
z = cone(y,x,R,Bc,Bl)
import matplotlib.pyplot as plt
plt.imshow(z,extent=[-1600e3,1600e3,-1600e3,1600e3],cmap=segmented_cmaps,vmin=-20e3,vmax=0.9e3)
plt.colorbar()
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.show()

## FIGURA 2. - 3D: Cone
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax = plt.axes(projection='3d')
surf=ax.plot_surface(x, y, z, rstride=1, cstride=1,
                cmap=segmented_cmaps, edgecolor='none')
# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

## FIGURA 3. - 2D: Thule
# Crea la malla para graficar:
x,y = np.mgrid[-1600e3:1600e3:500j, -1600e3:1600e3:500j]
z = b(y,x,R,Bc,Bl)
plt.imshow(z,extent=[-1600e3,1600e3,-1600e3,1600e3],cmap=segmented_cmaps,vmin=-3500,vmax=2000)
plt.colorbar()
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.show()


