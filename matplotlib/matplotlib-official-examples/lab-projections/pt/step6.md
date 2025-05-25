# Definir as Projeções de Perspectiva

Defina o segundo subplot para usar uma projeção de perspectiva com o `FOV` (campo de visão) padrão de 90 graus e um `focal_length` (distância focal) de 1.

```python
axs[1].set_proj_type('persp')  # FOV = 90 deg
axs[1].set_title("'persp'\nfocal_length = 1 (default)", fontsize=10)
```

Defina o terceiro subplot para usar uma projeção de perspectiva com um `FOV` (campo de visão) de 157.4 graus e um `focal_length` (distância focal) de 0.2.

```python
axs[2].set_proj_type('persp', focal_length=0.2)  # FOV = 157.4 deg
axs[2].set_title("'persp'\nfocal_length = 0.2", fontsize=10)
```
