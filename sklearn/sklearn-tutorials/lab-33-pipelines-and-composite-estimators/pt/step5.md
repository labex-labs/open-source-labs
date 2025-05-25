# FeatureUnion - Espaços de Recursos Compostos

A classe `FeatureUnion` é usada para combinar múltiplos objetos transformadores num novo transformador que combina as suas saídas. Isto é útil quando se pretende aplicar diferentes transformações a diferentes características dos dados, como pré-processar texto, números flutuantes e datas separadamente. Os transformadores são aplicados em paralelo, e as matrizes de características que produzem são concatenadas lado a lado numa matriz maior. Aqui está um exemplo:

```python
from sklearn.pipeline import FeatureUnion
from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA

estimators = [('linear_pca', PCA()), ('kernel_pca', KernelPCA())]
combined = FeatureUnion(estimators)
```
