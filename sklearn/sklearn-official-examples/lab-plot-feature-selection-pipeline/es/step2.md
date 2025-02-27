# Construir la Canalización

Ahora construiremos una canalización que consta de dos pasos: selección de características y clasificación SVM. Utilizaremos la función `SelectKBest` de Scikit-learn para la selección de características y la función `LinearSVC` de Scikit-learn para la clasificación SVM. La función `SelectKBest` selecciona las `k` características más informativas basadas en el método `f_classif`, que calcula el valor F de ANOVA entre cada característica y la variable objetivo. En este ejemplo, estableceremos `k = 3`.

```python
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC

anova_filter = SelectKBest(f_classif, k=3)
clf = LinearSVC(dual="auto")
anova_svm = make_pipeline(anova_filter, clf)
```
