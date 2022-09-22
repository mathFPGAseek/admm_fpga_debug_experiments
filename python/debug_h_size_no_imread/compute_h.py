import numpy as np
from scipy import fft
from scipy.fftpack import next_fast_len


class ADMM_DEBUG:

    def __init__(
            self,
            psf,
            dtype=np.float32):

        #if self.dtype == np.float32 or dtype == "float32":
        self._complex_dtype = np.complex64
        self._real_dtype = np.float32

        self._psf = psf
        #self._psf = psf[:, :, :]
        self._psf_shape = np.array(self._psf.shape)
        self._n_channels = 3

        self._padded_shape = 2 * self._psf_shape[:2] - 1
        self._padded_shape = np.array([next_fast_len(i) for i in self._padded_shape])
        self._padded_shape = np.r_[self._padded_shape, [self._n_channels]]
        self._start_idx = (self._padded_shape[:2] - self._psf_shape[:2]) // 2
        self._end_idx = self._start_idx + self._psf_shape[:2]

        #debug
        self._debug = 1

    def _pad(self, v):
        """ adjoint of cropping"""
        vpad = np.zeros(self._padded_shape).astype(v.dtype)
        vpad[self._start_idx[0]: self._end_idx[0], self._start_idx[1]: self._end_idx[1]] = v
        return vpad

    def comp_h(self):
        self._H = fft.rfft2(self._pad(self._psf), axes=(0, 1), s=self._padded_shape[:2]).astype(self._complex_dtype)
        #self._H = fft.rfft2(self._pad(self._psf), axes=(0, 1), s=self._padded_shape[:2]).astype(self._real_dtype)

    def dummy_debug_diag(self):
        self._debug += self._debug
