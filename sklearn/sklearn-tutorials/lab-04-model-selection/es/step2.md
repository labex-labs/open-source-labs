# Generadores de validación cruzada

Scikit-learn proporciona una colección de clases que se pueden utilizar para generar índices de entrenamiento/prueba para las estrategias de validación cruzada populares. Estas clases tienen un método `split` que acepta el conjunto de datos de entrada y produce los índices del conjunto de entrenamiento/prueba para cada iteración del proceso de validación cruzada.

```python
from sklearn.model_selection import KFold

# Dividir los datos en K pliegues utilizando la validación cruzada KFold
k_fold = KFold(n_splits=5)
for train_indices, test_indices in k_fold.split(X_digits):
    print(f'Tren: {train_indices} | prueba: {test_indices}')
```

La función auxiliar `cross_val_score` se puede utilizar para calcular directamente la puntuación de validación cruzada. Divide los datos en conjuntos de entrenamiento y prueba para cada iteración de la validación cruzada, entrena el estimador en el conjunto de entrenamiento y calcula la puntuación en base al conjunto de prueba.

```python
from sklearn.model_selection import cross_val_score

# Calcular la puntuación de validación cruzada para el clasificador SVM
scores = cross_val_score(svc, X_digits, y_digits, cv=k_fold, n_jobs=-1)
print(scores)
```
