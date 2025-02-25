# Establecer las proyecciones perspectivas

Establece el segundo subgráfico para que utilice una proyección perspectiva con el `FOV` predeterminado de 90 grados y una `focal_length` de 1.

```python
axs[1].set_proj_type('persp')  # FOV = 90 deg
axs[1].set_title("'persp'\nfocal_length = 1 (default)", fontsize=10)
```

Establece el tercer subgráfico para que utilice una proyección perspectiva con un `FOV` de 157.4 grados y una `focal_length` de 0.2.

```python
axs[2].set_proj_type('persp', focal_length=0.2)  # FOV = 157.4 deg
axs[2].set_title("'persp'\nfocal_length = 0.2", fontsize=10)
```
