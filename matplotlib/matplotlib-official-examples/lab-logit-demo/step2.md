# Create a plot with logit scale and standard notation

We will create a plot with logit scale and standard notation. This can be done by setting the y-axis scale to logit using `set_yscale("logit")` and setting the y-axis limits using `set_ylim()`. We will also plot the cumulative distribution functions for the normal, Laplacian, and Cauchy distributions using `plot()` and add a legend using `legend()`.

```python
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(6.4, 4.8))

axs.plot(x, cdf_norm, label=r"$\mathcal{N}$")
axs.plot(x, cdf_laplacian, label=r"$\mathcal{L}$")
axs.plot(x, cdf_cauchy, label="Cauchy")
axs.set_yscale("logit")
axs.set_ylim(1e-5, 1 - 1e-5)
axs.legend()
axs.grid()

plt.show()
```
