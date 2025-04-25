# 計測時間と精度のプロット

```python
# このデータに分類器を適用するには、画像をフラット化して
# データを (サンプル数，特徴量) の行列に変換する必要があります。
n_samples = len(digits.data)
data = digits.data / 16.0
data -= data.mean(axis=0)

# 最初の半分の手書き数字で学習します
data_train, targets_train = (data[: n_samples // 2], digits.target[: n_samples // 2])

# 次に、後半の手書き数字の値を予測します：
data_test, targets_test = (data[n_samples // 2 :], digits.target[n_samples // 2 :])

# 分類器を作成します：サポートベクトル分類器
kernel_svm = svm.SVC(gamma=0.2)
linear_svm = svm.LinearSVC(dual="auto")

# カーネル近似と線形 SVM からパイプラインを作成します
feature_map_fourier = RBFSampler(gamma=0.2, random_state=1)
feature_map_nystroem = Nystroem(gamma=0.2, random_state=1)

fourier_approx_svm = pipeline.Pipeline([
  ("feature_map", feature_map_fourier),
  ("svm", svm.LinearSVC(dual="auto"))
])

nystroem_approx_svm = pipeline.Pipeline([
  ("feature_map", feature_map_nystroem),
  ("svm", svm.LinearSVC(dual="auto"))
])

# 線形およびカーネル SVM を使って学習と予測を行います：
kernel_svm_time = time()
kernel_svm.fit(data_train, targets_train)
kernel_svm_score = kernel_svm.score(data_test, targets_test)
kernel_svm_time = time() - kernel_svm_time

linear_svm_time = time()
linear_svm.fit(data_train, targets_train)
linear_svm_score = linear_svm.score(data_test, targets_test)
linear_svm_time = time() - linear_svm_time

sample_sizes = 30 * np.arange(1, 10)
fourier_scores = []
nystroem_scores = []
fourier_times = []
nystroem_times = []

for D in sample_sizes:
  fourier_approx_svm.set_params(feature_map__n_components=D)
  nystroem_approx_svm.set_params(feature_map__n_components=D)

  start = time()
  nystroem_approx_svm.fit(data_train, targets_train)
  nystroem_times.append(time() - start)

  start = time()
  fourier_approx_svm.fit(data_train, targets_train)
  fourier_times.append(time() - start)

  fourier_score = fourier_approx_svm.score(data_test, targets_test)
  nystroem_score = nystroem_approx_svm.score(data_test, targets_test)
  nystroem_scores.append(nystroem_score)
  fourier_scores.append(fourier_score)

# 結果をプロットします：
plt.figure(figsize=(16, 4))
accuracy = plt.subplot(121)
# 計測時間用の 2 番目の y 軸
timescale = plt.subplot(122)

accuracy.plot(sample_sizes, nystroem_scores, label="Nystroem 近似カーネル")
timescale.plot(sample_sizes, nystroem_times, "--", label="Nystroem 近似カーネル")

accuracy.plot(sample_sizes, fourier_scores, label="Fourier 近似カーネル")
timescale.plot(sample_sizes, fourier_times, "--", label="Fourier 近似カーネル")

# 正確な RBF と線形カーネル用の水平線：
accuracy.plot([sample_sizes[0], sample_sizes[-1]], [linear_svm_score, linear_svm_score], label="線形 SVM")
timescale.plot([sample_sizes[0], sample_sizes[-1]], [linear_svm_time, linear_svm_time], "--", label="線形 SVM")

accuracy.plot([sample_sizes[0], sample_sizes[-1]], [kernel_svm_score, kernel_svm_score], label="RBF SVM")
timescale.plot([sample_sizes[0], sample_sizes[-1]], [kernel_svm_time, kernel_svm_time], "--", label="RBF SVM")

# データセット次元 = 64 の垂直線
accuracy.plot([64, 64], [0.7, 1], label="n_features")

# 凡例とラベル
accuracy.set_title("分類精度")
timescale.set_title("学習時間")
accuracy.set_xlim(sample_sizes[0], sample_sizes[-1])
accuracy.set_xticks(())
accuracy.set_ylim(np.min(fourier_scores), 1)
timescale.set_xlabel("サンプリングステップ = 変換された特徴次元")
accuracy.set_ylabel("分類精度")
timescale.set_ylabel("秒単位の学習時間")
accuracy.legend(loc="best")
timescale.legend(loc="best")
plt.tight_layout()
plt.show()
```
