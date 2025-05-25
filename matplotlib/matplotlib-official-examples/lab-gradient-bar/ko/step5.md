# 플롯 생성

이제 플롯을 생성할 수 있습니다. 먼저 figure 와 axes 객체를 생성합니다. 그런 다음 axes 의 x 및 y 제한을 설정합니다. `gradient_image()` 함수를 사용하여 그라데이션 배경을 생성합니다. 마지막으로, 임의의 데이터 세트를 생성하고 `gradient_bar()` 함수를 사용하여 막대 차트를 생성합니다.

```python
fig, ax = plt.subplots()
ax.set(xlim=(0, 10), ylim=(0, 1))

# background image
gradient_image(ax, direction=1, extent=(0, 1, 0, 1), transform=ax.transAxes,
               cmap=plt.cm.RdYlGn, cmap_range=(0.2, 0.8), alpha=0.5)

N = 10
x = np.arange(N) + 0.15
y = np.random.rand(N)
gradient_bar(ax, x, y, width=0.7)
plt.show()
```
