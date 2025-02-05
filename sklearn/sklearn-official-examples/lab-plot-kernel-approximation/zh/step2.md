# 时间和准确率绘图

```python
# 要在此数据上应用分类器，我们需要将图像展平，
# 把数据转换为（样本数, 特征数）矩阵：
n_samples = len(digits.data)
data = digits.data / 16.0
data -= data.mean(axis=0)

# 我们在前半部分数字上学习数字特征
data_train, targets_train = (data[: n_samples // 2], digits.target[: n_samples // 2])

# 现在预测后半部分数字的值：
data_test, targets_test = (data[n_samples // 2 :], digits.target[n_samples // 2 :])

# 创建一个分类器：一个支持向量分类器
kernel_svm = svm.SVC(gamma=0.2)
linear_svm = svm.LinearSVC(dual="auto")

# 从核近似和线性支持向量机创建管道
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

# 使用线性和核支持向量机进行拟合和预测：
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

# 绘制结果：
plt.figure(figsize=(16, 4))
accuracy = plt.subplot(121)
# 第二个y轴用于时间
timescale = plt.subplot(122)

accuracy.plot(sample_sizes, nystroem_scores, label="Nystroem近似核")
timescale.plot(sample_sizes, nystroem_times, "--", label="Nystroem近似核")

accuracy.plot(sample_sizes, fourier_scores, label="傅里叶近似核")
timescale.plot(sample_sizes, fourier_times, "--", label="傅里叶近似核")

# 精确的rbf和线性核的水平线：
accuracy.plot([sample_sizes[0], sample_sizes[-1]], [linear_svm_score, linear_svm_score], label="线性支持向量机")
timescale.plot([sample_sizes[0], sample_sizes[-1]], [linear_svm_time, linear_svm_time], "--", label="线性支持向量机")

accuracy.plot([sample_sizes[0], sample_sizes[-1]], [kernel_svm_score, kernel_svm_score], label="rbf支持向量机")
timescale.plot([sample_sizes[0], sample_sizes[-1]], [kernel_svm_time, kernel_svm_time], "--", label="rbf支持向量机")

# 数据集维度 = 64的垂直线
accuracy.plot([64, 64], [0.7, 1], label="n_features")

# 图例和标签
accuracy.set_title("分类准确率")
timescale.set_title("训练时间")
accuracy.set_xlim(sample_sizes[0], sample_sizes[-1])
accuracy.set_xticks(())
accuracy.set_ylim(np.min(fourier_scores), 1)
timescale.set_xlabel("采样步数 = 变换后的特征维度")
accuracy.set_ylabel("分类准确率")
timescale.set_ylabel("训练时间（秒）")
accuracy.legend(loc="最佳")
timescale.legend(loc="最佳")
plt.tight_layout()
plt.show()
```
