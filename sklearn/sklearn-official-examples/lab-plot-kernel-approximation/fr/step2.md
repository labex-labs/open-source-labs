# Courbes de temps d'exécution et de précision

```python
# Pour appliquer un classifieur sur ces données, nous devons aplatir l'image, pour
# transformer les données en une matrice (échantillons, caractéristiques) :
n_samples = len(digits.data)
data = digits.data / 16.0
data -= data.mean(axis=0)

# Nous apprenons les chiffres sur la première moitié des chiffres
data_train, targets_train = (data[: n_samples // 2], digits.target[: n_samples // 2])

# Maintenant, prédisons la valeur du chiffre sur la deuxième moitié :
data_test, targets_test = (data[n_samples // 2 :], digits.target[n_samples // 2 :])

# Créez un classifieur : un classifieur à vecteurs de support
kernel_svm = svm.SVC(gamma=0.2)
linear_svm = svm.LinearSVC(dual="auto")

# créez un pipeline à partir d'une approximation de noyau et d'un svm linéaire
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

# ajustez et prédisez en utilisant svm linéaire et svm à noyau :
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

# tracez les résultats :
plt.figure(figsize=(16, 4))
accuracy = plt.subplot(121)
# deuxième axe y pour les temps d'exécution
timescale = plt.subplot(122)

accuracy.plot(sample_sizes, nystroem_scores, label="Approx. noyau Nystroem")
timescale.plot(sample_sizes, nystroem_times, "--", label="Approx. noyau Nystroem")

accuracy.plot(sample_sizes, fourier_scores, label="Approx. noyau Fourier")
timescale.plot(sample_sizes, fourier_times, "--", label="Approx. noyau Fourier")

# lignes horizontales pour les noyaux rbf et linéaires exacts :
accuracy.plot([sample_sizes[0], sample_sizes[-1]], [linear_svm_score, linear_svm_score], label="svm linéaire")
timescale.plot([sample_sizes[0], sample_sizes[-1]], [linear_svm_time, linear_svm_time], "--", label="svm linéaire")

accuracy.plot([sample_sizes[0], sample_sizes[-1]], [kernel_svm_score, kernel_svm_score], label="svm rbf")
timescale.plot([sample_sizes[0], sample_sizes[-1]], [kernel_svm_time, kernel_svm_time], "--", label="svm rbf")

# ligne verticale pour la dimensionnalité du jeu de données = 64
accuracy.plot([64, 64], [0.7, 1], label="n_features")

# légendes et étiquettes
accuracy.set_title("Précision de la classification")
timescale.set_title("Temps d'entraînement")
accuracy.set_xlim(sample_sizes[0], sample_sizes[-1])
accuracy.set_xticks(())
accuracy.set_ylim(np.min(fourier_scores), 1)
timescale.set_xlabel("Étapes d'échantillonnage = dimension de la caractéristique transformée")
accuracy.set_ylabel("Précision de la classification")
timescale.set_ylabel("Temps d'entraînement en secondes")
accuracy.legend(loc="best")
timescale.legend(loc="best")
plt.tight_layout()
plt.show()
```
