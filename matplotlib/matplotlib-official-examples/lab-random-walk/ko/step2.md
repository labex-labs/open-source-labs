# 랜덤 워크 함수 정의

주어진 단계 수와 최대 단계 크기로 랜덤 워크를 생성하는 함수를 정의합니다. 이 함수는 두 개의 입력을 받습니다: `num_steps`는 랜덤 워크의 총 단계 수이고, `max_step`은 각 단계의 최대 크기입니다. `numpy.random`을 사용하여 단계에 대한 랜덤 숫자를 생성하고, `numpy.cumsum`을 사용하여 단계의 누적 합을 계산하여 최종 위치를 얻습니다.

```python
def random_walk(num_steps, max_step=0.05):
    """Return a 3D random walk as (num_steps, 3) array."""
    start_pos = np.random.random(3)
    steps = np.random.uniform(-max_step, max_step, size=(num_steps, 3))
    walk = start_pos + np.cumsum(steps, axis=0)
    return walk
```
