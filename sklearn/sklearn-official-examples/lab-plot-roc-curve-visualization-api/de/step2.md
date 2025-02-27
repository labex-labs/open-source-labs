# Die ROC-Kurve zeichnen

Als nächstes werden wir die ROC-Kurve mit der Funktion `RocCurveDisplay.from_estimator` zeichnen. Diese Funktion nimmt den trainierten Klassifizierer, den Testdatensatz und die wahren Labels als Eingaben entgegen und gibt ein Objekt zurück, das zur Zeichnung der ROC-Kurve verwendet werden kann. Anschließend werden wir die Methode `show()` aufrufen, um das Diagramm anzuzeigen.

```python
svc_disp = RocCurveDisplay.from_estimator(svc, X_test, y_test)
svc_disp.show()
```
