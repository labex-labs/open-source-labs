# Dataset

Usaremos un conjunto de datos de clasificación binaria sintético con 100.000 muestras y 20 características. De las 20 características, solo 2 son informativas, 10 son redundantes (combinaciones aleatorias de las características informativas) y las 8 restantes son no informativas (números aleatorios). De las 100.000 muestras, 1.000 se usarán para ajustar el modelo y el resto para la prueba.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_samples=100_000, n_features=20, n_informative=2, n_redundant=10, random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.99, random_state=42
)
```
