# Skewed Chi Squared (SCS)-Kernel-Approximation

Der SCS-Kernel ist eine Variante des exponentiierten chi quadrat-Kernels, der eine einfache Monte Carlo-Approximation der Merkmalsabbildung ermöglicht. Die SkewedChi2Sampler-Klasse bietet eine approximative Abbildung für diesen Kernel.

Um SkewedChi2Sampler zur Kernel-Approximation zu verwenden, führen Sie die folgenden Schritte aus:

1. Initialisieren Sie das SkewedChi2Sampler-Objekt mit der gewünschten Anzahl von Proben (n) und dem Regularisierungsparameter (c).

```python
from sklearn.kernel_approximation import SkewedChi2Sampler

n_samples = 1000
c = 1.0
skewed_chi2_sampler = SkewedChi2Sampler(n_samples=n_samples, sample_steps=2, sample_interval=2, sample_octave=1, c=c)
```

2. Passen Sie das SkewedChi2Sampler-Objekt an Ihre Trainingsdaten an.

```python
skewed_chi2_sampler.fit(X_train)
```

3. Transformieren Sie Ihre Trainings- und Testdaten mit dem SkewedChi2Sampler-Objekt.

```python
X_train_transformed = skewed_chi2_sampler.transform(X_train)
X_test_transformed = skewed_chi2_sampler.transform(X_test)
```
