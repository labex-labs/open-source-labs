# 데이터 생성

이 단계에서는 10x10 힐버트 행렬을 생성하고, 목표 변수 `y`를 1 로 구성된 벡터로 설정합니다.

```python
X = 1.0 / (np.arange(1, 11) + np.arange(0, 10)[:, np.newaxis])
y = np.ones(10)
```
