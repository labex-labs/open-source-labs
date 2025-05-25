# 가상 데이터 생성

이제 scikit-learn 의 `make_regression` 함수를 사용하여 가상 데이터셋을 생성합니다. 샘플 수는 20 개, 특징은 1 개, 난수 시드는 0 으로 설정합니다. 또한 데이터셋에 약간의 노이즈를 추가합니다.

```python
rng = np.random.RandomState(0)
X, y = make_regression(
    n_samples=20, n_features=1, random_state=0, noise=4.0, bias=100.0
)
```
