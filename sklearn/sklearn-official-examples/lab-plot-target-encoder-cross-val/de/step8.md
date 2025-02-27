# Bewerten der Koeffizienten des linearen Modells ohne Cross-Validation

Das Ridge-Modell überanpasst sich, da es dem extrem hochkardinalen Feature im Vergleich zum informativen Feature mehr Gewicht zuweist. Führen Sie den folgenden Code aus, um die Koeffizienten des linearen Modells ohne Cross-Validation zu bewerten:

```python
coefs_no_cv = pd.Series(
    model_no_cv.coef_, index=model_no_cv.feature_names_in_
).sort_values()
_ = coefs_no_cv.plot(kind="barh")
```