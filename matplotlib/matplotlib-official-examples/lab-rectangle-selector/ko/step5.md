# 서브플롯에 무언가 플롯하기

사용자가 RectangleSelector 및 EllipseSelector 의 효과를 볼 수 있도록 서브플롯에 무언가를 플롯합니다.

```python
N = 100000  # If N is large one can see improvement by using blitting.
x = np.linspace(0, 10, N)

for ax in axs:
    ax.plot(x, np.sin(2*np.pi*x))  # plot something
```
