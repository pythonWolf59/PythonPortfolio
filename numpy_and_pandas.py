# We will learn numpy and pandas

import string
import numpy as np
import pandas as pd

array1 = np.array([2,3,4,5])
print(array1)

array2d = np.array([[2,3],[3,4]])
print(array2d)

#using core ndarray function
n_dim_array = np.ndarray(shape=(13,2), dtype='<U1') #U => unicode , 1 => 1 charcter as a value

# Fill the array with the alphabets 'a' to 'z'
alphabets = list(string.ascii_lowercase)  # Get a list of alphabets ['a', 'b', ..., 'z']

# Now assign the alphabets to the ndarray
n_dim_array[:] = np.array(alphabets).reshape(n_dim_array.shape)

print(n_dim_array)