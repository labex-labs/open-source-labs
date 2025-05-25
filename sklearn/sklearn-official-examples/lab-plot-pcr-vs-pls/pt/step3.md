# Criar os Regressores

Criamos dois regressores: PCR e PLS, e, para fins ilustrativos, definimos o número de componentes como 1. Antes de alimentar os dados para a etapa PCA do PCR, primeiro os padronizamos, conforme recomendado pelas boas práticas. O estimador PLS possui recursos de escalonamento embutidos.

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
pca = pcr.named_steps["pca"]  # recuperar a etapa PCA do pipeline

pls = PLSRegression(n_components=1)
pls.fit(X_train, y_train)
```
