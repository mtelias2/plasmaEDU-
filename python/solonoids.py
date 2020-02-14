#Code helps In playing with magnetic fields
#designed for solonoids
#written by Moutaz Elias

#importing needed libraries
import matplotlib.pyplot as plt
import numpy as np

# global variables Current loops and others done in config
import config as cfg
import roto as roto
import pltloops as pllt
import bfield as bf


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
    print(Bnorm)
    for i in range(0,Px.size):
        for j in range(0,Py.size):
            P = [ Px[i], Py[j], Pz ]
            B = bf.bfield(P)
            Bnorm[i][j] = np.sqrt( B[0]*B[0] + B[1]*B[1] + B[2]*B[3] )



#    XX,YY = meshgrid(Px,Py);
    #contour(XX',YY',Bnorm, 250)
    #axis equal

    #% Fieldlines
    #% (Set: coordinates of the seed points, direction, length along 's', ds_maxstep  )
    Y0x       = [ -0.1*ones(1,11),  0.1*ones(1,11),  0.1*ones(1,11),  0.3*ones(1,11)  ]
    Y0y       = [  np.arange(0.0,0.03,0.003),  np.arange(0.0,0.06,0.006),  np.arange(0.0,0.06,0.006),  np.arange(0.0,0.03,0.003)]
    Y0z       = [  0.0*ones(1,11),  0.0*ones(1,11),  0.0*ones(1,11),  0.0*ones(1,11)  ]
    direction = [  1.0*ones(1,11),  1.0*ones(1,11), -1.0*ones(1,11), -1.0*ones(1,11)  ]
    length    = [  0.4*ones(1,11),  0.3*ones(1,11),  0.3*ones(1,11),  0.4*ones(1,11)  ]
    #options   = odeset( 'maxstep', 2.0e-3 );
    for i in range(0,Y0y.size)
        Y0 = [ Y0x[i], Y0y[i],Y0z[i],direction[i] ]
        #s,y = ode113( @ blines, [ 0.0 length(i) ], Y0, options);
    #    plot3( y(:,1), y(:,2), y(:,3), 'k-' )
    #end



if __name__ == '__main__':
    main()





#% Set a view
#view([0 0 1])

#% Print figure on file
#print( '-f1', '-dpdf', 'fig01' )
