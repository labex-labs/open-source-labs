# Pipeline trainieren

Wir werden jetzt die Pipeline auf der Trainingsuntermenge mit der `fit`-Methode trainieren. Während des Trainings wird die `SelectKBest`-Funktion die 3 am besten informativen Features basierend auf dem ANOVA-F-Wert auswählen, und die `LinearSVC`-Funktion wird einen linearen SVM-Klassifikator auf den ausgewählten Features trainieren.

```python
anova_svm.fit(X_train, y_train)
```
