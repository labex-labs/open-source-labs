# 不间断的流线

在这一步中，我们将创建一个具有不间断流线的流线图。`broken_streamlines` 参数控制当流线超出单个网格单元内的线条限制时是否应断开。

```python
plt.streamplot(X, Y, U, V, broken_streamlines=False)
plt.title('Streamplot with Unbroken Streamlines')
plt.show()
```
