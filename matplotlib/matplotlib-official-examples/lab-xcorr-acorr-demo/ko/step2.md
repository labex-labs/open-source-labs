# 랜덤 데이터 생성

다음으로, NumPy 를 사용하여 두 개의 랜덤 데이터 배열을 생성합니다. 이 배열을 사용하여 상호 상관 (cross-correlation) 과 자기 상관 (auto-correlation) 을 시연합니다.

```python
np.random.seed(19680801)
x, y = np.random.randn(2, 100)
```
