# Gráficos de Tempo e Precisão

```python
# Para aplicar um classificador a estes dados, precisamos achatá-los para
# transformar os dados numa matriz (amostras, características):
n_samples = len(digits.data)
data = digits.data / 16.0
data -= data.mean(axis=0)

# Aprendemos os dígitos na primeira metade dos dígitos
data_train, targets_train = (data[: n_samples // 2], digits.target[: n_samples // 2])

# Agora prevemos o valor do dígito na segunda metade:
data_test, targets_test = (data[n_samples // 2 :], digits.target[n_samples // 2 :])

# Criamos um classificador: um classificador de vetores de suporte
kernel_svm = svm.SVC(gamma=0.2)
linear_svm = svm.LinearSVC(dual="auto")

# Criamos um pipeline a partir da aproximação do kernel e da svm linear
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

# Ajustar e prever usando svm linear e kernel:
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

# plotar os resultados:
plt.figure(figsize=(16, 4))
accuracy = plt.subplot(121)
# segundo eixo y para tempos
timescale = plt.subplot(122)

accuracy.plot(sample_sizes, nystroem_scores, label="kernel aproximado Nystroem")
timescale.plot(sample_sizes, nystroem_times, "--", label="kernel aproximado Nystroem")

accuracy.plot(sample_sizes, fourier_scores, label="kernel aproximado Fourier")
timescale.plot(sample_sizes, fourier_times, "--", label="kernel aproximado Fourier")

# linhas horizontais para kernels rbf e lineares exatos:
accuracy.plot([sample_sizes[0], sample_sizes[-1]], [linear_svm_score, linear_svm_score], label="svm linear")
timescale.plot([sample_sizes[0], sample_sizes[-1]], [linear_svm_time, linear_svm_time], "--", label="svm linear")

accuracy.plot([sample_sizes[0], sample_sizes[-1]], [kernel_svm_score, kernel_svm_score], label="svm rbf")
timescale.plot([sample_sizes[0], sample_sizes[-1]], [kernel_svm_time, kernel_svm_time], "--", label="svm rbf")

# linha vertical para dimensionalidade do conjunto de dados = 64
accuracy.plot([64, 64], [0.7, 1], label="n_features")

# legendas e rótulos
accuracy.set_title("Precisão de classificação")
timescale.set_title("Tempos de treino")
accuracy.set_xlim(sample_sizes[0], sample_sizes[-1])
accuracy.set_xticks(())
accuracy.set_ylim(np.min(fourier_scores), 1)
timescale.set_xlabel("Passos de amostragem = dimensão da característica transformada")
accuracy.set_ylabel("Precisão de classificação")
timescale.set_ylabel("Tempo de treino em segundos")
accuracy.legend(loc="best")
timescale.legend(loc="best")
plt.tight_layout()
plt.show()
```
