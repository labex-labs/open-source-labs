# Isotone und lineare Regressionsmodelle anpassen

Wir werden nun sowohl das isotone als auch das lineare Regressionsmodell an die generierten Daten anpassen.

```python
ir = IsotonicRegression(out_of_bounds="clip")
y_ = ir.fit_transform(x, y)

lr = LinearRegression()
lr.fit(x[:, np.newaxis], y)  # x muss 2d für LinearRegression sein
```
