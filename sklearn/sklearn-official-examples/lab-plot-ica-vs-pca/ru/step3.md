# Использование алгоритма FastICA

В этом шаге мы используем алгоритм FastICA, который находит направления в пространстве признаков, соответствующие проекциям с высокой негауссовостью.

```python
ica = FastICA(random_state=rng, whiten="arbitrary-variance")
S_ica_ = ica.fit(X).transform(X)  # Estimate the sources

S_ica_ /= S_ica_.std(axis=0)
```
