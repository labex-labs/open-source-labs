# 데이터셋 생성

다음으로, `make_circles`를 사용하여 두 개의 동심원으로 구성된 데이터셋을 생성합니다. 데이터셋에 레이블을 할당하여, 외부 원과 내부 원에 각각 속하는 두 개의 샘플을 제외하고 모든 샘플은 알 수 없는 상태로 설정합니다.

```python
n_samples = 200
X, y = make_circles(n_samples=n_samples, shuffle=False)
outer, inner = 0, 1
labels = np.full(n_samples, -1.0)
labels[0] = outer
labels[-1] = inner
```
