# Rotulagem Avançada de Barras

Nesta etapa, mostraremos algumas coisas mais avançadas que podem ser feitas com rótulos de barras. Usaremos o mesmo gráfico de barras horizontal da etapa anterior.

```python
fig, ax = plt.subplots()

hbars = ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

# Label with given captions, custom padding and annotate options
ax.bar_label(hbars, labels=[f'±{e:.2f}' for e in error],
             padding=8, color='b', fontsize=14)
ax.set_xlim(right=16)

plt.show()
```
