# 加载数据

第一步是加载 Olivetti 人脸数据集，该数据集包含 400 张 64x64 像素的灰度图像。数据被分为训练集和测试集。训练集包含 30 个人的人脸，测试集包含其余人的人脸。对于本实验，我们将在五个人的子集上测试算法。

```python
# 加载人脸数据集
data, targets = fetch_olivetti_faces(return_X_y=True)

train = data[targets < 30]
test = data[targets >= 30]  # 在独立的人上进行测试

# 在人的一个子集上进行测试
n_faces = 5
rng = check_random_state(4)
face_ids = rng.randint(test.shape[0], size=(n_faces,))
test = test[face_ids, :]

n_pixels = data.shape[1]
# 人脸的上半部分
X_train = train[:, : (n_pixels + 1) // 2]
# 人脸的下半部分
y_train = train[:, n_pixels // 2 :]
X_test = test[:, : (n_pixels + 1) // 2]
y_test = test[:, n_pixels // 2 :]
```
