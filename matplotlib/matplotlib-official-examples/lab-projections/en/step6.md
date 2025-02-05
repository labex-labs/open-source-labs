# Set the Perspective Projections

Set the second subplot to use a perspective projection with the default `FOV` of 90 degrees and a `focal_length` of 1.

```python
axs[1].set_proj_type('persp')  # FOV = 90 deg
axs[1].set_title("'persp'\nfocal_length = 1 (default)", fontsize=10)
```

Set the third subplot to use a perspective projection with a `FOV` of 157.4 degrees and a `focal_length` of 0.2.

```python
axs[2].set_proj_type('persp', focal_length=0.2)  # FOV = 157.4 deg
axs[2].set_title("'persp'\nfocal_length = 0.2", fontsize=10)
```
