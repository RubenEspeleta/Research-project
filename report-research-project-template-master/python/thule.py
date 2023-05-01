import numpy as np # Imports a library called numpy. The name in the program is going to be np.
import matplotlib # if you don't include an "as" then the local-name is going to be matplotlib.
# from matplotlib import * ### In this case you import all contained libraries in matplotlib and you call them only by their name.
import matplotlib.pyplot as plt
#########################FUNCTIONS DEFINITION ###############################################################
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
def PlotCone2D():
	## FIGURA 1. - 2D: Cone
	#R=800e3
    x,y = np.mgrid[-800e3:800e3:100j, -800e3:800e3:100j]
    plt.rcParams.update({'font.size': 22})
    z = cone(x,y,R,Bc,Bl) 
    plt.imshow(z,extent=[-800,800,-800,800],cmap=segmented_cmaps,vmin=-5000,vmax=1000)
    plt.colorbar()
    plt.xlabel("x(km)") 
    plt.ylabel("y(km)")
    plt.show()

def PlotCone3D():
	## FIGURA 2. - 3D: Cone
    x,y = np.mgrid[-800e3:800e3:100j, -800e3:800e3:100j]
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    z = cone(y,x,R,Bc,Bl)
    ax = plt.axes(projection='3d')
    surf=ax.plot_surface(x/1000, y/1000, z, rstride=1, cstride=1,cmap=segmented_cmaps, edgecolor='none')
    ax.set_zticks([])
    plt.xlabel("x (km)")
    plt.ylabel("y (km)")
	# Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)
    ax.xaxis.labelpad=20
    ax.yaxis.labelpad=20
    plt.show()

def PlotThule2D():
	## FIGURA 3. - 2D: Thule
	# Crea la malla para graficar:
    x,y = np.mgrid[-800e3:800e3:100j, -800e3:800e3:100j]
    z = b(y,x,R,Bc,Bl)
    plt.imshow(z,extent=[-800,800,-800,800],cmap=segmented_cmaps,vmin=-5000,vmax=2000)
    plt.colorbar()
    plt.xlabel("x (km)")
    plt.ylabel("y (km)")
    plt.show()

def PlotThule3D():
	##FIGURA 4. -3D: Thule
    x,y = np.mgrid[-800e3:800e3:100j, -800e3:800e3:100j]
    z = b(x,y,R,Bc,Bl)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax = plt.axes(projection='3d')
    ax.set_zticks([])
    plt.xlabel("x (km)")
    plt.ylabel("y (km)")
    surf=ax.plot_surface(x/1000, y/1000, z, rstride=1, cstride=1, cmap=segmented_cmaps, edgecolor='none')
	# Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=10,ticks=[-5000,-4000,-3000,-2000,-1000,0,1000,1500])
    ax.xaxis.labelpad=20
    ax.yaxis.labelpad=20
	#ax.dist = 10
	#ax.xaxis._axinfo['label']['space_factor'] = 2
    plt.show()
