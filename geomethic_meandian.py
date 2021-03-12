from scipy.stats.mstats import gmean
import numpy as np

def get_centers(a,tol=0.00001):
    a = np.array(a)
    result = False
    if len(a)==3:
        if np.abs(a[0]-a[1])<=tol and np.abs(a[0]-a[2])<=tol and np.abs(a[2]-a[1])<=tol:
            result=True
    print([np.mean(a),np.median(a),gmean(a)])
    if result:
        return a[0]
    return get_centers([np.mean(a),np.median(a),gmean(a)])
