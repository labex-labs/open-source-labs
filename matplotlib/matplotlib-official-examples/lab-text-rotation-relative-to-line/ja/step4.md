# 正しく回転させないでテキストを描画する

次に、線の回転を考慮せずに指定された場所にテキストを描画します。これにより、テキストが 45 度の角度で回転してしまい、これは私たちが望むものではありません。

```python
# Plot text
th1 = ax.text(*l1, 'text not rotated correctly', fontsize=16,
              rotation=angle, rotation_mode='anchor')
```
