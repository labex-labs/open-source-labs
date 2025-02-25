# Построим накопленные распределения

В этом шаге мы построим накопленные распределения. Мы будем использовать метод `.ecdf` для построения ECDF и дополнительного ECDF. Также построим теоретическую CDF с использованием нормального распределения с математическим ожиданием 200 и стандартным отклонением 25.

```python
# Накопленные распределения
axs[0].ecdf(data, label="CDF")
n, bins, patches = axs[0].hist(data, 25, density=True, histtype="step",
                               cumulative=True, label="Накопленная гистограмма")
x = np.linspace(data.min(), data.max())
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (x - mu))**2))
y = y.cumsum()
y /= y[-1]
axs[0].plot(x, y, "k--", linewidth=1.5, label="Теория")

# Дополнительные накопленные распределения
axs[1].ecdf(data, complementary=True, label="CCDF")
axs[1].hist(data, bins=bins, density=True, histtype="step", cumulative=-1,
            label="Обратная накопленная гистограмма")
axs[1].plot(x, 1 - y, "k--", linewidth=1.5, label="Теория")
```
