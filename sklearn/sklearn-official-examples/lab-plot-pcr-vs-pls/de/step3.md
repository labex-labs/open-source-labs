# Erstelle die Regressoren

Wir erstellen zwei Regressoren: PCR und PLS. Und zu illustrativen Zwecken setzen wir die Anzahl der Komponenten auf 1. Bevor wir die Daten der PCA-Schritt des PCR zuführen, standardisieren wir sie zunächst, wie es die gute Praxis empfiehlt. Der PLS-Schätzer hat integrierte Skalierungsfähigkeiten.

```python
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cross_decomposition import PLSRegression

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=rng)

pcr = make_pipeline(StandardScaler(), PCA(n_components=1), LinearRegression())
pcr.fit(X_train, y_train)
pca = pcr.named_steps["pca"]  # retrieve the PCA step of the pipeline

pls = PLSRegression(n_components=1)
pls.fit(X_train, y_train)
```
