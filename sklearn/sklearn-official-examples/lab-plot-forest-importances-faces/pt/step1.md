# Carregar os dados e ajuste do modelo

Começamos carregando o conjunto de dados Olivetti Faces e limitando o conjunto de dados para conter apenas as cinco primeiras classes. Em seguida, treinamos uma floresta aleatória no conjunto de dados e avaliamos a importância das características baseada na impureza. Definiremos o número de núcleos a utilizar para as tarefas.

```python
from sklearn.datasets import fetch_olivetti_faces

# Selecionamos o número de núcleos a utilizar para o ajuste paralelo do modelo de floresta. `-1` significa utilizar todos os núcleos disponíveis.
n_jobs = -1

# Carregar o conjunto de dados de rostos
data = fetch_olivetti_faces()
X, y = data.data, data.target

# Limitar o conjunto de dados a 5 classes.
mask = y < 5
X = X[mask]
y = y[mask]

# Um classificador de floresta aleatória será ajustado para calcular as importâncias das características.
from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier(n_estimators=750, n_jobs=n_jobs, random_state=42)

forest.fit(X, y)
```
