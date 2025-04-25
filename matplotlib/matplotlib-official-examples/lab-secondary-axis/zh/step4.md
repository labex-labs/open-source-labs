# 绘制另一个示例

现在我们将绘制另一个示例，即在对数 - 对数尺度下将波数转换为波长。在这个示例中，我们将使用一个随机频谱。

```python
fig, ax = plt.subplots(layout='constrained')
x = np.arange(0.02, 1, 0.02)
np.random.seed(19680801)
y = np.random.randn(len(x)) ** 2
ax.loglog(x, y)
ax.set_xlabel('f [Hz]')
ax.set_ylabel('PSD')
ax.set_title('Random spectrum')
```
