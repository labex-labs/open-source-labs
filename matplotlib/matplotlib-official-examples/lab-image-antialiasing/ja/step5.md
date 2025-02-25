# 「アンチエイリアス」補間を使った画像のアップサンプリング

最後に、「アンチエイリアス」補間を使って画像を 500 データピクセルから 530 レンダリングピクセルにアップサンプリングします。これにより、より良いアンチエイリアシングアルゴリズムを使用することがどのようにしてモアレパターンを軽減できるかを示します。

```python
fig, ax = plt.subplots(figsize=(6.8, 6.8))
ax.imshow(a, interpolation='antialiased', cmap='gray')
ax.set_title("upsampled by factor a 1.048, interpolation='antialiased'")
plt.show()
```
