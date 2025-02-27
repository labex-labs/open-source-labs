# Factorización de Matriz No Negativa (NMF)

#### NMF con la norma de Frobenius

La Factorización de Matriz No Negativa (NMF, por sus siglas en inglés) es un enfoque alternativo para la descomposición que asume datos y componentes no negativos. Encuentra una descomposición de los datos en dos matrices de elementos no negativos optimizando la distancia entre los datos y el producto matricial de las dos matrices. La NMF se puede implementar utilizando la clase `NMF` de scikit-learn.

```python
from sklearn.decomposition import NMF

# Crea un objeto NMF con n_components como el número de componentes deseados
nmf = NMF(n_components=2)

# Ajusta el modelo NMF a los datos
nmf.fit(data)

# Descompone los datos en las dos matrices no negativas
matrix_W = nmf.transform(data)
matrix_H = nmf.components_
```
