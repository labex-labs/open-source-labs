# 画像の表示

ここでは、Matplotlib の`imshow`メソッドを使って画像を表示します。また、軸を非表示にして画像のみを表示するようにします。

```python
fig, ax = plt.subplots()
im = ax.imshow(image)
ax.axis('off')
```
