# Cargar datos

Primero, cargamos el conjunto de datos de dígitos de scikit-learn. Este conjunto de datos contiene imágenes de 8x8 de dígitos del 0 al 9. Usaremos Análisis de Componentes Principales (PCA, por sus siglas en inglés) para reducir la dimensión del conjunto de datos a 15.

```python
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA

# load the digits dataset
digits = load_digits()

# reduce the dimension of the dataset to 15 using PCA
pca = PCA(n_components=15, whiten=False)
data = pca.fit_transform(digits.data)
```
