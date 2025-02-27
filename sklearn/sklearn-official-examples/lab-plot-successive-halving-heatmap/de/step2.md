# Führen Sie das Grid Search durch

Wir werden Grid Search verwenden, um eine Parameter-Suche auf dem SVC-Modell durchzuführen. Wir werden den generierten synthetischen Datensatz und das in Schritt 1 generierte Parameter-Gitter verwenden.

```python
tic = time()
gs = GridSearchCV(estimator=clf, param_grid=param_grid)
gs.fit(X, y)
gs_time = time() - tic
```
