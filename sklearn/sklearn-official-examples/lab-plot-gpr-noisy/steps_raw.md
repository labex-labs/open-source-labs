# Gaussian Process Regression

## Introduction

Gaussian process regression is a statistical modelling technique used to predict the outcome of a target variable based on input variables. The technique models the distribution of the target variable as a Gaussian process, which is a collection of random variables, any finite number of which have a joint Gaussian distribution. The technique is particularly useful in cases where the relationship between the input and target variables is non-linear.

In this lab, we will learn how to use Gaussian process regression with noise-level estimation in Python, using the scikit-learn library.

## Steps

### Step 1: Data Generation

In this step, we will generate some data with a single feature using a sine function.

```python
import numpy as np

def target_generator(X, add_noise=False):
    target = 0.5 + np.sin(3 * X)
    if add_noise:
        rng = np.random.RandomState(1)
        target += rng.normal(0, 0.3, size=target.shape)
    return target.squeeze()

X = np.linspace(0, 5, num=30).reshape(-1, 1)
y = target_generator(X, add_noise=False)
```

### Step 2: Data Visualization

In this step, we will visualize the generated data.

```python
import matplotlib.pyplot as plt

plt.plot(X, y, label="Expected signal")
plt.legend()
plt.xlabel("X")
_ = plt.ylabel("y")
```

### Step 3: Adding Noise

In this step, we will add some noise to the generated data to create a more realistic training dataset.

```python
rng = np.random.RandomState(0)
X_train = rng.uniform(0, 5, size=20).reshape(-1, 1)
y_train = target_generator(X_train, add_noise=True)
```

### Step 4: Data Visualization

In this step, we will visualize the noisy training dataset together with the expected signal.

```python
plt.plot(X, y, label="Expected signal")
plt.scatter(
    x=X_train[:, 0],
    y=y_train,
    color="black",
    alpha=0.4,
    label="Observations",
)
plt.legend()
plt.xlabel("X")
_ = plt.ylabel("y")
```

### Step 5: Gaussian Process Regression

In this step, we will create a Gaussian process regressor using an additive kernel adding a RBF and WhiteKernel kernels. The WhiteKernel is a kernel that will be able to estimate the amount of noise present in the data while the RBF will serve at fitting the non-linearity between the data and the target.

```python
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel

kernel = 1.0 * RBF(length_scale=1e-1, length_scale_bounds=(1e-2, 1e3)) + WhiteKernel(
    noise_level=1e-2, noise_level_bounds=(1e-10, 1e1)
)
gpr = GaussianProcessRegressor(kernel=kernel, alpha=0.0)
gpr.fit(X_train, y_train)
y_mean, y_std = gpr.predict(X, return_std=True)
```

### Step 6: Data Visualization

In this step, we will visualize the predictions made by the Gaussian process regressor.

```python
plt.plot(X, y, label="Expected signal")
plt.scatter(x=X_train[:, 0], y=y_train, color="black", alpha=0.4, label="Observations")
plt.errorbar(X, y_mean, y_std)
plt.legend()
plt.xlabel("X")
plt.ylabel("y")
_ = plt.title(
    (
        f"Initial: {kernel}\nOptimum: {gpr.kernel_}\nLog-Marginal-Likelihood: "
        f"{gpr.log_marginal_likelihood(gpr.kernel_.theta)}"
    ),
    fontsize=8,
)
```

### Step 7: Log-Marginal-Likelihood

In this step, we will inspect the Log-Marginal-Likelihood (LML) of GaussianProcessRegressor for different hyperparameters to get a sense of the local minima.

```python
from matplotlib.colors import LogNorm

length_scale = np.logspace(-2, 4, num=50)
noise_level = np.logspace(-2, 1, num=50)
length_scale_grid, noise_level_grid = np.meshgrid(length_scale, noise_level)

log_marginal_likelihood = [
    gpr.log_marginal_likelihood(theta=np.log([0.36, scale, noise]))
    for scale, noise in zip(length_scale_grid.ravel(), noise_level_grid.ravel())
]
log_marginal_likelihood = np.reshape(
    log_marginal_likelihood, newshape=noise_level_grid.shape
)

vmin, vmax = (-log_marginal_likelihood).min(), 50
level = np.around(np.logspace(np.log10(vmin), np.log10(vmax), num=50), decimals=1)
plt.contour(
    length_scale_grid,
    noise_level_grid,
    -log_marginal_likelihood,
    levels=level,
    norm=LogNorm(vmin=vmin, vmax=vmax),
)
plt.colorbar()
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Length-scale")
plt.ylabel("Noise-level")
plt.title("Log-marginal-likelihood")
plt.show()
```

### Step 8: Conclusion

In this lab, we learned how to use Gaussian process regression with noise-level estimation in Python, using the scikit-learn library. We generated some data with a single feature using a sine function, added some noise to the generated data to create a more realistic training dataset, and visualized the generated data. We created a Gaussian process regressor using an additive kernel adding a RBF and WhiteKernel kernels, and visualized the predictions made by the Gaussian process regressor. We also inspected the Log-Marginal-Likelihood (LML) of GaussianProcessRegressor for different hyperparameters to get a sense of the local minima.
