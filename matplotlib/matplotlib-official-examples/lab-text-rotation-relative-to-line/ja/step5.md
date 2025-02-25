# 正しく回転させてテキストを描画する

最後に、線の回転を考慮しながら指定された場所にテキストを描画します。これにより、テキストが線に対して正しい角度で回転します。

```python
# Plot text
th2 = ax.text(*l2, 'text rotated correctly', fontsize=16,
              rotation=angle, rotation_mode='anchor',
              transform_rotates_text=True)
```
