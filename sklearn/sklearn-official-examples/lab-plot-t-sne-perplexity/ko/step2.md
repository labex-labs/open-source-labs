# 데이터 생성

t-SNE 의 사용을 보여주기 위해 세 가지 다른 데이터셋을 생성합니다. 첫 번째 데이터셋은 두 개의 동심원입니다.

```python
n_samples = 150
n_components = 2

X, y = datasets.make_circles(
    n_samples=n_samples, factor=0.5, noise=0.05, random_state=0
)

red = y == 0
green = y == 1
```
