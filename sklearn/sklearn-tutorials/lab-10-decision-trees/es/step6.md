# Evaluar el modelo

Finalmente, podemos evaluar la precisión de nuestro modelo comparando los valores predichos con los valores reales.

```python
# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)

# Imprimir la precisión
print("Precisión:", accuracy)
```
