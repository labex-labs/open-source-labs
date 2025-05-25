# 데이터 생성

다음으로, 시각화에 사용할 임의의 데이터를 생성합니다. 이 예제에서는 numpy 를 사용하여 두 개의 임의 데이터 배열을 생성합니다.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

x = np.random.rand(20)
y = 1e7 * np.random.rand(20)
```
