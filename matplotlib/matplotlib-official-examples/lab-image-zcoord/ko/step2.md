# 랜덤 행렬 생성

다음으로, numpy 를 사용하여 랜덤 행렬을 생성합니다. `rand` 메서드를 사용하여 0 과 1 사이의 랜덤 값을 갖는 5x3 행렬을 생성합니다. 또한 결과의 재현성을 보장하기 위해 랜덤 시드 (random seed) 를 설정합니다.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

X = 10*np.random.rand(5, 3)
```
