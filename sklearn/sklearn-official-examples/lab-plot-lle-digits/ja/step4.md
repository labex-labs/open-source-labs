# 結果をプロットする

各手法によって得られた結果の射影をプロットします。

```python
for name in timing:
    title = f"{name} (time {timing[name]:.3f}s)"
    plot_embedding(projections[name], title)

plt.show()
```
