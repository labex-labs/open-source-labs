# 设置正交投影

将第一个子图设置为使用视场（FOV）为0度且焦距为无穷大的正交投影。

```python
axs[0].set_proj_type('ortho')  # FOV = 0 deg
axs[0].set_title("'ortho'\nfocal_length = ∞", fontsize=10)
```
