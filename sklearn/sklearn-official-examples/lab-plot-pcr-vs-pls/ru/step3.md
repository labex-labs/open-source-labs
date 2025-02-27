# Создание регрессоров

Создадим два регрессора: PCR и PLS. Для наглядности примем количество компонентов равным 1. Перед подачей данных на этап PCA в PCR их необходимо стандартизировать, как рекомендует хороший практика. Экстремальный оценщик PLS имеет встроенные возможности масштабирования.

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
