# Plotting 1D Density Example

We will plot a 1D density example with 100 samples in one dimension. We will compare three different kernel density estimations: tophat, Gaussian, and epanechnikov.

```python
# Generate data
N = 100
np.random.seed(1)
X = np.concatenate(
    (np.random.normal(0, 1, int(0.3 * N)), np.random.normal(5, 1, int(0.7 * N)))
)[:, np.newaxis]

X_plot = np.linspace(-5, 10, 1000)[:, np.newaxis]

true_dens = 0.3 * norm(0, 1).pdf(X_plot[:, 0]) + 0.7 * norm(5, 1).pdf(X_plot[:, 0])

# Create figure and axes
fig, ax = plt.subplots()

# Plot input distribution
ax.fill(X_plot[:, 0], true_dens, fc="black", alpha=0.2, label="input distribution")

# Set colors and kernels
colors = ["navy", "cornflowerblue", "darkorange"]
kernels = ["gaussian", "tophat", "epanechnikov"]
lw = 2

# Plot kernel density estimations
for color, kernel in zip(colors, kernels):
    kde = KernelDensity(kernel=kernel, bandwidth=0.5).fit(X)
    log_dens = kde.score_samples(X_plot)
    ax.plot(
        X_plot[:, 0],
        np.exp(log_dens),
        color=color,
        lw=lw,
        linestyle="-",
        label="kernel = '{0}'".format(kernel),
    )

ax.text(6, 0.38, "N={0} points".format(N))

# Set legend and plot data points
ax.legend(loc="upper left")
ax.plot(X[:, 0], -0.005 - 0.01 * np.random.random(X.shape[0]), "+k")

# Set x and y limits
ax.set_xlim(-4, 9)
ax.set_ylim(-0.02, 0.4)

# Show plot
plt.show()
```
