# GPCの例

GPCによる確率的予測：この例は、異なるハイパーパラメータの選択によるGPCの予測確率を示しています。

```python
# RBFカーネルを持つGPCモデルを作成する
kernel = RBF()
model = GaussianProcessClassifier(kernel=kernel)

# 学習データにモデルをフィッティングする
model.fit(X_train, y_train)

# テストデータのクラス確率を予測する
y_prob = model.predict_proba(X_test)
```

XORデータセットにおけるGPCの例示：この例は、XORデータセットでのGPCの使用を示しています。静止的な等方性カーネル（RBF）と非静止的なカーネル（DotProduct）を使用した結果を比較しています。

```python
# 異なるカーネルを持つGPCモデルを作成する
isotropic_kernel = RBF(length_scale=1.0)
non_stationary_kernel = DotProduct(sigma_0=1.0)

# XORデータセットにモデルをフィッティングする
isotropic_model = GaussianProcessClassifier(kernel=isotropic_kernel)
non_stationary_model = GaussianProcessClassifier(kernel=non_stationary_kernel)
isotropic_model.fit(X_xor, y_xor)
non_stationary_model.fit(X_xor, y_xor)

# 学習済みモデルを使って予測する
isotropic_y_pred = isotropic_model.predict(X_test)
non_stationary_y_pred = non_stationary_model.predict(X_test)
```

アイリスデータセットにおけるGPC：この例は、等方性RBFカーネルと異方性RBFカーネルを使用したアイリスデータセットでのGPCを示しています。異なるハイパーパラメータの選択が予測確率にどのように影響するかを示しています。

```python
# 異なるカーネルを持つGPCモデルを作成し、アイリスデータセットにフィッティングする
isotropic_kernel = RBF(length_scale=1.0)
anisotropic_kernel = RBF(length_scale=[1.0, 2.0])
isotropic_model = GaussianProcessClassifier(kernel=isotropic_kernel)
anisotropic_model = GaussianProcessClassifier(kernel=anisotropic_kernel)
isotropic_model.fit(X_train, y_train)
anisotropic_model.fit(X_train, y_train)

# クラス確率を予測する
isotropic_y_prob = isotropic_model.predict_proba(X_test)
anisotropic_y_prob = anisotropic_model.predict_proba(X_test)
```
