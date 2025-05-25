# 새로운 샘플 생성

최적의 추정자를 사용하여 데이터에서 44 개의 새로운 점을 샘플링합니다. 그런 다음 PCA 의 역변환을 사용하여 새로운 데이터를 원래 64 차원으로 변환합니다.

```python
# 데이터에서 44 개의 새로운 점을 샘플링
new_data = kde.sample(44, random_state=0)
new_data = pca.inverse_transform(new_data)
```
