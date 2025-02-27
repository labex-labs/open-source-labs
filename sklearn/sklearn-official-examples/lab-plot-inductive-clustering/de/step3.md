# Neue Proben generieren

In diesem Schritt werden wir neue Proben generieren und sie zusammen mit dem ursprünglichen Datensatz plotten. Wir werden die Funktion `make_blobs` erneut verwenden, um 10 neue Proben zu generieren.

```python
X_new, y_new = make_blobs(
    n_samples=10, centers=[(-7, -1), (-2, 4), (3, 6)], random_state=42
)
```
