# Lorenz 어트랙터 계산

시간을 단계별로 진행하고 이전 지점과 Lorenz 함수를 사용하여 다음 지점을 추정하여 Lorenz 어트랙터를 계산합니다.

```python
for i in range(num_steps):
    xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i]) * dt
```
