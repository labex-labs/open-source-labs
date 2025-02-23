# Diagrama de dispersión con un margen adicional

En este paso, estableceremos un margen adicional alrededor de los datos utilizando `.Axes.set_xmargin` / `.Axes.set_ymargin` mientras que todavía se respeta el modo de autolimitación de números redondeados.

```python
fig, ax = plt.subplots()
ax.scatter(x, y, c=x+y)
ax.set_xmargin(0.8)
plt.show()
```
