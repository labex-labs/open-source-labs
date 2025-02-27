# Построение конвейера

Теперь построим конвейер, состоящий из двух шагов: отбора признаков и классификации с использованием SVM. Для отбора признаков мы будем использовать функцию `SelectKBest` из Scikit-learn, а для классификации с использованием SVM — функцию `LinearSVC` из Scikit-learn. Функция `SelectKBest` выбирает `k` наиболее информативных признаков на основе метода `f_classif`, который вычисляет значение F-статистики ANOVA между каждым признаком и целевой переменной. В этом примере мы установим `k = 3`.

```python
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC

anova_filter = SelectKBest(f_classif, k=3)
clf = LinearSVC(dual="auto")
anova_svm = make_pipeline(anova_filter, clf)
```
