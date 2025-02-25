# Interactuar con matrices dispersas de scipy

Por último, podemos crear un DataFrame con valores dispersos a partir de una matriz dispersa de scipy, y viceversa.

```python
# Importando las bibliotecas necesarias
from scipy.sparse import csr_matrix

# Creando una matriz dispersa con scipy
arr = np.random.random(size=(1000, 5))
arr[arr <.9] = 0
sp_arr = csr_matrix(arr)

# Creando un DataFrame a partir de la matriz dispersa
sdf = pd.DataFrame.sparse.from_spmatrix(sp_arr)

# Imprimiendo el DataFrame
print(sdf.head())
print(sdf.dtypes)

# Volviendo a convertir a matriz dispersa
print(sdf.sparse.to_coo())
```
