"""
Initialization and sanity checking routines
"""

# Author: Francois Role <francois.role@gmail.com>
#         Stanislas Morbieu <stanislas.morbieu@gmail.com>

# License: BSD 3 clause

import numpy as np
import scipy.sparse as sp
from sklearn.utils import check_random_state
import sys


def random_init(n_clusters, n_cols, random_state=None):
    """ Random Initialization
    """
    random_state = check_random_state(random_state)
    W_a = random_state.randint(n_clusters, size=n_cols)
    W = np.zeros((n_cols, n_clusters))
    W[np.arange(n_cols), W_a] = 1
    return W


def check_array(a) :
  if not ( type(a) == np.ndarray or type(a) == np.matrix or sp.issparse(a) ): 
    print("ERROR: The input data must be an numpy/scipy array or matrix.")
    sys.exit(0)
    
  if a.dtype.type not in (np.int8,np.int16,np.int32, np.float16,np.float32,np.float64) :
    print("ERROR: The numpy/scipy input array or matrix must be of a numeric type")
    sys.exit(0)

  if not sp.issparse(a):
    a = np.matrix(a)

    if len(np.where(~a.any(axis=0))[0]) > 0 :
       print("ERROR: Zero-valued columns in data.")
       sys.exit(0)
    if len(np.where(~a.any(axis=1))[1]) > 0 :
       print("ERROR: Zero-valued rows in data.")
       sys.exit(0)
    if (a < 0).any():
        print("ERROR: Negative values in data")
        sys.exit(0)
    if np.isnan(a).any() :
        print("ERROR: NaN in data")
        sys.exit(0)
        
def check_numbers(a, n_clusters) :
    if a.shape[0] <  n_clusters or a.shape[1] <  n_clusters:
        print("ERROR: the data matrix has not enough rows or columns")
        sys.exit(0)

def check_numbers_non_diago(a,n_row_clusters,n_col_clusters) :
    if a.shape[0] < n_row_clusters or a.shape[1] < n_col_clusters :
        print("ERROR: the data matrix has not enough rows or columns")
        sys.exit(0)

        
    
