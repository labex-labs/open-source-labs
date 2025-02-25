# Personalizar el histograma

En este paso, personalizaremos el histograma agregando etiquetas, título y ajustando el diseño.

```python
ax.set_xlabel('Smarts')
ax.set_ylabel('Probabilidad de densidad')
ax.set_title(r'Histograma de IQ: $\mu=100$, $\sigma=15$')
fig.tight_layout()
plt.show()
```
