# 해칭 (Hatching) 을 사용한 막대 그래프 생성

이제 데이터를 갖추었으므로 해칭을 사용하여 막대 그래프를 생성할 수 있습니다. 해칭을 사용하여 플롯의 막대에 패턴을 만들 수 있습니다. 이 경우, `hatch` 매개변수를 사용하여 막대에 해칭을 추가합니다.

```python
plt.bar(x, y1, edgecolor='black', hatch="/")
plt.bar(x, y2, bottom=y1, edgecolor='black', hatch='//')
```
