# -*- coding:utf-8 -*-

from numpy import *
import matplotlib.pyplot as pyplot



def gauss_distribution(datain,miu , delta):
    return (exp(-(datain-miu)**2/2/delta))/sqrt(2*pi*delta)

def Rjk(alpha , gauss):
    rjk = (alpha* gauss).T / sum(alpha * gauss , axis=1)
    return rjk

def Em(datain , k , epoch):
    N = shape(datain)[0]
    alpha = zeros(k)+ [0.8 , 0.2]
    miu = zeros(k) + [50 ,20]
    delta = ones(k) + [5, 15]

    datain1 = ones((N,k) )

    for j in range(epoch):
        gauss = gauss_distribution(datain1 , miu , delta)
        rij = Rjk(alpha , gauss )
        miu = sum(rij * datain , axis=1) / sum(rij , axis=1)
        deta = sum(rij * (datain1 - miu ).T**2 , axis=1)/sum(rij , axis=1)
        alpha = sum(rij , axis=1)/N
        print 'the %d step: alpha = %s  miu = %s , delta = %s ' % (j , miu , delta , alpha)
    return  alpha , miu , delta


if __name__ == "__main__":
    datain = [-64, -48, 6, 8, 14, 16, 23, 24, 28, 29, 41, 49, 56, 60, 75]
    alpha , miu , delta = Em(datain , 2 , 60 )
    pyplot.figure(figsize=(8,5) , dpi=80)
    pyplot.subplot(111)
    pyplot.hist(datain)
    ax = pyplot.gca()
    fangda = 230
    x = xrange(-80 , 80 ,1)
