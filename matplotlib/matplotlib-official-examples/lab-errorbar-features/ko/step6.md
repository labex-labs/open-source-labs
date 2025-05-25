# 오차 막대 그래프와 로그 스케일 그리기

마지막으로, 로그 스케일과 오차 막대 그래프를 함께 그립니다. `ax.set_yscale()` 함수를 사용하여 y 축을 로그 스케일로 설정합니다.

```python
# plot log scale with error bars
fig, ax = plt.subplots()
ax.errorbar(x, y, yerr=error, fmt='o')
ax.set_title('Log Scale with Error Bars')
ax.set_yscale('log')
plt.show()
```
