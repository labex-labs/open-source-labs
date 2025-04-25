# グラフを作成する

次に、`imshow` と `numpy.random` で生成されたランダムな配列を使って 2 つのグラフを作成しましょう。また、グラフにカラーバーも追加します。次のコードを実行してください。

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

plt.subplot(211)
plt.imshow(np.random.random((100, 100)))
plt.subplot(212)
plt.imshow(np.random.random((100, 100)))

cax = plt.axes([0.85, 0.1, 0.075, 0.8])
plt.colorbar(cax=cax)

plt.show()
```
