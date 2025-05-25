# Calcular a informação mútua

Agora, calcularemos a pontuação da informação mútua para cada característica. A informação mútua pode capturar qualquer tipo de dependência entre as variáveis. Normalizaremos as pontuações da informação mútua dividindo-as pela pontuação máxima da informação mútua.

```python
mi = mutual_info_regression(X, y)
mi /= np.max(mi)
```
