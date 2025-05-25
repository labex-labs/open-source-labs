# Definir a Projeção Ortográfica

Defina o primeiro subplot para usar uma projeção ortográfica com um `FOV` (campo de visão) de 0 graus e um `focal_length` (distância focal) de infinito.

```python
axs[0].set_proj_type('ortho')  # FOV = 0 deg
axs[0].set_title("'ortho'\nfocal_length = ∞", fontsize=10)
```
