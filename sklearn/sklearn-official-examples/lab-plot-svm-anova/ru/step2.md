# Создание конвейера

Далее создадим конвейер, состоящий из трансформера отбора признаков, масштабировщика и экземпляра SVM, которые мы объединим, чтобы получить полноценный оценщик.

```python
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectPercentile, f_classif
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

clf = Pipeline(
    [
        ("anova", SelectPercentile(f_classif)),
        ("scaler", StandardScaler()),
        ("svc", SVC(gamma="auto")),
    ]
)
```
