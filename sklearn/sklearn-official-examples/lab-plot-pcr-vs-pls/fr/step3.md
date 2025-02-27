# Créer les régresseurs

Nous créons deux régresseurs : la PCR et la PLS. Pour notre illustration, nous fixons le nombre de composantes à 1. Avant d'alimenter les données dans l'étape PCA de la PCR, nous les standardisons tout d'abord, comme le recommande la bonne pratique. L'estimateur PLS dispose de capacités d'échelle intégrées.

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
pca = pcr.named_steps["pca"]  # récupérer l'étape PCA du pipeline

pls = PLSRegression(n_components=1)
pls.fit(X_train, y_train)
```
