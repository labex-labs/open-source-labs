# Bild mit L1-Penalisierung rekonstruieren

In diesem Schritt werden wir das Bild unter Verwendung von L1- (Lasso-)Penalisierung rekonstruieren.

```python
rgr_lasso = Lasso(alpha=0.001)
rgr_lasso.fit(proj_operator, proj.ravel())
rec_l1 = rgr_lasso.coef_.reshape(l, l)
```
