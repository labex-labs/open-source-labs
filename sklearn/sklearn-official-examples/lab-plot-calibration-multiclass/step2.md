# Fitting and Calibration

We train a random forest classifier with 25 base estimators (trees) on the concatenated train and validation data (1000 samples). This is the uncalibrated classifier.

```python
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=25)
clf.fit(X_train_valid, y_train_valid)
```

To train the calibrated classifier, we start with the same random forest classifier but train it using only the train data subset (600 samples) then calibrate, with `method='sigmoid'`, using the valid data subset (400 samples) in a 2-stage process.

```python
from sklearn.calibration import CalibratedClassifierCV

clf = RandomForestClassifier(n_estimators=25)
clf.fit(X_train, y_train)
cal_clf = CalibratedClassifierCV(clf, method="sigmoid", cv="prefit")
cal_clf.fit(X_valid, y_valid)
```
