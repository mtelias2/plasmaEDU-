#Code helps In playing with magnetic fields
#designed for solonoids
#written by Moutaz Elias

#importing needed libraries
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


# global variables Current loops and others done in config
import config as cfg
import roto as roto
import pltloops as pllt
import bfield as bf
import blines as bl


def main():

    figureNumber=1
    plt.figure(figureNumber)

    #plotting the current loops
    pllt.plot3D_currentloops(100,figureNumber)


    #% Grid of points for contour map of B-field isolines
    Px =    np.array([-0.1 , 0.2/45  , 0.30])
    Py =    np.array([0.001 , 0.15/40 , 0.15])
    Pz =    np.array(0.0)

    #% Contour map of B-field isolines
    Bnorm = np.zeros((Px.size,Py.size))

    for i in range(0,Px.size):
        for j in range(0,Py.size):
            P = [ Px[i], Py[j], Pz ]
            B = bf.bfield(P)
            Bnorm[i][j] = np.sqrt( B[0]*B[0] + B[1]*B[1] + B[2]*B[2] )


    plt.figure( 1)
    ax = plt.axes(projection='3d')
    ax.hold(True)
    XX,YY = np.meshgrid(Px,Py);
    ax.contour(XX,YY,np.transpose(Bnorm))
    #axis equal

    #% Fieldlines
    #% (Set: coordinates of the seed points, direction, length along 's', ds_maxstep  )
    Y0x       = np.array([ -0.1*np.ones(11),  0.1*np.ones(11),  0.1*np.ones(11),  0.3*np.ones(11)  ])
    Y0y       = np.array([  np.arange(0.0,0.03,0.003),  np.arange(0.0,0.06,0.006),  np.arange(0.0,0.06,0.006),  np.arange(0.0,0.03,0.003)])
    Y0z       = np.array([  0.0*np.ones(11),  0.0*np.ones(11),  0.0*np.ones(11),  0.0*np.ones(11)  ])
    direction = np.array([  1.0*np.ones(11),  1.0*np.ones(11), -1.0*np.ones(11), -1.0*np.ones(11)  ])
    length    = np.array([  0.4*np.ones(11),  0.3*np.ones(11),  0.3*np.ones(11),  0.4*np.ones(11)  ])
    #options   = odeset( 'maxstep', 2.0e-3 )



    for i in range(0,Y0y.shape[1]):
        for j in range(0,Y0y.shape[0]):
            Y0 = np.array([ Y0x[j][i], Y0y[j][i],Y0z[j][i],direction[j][i]])
            x=np.arange(0.0,length[j][i],2.0**(-3))
            y= odeint(bl.blines, Y0, x)

            y=np.array(np.transpose(y))
            #% plot 3D loop coil
            ax.plot3D( y[0], y[1], y[2] )
            plt.grid()
            ax.set_xlabel("X")
            ax.set_ylabel("Y")
            ax.set_zlabel("Z")


    plt.show()
    ax.hold(False)

    #% Set a view
    #view([0 0 1])

    #% Print figure on file
    #print( '-f1', '-dpdf', 'fig01' )


if __name__ == '__main__':
    main()
