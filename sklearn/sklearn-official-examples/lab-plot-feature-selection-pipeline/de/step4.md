# Pipeline auswerten

Wir werden jetzt die Pipeline auf der Testuntermenge mit der `predict`-Methode auswerten. Die Pipeline wird die 3 am besten informativen Features basierend auf dem ANOVA-F-Wert auswählen, und die `LinearSVC`-Funktion wird Vorhersagen für die ausgewählten Features machen.

```python
from sklearn.metrics import classification_report

y_pred = anova_svm.predict(X_test)
print(classification_report(y_test, y_pred))
```
