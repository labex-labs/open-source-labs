# Interaction avec les matrices creuses de scipy

Enfin, nous pouvons créer un DataFrame avec des valeurs creuses à partir d'une matrice creuse de scipy, et vice versa.

```python
# Importing necessary libraries
from scipy.sparse import csr_matrix

# Creating a sparse matrix with scipy
arr = np.random.random(size=(1000, 5))
arr[arr <.9] = 0
sp_arr = csr_matrix(arr)

# Creating a DataFrame from the sparse matrix
sdf = pd.DataFrame.sparse.from_spmatrix(sp_arr)

# Printing the DataFrame
print(sdf.head())
print(sdf.dtypes)

# Converting back to sparse matrix
print(sdf.sparse.to_coo())
```
