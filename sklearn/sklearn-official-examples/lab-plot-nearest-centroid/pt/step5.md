# Predizer e Medir a Precisão

Prevemos as etiquetas de classe para os dados de entrada e medimos a precisão do classificador.

```python
y_pred = clf.predict(X)
print("Precisão: ", np.mean(y == y_pred))
```
