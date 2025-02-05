# 显示徽标

在这一步中，我们将显示不同大小的 Matplotlib 徽标。

```python
# 一个大徽标：
make_logo(height_px=110, lw_bars=0.7, lw_grid=0.5, lw_border=1,
          rgrid=[1, 3, 5, 7])

# 一个 32 像素的小徽标：
make_logo(height_px=32, lw_bars=0.3, lw_grid=0.3, lw_border=0.3, rgrid=[5])

# 一个包含文本的大徽标，如 Matplotlib 网站上使用的那样。
make_logo(height_px=110, lw_bars=0.7, lw_grid=0.5, lw_border=1,
          rgrid=[1, 3, 5, 7], with_text=True)
plt.show()
```
