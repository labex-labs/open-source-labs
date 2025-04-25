# 设置透视投影

将第二个子图设置为使用默认视场（FOV）为 90 度且焦距为 1 的透视投影。

```python
axs[1].set_proj_type('persp')  # FOV = 90 deg
axs[1].set_title("'persp'\nfocal_length = 1 (default)", fontsize=10)
```

将第三个子图设置为使用视场为 157.4 度且焦距为 0.2 的透视投影。

```python
axs[2].set_proj_type('persp', focal_length=0.2)  # FOV = 157.4 deg
axs[2].set_title("'persp'\nfocal_length = 0.2", fontsize=10)
```
