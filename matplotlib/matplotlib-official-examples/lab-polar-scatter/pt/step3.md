# Criar um gráfico de dispersão em um eixo polar

Criaremos um gráfico de dispersão em um eixo polar usando a função `plt.scatter()`. Definiremos o parâmetro `projection` como `'polar'` e passaremos os valores de raio, ângulo, cor e área como parâmetros.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
```
