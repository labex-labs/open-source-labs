# ロゴの表示

このステップでは、異なるサイズの Matplotlib のロゴを表示します。

```python
# 大きなロゴ:
make_logo(height_px=110, lw_bars=0.7, lw_grid=0.5, lw_border=1,
          rgrid=[1, 3, 5, 7])

# 小さな 32px のロゴ:
make_logo(height_px=32, lw_bars=0.3, lw_grid=0.3, lw_border=0.3, rgrid=[5])

# Matplotlib のウェブサイトで使用されているような、テキスト付きの大きなロゴ。
make_logo(height_px=110, lw_bars=0.7, lw_grid=0.5, lw_border=1,
          rgrid=[1, 3, 5, 7], with_text=True)
plt.show()
```
