# Blind Source Separation

## Introduction

In this lab, we will use FastICA to perform blind source separation on a mixed signal. Blind source separation is a technique used to separate mixed signals into their original independent components. This is useful in various fields such as signal processing, image processing, and data analysis. We will use Python's scikit-learn library to perform ICA and PCA on a sample mixed signal.

## Steps

### Step 1: Generate Sample Data

We will generate a sample mixed signal consisting of three independent components. We will add noise to the signal and standardize the data. We will also generate a mixing matrix to mix our three independent components.

```python
import numpy as np
from scipy import signal

np.random.seed(0)
n_samples = 2000
time = np.linspace(0, 8, n_samples)

s1 = np.sin(2 * time)  # Signal 1 : sinusoidal signal
s2 = np.sign(np.sin(3 * time))  # Signal 2 : square signal
s3 = signal.sawtooth(2 * np.pi * time)  # Signal 3: saw tooth signal

S = np.c_[s1, s2, s3]
S += 0.2 * np.random.normal(size=S.shape)  # Add noise

S /= S.std(axis=0)  # Standardize data
# Mix data
A = np.array([[1, 1, 1], [0.5, 2, 1.0], [1.5, 1.0, 2.0]])  # Mixing matrix
X = np.dot(S, A.T)  # Generate observations
```

### Step 2: Fit ICA and PCA Models

We will use FastICA to estimate the independent sources. We will then compute PCA for comparison.

```python
from sklearn.decomposition import FastICA, PCA

# Compute ICA
ica = FastICA(n_components=3, whiten="arbitrary-variance")
S_ = ica.fit_transform(X)  # Reconstruct signals
A_ = ica.mixing_  # Get estimated mixing matrix

# We can `prove` that the ICA model applies by reverting the unmixing.
assert np.allclose(X, np.dot(S_, A_.T) + ica.mean_)

# For comparison, compute PCA
pca = PCA(n_components=3)
H = pca.fit_transform(X)  # Reconstruct signals based on orthogonal components
```

### Step 3: Plot Results

We will plot the original mixed signal, the original independent sources, the sources estimated by ICA, and the sources estimated by PCA.

```python
import matplotlib.pyplot as plt

plt.figure()

models = [X, S, S_, H]
names = [
    "Observations (mixed signal)",
    "True Sources",
    "ICA recovered signals",
    "PCA recovered signals",
]
colors = ["red", "steelblue", "orange"]

for ii, (model, name) in enumerate(zip(models, names), 1):
    plt.subplot(4, 1, ii)
    plt.title(name)
    for sig, color in zip(model.T, colors):
        plt.plot(sig, color=color)

plt.tight_layout()
plt.show()
```

## Summary

We have successfully performed blind source separation on a mixed signal using FastICA and PCA. We generated a sample mixed signal consisting of three independent components, added noise, and standardized the data. We then generated a mixing matrix to mix our independent components. We used FastICA to estimate the independent sources and computed PCA for comparison. Finally, we plotted the original mixed signal, the original independent sources, the sources estimated by ICA, and the sources estimated by PCA.
