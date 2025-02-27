# Additive Chi Squared (ACS)-Kernel-Approximation

Der ACS-Kernel ist ein Kernel für Histogramme, der in der Computer Vision häufig verwendet wird. Die AdditiveChi2Sampler-Klasse bietet eine approximative Abbildung für diesen Kernel.

Um AdditiveChi2Sampler zur Kernel-Approximation zu verwenden, führen Sie die folgenden Schritte aus:

1. Initialisieren Sie das AdditiveChi2Sampler-Objekt mit der gewünschten Anzahl von Proben (n) und dem Regularisierungsparameter (c).

```python
from sklearn.kernel_approximation import AdditiveChi2Sampler

n_samples = 1000
c = 1.0
additive_chi2_sampler = AdditiveChi2Sampler(n_samples=n_samples, sample_steps=2, sample_interval=2, sample_octave=2, c=c)
```

2. Passen Sie das AdditiveChi2Sampler-Objekt an Ihre Trainingsdaten an.

```python
additive_chi2_sampler.fit(X_train)
```

3. Transformieren Sie Ihre Trainings- und Testdaten mit dem AdditiveChi2Sampler-Objekt.

```python
X_train_transformed = additive_chi2_sampler.transform(X_train)
X_test_transformed = additive_chi2_sampler.transform(X_test)
```
