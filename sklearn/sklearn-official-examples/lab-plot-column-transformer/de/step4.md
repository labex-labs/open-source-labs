# Training und Testing

Wir werden unsere Pipeline auf den Trainingsdaten anpassen und sie verwenden, um Themen für `X_test` vorherzusagen. Anschließend werden die Leistungsmesswerte unserer Pipeline ausgegeben.

```python
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print("Classification report:\n\n{}".format(classification_report(y_test, y_pred)))
```
