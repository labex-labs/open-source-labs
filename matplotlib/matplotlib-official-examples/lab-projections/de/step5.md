# Die orthogonale Projektion einstellen

Stellen Sie die erste Teilfigur so ein, dass sie eine orthogonale Projektion mit einem `FOV` von 0 Grad und einer `Brennweite` von unendlich verwendet.

```python
axs[0].set_proj_type('ortho')  # FOV = 0 deg
axs[0].set_title("'ortho'\nfocal_length = ∞", fontsize=10)
```
