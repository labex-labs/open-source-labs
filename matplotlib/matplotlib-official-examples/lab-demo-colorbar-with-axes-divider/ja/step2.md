# プロットを作成する

次に、Matplotlib の`imshow`関数を使ってプロットを作成します。この関数は、プロット上に画像を表示します。また、2 つのサブプロット付きのグラフを作成します。

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.subplots_adjust(wspace=0.5)

im1 = ax1.imshow([[1, 2], [3, 4]])

im2 = ax2.imshow([[1, 2], [3, 4]])
```
