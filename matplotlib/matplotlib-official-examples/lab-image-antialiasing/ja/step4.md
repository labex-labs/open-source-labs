# 「最寄り」補間を使った画像のアップサンプリング

次に、「最寄り」補間を使って画像を 500 データピクセルから 530 レンダリングピクセルにアップサンプリングします。これにより、アップサンプリング係数が整数でない場合、画像をアップサンプリングしたときでもモアレパターンが発生する可能性があることを示します。

```python
fig, ax = plt.subplots(figsize=(6.8, 6.8))
ax.imshow(a, interpolation='nearest', cmap='gray')
ax.set_title("upsampled by factor a 1.048, interpolation='nearest'")
plt.show()
```
