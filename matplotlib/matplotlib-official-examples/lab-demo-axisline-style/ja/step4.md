# グラフを描画する

次に、`np.linspace` と `np.sin` を使ってグラフを描画します。

```python
x = np.linspace(-0.5, 1., 100)
ax.plot(x, np.sin(x*np.pi))
```
