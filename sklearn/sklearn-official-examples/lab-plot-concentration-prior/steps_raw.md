# Concentration Prior Type Analysis of Variation Bayesian Gaussian Mixture

## Introduction

This lab demonstrates how to use the scikit-learn `BayesianGaussianMixture` class to fit a toy dataset containing a mixture of three Gaussians. The class can adapt its number of mixture components automatically using a concentration prior, which is specified using the `weight_concentration_prior_type` parameter. This lab shows the difference between using a Dirichlet distribution prior and a Dirichlet process prior to select the number of components with non-zero weights.

## Steps

### Step 1: Import Libraries

In this step, we will import the necessary libraries, which are `numpy`, `matplotlib`, `gridspec`, and `BayesianGaussianMixture` from `sklearn.mixture`.

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from sklearn.mixture import BayesianGaussianMixture
```

### Step 2: Define Functions

In this step, we define two functions. The first function plots ellipsoids obtained from the toy dataset fitted by the `BayesianGaussianMixture` class models. The second function plots the results for three different values of the weight concentration prior.

```python
def plot_ellipses(ax, weights, means, covars):
    for n in range(means.shape[0]):
        eig_vals, eig_vecs = np.linalg.eigh(covars[n])
        unit_eig_vec = eig_vecs[0] / np.linalg.norm(eig_vecs[0])
        angle = np.arctan2(unit_eig_vec[1], unit_eig_vec[0])
        angle = 180 * angle / np.pi
        eig_vals = 2 * np.sqrt(2) * np.sqrt(eig_vals)
        ell = mpl.patches.Ellipse(
            means[n], eig_vals[0], eig_vals[1], angle=180 + angle, edgecolor="black"
        )
        ell.set_clip_box(ax.bbox)
        ell.set_alpha(weights[n])
        ell.set_facecolor("#56B4E9")
        ax.add_artist(ell)

def plot_results(ax1, ax2, estimator, X, y, title, plot_title=False):
    ax1.set_title(title)
    ax1.scatter(X[:, 0], X[:, 1], s=5, marker="o", color=colors[y], alpha=0.8)
    ax1.set_xlim(-2.0, 2.0)
    ax1.set_ylim(-3.0, 3.0)
    ax1.set_xticks(())
    ax1.set_yticks(())
    plot_ellipses(ax1, estimator.weights_, estimator.means_, estimator.covariances_)

    ax2.get_xaxis().set_tick_params(direction="out")
    ax2.yaxis.grid(True, alpha=0.7)
    for k, w in enumerate(estimator.weights_):
        ax2.bar(
            k,
            w,
            width=0.9,
            color="#56B4E9",
            zorder=3,
            align="center",
            edgecolor="black",
        )
        ax2.text(k, w + 0.007, "%.1f%%" % (w * 100.0), horizontalalignment="center")
    ax2.set_xlim(-0.6, 2 * n_components - 0.4)
    ax2.set_ylim(0.0, 1.1)
    ax2.tick_params(axis="y", which="both", left=False, right=False, labelleft=False)
    ax2.tick_params(axis="x", which="both", top=False)
    if plot_title:
        ax1.set_ylabel("Estimated Mixtures")
        ax2.set_ylabel("Weight of each component")
```

### Step 3: Set Parameters for the Toy Dataset

In this step, we set the parameters for the toy dataset, which include the random state, number of components, number of features, colors, covariances, samples, and means.

```python
random_state, n_components, n_features = 2, 3, 2
colors = np.array(["#0072B2", "#F0E442", "#D55E00"])
covars = np.array(
    [[[0.7, 0.0], [0.0, 0.1]], [[0.5, 0.0], [0.0, 0.1]], [[0.5, 0.0], [0.0, 0.1]]]
)
samples = np.array([200, 500, 200])
means = np.array([[0.0, -0.70], [0.0, 0.0], [0.0, 0.70]])
```

### Step 4: Define Estimators

In this step, we define two estimators. The first estimator uses a Dirichlet distribution prior to set the number of components with non-zero weights. The second estimator uses a Dirichlet process prior to select the number of components.

```python
estimators = [
    (
        "Finite mixture with a Dirichlet distribution\nprior and " r"$\gamma_0=$",
        BayesianGaussianMixture(
            weight_concentration_prior_type="dirichlet_distribution",
            n_components=2 * n_components,
            reg_covar=0,
            init_params="random",
            max_iter=1500,
            mean_precision_prior=0.8,
            random_state=random_state,
        ),
        [0.001, 1, 1000],
    ),
    (
        "Infinite mixture with a Dirichlet process\n prior and" r"$\gamma_0=$",
        BayesianGaussianMixture(
            weight_concentration_prior_type="dirichlet_process",
            n_components=2 * n_components,
            reg_covar=0,
            init_params="random",
            max_iter=1500,
            mean_precision_prior=0.8,
            random_state=random_state,
        ),
        [1, 1000, 100000],
    ),
]
```

### Step 5: Generate Data

In this step, we generate data using the `numpy.random.RandomState` function and the parameters defined in Step 3.

```python
rng = np.random.RandomState(random_state)
X = np.vstack(
    [
        rng.multivariate_normal(means[j], covars[j], samples[j])
        for j in range(n_components)
    ]
)
y = np.concatenate([np.full(samples[j], j, dtype=int) for j in range(n_components)])
```

### Step 6: Plot Results

In this step, we plot the results for each estimator using the `plot_results` function defined in Step 2.

```python
for title, estimator, concentrations_prior in estimators:
    plt.figure(figsize=(4.7 * 3, 8))
    plt.subplots_adjust(
        bottom=0.04, top=0.90, hspace=0.05, wspace=0.05, left=0.03, right=0.99
    )

    gs = gridspec.GridSpec(3, len(concentrations_prior))
    for k, concentration in enumerate(concentrations_prior):
        estimator.weight_concentration_prior = concentration
        estimator.fit(X)
        plot_results(
            plt.subplot(gs[0:2, k]),
            plt.subplot(gs[2, k]),
            estimator,
            X,
            y,
            r"%s$%.1e$" % (title, concentration),
            plot_title=k == 0,
        )

plt.show()
```

## Summary

This lab demonstrated how to use the `BayesianGaussianMixture` class in scikit-learn to fit a toy dataset containing a mixture of three Gaussians. The class can adapt its number of mixture components automatically using a concentration prior, which is specified using the `weight_concentration_prior_type` parameter. This lab showed the difference between using a Dirichlet distribution prior and a Dirichlet process prior to select the number of components with non-zero weights.
