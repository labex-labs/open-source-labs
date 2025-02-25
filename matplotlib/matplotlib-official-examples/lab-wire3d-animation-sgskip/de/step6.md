# Die durchschnittliche FPS anzeigen

Der sechste Schritt besteht darin, die durchschnittlichen Bilder pro Sekunde (Frames per Second, FPS) mithilfe der gesamten Zeit anzuzeigen, die das Ausführen der Animation gedauert hat.

```python
print('Average FPS: %f' % (100 / (time.time() - tstart)))
```
