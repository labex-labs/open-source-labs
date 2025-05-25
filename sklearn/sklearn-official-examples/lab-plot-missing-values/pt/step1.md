# Baixar Dados e Criar Conjuntos com Valores Ausentes

Primeiro, os dois conjuntos de dados são baixados. Usaremos apenas as primeiras 400 entradas do conjunto de dados de habitação da Califórnia para acelerar os cálculos. Em seguida, removeremos alguns valores para criar novas versões com dados artificialmente ausentes.

```python
import numpy as np
from sklearn.datasets import fetch_california_housing, load_diabetes

rng = np.random.RandomState(42)

X_diabetes, y_diabetes = load_diabetes(return_X_y=True)
X_california, y_california = fetch_california_housing(return_X_y=True)
X_california = X_california[:400]
y_california = y_california[:400]
X_diabetes = X_diabetes[:400]
y_diabetes = y_diabetes[:400]

def add_missing_values(X_full, y_full):
    n_samples, n_features = X_full.shape

    # Adicionar valores ausentes em 75% das linhas
    taxa_ausencia = 0.75
    n_amostras_ausentes = int(n_samples * taxa_ausencia)

    amostras_ausentes = np.zeros(n_samples, dtype=bool)
    amostras_ausentes[:n_amostras_ausentes] = True

    rng.shuffle(amostras_ausentes)
    recursos_ausentes = rng.randint(0, n_features, n_amostras_ausentes)
    X_missing = X_full.copy()
    X_missing[amostras_ausentes, recursos_ausentes] = np.nan
    y_missing = y_full.copy()

    return X_missing, y_missing

X_miss_california, y_miss_california = add_missing_values(X_california, y_california)
X_miss_diabetes, y_miss_diabetes = add_missing_values(X_diabetes, y_diabetes)
```
