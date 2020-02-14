#function dY=blines(s,y)
def blines(s,y):
    X=y[0]
    Y=y[1]
    Z=y[2]
    direction=y[3]
    B = bfield( [XY,Z])
    #Bnorm = norm(B)
    dY[0] = direction * B[0]/Bnorm
    dY[1] = direction * B[1]/Bnorm
    dY[2] = direction * B[2]/Bnorm
    dY[3] = 0.0
    return dY
