""" Apply compute_h"""

from compute_h import ADMM_DEBUG
#from io import load_image
import numpy as np

def debug_compute_h(
psf,

**kwargs
):

    # psf = load_image(psf)

    # Instantiate object

    inst_debug = ADMM_DEBUG(psf)

    # Compute h
    test = inst_debug.comp_h()
    test2 = inst_debug.dummy_debug_diag()

    debug = 1

if __name__ == "__main__":

 row = 380
 col = 507
 planes = 3
 #psf_fp = "C:/design/data/psf/tape_rgb.png"
 psf_in = np.random.rand(row,col,3)


 debug_compute_h(psf_in)
 debug = 1