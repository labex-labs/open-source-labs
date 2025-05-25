# 주요 눈금 레이블 및 보조 눈금 제거

눈금 사이의 레이블을 가운데 정렬하는 동작을 흉내내려면 주요 눈금 레이블과 보조 눈금을 제거하고 보조 눈금 레이블만 표시해야 합니다. `tick_params()` 함수를 사용하고 `tick1On` 및 `tick2On` 매개변수를 `False`로 설정하여 이를 수행할 수 있습니다.

```python
# Remove the tick lines
ax.tick_params(axis='x', which='minor', tick1On=False, tick2On=False)
```
