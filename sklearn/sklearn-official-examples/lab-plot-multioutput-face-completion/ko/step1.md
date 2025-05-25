# 데이터 로드

첫 번째 단계는 각각 64x64 픽셀인 400 개의 회색조 얼굴 이미지를 포함하는 Olivetti 얼굴 데이터 세트를 로드하는 것입니다. 데이터는 학습 세트와 테스트 세트로 분할됩니다. 학습 세트는 30 명의 얼굴을 포함하고, 테스트 세트는 나머지 사람들의 얼굴을 포함합니다. 이 실습에서는 5 명의 사람의 하위 집합에서 알고리즘을 테스트할 것입니다.

```python
# 얼굴 데이터 세트 로드
data, targets = fetch_olivetti_faces(return_X_y=True)

train = data[targets < 30]
test = data[targets >= 30]  # 독립적인 사람들에 대해 테스트

# 사람들의 하위 집합에 대해 테스트
n_faces = 5
rng = check_random_state(4)
face_ids = rng.randint(test.shape[0], size=(n_faces,))
test = test[face_ids, :]

n_pixels = data.shape[1]
# 얼굴의 상반부
X_train = train[:, : (n_pixels + 1) // 2]
# 얼굴의 하반부
y_train = train[:, n_pixels // 2 :]
X_test = test[:, : (n_pixels + 1) // 2]
y_test = test[:, n_pixels // 2 :]
```
