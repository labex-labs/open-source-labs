# Set the Orthographic Projection

Set the first subplot to use an orthographic projection with a `FOV` of 0 degrees and a `focal_length` of infinity.

```python
axs[0].set_proj_type('ortho')  # FOV = 0 deg
axs[0].set_title("'ortho'\nfocal_length = ∞", fontsize=10)
```
