# 역변환

이 단계에서는 감소된 데이터 세트에 역변환을 수행하여 원래 특징 수를 복원합니다.

```python
X_restored = agglo.inverse_transform(X_reduced)
images_restored = np.reshape(X_restored, images.shape)
```
