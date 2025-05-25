# 두 번째 시리즈를 3 만큼 이동

경우에 따라, 데이터의 다른 부분에 오차 막대 서브샘플링을 적용하고 싶을 수 있습니다. `errorevery` 매개변수에 튜플을 지정하여 이를 수행할 수 있습니다. 예를 들어, 두 번째 시리즈에 오차 막대 서브샘플링을 적용하되, 3 개의 데이터 포인트만큼 이동해 보겠습니다.

```python
fig, ax = plt.subplots()

ax.set_title('Second Series Shifted by 3')
ax.errorbar(x, y1, yerr=y1err, label='y1')
ax.errorbar(x, y2, yerr=y2err, errorevery=(3, 6), label='y2')

ax.legend()
plt.show()
```
