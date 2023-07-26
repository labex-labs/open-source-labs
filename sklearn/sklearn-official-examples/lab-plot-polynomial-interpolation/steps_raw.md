# Polynomial and Spline Interpolation

## Introduction

In this lab, we will learn how to approximate a function with polynomials up to a certain degree using ridge regression. We will show two different ways of doing this given `n_samples` of 1d points `x_i`:

1. `PolynomialFeatures`: generates all monomials up to a specified degree. This gives us the Vandermonde matrix with `n_samples` rows and `degree + 1` columns.
2. `SplineTransformer`: generates B-spline basis functions. A basis function of a B-spline is a piece-wise polynomial function of degree `degree` that is non-zero only between `degree+1` consecutive knots.

We will use the `make_pipeline` function to add non-linear features and show how these transformers are well-suited to model non-linear effects with a linear model. We will plot the function, training points, and the interpolation using polynomial features and B-splines. We will also plot all columns of both transformers separately and show the knots of spline. Finally, we will demonstrate the use of periodic splines.

## Steps

### Step 1: Prepare the Data

We start by defining a function that we intend to approximate and prepare plotting it.

```python
def f(x):
    """Function to be approximated by polynomial interpolation."""
    return x * np.sin(x)

# whole range we want to plot
x_plot = np.linspace(-1, 11, 100)

# To make it interesting, we only give a small subset of points to train on.
x_train = np.linspace(0, 10, 100)
rng = np.random.RandomState(0)
x_train = np.sort(rng.choice(x_train, size=20, replace=False))
y_train = f(x_train)

# create 2D-array versions of these arrays to feed to transformers
X_train = x_train[:, np.newaxis]
X_plot = x_plot[:, np.newaxis]
```

### Step 2: Polynomial Features Interpolation

We will use `PolynomialFeatures` to generate polynomial features and fit a ridge regression model to the training data. Then we plot the function, training points, and the interpolation using polynomial features.

```python
# plot function
lw = 2
fig, ax = plt.subplots()
ax.set_prop_cycle(
    color=["black", "teal", "yellowgreen", "gold", "darkorange", "tomato"]
)
ax.plot(x_plot, f(x_plot), linewidth=lw, label="ground truth")

# plot training points
ax.scatter(x_train, y_train, label="training points")

# polynomial features
for degree in [3, 4, 5]:
    model = make_pipeline(PolynomialFeatures(degree), Ridge(alpha=1e-3))
    model.fit(X_train, y_train)
    y_plot = model.predict(X_plot)
    ax.plot(x_plot, y_plot, label=f"degree {degree}")

ax.legend(loc="lower center")
ax.set_ylim(-20, 10)
plt.show()
```

### Step 3: B-Spline Interpolation

We will use `SplineTransformer` to generate B-spline basis functions and fit a ridge regression model to the training data. Then we plot the function, training points, and the interpolation using B-splines.

```python
# B-spline with 4 + 3 - 1 = 6 basis functions
model = make_pipeline(SplineTransformer(n_knots=4, degree=3), Ridge(alpha=1e-3))
model.fit(X_train, y_train)

y_plot = model.predict(X_plot)
ax.plot(x_plot, y_plot, label="B-spline")
ax.legend(loc="lower center")
ax.set_ylim(-20, 10)
plt.show()
```

### Step 4: Plotting the Transformers

We plot all columns of both transformers separately to give more insights into the generated feature bases.

```python
fig, axes = plt.subplots(ncols=2, figsize=(16, 5))
pft = PolynomialFeatures(degree=3).fit(X_train)
axes[0].plot(x_plot, pft.transform(X_plot))
axes[0].legend(axes[0].lines, [f"degree {n}" for n in range(4)])
axes[0].set_title("PolynomialFeatures")

splt = SplineTransformer(n_knots=4, degree=3).fit(X_train)
axes[1].plot(x_plot, splt.transform(X_plot))
axes[1].legend(axes[1].lines, [f"spline {n}" for n in range(6)])
axes[1].set_title("SplineTransformer")

# plot knots of spline
knots = splt.bsplines_[0].t
axes[1].vlines(knots[3:-3], ymin=0, ymax=0.8, linestyles="dashed")
plt.show()
```

### Step 5: Periodic Splines

We demonstrate the use of periodic splines by using the `SplineTransformer` and manually specifying the knots. We fit a ridge regression model to the training data and plot the function, training points, and the interpolation using periodic splines.

```python
def g(x):
    """Function to be approximated by periodic spline interpolation."""
    return np.sin(x) - 0.7 * np.cos(x * 3)


y_train = g(x_train)

# Extend the test data into the future:
x_plot_ext = np.linspace(-1, 21, 200)
X_plot_ext = x_plot_ext[:, np.newaxis]

lw = 2
fig, ax = plt.subplots()
ax.set_prop_cycle(color=["black", "tomato", "teal"])
ax.plot(x_plot_ext, g(x_plot_ext), linewidth=lw, label="ground truth")
ax.scatter(x_train, y_train, label="training points")

for transformer, label in [
    (SplineTransformer(degree=3, n_knots=10), "spline"),
    (
        SplineTransformer(
            degree=3,
            knots=np.linspace(0, 2 * np.pi, 10)[:, None],
            extrapolation="periodic",
        ),
        "periodic spline",
    ),
]:
    model = make_pipeline(transformer, Ridge(alpha=1e-3))
    model.fit(X_train, y_train)
    y_plot_ext = model.predict(X_plot_ext)
    ax.plot(x_plot_ext, y_plot_ext, label=label)

ax.legend()
fig.show()
```

### Summary

In this lab, we learned how to approximate a function with polynomials up to a certain degree using ridge regression. We showed two different ways of doing this given `n_samples` of 1d points `x_i`. We used `make_pipeline` function to add non-linear features and demonstrated how these transformers are well-suited to model non-linear effects with a linear model. We plotted the function, training points, and the interpolation using polynomial features and B-splines. We also plotted all columns of both transformers separately and showed the knots of spline. Finally, we demonstrated the use of periodic splines.
