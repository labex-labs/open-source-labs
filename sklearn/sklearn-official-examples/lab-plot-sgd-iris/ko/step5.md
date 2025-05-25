# 일대일 분류기 플롯

이제 결정 경계 위에 세 개의 일대일 (OVA) 분류기를 플롯합니다. 훈련된 모델의 coef* 및 intercept* 속성을 사용하여 OVA 분류기에 해당하는 초평면을 플롯합니다.

```python
xmin, xmax = plt.xlim()
ymin, ymax = plt.ylim()
coef = clf.coef_
intercept = clf.intercept_


def plot_hyperplane(c, color):
    def line(x0):
        return (-(x0 * coef[c, 0]) - intercept[c]) / coef[c, 1]

    plt.plot([xmin, xmax], [line(xmin), line(xmax)], ls="--", color=color)


for i, color in zip(clf.classes_, colors):
    plot_hyperplane(i, color)
plt.legend()
plt.show()
```
