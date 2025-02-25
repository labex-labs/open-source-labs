# 画像とそのヒストグラムを表示する

次に、Matplotlibの`imshow`関数を使って画像を表示し、`hist`を使ってそのヒストグラムを表示します。画像用のサブプロットとヒストグラム用のサブプロットを含む図を作成します。

```python
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
fig.subplots_adjust(bottom=0.25)

im = axs[0].imshow(img)
axs[1].hist(img.flatten(), bins='auto')
axs[1].set_title('Histogram of pixel intensities')
```
