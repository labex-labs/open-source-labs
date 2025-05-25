# 데이터 준비

이 단계에서는 특징 이산화를 위한 합성 분류 데이터 세트를 준비합니다. scikit-learn 라이브러리를 사용하여 세 가지 다른 데이터 세트 (달 모양, 동심원, 선형적으로 분리 가능한 데이터) 를 생성합니다.

```python
h = 0.02  # 메쉬의 단계 크기

n_samples = 100
datasets = [
    make_moons(n_samples=n_samples, noise=0.2, random_state=0),
    make_circles(n_samples=n_samples, noise=0.2, factor=0.5, random_state=1),
    make_classification(
        n_samples=n_samples,
        n_features=2,
        n_redundant=0,
        n_informative=2,
        random_state=2,
        n_clusters_per_class=1,
    ),
]
```
