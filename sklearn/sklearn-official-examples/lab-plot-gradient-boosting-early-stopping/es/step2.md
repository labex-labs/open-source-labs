# Preparar los datos

A continuación, prepararemos los datos dividiéndolos en conjuntos de entrenamiento y prueba.

```python
for X, y in data_list:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=0
    )
```
