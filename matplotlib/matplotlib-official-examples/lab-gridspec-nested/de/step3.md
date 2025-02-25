# Inneres GridSpec erstellen

Jetzt werden wir das innere GridSpec erstellen. Wir werden die Methode `GridSpecFromSubplotSpec` verwenden, um ein 3 x 3-GridSpec zu erstellen, das ein Teilplot des äußeren GridSpecs sein wird.

```python
gs00 = gridspec.GridSpecFromSubplotSpec(3, 3, subplot_spec=gs0[0])
```
