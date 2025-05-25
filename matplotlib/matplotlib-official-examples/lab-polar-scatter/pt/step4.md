# Criar um gráfico de dispersão em um eixo polar com origem deslocada

Podemos criar um gráfico de dispersão em um eixo polar com uma origem deslocada definindo os métodos `set_rorigin()` e `set_theta_zero_location()` do objeto `PolarAxes`. Definiremos o raio da origem como `-2.5` e a localização theta zero como `'W'` com um deslocamento de `10`.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

ax.set_rorigin(-2.5)
ax.set_theta_zero_location('W', offset=10)
```
