# 플롯을 위한 데이터 생성

시각화를 위해 플롯에 대한 데이터를 생성해야 합니다. 이 예제에서는 NumPy 를 사용하여 세 개의 서로 다른 데이터 세트를 생성합니다.

```python
t = np.arange(0.01, 5.0, 0.01)
s1 = np.sin(2 * np.pi * t)
s2 = np.exp(-t)
s3 = np.sin(4 * np.pi * t)
```
