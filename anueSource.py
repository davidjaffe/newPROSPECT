#!/usr/bin/env python
'''
dm2 sensitivity with anue source
20210112

RPP2020 eqn 14.40 disappearance as sin^2(X) with 
X = 1.267 * dm2*L/E 
with dm2 in eV^2, L in m, E in MeV

A proposed search for a fourth neutrino with a PBq antineutrino source
 Phys.Rev.Lett. 107 (2011) 201801, 1107.2335 [hep-ex]
https://doi.org/10.1103/PhysRevLett.107.201801

Test of nonstandard neutrino properties with the BOREXINO source experiments, Eur.Phys.J.C 8 (1999) 609-617, hep-ex/9901012 [hep-ex]
https://doi.org/10.1007/s100529900031

'''
import math
import sys

import numpy

import matplotlib.pyplot as plt


class anueSource():
    def __init__(self):
        self.colors = {0:'k', 1:'b',2:'g',3:'r',4:'c',5:'m',6:'y'}
        self.points = {0:'o', 1:'s',2:'D',3:'>',4:'.',5:'<',6:'v',7:'P',8:'X'} # filled circle, square, diamond
        
        self.figdir = ''


        return
    def osc(self,L,E,dm2):
        ''' effy of coincidence time cut given average capture time'''
        X = 1.267 * dm2 * L / E
        O = math.sin(X)
        return O*O

    def main(self):
        '''

        '''
        DM2 = [0.1,1.,2.,4.,8.,16.]
        Energy = [1.5, 2., 4.]
        x = BASELINE = numpy.arange(1.,5.,0.15)
        for imark,dm2 in enumerate(DM2):
            for icol,E in enumerate(Energy):
                y = [self.osc(L,E,dm2) for L in x]
                mc = self.points[imark]+self.colors[icol]+'-'
                label = 'dm2 {:.2f} E {:.1f}'.format(dm2,E)
                plt.plot(x,y,mc,label=label)

            plt.ylim(0.,1.3)
            plt.ylabel('Baseline (m)')
            plt.legend()
            plt.show()
            

        
        return
  
if __name__ == '__main__' :
    A = anueSource()
    A.main()
