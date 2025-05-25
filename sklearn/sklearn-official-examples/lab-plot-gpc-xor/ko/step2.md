# XOR 데이터셋 생성

이 단계에서는 numpy 를 사용하여 XOR 데이터셋을 생성합니다. 입력 특징에 기반하여 logical_xor 함수를 사용하여 레이블을 생성합니다.

```python
xx, yy = np.meshgrid(np.linspace(-3, 3, 50), np.linspace(-3, 3, 50))
rng = np.random.RandomState(0)
X = rng.randn(200, 2)
Y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0)
```
