# Zeit- und Genauigkeitsplots

```python
# Um einen Klassifizierer auf diesen Daten anzuwenden, müssen wir das Bild flachmachen, um
# die Daten in eine (Samples, Feature)-Matrix zu verwandeln:
n_samples = len(digits.data)
data = digits.data / 16.0
data -= data.mean(axis=0)

# Wir lernen die Ziffern auf der ersten Hälfte der Ziffern
data_train, targets_train = (data[: n_samples // 2], digits.target[: n_samples // 2])

# Nun predizieren wir den Wert der Ziffer auf der zweiten Hälfte:
data_test, targets_test = (data[n_samples // 2 :], digits.target[n_samples // 2 :])

# Erstellen eines Klassifizierers: eines Support-Vector-Klassifizierers
kernel_svm = svm.SVC(gamma=0.2)
linear_svm = svm.LinearSVC(dual="auto")

# Erstellen eines Pipelines aus Kernel-Approximation und linearem SVM
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

# Anpassen und Vorhersagen mit linearem und kernelisiertem SVM:
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

# Plotten der Ergebnisse:
plt.figure(figsize=(16, 4))
accuracy = plt.subplot(121)
# Zweite y-Achse für Zeitmessungen
timescale = plt.subplot(122)

accuracy.plot(sample_sizes, nystroem_scores, label="Nystroem approx. kernel")
timescale.plot(sample_sizes, nystroem_times, "--", label="Nystroem approx. kernel")

accuracy.plot(sample_sizes, fourier_scores, label="Fourier approx. kernel")
timescale.plot(sample_sizes, fourier_times, "--", label="Fourier approx. kernel")

# Horizontale Linien für exakte rbf- und lineare Kerne:
accuracy.plot([sample_sizes[0], sample_sizes[-1]], [linear_svm_score, linear_svm_score], label="linear svm")
timescale.plot([sample_sizes[0], sample_sizes[-1]], [linear_svm_time, linear_svm_time], "--", label="linear svm")

accuracy.plot([sample_sizes[0], sample_sizes[-1]], [kernel_svm_score, kernel_svm_score], label="rbf svm")
timescale.plot([sample_sizes[0], sample_sizes[-1]], [kernel_svm_time, kernel_svm_time], "--", label="rbf svm")

# Vertikale Linie für die Datenmenge = 64
accuracy.plot([64, 64], [0.7, 1], label="n_features")

# Legenden und Beschriftungen
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
