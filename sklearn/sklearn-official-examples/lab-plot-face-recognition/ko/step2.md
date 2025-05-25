# 데이터셋 로드 및 탐색

```python
lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)
n_samples, h, w = lfw_people.images.shape
X = lfw_people.data
n_features = X.shape[1]
y = lfw_people.target
target_names = lfw_people.target_names
n_classes = target_names.shape[0]
```

`scikit-learn`의 `fetch_lfw_people()` 함수를 사용하여 데이터셋을 다운로드합니다. 그런 다음 이미지의 샘플 수, 높이, 너비를 가져와 데이터셋을 탐색합니다. 또한 입력 데이터 `X`, 타겟 `y`, 타겟 이름 `target_names`, 클래스 수 `n_classes`를 가져옵니다.
