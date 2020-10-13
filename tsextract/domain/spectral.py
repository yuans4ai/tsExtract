#https://www.researchgate.net/figure/Spectral-Statistical-and-Temporal-Domain-Features-used-in-the-present-work-1-Features_fig6_301683665
#https://gist.github.com/endolith/359724/aa7fcc043776f16f126a0ccd12b599499509c3cc

import statsmodels.api as sm
import numpy as np

class spectral:

    def __init__(self):
        self.axis = 1

    def spectral_centroid(data):
        def _spectral(row):
            spectrum = abs(rfft(row))
            normalized_spectrum = spectrum / sum(spectrum)
            normalized_frequencies = linspace(0, 1, len(spectrum))
            return(sum(normalized_frequencies * normalized_spectrum))

        return(np.apply_along_axis(_spectral, data))
