# Construir o Pipeline

Agora, construiremos um pipeline composto por duas etapas: seleção de recursos e classificação SVM. Usaremos a função `SelectKBest` do Scikit-learn para seleção de recursos e a função `LinearSVC` do Scikit-learn para classificação SVM. A função `SelectKBest` seleciona os `k` recursos mais informativos com base no método `f_classif`, que calcula o valor F ANOVA entre cada recurso e a variável alvo. Neste exemplo, definiremos `k=3`.

```python
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC

anova_filter = SelectKBest(f_classif, k=3)
clf = LinearSVC(dual="auto")
anova_svm = make_pipeline(anova_filter, clf)
```
