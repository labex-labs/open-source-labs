# 변수, 비대칭 오차 막대 그래프 그리기

다음으로, 변수, 비대칭 오차 막대 그래프를 그립니다. `ax.errorbar()` 함수를 다시 사용하지만, 이번에는 `xerr` 매개변수를 사용하여 비대칭 오차 값을 지정합니다.

```python
# plot variable, asymmetric error bars
fig, ax = plt.subplots()
ax.errorbar(x, y, xerr=asymmetric_error, fmt='o')
ax.set_title('Variable, Asymmetric Error Bars')
plt.show()
```
