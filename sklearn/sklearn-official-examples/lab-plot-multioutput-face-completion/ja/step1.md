# データの読み込み

最初のステップは、オリベッティ顔データセットを読み込むことです。このデータセットには、それぞれ 64x64 ピクセルの 400 枚のグレースケール画像が含まれています。データは訓練用とテスト用に分割されています。訓練用セットには 30 人の顔が含まれ、テスト用セットには残りの人の顔が含まれます。この実験では、5 人のサブセットでアルゴリズムをテストします。

```python
# Load the faces datasets
data, targets = fetch_olivetti_faces(return_X_y=True)

train = data[targets < 30]
test = data[targets >= 30]  # Test on independent people

# Test on a subset of people
n_faces = 5
rng = check_random_state(4)
face_ids = rng.randint(test.shape[0], size=(n_faces,))
test = test[face_ids, :]

n_pixels = data.shape[1]
# Upper half of the faces
X_train = train[:, : (n_pixels + 1) // 2]
# Lower half of the faces
y_train = train[:, n_pixels // 2 :]
X_test = test[:, : (n_pixels + 1) // 2]
y_test = test[:, n_pixels // 2 :]
```
