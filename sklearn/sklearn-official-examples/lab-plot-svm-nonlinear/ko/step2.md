# 데이터 생성

이 단계에서는 SVM 분류기를 학습 및 테스트하기 위한 데이터를 생성합니다. 두 개의 특징을 가진 300 개의 랜덤 데이터 포인트를 생성합니다. 예측 대상은 입력값의 XOR 입니다.

```python
np.random.seed(0)
X = np.random.randn(300, 2)
Y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0)
```
