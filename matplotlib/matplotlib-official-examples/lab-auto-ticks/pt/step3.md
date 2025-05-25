# Gráfico de dispersão com margem adicional

Nesta etapa, definiremos uma margem adicional em torno dos dados usando `.Axes.set_xmargin` / `.Axes.set_ymargin`, enquanto o modo autolimit_mode round_numbers ainda é respeitado.

```python
fig, ax = plt.subplots()
ax.scatter(x, y, c=x+y)
ax.set_xmargin(0.8)
plt.show()
```
