# 노이즈 추가

이 단계에서는 생성된 데이터에 노이즈를 추가하여 더욱 현실적인 학습 데이터셋을 만듭니다.

```python
rng = np.random.RandomState(0)
X_train = rng.uniform(0, 5, size=20).reshape(-1, 1)
y_train = target_generator(X_train, add_noise=True)
```
