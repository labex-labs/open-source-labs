# 해치 패턴 사용자 정의

`pie()` 함수의 `hatch` 매개변수에 해치 패턴 (hatch patterns) 리스트를 전달하여 슬라이스의 해치 패턴을 사용자 정의할 수 있습니다.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, hatch=['**O', 'oO', 'O.O', '.||.'])
```
