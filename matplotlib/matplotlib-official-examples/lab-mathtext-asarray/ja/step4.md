# ピクセル座標での位置指定付きで図にテキストを描画する

代わりに、`.Figure.text`と`.transforms.IdentityTransform`を併用することで、ピクセル座標での位置指定付きで直接図にテキストを描画することができます。

```python
fig.text(100, 250, r"IQ: $\sigma_i=15$", color="blue", fontsize=20, transform=IdentityTransform())
fig.text(100, 350, r"some other string", color="red", fontsize=20, transform=IdentityTransform())

plt.show()
```
