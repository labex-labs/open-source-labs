# 여러 해칭 (Hatch) 을 사용한 막대 그래프 생성

막대 그래프에서 여러 해칭을 사용할 수도 있습니다. 이 경우, 해칭 배열을 사용하여 막대에 여러 해칭을 생성합니다.

```python
plt.bar(x, y1, edgecolor='black', hatch=['--', '+', 'x', '\\'])
plt.bar(x, y2, bottom=y1, edgecolor='black', hatch=['*', 'o', 'O', '.'])
```
