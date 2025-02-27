# Generar datos

Generaremos un conjunto de datos sintético con solo 3 características informativas. No barajaremos explícitamente el conjunto de datos para asegurarnos de que las características informativas correspondan a las tres primeras columnas de X. Además, dividiremos nuestro conjunto de datos en subconjuntos de entrenamiento y prueba.

```python
X, y = make_classification(
    n_samples=1000,
    n_features=10,
    n_informative=3,
    n_redundant=0,
    n_repeated=0,
    n_classes=2,
    random_state=0,
    shuffle=False,
)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
```
