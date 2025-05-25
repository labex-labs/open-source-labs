# Plotando os Dados com \dfrac

Plotaremos os dados com a macro TeX \dfrac e exibiremos o gráfico resultante.

```python
fig, ax = plt.subplots()
ax.plot(x, y, label=r'$\dfrac{sin(x)}{x}$')
ax.legend()
plt.show()
```
