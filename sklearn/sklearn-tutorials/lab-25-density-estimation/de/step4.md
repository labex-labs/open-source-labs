# Die Proben bewerten

Nachdem wir den Schätzer angepasst haben, können wir die `score_samples`-Methode verwenden, um die Log-Wahrscheinlichkeit der Proben unter der geschätzten Dichtefunktion zu berechnen. Dies wird uns einen Maßstab geben, wie wahrscheinlich jede Probe gemäß der Dichteschätzung ist.

```python
scores = kde.score_samples(X)
```
