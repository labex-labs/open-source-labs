# MRI画像を表示する

`matplotlib`の`imshow`関数を使って、MRI画像をグレースケールで表示します。

```python
fig, ax = plt.subplots(num="MRI_demo")
ax.imshow(im, cmap="gray")
ax.axis('off')
plt.show()
```
