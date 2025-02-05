# 设置透视投影

将第二个子图设置为使用默认视场（FOV）为90度且焦距为1的透视投影。

```python
axs[1].set_proj_type('persp')  # FOV = 90 deg
axs[1].set_title("'persp'\nfocal_length = 1 (default)", fontsize=10)
```

将第三个子图设置为使用视场为157.4度且焦距为0.2的透视投影。

```python
axs[2].set_proj_type('persp', focal_length=0.2)  # FOV = 157.4 deg
axs[2].set_title("'persp'\nfocal_length = 0.2", fontsize=10)
```
