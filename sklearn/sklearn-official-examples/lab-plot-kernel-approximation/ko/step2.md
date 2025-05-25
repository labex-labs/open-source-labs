# 시간 및 정확도 플롯

```python
# 이 데이터에 분류기를 적용하려면 이미지를 평면화하여 데이터를 (샘플, 특징) 행렬로 변환해야 합니다.
n_samples = len(digits.data)
data = digits.data / 16.0
data -= data.mean(axis=0)

# 숫자를 첫 번째 절반에서 학습합니다.
data_train, targets_train = (data[: n_samples // 2], digits.target[: n_samples // 2])

# 이제 두 번째 절반의 숫자 값을 예측합니다.
data_test, targets_test = (data[n_samples // 2 :], digits.target[n_samples // 2 :])

# 분류기 (지지 벡터 분류기) 를 만듭니다.
kernel_svm = svm.SVC(gamma=0.2)
linear_svm = svm.LinearSVC(dual="auto")

# 커널 근사 및 선형 SVM 의 파이프라인을 만듭니다.
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

# 선형 및 커널 SVM 을 사용하여 맞추고 예측합니다.
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

# 결과를 플롯합니다.
plt.figure(figsize=(16, 4))
accuracy = plt.subplot(121)
# 시간 측정을 위한 두 번째 y 축
timescale = plt.subplot(122)

accuracy.plot(sample_sizes, nystroem_scores, label="Nystroem 근사 커널")
timescale.plot(sample_sizes, nystroem_times, "--", label="Nystroem 근사 커널")

accuracy.plot(sample_sizes, fourier_scores, label="Fourier 근사 커널")
timescale.plot(sample_sizes, fourier_times, "--", label="Fourier 근사 커널")

# 정확한 rbf 및 선형 커널에 대한 수평선
accuracy.plot([sample_sizes[0], sample_sizes[-1]], [linear_svm_score, linear_svm_score], label="선형 SVM")
timescale.plot([sample_sizes[0], sample_sizes[-1]], [linear_svm_time, linear_svm_time], "--", label="선형 SVM")

accuracy.plot([sample_sizes[0], sample_sizes[-1]], [kernel_svm_score, kernel_svm_score], label="rbf SVM")
timescale.plot([sample_sizes[0], sample_sizes[-1]], [kernel_svm_time, kernel_svm_time], "--", label="rbf SVM")

# 데이터 차원 = 64 에 대한 수직선
accuracy.plot([64, 64], [0.7, 1], label="n_features")

# 범례 및 레이블
accuracy.set_title("분류 정확도")
timescale.set_title("훈련 시간")
accuracy.set_xlim(sample_sizes[0], sample_sizes[-1])
accuracy.set_xticks(())
accuracy.set_ylim(np.min(fourier_scores), 1)
timescale.set_xlabel("샘플링 단계 = 변환된 특징 차원")
accuracy.set_ylabel("분류 정확도")
timescale.set_ylabel("초 단위 훈련 시간")
accuracy.legend(loc="best")
timescale.legend(loc="best")
plt.tight_layout()
plt.show()
```
