# Vergleiche die Koeffizienten von Dense Lasso und Sparse Lasso

Wir vergleichen die Koeffizienten des dichten Lasso-Modells und des spärlichen Lasso-Modells, um sicherzustellen, dass sie die gleichen Ergebnisse liefern. Wir berechnen die euklidische Norm der Differenz zwischen den Koeffizienten.

```python
coeff_diff = linalg.norm(sparse_lasso.coef_ - dense_lasso.coef_)
print(f"Distance between coefficients : {coeff_diff:.2e}")
```
