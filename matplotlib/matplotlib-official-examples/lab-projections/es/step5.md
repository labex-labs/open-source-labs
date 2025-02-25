# Establecer la proyección ortográfica

Establece el primer subgráfico para que utilice una proyección ortográfica con un `FOV` de 0 grados y una `focal_length` de infinito.

```python
axs[0].set_proj_type('ortho')  # FOV = 0 deg
axs[0].set_title("'ortho'\nfocal_length = ∞", fontsize=10)
```
