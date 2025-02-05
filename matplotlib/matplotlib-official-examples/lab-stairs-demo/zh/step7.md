# 创建一个带阴影线的直方图

```python
plt.stairs(np.arange(1, 6, 1)*0.3, np.arange(2, 8, 1),
              orientation='horizontal', hatch='//',
              label='Hatched histogram\nw/ horizontal orientation')
plt.legend()
plt.show()
```
