# Zeichnen der kumulativen Verteilungen

In diesem Schritt zeichnen wir die kumulativen Verteilungen. Wir verwenden die `.ecdf`-Methode, um die ECDF und die komplementäre ECDF zu zeichnen. Wir zeichnen auch die theoretische CDF mit einer Normalverteilung mit einem Mittelwert von 200 und einer Standardabweichung von 25.

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
