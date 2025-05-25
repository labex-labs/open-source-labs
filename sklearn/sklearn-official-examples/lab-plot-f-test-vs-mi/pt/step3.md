# Calcular o teste F

Agora, calcularemos a pontuação do teste F para cada característica. O teste F captura apenas a dependência linear entre as variáveis. Normalizaremos as pontuações do teste F dividindo-as pela pontuação máxima do teste F.

```python
f_test, _ = f_regression(X, y)
f_test /= np.max(f_test)
```
