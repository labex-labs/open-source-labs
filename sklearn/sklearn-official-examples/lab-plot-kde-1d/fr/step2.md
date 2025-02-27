# Tracer les noyaux disponibles

Nous allons tracer tous les noyaux disponibles pour montrer leurs formes.

```python
# Generate data
X_plot = np.linspace(-6, 6, 1000)[:, None]
X_src = np.zeros((1, 1))

# Create figure and axes
fig, ax = plt.subplots(2, 3, sharex=True, sharey=True)
fig.subplots_adjust(left=0.05, right=0.95, hspace=0.05, wspace=0.05)

# Format function for x-axis labels
def format_func(x, loc):
    if x == 0:
        return "0"
    elif x == 1:
        return "h"
    elif x == -1:
        return "-h"
    else:
        return "%ih" % x

# Plot available kernels
for i, kernel in enumerate(
    ["gaussien", "tophat", "épanechnikov", "exponentielle", "linéaire", "cosinus"]
):
    axi = ax.ravel()[i]
    log_dens = KernelDensity(kernel=kernel).fit(X_src).score_samples(X_plot)
    axi.fill(X_plot[:, 0], np.exp(log_dens), "-k", fc="#AAAAFF")
    axi.text(-2.6, 0.95, kernel)

    axi.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
    axi.xaxis.set_major_locator(plt.MultipleLocator(1))
    axi.yaxis.set_major_locator(plt.NullLocator())

    axi.set_ylim(0, 1.05)
    axi.set_xlim(-2.9, 2.9)

# Set title for second row
ax[0, 1].set_title("Noyaux disponibles")

# Show plot
plt.show()
```
