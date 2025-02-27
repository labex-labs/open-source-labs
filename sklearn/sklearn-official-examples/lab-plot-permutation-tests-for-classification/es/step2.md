# Prueba de permutación de puntuación en los datos originales

A continuación, calculamos la `permutación_test_score` utilizando el conjunto de datos iris original y el clasificador `SVC` con la puntuación de `exactitud` para evaluar el modelo en cada ronda.

```python
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import permutation_test_score

clf = SVC(kernel="lineal", aleatorio_estado=7)
cv = StratifiedKFold(2, mezclar=True, aleatorio_estado=0)

puntuación_iris, puntuaciones_perm_iris, valor_p_iris = permutation_test_score(
    clf, X, y, puntuación="exactitud", cv=cv, n_permutaciones=1000
)
```

注：这里代码中的`aleatorio_estado`是对`random_state`不太准确的翻译，实际使用中建议保留`random_state`英文原文。
