# Schätzerparameter

Schätzerobjekte können Parameter haben, die ihr Verhalten beeinflussen. Diese Parameter können beim Instanziieren des Schätzers festgelegt oder durch Ändern des entsprechenden Attributs gesetzt werden. Legen wir einige Parameter für unseren Beispielschätzer fest:

```python
estimator = Estimator(param1=1, param2=2)
print(estimator.param1)
```

Ausgabe:

```
1
```
