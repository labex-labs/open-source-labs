# Gráfico de flujo con enmascaramiento

En este paso, crearemos un gráfico de flujo con enmascaramiento. Crearemos una máscara y la aplicaremos al componente `U` de nuestro campo vectorial. La región enmascarada será omitida por las líneas de corriente.

```python
mask = np.zeros(U.shape, dtype=bool)
mask[40:60, 40:60] = True
U[:20, :20] = np.nan
U = np.ma.array(U, mask=mask)

plt.streamplot(X, Y, U, V, color='r')
plt.title('Streamplot with Masking')
plt.imshow(~mask, extent=(-w, w, -w, w), alpha=0.5, cmap='gray', aspect='auto')
plt.gca().set_aspect('equal')
plt.show()
```
