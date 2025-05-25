# `get_correlated_dataset` 함수 정의

또한 지정된 평균, 차원 및 상관 관계를 가진 2 차원 데이터셋을 생성하는 함수가 필요합니다.

```python
def get_correlated_dataset(n, dependency, mu, scale):
    """
    지정된 2 차원 평균 (mu) 및 차원 (scale) 을 가진 무작위 2 차원 데이터셋을 생성합니다.
    상관 관계는 2x2 행렬인 'dependency' 매개변수를 통해 제어할 수 있습니다.
    """
    latent = np.random.randn(n, 2)
    dependent = latent.dot(dependency)
    scaled = dependent * scale
    scaled_with_offset = scaled + mu
    # return x and y of the new, correlated dataset
    return scaled_with_offset[:, 0], scaled_with_offset[:, 1]
```
