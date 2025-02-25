# Die perspektivischen Projektionen einstellen

Stellen Sie die zweite Teilfigur so ein, dass sie eine perspektivische Projektion mit der standardmäßigen `FOV` von 90 Grad und einer `Brennweite` von 1 verwendet.

```python
axs[1].set_proj_type('persp')  # FOV = 90 deg
axs[1].set_title("'persp'\nfocal_length = 1 (default)", fontsize=10)
```

Stellen Sie die dritte Teilfigur so ein, dass sie eine perspektivische Projektion mit einer `FOV` von 157,4 Grad und einer `Brennweite` von 0,2 verwendet.

```python
axs[2].set_proj_type('persp', focal_length=0.2)  # FOV = 157.4 deg
axs[2].set_title("'persp'\nfocal_length = 0.2", fontsize=10)
```
