# 축 레이블 및 제목 추가

`plt.ylabel`, `plt.yticks`, `plt.xticks`, 및 `plt.title` 함수를 사용하여 플롯에 축 레이블과 제목을 추가합니다.

```python
values = np.arange(0, 2500, 500)
value_increment = 1000

plt.ylabel(f"Loss in ${value_increment}'s")
plt.yticks(values * value_increment, ['%d' % val for val in values])
plt.xticks([])
plt.title('Loss by Disaster')
```
