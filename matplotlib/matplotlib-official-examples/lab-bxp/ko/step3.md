# 상자 그림 통계 사용자 정의

2 단계에서 계산된 상자 그림 통계 중 임의의 값을 수정할 수 있습니다. 이 예제에서는 각 세트의 중앙값을 전체 데이터의 중앙값으로 설정하고, 평균을 두 배로 늘립니다.

```python
for n in range(len(stats)):
    stats[n]['med'] = np.median(data)
    stats[n]['mean'] *= 2
```
