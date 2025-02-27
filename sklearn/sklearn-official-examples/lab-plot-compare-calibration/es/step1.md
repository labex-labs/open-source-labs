# Importar bibliotecas y generar conjunto de datos

Comenzamos importando las bibliotecas necesarias y generando un conjunto de datos de clasificación binaria sintético con 100.000 muestras y 20 características. De las 20 características, solo 2 son informativas, 2 son redundantes y las 16 restantes son no informativas. De las 100.000 muestras, 100 se utilizarán para ajustar el modelo y el resto para la prueba.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Generate dataset
X, y = make_classification(
    n_samples=100_000, n_features=20, n_informative=2, n_redundant=2, random_state=42
)

train_samples = 100  # Samples used for training the models
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    shuffle=False,
    test_size=100_000 - train_samples
)
```
