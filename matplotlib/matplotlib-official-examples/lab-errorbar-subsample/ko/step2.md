# 모든 오차 막대 플롯

다음으로, 서브샘플링 없이 `errorbar` 함수를 사용하여 모든 오차 막대를 플롯합니다. 이것은 우리의 기준 플롯 역할을 할 것입니다.

```python
fig, ax = plt.subplots()

ax.set_title('All Errorbars')
ax.errorbar(x, y1, yerr=y1err, label='y1')
ax.errorbar(x, y2, yerr=y2err, label='y2')

ax.legend()
plt.show()
```
