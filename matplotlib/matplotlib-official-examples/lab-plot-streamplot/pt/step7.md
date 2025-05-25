# Streamplot com Máscara

Nesta etapa, criaremos um streamplot com mascaramento (masking). Criaremos uma máscara e a aplicaremos ao componente `U` do nosso campo vetorial. A região mascarada será ignorada pelas linhas de fluxo (streamlines).

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
