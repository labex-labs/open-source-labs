# Bewerten der Koeffizienten des linearen Modells mit Cross-Validation

Die Koeffizienten des linearen Modells zeigen, dass der Großteil des Gewichts auf dem Feature in Spaltenindex 0 liegt, das das informative Feature ist. Führen Sie den folgenden Code aus, um die Koeffizienten des linearen Modells mit Cross-Validation zu bewerten:

```python
coefs_cv = pd.Series(
    model_with_cv[-1].coef_, index=model_with_cv[-1].feature_names_in_
).sort_values()
_ = coefs_cv.plot(kind="barh")
```