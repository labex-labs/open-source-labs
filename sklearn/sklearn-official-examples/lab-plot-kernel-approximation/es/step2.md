# Gráficos de tiempos y precisión

```python
# Para aplicar un clasificador a estos datos, necesitamos aplanar la imagen, para
# convertir los datos en una matriz (muestras, características):
n_samples = len(digits.data)
data = digits.data / 16.0
data -= data.mean(axis=0)

# Aprendemos los dígitos en la primera mitad de los dígitos
data_train, targets_train = (data[: n_samples // 2], digits.target[: n_samples // 2])

# Ahora predecimos el valor del dígito en la segunda mitad:
data_test, targets_test = (data[n_samples // 2 :], digits.target[n_samples // 2 :])

# Creamos un clasificador: un clasificador de vectores de soporte
kernel_svm = svm.SVC(gamma=0.2)
linear_svm = svm.LinearSVC(dual="auto")

# crear pipeline a partir de la aproximación del kernel y el svm lineal
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

# ajustar y predecir utilizando svm lineal y con kernel:
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

# graficar los resultados:
plt.figure(figsize=(16, 4))
accuracy = plt.subplot(121)
# segundo eje y para los tiempos
timescale = plt.subplot(122)

accuracy.plot(sample_sizes, nystroem_scores, label="Aprox. kernel de Nystroem")
timescale.plot(sample_sizes, nystroem_times, "--", label="Aprox. kernel de Nystroem")

accuracy.plot(sample_sizes, fourier_scores, label="Aprox. kernel de Fourier")
timescale.plot(sample_sizes, fourier_times, "--", label="Aprox. kernel de Fourier")

# líneas horizontales para los kernels rbf y lineal exactos:
accuracy.plot([sample_sizes[0], sample_sizes[-1]], [linear_svm_score, linear_svm_score], label="svm lineal")
timescale.plot([sample_sizes[0], sample_sizes[-1]], [linear_svm_time, linear_svm_time], "--", label="svm lineal")

accuracy.plot([sample_sizes[0], sample_sizes[-1]], [kernel_svm_score, kernel_svm_score], label="svm rbf")
timescale.plot([sample_sizes[0], sample_sizes[-1]], [kernel_svm_time, kernel_svm_time], "--", label="svm rbf")

# línea vertical para la dimensionalidad del conjunto de datos = 64
accuracy.plot([64, 64], [0.7, 1], label="n_features")

# leyendas y etiquetas
accuracy.set_title("Precisión de clasificación")
timescale.set_title("Tiempos de entrenamiento")
accuracy.set_xlim(sample_sizes[0], sample_sizes[-1])
accuracy.set_xticks(())
accuracy.set_ylim(np.min(fourier_scores), 1)
timescale.set_xlabel("Pasos de muestreo = dimensión de la característica transformada")
accuracy.set_ylabel("Precisión de clasificación")
timescale.set_ylabel("Tiempo de entrenamiento en segundos")
accuracy.legend(loc="best")
timescale.legend(loc="best")
plt.tight_layout()
plt.show()
```
