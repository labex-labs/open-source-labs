# Zugang zu Ausreißerscores

Neben der Vorhersage von Ausreißern können wir auch die Ausreißerscores für jede Beobachtung über das Attribut `negative_outlier_factor_` zugreifen. Niedrigere Ausreißerscores deuten auf eine höhere Abnormalität hin.

```python
outlier_scores = estimator.negative_outlier_factor_
print(outlier_scores)
```
