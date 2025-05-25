# 반지도 학습을 위한 데이터 준비

340 개의 샘플을 선택하고, 이 중 40 개의 샘플만 알려진 레이블을 갖습니다. 레이블을 알 수 없는 나머지 300 개 샘플의 인덱스를 저장합니다. 그런 다음 레이블을 섞어서 레이블이 없는 샘플은 -1 로 표시합니다.

```python
X = digits.data[indices[:340]]
y = digits.target[indices[:340]]

n_total_samples = len(y)
n_labeled_points = 40

indices = np.arange(n_total_samples)

unlabeled_set = indices[n_labeled_points:]

y_train = np.copy(y)
y_train[unlabeled_set] = -1
```
