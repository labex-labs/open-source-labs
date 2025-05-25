# 데이터 생성

플롯할 샘플 데이터를 생성합니다. 여기서는 `numpy` 라이브러리를 사용하여 세 개의 데이터 배열을 생성합니다.

```python
t = np.arange(0.0, 2.0, 0.01)

s1 = np.sin(2 * np.pi * t)
s2 = np.exp(-t)
s3 = s1 * s2
```
