# 데이터 변형

때때로 데이터가 scikit-learn 에서 요구하는 형태가 아닐 수 있습니다. 이러한 경우 데이터를 `(n_samples, n_features)` 형태로 변환하기 위해 데이터를 전처리해야 합니다. 데이터 변형의 예시로 손글씨 숫자 이미지 1797 개 (8x8 크기) 로 구성된 digits 데이터셋이 있습니다.

```python
digits = datasets.load_digits()
print(digits.images.shape)
```

출력:

```
(1797, 8, 8)
```

이 데이터셋을 scikit-learn 과 함께 사용하려면 각 8x8 이미지를 길이 64 의 특징 벡터로 변형해야 합니다.

```python
data = digits.images.reshape((digits.images.shape[0], -1))
```
