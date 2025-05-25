# 가중 평균 (Weighted Average)

두 개의 동일한 길이의 리스트 `nums`와 `weights`를 입력으로 받는 함수 `weighted_average(nums, weights)`를 작성하십시오. 이 함수는 `nums`의 숫자들의 가중 평균을 반환해야 하며, 여기서 각 숫자는 `weights`에서 해당 가중치와 곱해집니다. 가중 평균은 각 숫자와 해당 가중치의 곱의 합을 가중치의 합으로 나누어 계산합니다.

```python
def weighted_average(nums, weights):
  return sum(x * y for x, y in zip(nums, weights)) / sum(weights)
```

```python
weighted_average([1, 2, 3], [0.6, 0.2, 0.3]) # 1.72727
```
