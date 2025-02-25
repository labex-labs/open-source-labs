# Graficar los datos con \dfrac

Vamos a graficar los datos con la macro TeX \dfrac y mostrar la gráfica resultante.

```python
fig, ax = plt.subplots()
ax.plot(x, y, label=r'$\dfrac{sin(x)}{x}$')
ax.legend()
plt.show()
```
