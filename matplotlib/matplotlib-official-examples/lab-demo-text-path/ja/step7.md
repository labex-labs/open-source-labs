# 画像を表示する

以下のコードを使用して最終的な画像を表示します。

```python
ax1.imshow([[0, 1, 2], [1, 2, 3]], cmap=plt.cm.gist_gray_r,
               interpolation="bilinear", aspect="auto")
plt.show()
```
