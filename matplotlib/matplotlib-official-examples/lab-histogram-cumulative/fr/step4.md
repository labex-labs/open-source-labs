# Tracez les distributions cumulatives

Dans cette étape, nous allons tracer les distributions cumulatives. Nous utiliserons la méthode `.ecdf` pour tracer la fonction de répartition empirique cumulative (ECDF) et la fonction de répartition empirique cumulative complémentaire (ECCDF). Nous tracerons également la fonction de répartition théorique en utilisant une distribution normale avec une moyenne de 200 et un écart-type de 25.

```python
# Cumulative distributions
axs[0].ecdf(data, label="CDF")
n, bins, patches = axs[0].hist(data, 25, density=True, histtype="step",
                               cumulative=True, label="Cumulative histogram")
x = np.linspace(data.min(), data.max())
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (x - mu))**2))
y = y.cumsum()
y /= y[-1]
axs[0].plot(x, y, "k--", linewidth=1.5, label="Theory")

# Complementary cumulative distributions
axs[1].ecdf(data, complementary=True, label="CCDF")
axs[1].hist(data, bins=bins, density=True, histtype="step", cumulative=-1,
            label="Reversed cumulative histogram")
axs[1].plot(x, 1 - y, "k--", linewidth=1.5, label="Theory")
```
