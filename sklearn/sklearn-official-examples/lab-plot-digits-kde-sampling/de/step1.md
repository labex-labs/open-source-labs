# Daten laden

Zunächst laden wir den Digits-Datensatz aus scikit-learn. Dieser Datensatz enthält 8x8-Bilder von Ziffern von 0 bis 9. Wir werden die Hauptkomponentenanalyse (Principal Component Analysis, PCA) verwenden, um die Dimension des Datensatzes auf 15 zu reduzieren.

```python
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA

# ladet den Digits-Datensatz
digits = load_digits()

# reduziert die Dimension des Datensatzes auf 15 mit PCA
pca = PCA(n_components=15, whiten=False)
data = pca.fit_transform(digits.data)
```
