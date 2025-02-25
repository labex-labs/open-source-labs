# 縦型のカラーバー付きのプロットを作成する

まずは、縦型のカラーバー付きのプロットを作成します。`numpy` の `randn` を使っていくつかの乱数データを生成し、その値を -1 から 1 の範囲にクリップします。その後、`imshow` と `coolwarm` カラーマップを使って `AxesImage` オブジェクトを作成します。最後に、プロットにタイトルを追加します。

```python
# Make plot with vertical (default) colorbar
fig, ax = plt.subplots()

data = np.clip(randn(250, 250), -1, 1)

cax = ax.imshow(data, cmap=cm.coolwarm)
ax.set_title('Gaussian noise with vertical colorbar')
```
