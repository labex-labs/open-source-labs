# PLSRegression

#### Anpassen des PLSRegression-Modells

Wir beginnen mit dem `PLSRegression`-Algorithmus, der eine Form der regularisierten linearen Regression ist. Wir werden das Modell an unsere Daten anpassen.

```python
pls = PLSRegression(n_components=2)
pls.fit(X, Y)
```

#### Transformation der Daten

Wir können die ursprünglichen Daten mit dem angepassten Modell transformieren. Die transformierten Daten werden eine reduzierte Dimension haben.

```python
X_transformed = pls.transform(X)
Y_transformed = pls.transform(Y)
```
