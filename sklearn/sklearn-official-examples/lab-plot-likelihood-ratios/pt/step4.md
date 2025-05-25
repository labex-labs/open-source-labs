# Invariância em Relação à Prevalência

Vamos mostrar que as razões de verossimilhança das classes são independentes da prevalência da doença e podem ser extrapoladas entre populações, independentemente de qualquer possível desequilíbrio de classes.

## Preparando os Dados

Vamos gerar um conjunto de dados sintético usando a função `make_classification` do scikit-learn. Este conjunto de dados simulará uma população com uma minoria de indivíduos portadores de uma doença.

```python
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=10_000, weights=[0.9, 0.1], random_state=0)
print(f"Porcentagem de pessoas portadoras da doença: {100*y.mean():.2f}%")
```

## Análise Pré-teste vs. Pós-teste

Ajustaremos um modelo de regressão logística aos dados e avaliaremos seu desempenho em um conjunto de teste separado. Calcularemos a razão de verossimilhança positiva para avaliar a utilidade deste classificador como ferramenta de diagnóstico de doenças.

```python
from sklearn.model_selection import train_test_split
from sklearn.metrics import class_likelihood_ratios
from sklearn.linear_model import LogisticRegression

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

estimator = LogisticRegression().fit(X_train, y_train)
y_pred = estimator.predict(X_test)
pos_LR, neg_LR = class_likelihood_ratios(y_test, y_pred)

print(f"LR+: {pos_LR:.3f}")
```

## Validação Cruzada das Razões de Verossimilhança

Avaliaremos a variabilidade das medidas das razões de verossimilhança das classes em alguns casos específicos usando validação cruzada.

```python
import pandas as pd
from sklearn.model_selection import cross_validate
from sklearn.dummy import DummyClassifier

def scoring(estimator, X, y):
    y_pred = estimator.predict(X)
    pos_lr, neg_lr = class_likelihood_ratios(y, y_pred, raise_warning=False)
    return {"positive_likelihood_ratio": pos_lr, "negative_likelihood_ratio": neg_lr}

def extract_score(cv_results):
    lr = pd.DataFrame(
        {
            "positive": cv_results["test_positive_likelihood_ratio"],
            "negative": cv_results["test_negative_likelihood_ratio"],
        }
    )
    return lr.aggregate(["mean", "std"])

estimator = LogisticRegression()
extract_score(cross_validate(estimator, X, y, scoring=scoring, cv=10))

estimator = DummyClassifier(strategy="stratified", random_state=1234)
extract_score(cross_validate(estimator, X, y, scoring=scoring, cv=10))

estimator = DummyClassifier(strategy="most_frequent")
extract_score(cross_validate(estimator, X, y, scoring=scoring, cv=10))
```

## Invariância em Relação à Prevalência

Vamos mostrar que as razões de verossimilhança das classes são independentes da prevalência da doença e podem ser extrapoladas entre populações, independentemente de qualquer possível desequilíbrio de classes.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.inspection import DecisionBoundaryDisplay
from collections import defaultdict

# ... (restante do código Python)
```
