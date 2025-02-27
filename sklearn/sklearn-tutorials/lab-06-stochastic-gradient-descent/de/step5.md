# Klassifikator trainieren

Jetzt können wir den SGD-Klassifikator (SGD classifier) mit der Klasse `SGDClassifier` von scikit-learn erstellen und trainieren. Wir werden die 'hinge'-Verlustfunktion (loss function) verwenden, die häufig für lineare Klassifikatoren eingesetzt wird.

```python
clf = SGDClassifier(loss='hinge', random_state=42)
clf.fit(X_train, y_train)
```
