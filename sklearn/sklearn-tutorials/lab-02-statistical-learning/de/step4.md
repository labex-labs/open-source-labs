# Das Anpassen von Daten

Die Haupt-API, die von scikit-learn implementiert wird, ist die `fit`-Methode eines Schätzerobjekts. Sie nimmt einen Datensatz (gewöhnlich ein 2D-Array) als Eingabe entgegen. Um Daten mit einem Schätzer anzupassen, können wir die `fit`-Methode aufrufen:

```python
estimator.fit(data)
```
