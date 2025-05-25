# Criar um gráfico de dispersão em um eixo polar confinado a um setor

Podemos criar um gráfico de dispersão em um eixo polar confinado a um setor definindo os métodos `set_thetamin()` e `set_thetamax()` do objeto `PolarAxes`. Definiremos os limites theta inicial e final como `45` e `135`, respectivamente.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

ax.set_thetamin(45)
ax.set_thetamax(135)
```
