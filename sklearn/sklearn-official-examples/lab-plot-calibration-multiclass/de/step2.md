# Anpassen und Kalibrierung

Wir trainieren einen Random Forest-Klassifikator mit 25 Basis-Schätzern (Bäumen) auf den zusammengefügten Trainings- und Validierungsdaten (1000 Proben). Dies ist der unkalibrierte Klassifikator.

```python
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=25)
clf.fit(X_train_valid, y_train_valid)
```

Um den kalibrierten Klassifikator zu trainieren, beginnen wir mit demselben Random Forest-Klassifikator, trainieren ihn jedoch nur mit der Trainingsdatensatzuntermenge (600 Proben) und kalibrieren ihn dann in einem zweistufigen Prozess mit `method='sigmoid'` unter Verwendung der Validierungsdatensatzuntermenge (400 Proben).

```python
from sklearn.calibration import CalibratedClassifierCV

clf = RandomForestClassifier(n_estimators=25)
clf.fit(X_train, y_train)
cal_clf = CalibratedClassifierCV(clf, method="sigmoid", cv="prefit")
cal_clf.fit(X_valid, y_valid)
```
