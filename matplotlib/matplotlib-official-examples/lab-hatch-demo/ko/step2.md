# 데이터 생성

다음으로, 플롯에 사용할 데이터를 생성해야 합니다. 이 경우 NumPy 라이브러리를 사용하여 두 개의 배열을 생성합니다.

```python
x = np.arange(1, 5)
y1 = np.arange(1, 5)
y2 = np.ones(y1.shape) * 4
```
