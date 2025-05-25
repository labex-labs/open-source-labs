# 결과 플롯

이제 `SpectralBiclustering` 모델이 할당한 행 및 열 레이블을 오름차순으로 기반으로 데이터를 재정렬하고 다시 플롯합니다. `row_labels_`는 0 에서 3 까지, `column_labels_`는 0 에서 2 까지의 범위를 가지며, 각 행당 4 개의 클러스터와 각 열당 3 개의 클러스터를 나타냅니다.

```python
# 먼저 행, 그 다음 열을 재정렬합니다.
reordered_rows = data[np.argsort(model.row_labels_)]
reordered_data = reordered_rows[:, np.argsort(model.column_labels_)]

plt.matshow(reordered_data, cmap=plt.cm.Blues)
plt.title("바이클러스터링 후; 바이클러스터를 보여주도록 재정렬됨")
_ = plt.show()
```

마지막 단계로, 모델이 할당한 행 및 열 레이블 간의 관계를 보여주고자 합니다. 따라서 `numpy.outer`를 사용하여 그리드를 만듭니다. 이 함수는 정렬된 `row_labels_`와 `column_labels_`를 받아 각 레이블이 시각화를 위해 0 대신 1 부터 시작하도록 1 을 더합니다.

```python
plt.matshow(
    np.outer(np.sort(model.row_labels_) + 1, np.sort(model.column_labels_) + 1),
    cmap=plt.cm.Blues,
)
plt.title("재정렬된 데이터의 체커보드 구조")
plt.show()
```
