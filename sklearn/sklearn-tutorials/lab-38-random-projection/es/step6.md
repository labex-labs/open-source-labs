# Verificación

Para verificar la corrección de la transformada inversa, podemos comparar los datos originales `X` con el resultado de la transformada inversa.

```python
X_new_again = transformer.transform(X_new_inversed)
np.allclose(X_new, X_new_again)
```

Aquí, aplicamos la transformación a los datos transformados inversamente `X_new_inversed` y comprobamos si es igual a los datos proyectados originales `X_new` utilizando la función `np.allclose`.
