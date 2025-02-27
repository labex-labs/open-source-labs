# Обучение случайного леса и построение кривой ROC

В этом шаге мы обучим классификатор случайного леса и построим его кривую ROC рядом с кривой ROC для SVC. Для этого мы создадим новый объект `RandomForestClassifier`, обучим его на тренировочных данных, а затем создадим новый объект `RocCurveDisplay` с использованием этого классификатора. Мы также передадим параметр `ax` в эту функцию, чтобы построить кривые на одной оси. Наконец, мы вызовем метод `plot()` объекта `svc_disp`, чтобы построить кривую ROC для SVC.

```python
from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=10, random_state=42)
rfc.fit(X_train, y_train)

ax = plt.gca()
rfc_disp = RocCurveDisplay.from_estimator(rfc, X_test, y_test, ax=ax, alpha=0.8)
svc_disp.plot(ax=ax, alpha=0.8)
plt.show()
```
