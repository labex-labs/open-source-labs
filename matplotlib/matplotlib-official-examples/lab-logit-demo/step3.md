# Create a plot with logit scale and survival notation

We will create a plot with logit scale and survival notation. This can be done by setting the y-axis scale to logit and setting the `one_half` parameter to `"1/2"` and `use_overline` parameter to `True` using `set_yscale("logit", one_half="1/2", use_overline=True)"`. We will also plot the cumulative distribution functions for the normal, Laplacian, and Cauchy distributions using `plot()` and add a legend using `legend()`.

```python
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(6.4, 4.8))

axs.plot(x, cdf_norm, label=r"$\mathcal{N}$")
axs.plot(x, cdf_laplacian, label=r"$\mathcal{L}$")
axs.plot(x, cdf_cauchy, label="Cauchy")
axs.set_yscale("logit", one_half="1/2", use_overline=True)
axs.set_ylim(1e-5, 1 - 1e-5)
axs.legend()
axs.grid()

plt.show()
```
