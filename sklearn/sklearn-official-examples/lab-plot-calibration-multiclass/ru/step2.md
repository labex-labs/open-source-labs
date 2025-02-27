# Обучение и калибровка

Мы обучаем классификатор случайного леса с 25 базовыми оценщиками (деревьями) на объединенных обучающих и валидационных данных (1000 образцов). Это классификатор без калибровки.

```python
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=25)
clf.fit(X_train_valid, y_train_valid)
```

Для обучения классификатора с калибровкой мы начинаем с того же классификатора случайного леса, но обучаем его только на подмножестве обучающих данных (600 образцов), а затем калибрируем с использованием `method='sigmoid'` на подмножестве валидационных данных (400 образцов) в двухэтапном процессе.

```python
from sklearn.calibration import CalibratedClassifierCV

clf = RandomForestClassifier(n_estimators=25)
clf.fit(X_train, y_train)
cal_clf = CalibratedClassifierCV(clf, method="sigmoid", cv="prefit")
cal_clf.fit(X_valid, y_valid)
```
