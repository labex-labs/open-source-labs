# Определение классификаторов

Мы определим два различных классификатора, чтобы сравнить их статистическую производительность по разным порогам с использованием кривых ROC и DET. Мы будем использовать функцию `make_pipeline` из scikit - learn для создания конвейера, который масштабирует данные с использованием `StandardScaler` и обучает классификатор `LinearSVC`. Мы также будем использовать класс `RandomForestClassifier` из scikit - learn для обучения случайного леса с максимальной глубиной 5, 10 оценщиками и максимумом 1 признака.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC

classifiers = {
    "Linear SVM": make_pipeline(StandardScaler(), LinearSVC(C=0.025, dual="auto")),
    "Random Forest": RandomForestClassifier(
        max_depth=5, n_estimators=10, max_features=1
    ),
}
```
