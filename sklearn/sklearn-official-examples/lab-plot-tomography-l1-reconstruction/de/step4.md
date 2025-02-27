# Bild mit L2-Penalisierung rekonstruieren

In diesem Schritt werden wir das Bild unter Verwendung von L2- (Ridge-)Penalisierung rekonstruieren.

```python
rgr_ridge = Ridge(alpha=0.2)
rgr_ridge.fit(proj_operator, proj.ravel())
rec_l2 = rgr_ridge.coef_.reshape(l, l)
```
