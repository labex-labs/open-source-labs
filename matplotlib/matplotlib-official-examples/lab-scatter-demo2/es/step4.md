# Crear un diagrama de dispersión

Crearemos un diagrama de dispersión con diferentes colores y tamaños de marcadores utilizando los valores calculados.

```python
fig, ax = plt.subplots()
ax.scatter(delta1[:-1], delta1[1:], c=close, s=volume, alpha=0.5)

ax.set_xlabel(r'$\Delta_i$', fontsize=15)
ax.set_ylabel(r'$\Delta_{i+1}$', fontsize=15)
ax.set_title('Volumen y cambio porcentual')

ax.grid(True)
fig.tight_layout()

plt.show()
```
