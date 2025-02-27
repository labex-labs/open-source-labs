# Lasso auf spärliche Daten anpassen

Wir passen die Lasso-Regressionsmodelle an die spärlichen Daten an, indem wir die `fit`-Funktion von Scikit-learn verwenden. Wir messen auch die Zeit für den Anpassungsprozess und drucken die Zeit für jedes Lasso-Modell aus.

```python
t0 = time()
sparse_lasso.fit(Xs_sp, y)
print(f"Sparse Lasso done in {(time() - t0):.3f}s")

t0 = time()
dense_lasso.fit(Xs, y)
print(f"Dense Lasso done in  {(time() - t0):.3f}s")
```
