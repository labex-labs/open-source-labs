# Avaliar o Modelo

Avaliaremos o desempenho de classificação do modelo GPC treinado. Geraremos uma grade de pontos e calcularemos as probabilidades previstas para cada ponto usando o modelo treinado.

```python
# Avaliar a função real e a probabilidade prevista
res = 50
x1, x2 = np.meshgrid(np.linspace(-lim, lim, res), np.linspace(-lim, lim, res))
xx = np.vstack([x1.reshape(x1.size), x2.reshape(x2.size)]).T

y_true = g(xx)
y_prob = gp.predict_proba(xx)[:, 1]
y_true = y_true.reshape((res, res))
y_prob = y_prob.reshape((res, res))
```
