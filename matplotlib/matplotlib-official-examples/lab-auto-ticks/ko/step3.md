# 추가 여백이 있는 산점도 그리기

이 단계에서는 round numbers autolimit_mode 가 여전히 적용되는 동안 `.Axes.set_xmargin` / `.Axes.set_ymargin`을 사용하여 데이터 주변에 추가 여백을 설정합니다.

```python
fig, ax = plt.subplots()
ax.scatter(x, y, c=x+y)
ax.set_xmargin(0.8)
plt.show()
```
