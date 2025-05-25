# Personalizar o histograma

Nesta etapa, personalizaremos o histograma adicionando rótulos, título e ajustando o layout.

```python
ax.set_xlabel('Smarts')
ax.set_ylabel('Probability density')
ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')
fig.tight_layout()
plt.show()
```
