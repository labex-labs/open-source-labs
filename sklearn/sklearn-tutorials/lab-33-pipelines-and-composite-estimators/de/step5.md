# FeatureUnion - Zusammengesetzte Merkmalsräume

Die `FeatureUnion`-Klasse wird verwendet, um mehrere Transformatorobjekte zu einem neuen Transformator zu kombinieren, der ihre Ausgabe zusammenfasst. Dies ist nützlich, wenn Sie verschiedene Transformationen auf verschiedene Merkmale der Daten anwenden möchten, z. B. die Text-, Float- und Datumsvorverarbeitung separat durchführen. Die Transformatoren werden parallel angewendet, und die von ihnen ausgegebenen Merkmalsmatrizen werden nebeneinander zu einer größeren Matrix zusammengefügt. Hier ist ein Beispiel:

```python
from sklearn.pipeline import FeatureUnion
from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA

estimators = [('linear_pca', PCA()), ('kernel_pca', KernelPCA())]
combined = FeatureUnion(estimators)
```
