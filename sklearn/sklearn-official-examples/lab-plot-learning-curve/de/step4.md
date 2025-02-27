# Analysiere die Lernkurven

```python
# Interpret the learning curves
```

Wir können die Lernkurve des Naiven Bayes-Klassifikators analysieren. Ihre Form kann in komplexeren Datensätzen sehr häufig gefunden werden: Die Trainingsgenauigkeit ist sehr hoch, wenn nur wenige Proben zum Training verwendet werden, und sinkt, wenn die Anzahl der Proben erhöht wird, während die Testgenauigkeit am Anfang sehr niedrig ist und dann steigt, wenn Proben hinzugefügt werden. Die Trainings- und Testgenauigkeiten werden realistischer, wenn alle Proben zum Training verwendet werden.

Wir sehen eine andere typische Lernkurve für den SVM-Klassifikator mit RBF-Kern. Die Trainingsgenauigkeit bleibt hoch, unabhängig von der Größe des Trainingssatzes. Andererseits steigt die Testgenauigkeit mit der Größe des Trainingsdatensatzes. Tatsächlich steigt sie bis zu einem Punkt, an dem sie einen Plateau erreicht. Das Beobachten eines solchen Plateaus deutet darauf hin, dass es möglicherweise nicht nützlich ist, neue Daten zum Trainieren des Modells zu erwerben, da die Generalisierungskapazität des Modells nicht mehr zunehmen wird.
