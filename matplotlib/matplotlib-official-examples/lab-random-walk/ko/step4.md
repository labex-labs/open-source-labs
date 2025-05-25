# 랜덤 워크 생성

앞서 정의한 `random_walk()` 함수를 사용하여 각각 30 단계로 구성된 40 개의 랜덤 워크를 생성합니다. 모든 랜덤 워크를 `walks`라는 리스트에 저장합니다.

```python
# Data: 40 random walks as (num_steps, 3) arrays
num_steps = 30
walks = [random_walk(num_steps) for index in range(40)]
```
