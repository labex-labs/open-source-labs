# データの生成とサブプロットの作成

次に、画像用のデータを生成します。3x2のサブプロットのグリッドを作成し、各サブプロットにはランダムに生成された値の配列を含めます。

```python
np.random.seed(19680801)
Nr = 3
Nc = 2

fig, axs = plt.subplots(Nr, Nc)
fig.suptitle('Multiple images')

images = []
for i in range(Nr):
    for j in range(Nc):
        # Generate data with a range that varies from one plot to the next.
        data = ((1 + i + j) / 10) * np.random.rand(10, 20)
        images.append(axs[i, j].imshow(data))
        axs[i, j].label_outer()
```
