#!/usr/bin/env python
# -*- coding: utf-8 -*-

# write a correct test!
import sys
import unittest
import numpy as np

import pygimli as pg
from pygimli.physics import VESManager


class TestManagers(unittest.TestCase):

    def test_ERT(self, showProgress=False):
        pass

    def test_TT(self, showProgress=False):
        pass

    def test_VMD(self, showProgress=False):
        pass

    def test_VES(self, showProgress=False):
        """
        """
        thicks = [2., 10.]
        res = [100., 5., 30]
        phi = [0., 20., 0.]

        # model fails
        # thicks = [2., 6., 10.]
        # res = [100., 500., 20., 800.]
        # phi = [0., 20., 50., 0]

        synthModel = pg.cat(thicks, res)
        ab2 = np.logspace(np.log10(1.5), np.log10(100.), 25)

        mgr = VESManager(verbose=False, debug=False)
        
        if showProgress:
            mgr.verbose = True
        fig, axs = pg.plt.subplots(2, 4, figsize=(12,7))
        mgr.inv.axs = [axs[0][0], axs[1][0]]

        ### Test -- basic
        ra, err = mgr.simulate(synthModel, ab2=ab2, mn2=1.0, noiseLevel=0.01)
        mgr.exportData('synth.ves', ra, err)

        mgr.invert(ra, err, nLayers=4, lam=100, layerLimits=False,
                   showProgress=showProgress)
        mgr.fop.drawModel(ax=axs[0][0], model=synthModel, label='Synth')
        np.testing.assert_array_less(mgr.fw.chi2(), 1.0)

        ### Test -- reinit with new parameter count
        mgr.inv.axs = [axs[0][1], axs[1][1]]
        mgr.invert(ra, err, nLayers=5, layerLimits=False,
                   showProgress=showProgress)
        mgr.fop.drawModel(ax=axs[0][1], model=synthModel, label='Synth')
        # axs[0][1].legend()
        np.testing.assert_array_less(mgr.inv.inv.chi2(), 1)

        ### Test -- reinit with new data basis
        ab2_2 = np.logspace(np.log10(1.5), np.log10(50.), 10)
        ra, err = mgr.simulate(synthModel, ab2=ab2_2, mn2=1.0, noiseLevel=0.01)

        mgr.inv.axs = [axs[0][2], axs[1][2]]
        mgr.invert(ra, err, nLayers=4, ab2=ab2_2, mn2=1.0, layerLimits=False,
                    showProgress=showProgress)
        mgr.fop.drawModel(ax=axs[0][2], model=synthModel, label='Synth')
        # axs[0][2].legend()
        np.testing.assert_array_less(mgr.inv.inv.chi2(), 1)

        ### Test -- reinit with complex resistivies
        mgr.complex = True
        synthModel =  pg.cat(synthModel, phi)

        ra, err = mgr.simulate(synthModel, ab2=ab2, mn2=1.0, noiseLevel=0.01)

        mgr.inv.axs = [axs[0][3], axs[1][3]]
        mgr.invert(ra, err, layerLimits=False,
                showProgress=showProgress)

        np.testing.assert_array_less(mgr.inv.inv.chi2(), 1)

        if showProgress:
            print("test done")
            pg.wait()


if __name__ == '__main__':
    if len(sys.argv) > 1:

        test = TestManagers()
        test.test_VES(showProgress=True)
    else:       
        unittest.main()
