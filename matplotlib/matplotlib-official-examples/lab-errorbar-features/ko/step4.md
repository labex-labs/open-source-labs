# 변수, 대칭 오차 막대 그래프 그리기

이제 변수, 대칭 오차 막대 그래프를 그립니다. `ax.errorbar()` 함수를 사용하여 그래프를 생성하고, `yerr` 매개변수를 사용하여 오차 값을 지정합니다.

```python
# plot variable, symmetric error bars
fig, ax = plt.subplots()
ax.errorbar(x, y, yerr=error, fmt='-o')
ax.set_title('Variable, Symmetric Error Bars')
plt.show()
```
