# 透視投影を設定する

2 番目のサブプロットに、既定の視野角（`FOV`）90 度と焦点距離（`focal_length`）1 の透視投影を使用するように設定します。

```python
axs[1].set_proj_type('persp')  # FOV = 90 deg
axs[1].set_title("'persp'\nfocal_length = 1 (default)", fontsize=10)
```

3 番目のサブプロットに、視野角（`FOV`）157.4 度と焦点距離（`focal_length`）0.2 の透視投影を使用するように設定します。

```python
axs[2].set_proj_type('persp', focal_length=0.2)  # FOV = 157.4 deg
axs[2].set_title("'persp'\nfocal_length = 0.2", fontsize=10)
```
