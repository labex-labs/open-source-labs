# Kernels

Los kernels son medidas de similitud entre dos objetos. Se pueden utilizar en varios algoritmos de aprendizaje automático para capturar relaciones no lineales entre las características.

Scikit-learn proporciona diferentes funciones de kernel, como el kernel lineal, el kernel polinomial, el kernel sigmoide, el kernel RBF, el kernel Laplaciano y el kernel chi-cuadrado.

Calculemos los kernels entre pares de dos conjuntos de muestras utilizando la función `pairwise_kernels`:

```python
from sklearn.metrics.pairwise import pairwise_kernels

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Calculate pairwise kernels between X and Y using linear kernel
kernels = pairwise_kernels(X, Y, metric='linear')
print(kernels)
```

Salida:

```
array([[ 2.,  7.],
       [ 3., 11.],
       [ 5., 18.]])
```
