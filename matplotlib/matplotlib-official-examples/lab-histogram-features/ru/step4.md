# Добавляем линию наилучшего соответствия

В этом шаге мы добавим линию наилучшего соответствия к гистограмме. Мы вычислим значения y для линии и построим ее поверх гистограммы.

```python
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y, '--')
```
