# 데이터 생성

다음으로, 히스토그램에 사용할 임의의 2D 데이터를 생성합니다. NumPy 의 `random.rand()` 함수를 사용하여 x 및 y 변수 모두에 대해 100 개의 임의 값을 생성합니다.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

x, y = np.random.rand(2, 100) * 4
```
