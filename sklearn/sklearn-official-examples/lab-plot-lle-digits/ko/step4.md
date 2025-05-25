# 결과 플롯

각 방법으로 얻은 결과 투영을 플롯합니다.

```python
for name in timing:
    title = f"{name} (time {timing[name]:.3f}s)"
    plot_embedding(projections[name], title)

plt.show()
```
