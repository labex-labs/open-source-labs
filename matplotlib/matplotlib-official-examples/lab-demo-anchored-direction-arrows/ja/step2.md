# プロットを作成する

次に、NumPy を使って簡単なプロットを作成します。このプロットは、固定方向矢印の背景として機能します。

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

fig, ax = plt.subplots()
ax.imshow(np.random.random((10, 10)))
```
