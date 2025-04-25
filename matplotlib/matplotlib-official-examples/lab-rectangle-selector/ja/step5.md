# サブプロットに何かをプロットする

RectangleSelector と EllipseSelector の効果をユーザーが確認できるように、サブプロットに何かをプロットします。

```python
N = 100000  # If N is large one can see improvement by using blitting.
x = np.linspace(0, 10, N)

for ax in axs:
    ax.plot(x, np.sin(2*np.pi*x))  # plot something
```
