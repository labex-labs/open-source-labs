# Crear los regresores

Creamos dos regresores: PCR y PLS, y para fines de ilustración, establecemos el número de componentes en 1. Antes de alimentar los datos al paso de PCA de la PCR, los estandarizamos primero, como se recomienda por buenas prácticas. El estimador PLS tiene capacidades de escalado integradas.

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
pca = pcr.named_steps["pca"]  # recuperar el paso de PCA de la tubería

pls = PLSRegression(n_components=1)
pls.fit(X_train, y_train)
```
