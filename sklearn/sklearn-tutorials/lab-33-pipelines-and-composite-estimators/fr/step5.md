# FeatureUnion - Espaces de caractéristiques composites

La classe `FeatureUnion` est utilisée pour combiner plusieurs objets transformateurs en un nouveau transformateur qui combine leur sortie. Cela est utile lorsque vous voulez appliquer différentes transformations à différentes caractéristiques des données, par exemple le prétraitement du texte, des nombres à virgule flottante et des dates séparément. Les transformateurs sont appliqués en parallèle, et les matrices de caractéristiques qu'ils produisent sont concaténées côte à côte pour former une matrice plus grande. Voici un exemple :

```python
from sklearn.pipeline import FeatureUnion
from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA

estimators = [('linear_pca', PCA()), ('kernel_pca', KernelPCA())]
combined = FeatureUnion(estimators)
```
