# Criar um Gráfico de Contorno Simples com Rótulos

Agora que temos nossos dados, podemos criar um gráfico de contorno simples com rótulos usando cores padrão.

```python
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Simplest default with labels')
```
