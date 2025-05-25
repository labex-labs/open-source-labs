# 여러 서브플롯의 박스 종횡비

초기화 시 Axes 에 박스 종횡비를 전달하는 것이 가능합니다. 다음은 모든 Axes 가 정사각형인 2x3 서브플롯 그리드를 생성합니다.

```python
fig7, axs = plt.subplots(2, 3, subplot_kw=dict(box_aspect=1),
                         sharex=True, sharey=True, layout="constrained")

for i, ax in enumerate(axs.flat):
    ax.scatter(i % 3, -((i // 3) - 0.5)*200, c=[plt.cm.hsv(i / 6)], s=300)
plt.show()
```
