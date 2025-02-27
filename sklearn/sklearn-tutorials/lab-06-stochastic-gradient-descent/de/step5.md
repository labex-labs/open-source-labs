# Klassifizierer trainieren

Jetzt können wir den SGD-Klassifizierer mit der SGDClassifier-Klasse aus scikit-learn erstellen und trainieren. Wir werden die Verlustfunktion 'hinge' verwenden, die üblicherweise für lineare Klassifizierer verwendet wird.

```python
clf = SGDClassifier(loss='hinge', random_state=42)
clf.fit(X_train, y_train)
```