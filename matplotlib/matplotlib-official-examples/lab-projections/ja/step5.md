# 正射投影を設定する

最初のサブプロットに、視野角（`FOV`）が0度で焦点距離（`focal_length`）が無限大の正射投影を使用するように設定します。

```python
axs[0].set_proj_type('ortho')  # FOV = 0 deg
axs[0].set_title("'ortho'\nfocal_length = ∞", fontsize=10)
```
