# 6 번째 오차 막대마다 서브샘플링

이제, 6 번째 오차 막대마다 플롯하기 위해 오차 막대 서브샘플링을 적용해 보겠습니다. `errorbar` 함수의 `errorevery` 매개변수를 사용하여 이를 수행할 수 있습니다.

```python
fig, ax = plt.subplots()

ax.set_title('Every 6th Errorbar')
ax.errorbar(x, y1, yerr=y1err, errorevery=6, label='y1')
ax.errorbar(x, y2, yerr=y2err, errorevery=6, label='y2')

ax.legend()
plt.show()
```
