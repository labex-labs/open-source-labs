# Entrenar el clasificador

Ahora podemos crear y entrenar el clasificador SGD utilizando la clase SGDClassifier de scikit-learn. Utilizaremos la función de pérdida 'hinge', que se utiliza comúnmente para clasificadores lineales.

```python
clf = SGDClassifier(loss='hinge', random_state=42)
clf.fit(X_train, y_train)
```
