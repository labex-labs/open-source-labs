# 가짜 이미지 생성

먼저, NumPy 의 random 모듈을 사용하여 가짜 흑백 이미지를 생성합니다. 결과를 재현 가능하게 하기 위해 시드 (seed) 를 설정합니다.

```python
np.random.seed(19680801)
N = 128
img = np.random.randn(N, N)
```
