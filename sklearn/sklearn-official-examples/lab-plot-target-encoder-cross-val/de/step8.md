# Auswerten der Koeffizienten des linearen Modells ohne Kreuzvalidierung

Das Ridge-Modell überanpasst sich (Overfitting), weil es im Vergleich zum informativen Merkmal mehr Gewicht auf das Merkmal mit extrem hoher Kardinalität legt. Führen Sie den folgenden Code aus, um die Koeffizienten des linearen Modells ohne Kreuzvalidierung auszuwerten:

```python
coefs_no_cv = pd.Series(
    model_no_cv.coef_, index=model_no_cv.feature_names_in_
).sort_values()
_ = coefs_no_cv.plot(kind="barh")
```
