# FeatureUnion - Композитные пространства признаков

Класс `FeatureUnion` используется для объединения нескольких объектов трансформеров в новый трансформер, который объединяет их выход. Это полезно, когда вы хотите применить разные преобразования к разным признакам данных, например, предобрабатывать текст, вещественные числа и даты отдельно. Трансформеры применяются параллельно, и матрицы признаков, которые они выводят, конкатенируются рядом в одну большую матрицу. Вот пример:

```python
from sklearn.pipeline import FeatureUnion
from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA

estimators = [('linear_pca', PCA()), ('kernel_pca', KernelPCA())]
combined = FeatureUnion(estimators)
```
