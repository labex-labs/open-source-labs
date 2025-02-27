# Auswerten der Koeffizienten des linearen Modells mit Kreuzvalidierung

Die Koeffizienten des linearen Modells zeigen, dass der Großteil des Gewichts auf dem Merkmal in Spaltenindex 0 liegt, welches das informative Merkmal ist. Führen Sie den folgenden Code aus, um die Koeffizienten des linearen Modells mit Kreuzvalidierung auszuwerten:

```python
coefs_cv = pd.Series(
    model_with_cv[-1].coef_, index=model_with_cv[-1].feature_names_in_
).sort_values()
_ = coefs_cv.plot(kind="barh")
```
