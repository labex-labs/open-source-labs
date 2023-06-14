# Timing and Accuracy Plots

```python
# To apply an classifier on this data, we need to flatten the image, to
# turn the data in a (samples, feature) matrix:
n_samples = len(digits.data)
data = digits.data / 16.0
data -= data.mean(axis=0)

# We learn the digits on the first half of the digits
data_train, targets_train = (data[: n_samples // 2], digits.target[: n_samples // 2])

# Now predict the value of the digit on the second half:
data_test, targets_test = (data[n_samples // 2 :], digits.target[n_samples // 2 :])

# Create a classifier: a support vector classifier
kernel_svm = svm.SVC(gamma=0.2)
linear_svm = svm.LinearSVC(dual="auto")

# create pipeline from kernel approximation and linear svm
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

# fit and predict using linear and kernel svm:
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

# plot the results:
plt.figure(figsize=(16, 4))
accuracy = plt.subplot(121)
# second y axis for timings
timescale = plt.subplot(122)

accuracy.plot(sample_sizes, nystroem_scores, label="Nystroem approx. kernel")
timescale.plot(sample_sizes, nystroem_times, "--", label="Nystroem approx. kernel")

accuracy.plot(sample_sizes, fourier_scores, label="Fourier approx. kernel")
timescale.plot(sample_sizes, fourier_times, "--", label="Fourier approx. kernel")

# horizontal lines for exact rbf and linear kernels:
accuracy.plot([sample_sizes[0], sample_sizes[-1]], [linear_svm_score, linear_svm_score], label="linear svm")
timescale.plot([sample_sizes[0], sample_sizes[-1]], [linear_svm_time, linear_svm_time], "--", label="linear svm")

accuracy.plot([sample_sizes[0], sample_sizes[-1]], [kernel_svm_score, kernel_svm_score], label="rbf svm")
timescale.plot([sample_sizes[0], sample_sizes[-1]], [kernel_svm_time, kernel_svm_time], "--", label="rbf svm")

# vertical line for dataset dimensionality = 64
accuracy.plot([64, 64], [0.7, 1], label="n_features")

# legends and labels
accuracy.set_title("Classification accuracy")
timescale.set_title("Training times")
accuracy.set_xlim(sample_sizes[0], sample_sizes[-1])
accuracy.set_xticks(())
accuracy.set_ylim(np.min(fourier_scores), 1)
timescale.set_xlabel("Sampling steps = transformed feature dimension")
accuracy.set_ylabel("Classification accuracy")
timescale.set_ylabel("Training time in seconds")
accuracy.legend(loc="best")
timescale.legend(loc="best")
plt.tight_layout()
plt.show()
```


