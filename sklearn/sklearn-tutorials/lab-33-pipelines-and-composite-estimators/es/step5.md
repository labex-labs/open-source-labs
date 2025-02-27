# FeatureUnion - Espacios de Características Compuestas

La clase `FeatureUnion` se utiliza para combinar múltiples objetos transformadores en un nuevo transformador que combina su salida. Esto es útil cuando desea aplicar diferentes transformaciones a diferentes características de los datos, como preprocesar texto, números de punto flotante y fechas por separado. Los transformadores se aplican en paralelo, y las matrices de características que generan se concatenan lado a lado en una matriz más grande. Aquí hay un ejemplo:

```python
from sklearn.pipeline import FeatureUnion
from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA

estimators = [('linear_pca', PCA()), ('kernel_pca', KernelPCA())]
combined = FeatureUnion(estimators)
```
