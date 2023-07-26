# Interacting with scipy sparse

Lastly, we can create a DataFrame with sparse values from a scipy sparse matrix, and vice versa.

```python
# Importing necessary libraries
from scipy.sparse import csr_matrix

# Creating a sparse matrix with scipy
arr = np.random.random(size=(1000, 5))
arr[arr < .9] = 0
sp_arr = csr_matrix(arr)

# Creating a DataFrame from the sparse matrix
sdf = pd.DataFrame.sparse.from_spmatrix(sp_arr)

# Printing the DataFrame
print(sdf.head())
print(sdf.dtypes)

# Converting back to sparse matrix
print(sdf.sparse.to_coo())
```
